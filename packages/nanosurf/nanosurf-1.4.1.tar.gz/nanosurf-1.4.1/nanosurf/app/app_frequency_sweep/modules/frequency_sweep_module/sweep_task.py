""" The long lasting worker thread to perform the frequency sweep
Copyright Nanosurf AG 2021
License - MIT
"""
import time
import numpy as np
import pythoncom
from PySide2.QtCore import Signal
import nanosurf
import nanosurf.lib.spm.workflow.frequency_sweep as freq_sweep
import nanosurf.lib.datatypes.nsf_thread as nsf_thread
from app import app_common, module_base
from modules.frequency_sweep_module import sweep_settings

class FrequencySweepData():
    def __init__(self):
        self.result_ok = False
        self.result_freq:list[float] = []
        self.result_amplitude:list[float] = []
        self.result_phase:list[float] = []

class FrequencySweepWorker(nsf_thread.NSFBackgroundWorker):
    
    sig_message = Signal(str, int)
    sig_sweep_tick = Signal(float, float) # send out ticker during sweeping with remaining time

    """ parameter for the background work"""
    par_cantilever = None
    par_excitation_method : sweep_settings.ExcitationMethodID = sweep_settings.ExcitationMethodID.PiezoDrive 
    par_input_source:freq_sweep.InputSource = freq_sweep.InputSource.Deflection
    par_output_source:freq_sweep.FrequencySweepOutput = freq_sweep.FrequencySweepOutput.Normal_Excitation
    par_bandwidth:freq_sweep.Bandwidths = freq_sweep.Bandwidths.Hz_360

    par_center_frequency = 150000
    par_frequency_range = 100000
    par_frequency_step = 100
    par_excitation_amplitude = 0.2
    par_deflection_setpoint = 0

    par_plot_style_id=sweep_settings.PlotStyleID.Linear

    def __init__(self, my_module: module_base.ModuleBase):
        self.module = my_module
        self.resulting_data = FrequencySweepData()
        self.spm:nanosurf.spm.Spm = None
        super().__init__()

    def _init_in_new_thread(self):
        super()._init_in_new_thread()
        self.sig_message.connect(self.module.app.show_message)

    def send_message(self, msg:str, msg_type : app_common.MsgType = app_common.MsgType.Info):
        self.sig_message.emit(msg, msg_type)
        self.logger.info(msg)       

    def get_result(self) -> FrequencySweepData:
        return self.resulting_data

    def do_work(self):
        """ This is the working function for the long task"""
        self.resulting_data = FrequencySweepData()
        if self._connect_to_controller():
            self.application = self.spm.application
            self.freq_sweeper = freq_sweep.FrequencySweep(self.spm)
            if self.par_excitation_method == sweep_settings.ExcitationMethodID.PiezoDrive:
                self.application.OperatingMode.ExcitationMode = nanosurf.Spm.ExcitationMode.PhotoThermal 
            else:
                self.application.OperatingMode.ExcitationMode = nanosurf.Spm.ExcitationMode.PiezoElectric

            sweep_time = self.freq_sweeper.start_execute(
                start_frequency=self.par_center_frequency-(self.par_frequency_range/2),
                end_frequency=self.par_center_frequency+(self.par_frequency_range/2),
                frequency_step=self.par_frequency_step,
                sweep_amplitude=self.par_excitation_amplitude,
                input_source=self.par_input_source,
                input_range=freq_sweep.InputRanges.Full,
                mixer_bw_select=self.par_bandwidth,
                reference_phase=0.0, 
                output=self.par_output_source
                )

            print(f"Wait for {sweep_time:.1f}s.")
            start_time = time.time()
            while self.freq_sweeper.is_executing() and not self.is_stop_request_pending():
                time.sleep(0.1)
                cur_freq = self.freq_sweeper.get_current_sweep_frequency()
                remaining_time = sweep_time - (time.time() - start_time)
                self.sig_sweep_tick.emit(cur_freq, remaining_time)
            data = self.freq_sweeper.finish_execution()

            if not self.is_stop_request_pending():
                self.resulting_data.result_amplitude = np.abs(data[0])
                self.resulting_data.result_phase = np.unwrap(np.angle(data[0], deg=True), discont=180)
                self.resulting_data.result_freq = data[1]
                self.resulting_data.result_ok = True
            else:
                self.resulting_data.result_ok = False

        self._disconnect_from_controller()

    def get_result(self) -> FrequencySweepData:
        return self.resulting_data

    def _connect_to_controller(self) -> bool:
        self.send_message("Connecting to Nanosurf controller")
        ok = False
        if self.spm is None:
            pythoncom.CoInitialize()
            self.spm = nanosurf.SPM()
            if self.spm.is_connected():
                if self.spm.is_scripting_enabled():
                    ok = True
                else:
                    self.send_message("Error: Scripting interface is not enabled", app_common.MsgType.Error)
            else:
                self.send_message("Error: Could not connect to controller. Check if software is started", app_common.MsgType.Error)
        else:
            ok = True
        return ok

    def _disconnect_from_controller(self):
        if self.spm is not None:
            if self.spm.application is not None:
                del self.spm
            self.spm = None
 