""" The long lasting worker thread as demo - just wait some time and create data periodically
Copyright Nanosurf AG 2021
License - MIT
"""
import time
import enum
import pythoncom # to connect to SPM Controller within thread
from PySide2.QtCore import Signal
import nanosurf
from nanosurf.lib.datatypes import nsf_thread, sci_channel, sci_stream
import nanosurf.lib.spm.lowlevel as ll
import nanosurf.lib.spm.lowlevel.ctrlunits as cu
from app import app_common, module_base
from modules.switching_spec_module import settings

class SpecWorkerData():
    def __init__(self):
        self.output : float = 0.0
        self.output_unit = str = ""
        self.amplitude_on : float = 0.0
        self.amplitude_off : float = 0.0
        self.amplitude_unit = str = ""
        self.phase_on : float = 0.0
        self.phase_off : float = 0.0

OutputChannel_ID_to_LUInst_Map = {
    settings.OutputChannelID.User1.value : cu.DAC.HiResOut_USER1,
    settings.OutputChannelID.User2.value : cu.DAC.HiResOut_USER2,
    settings.OutputChannelID.TipVoltage.value : cu.DAC.HiResOut_TIPVOLTAGE,
}

class SpecDir(enum.Enum):
    SpecFwd = 0
    SpecBwd = 1

class SpecWorker(nsf_thread.NSFBackgroundWorker):
    """ This class implements the long lasting activity in the background to not freeze the gui """

    sig_tick = Signal() # is emitted if par_send_tick is True
    sig_new_data = Signal() # is emitted each time new data are available . Result is read by self.get_result()

    """ parameter for the background work"""
    par_output_id = settings.OutputChannelID.User1
    par_output_span = 10.0   # V: spec range, using the scaling and unit as defined in the software
    par_output_center = 0.0
    par_time_per_step = 0.1    # equilibration time for voltage and lock-in to settle
    par_steps = 10             # number of steps per direction

    _sig_message = Signal(str, int)

    def __init__(self, my_module: module_base.ModuleBase):
        self.module = my_module
        self.resulting_data = SpecWorkerData()
        self.spm:nanosurf.Spm = None
        super().__init__()
        self._sig_message.connect(self.module.app.show_message)

    def do_work(self):
        """ This is the working function for the long task"""
        # clear data
        self.resulting_data = SpecWorkerData()

        if self._connect_to_controller():
                           
            lockin = self.spm.lowlevel.ctrlunits.get_lock_in()
            dacout = self.spm.lowlevel.ctrlunits.get_dac(OutputChannel_ID_to_LUInst_Map[self.par_output_id])
            original_out = dacout.dc
            original_source = dacout._lu.input.value

            self.cur_voltage_range = self.par_output_span
            self.cur_steps = self.par_steps 
            self.cur_time_per_step = self.par_time_per_step 
            self.cur_offset_voltage = self.par_output_center

            self.resulting_data.amplitude_unit = lockin.input_amp_unit 
            self.resulting_data.output_unit = dacout.unit
            
            #move in both spectroscopy directions
            for spec_dir in SpecDir:
                #voltage step size with opposite sign for fwd and bwd
                cur_offset = self.cur_offset_voltage  + self.cur_voltage_range/2*(2*(spec_dir.value%2)-1)
                cur_voltage_step = self.cur_voltage_range/(self.cur_steps-1)*(1-2*(spec_dir.value%2)) 
                
                # This loop creates the shape of switching spectroscopy in time
                for cur_step in range(self.cur_steps): 
                    cur_output = cur_offset + cur_step*cur_voltage_step
                    self.resulting_data.output = cur_output

                    # write a dc level to an output and measure response during voltage application
                    dacout.dc = cur_output
                    time.sleep(self.cur_time_per_step)
                    self.resulting_data.amplitude_on = lockin.input_amp 
                    self.resulting_data.phase_on = lockin.input_phase

                    # switch potential back to offset voltage and measure response again
                    dacout.dc = self.cur_offset_voltage 
                    time.sleep(self.cur_time_per_step)
                    self.resulting_data.amplitude_off = lockin.input_amp 
                    self.resulting_data.phase_off = lockin.input_phase
            
                    if self.is_stop_request_pending():
                        break
                    self.sig_new_data.emit()

            # restore original setting of output        
            dacout.dc = original_out
            dacout._lu.input.value = original_source
        self._disconnect_from_controller()

    def get_result(self) -> SpecWorkerData:
        return self.resulting_data

    def send_message(self, msg:str, msg_type: app_common.MsgType = app_common.MsgType.Info):
        self._sig_message.emit(msg, msg_type)
        self.logger.info(msg)   

    def _connect_to_controller(self) -> bool:
        self.send_message("Connecting to Nanosurf controller")
        pythoncom.CoInitialize()
        ok = False
        if self.spm is None:
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
        