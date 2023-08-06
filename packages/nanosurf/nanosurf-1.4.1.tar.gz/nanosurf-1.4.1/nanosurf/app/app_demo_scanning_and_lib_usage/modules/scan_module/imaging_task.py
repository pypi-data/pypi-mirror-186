""" The long lasting worker thread which start the scan and store the scan lines
Copyright Nanosurf AG 2021
License - MIT
"""
import time
import pythoncom # to connect to SPM Controller within thread
from PySide2.QtCore import Signal

import nanosurf
from nanosurf.lib.datatypes import nsf_thread, sci_channel, sci_stream
from app import app_common, module_base
from modules.scan_module import settings

class ScanData():
    def __init__(self):
        self.stream = sci_stream.SciStream(channels=2)
        self.scan_line_index = -1

class ScanFrameWorker(nsf_thread.NSFBackgroundWorker):
    """ This class implements the long lasting activity of reading the scan data in the background to not freeze the gui """    

    sig_tick = Signal() # is emitted if par_send_tick is True
    sig_new_data = Signal() # is emitted each time a new scan line is measured. Result is read by self.get_result()

    """ parameter for the background work"""
    
    par_image_size = 1e-9
    par_time_per_line = 1.0
    par_points_per_line = 128
    par_channel_id = settings.ChannelD.Topography
    par_send_ticks = True
    par_time_between_ticks = 0.1

    _sig_message = Signal(str, int)

    def __init__(self, my_module: module_base.ModuleBase):
        """ setup the thread and wait until the task is started by thread.start()"""
        self.module = my_module
        self.resulting_data = ScanData()
        self.spm:nanosurf.spm.Spm = None
        super().__init__()
        self._sig_message.connect(self.module.app.show_message)

    def do_work(self):
        """ This is the working function for the long task"""
        self.resulting_data = ScanData()

        if self._connect_to_controller():
            self.spm_scan = self.spm.application.Scan

            #first stop a running scan
            if self.spm_scan.IsScanning:
                self.spm_scan.Stop()
                while self.spm_scan.IsScanning:
                    time.sleep(0.01)

            # prepare frame
            self.spm_scan.ImageSize(self.par_image_size, self.par_image_size)
            self.spm_scan.Scantime = self.par_time_per_line
            self.spm_scan.Points = self.par_points_per_line
            self.spm_scan.Lines = self.par_points_per_line
            
            self.resulting_data.stream.set_stream_length(self.par_points_per_line)
            self.resulting_data.stream.define_stream_range(min=0.0, max=self.par_image_size, unit="m")
            self.resulting_data.stream.set_channel_count(2)
            #start our frame
            self.spm_scan.StartFrameUp()

            # monitor scanning and read new scan lines as they are available
            self.next_scan_line = 0
            self.tick_time = 0.0
            while (self.next_scan_line < self.par_points_per_line) and not self.is_stop_request_pending():
                
                # wait for new data 
                self.tick_time = 0.0
                while (self.next_scan_line > (self.spm_scan.Currentline - 1)) and not self.is_stop_request_pending():
                    time.sleep(self.par_time_between_ticks)
                    self.tick_time += self.par_time_between_ticks
                    if self.par_send_ticks:
                        self.sig_tick.emit()
                    self.send_message(f"Wait for scan line {self.next_scan_line} since {self.tick_time:.2f}s")

                # read new measured line
                channel = self.par_channel_id
                self.resulting_data.stream.set_channel(0, self._read_scan_line(self.next_scan_line, channel, forward=True, raw=False))
                self.resulting_data.stream.set_channel(1, self._read_scan_line(self.next_scan_line, channel, forward=False, raw=False))
                self.resulting_data.scan_line_index = self.next_scan_line
                self.sig_new_data.emit()
                
                # prepare for next line
                self.next_scan_line += 1

            self.spm_scan.Stop()
            self.logger.info(f"Scan ended at line: {self.spm_scan.Currentline}")

        self._disconnect_from_controller()

    def get_result(self) -> ScanData:
        return self.resulting_data

    def send_message(self, msg:str, msg_type : app_common.MsgType = app_common.MsgType.Info):
        self._sig_message.emit(msg, msg_type)
        self.logger.info(msg)       
        
    def _read_scan_line(self, line: int, channel: int, forward=True, raw: bool = True) -> sci_channel.SciChannel:
        group  = nanosurf.Spm.ScanGroupID.Forward if forward else nanosurf.Spm.ScanGroupID.Backward
        filter = nanosurf.Spm.DataFilter.RAW if raw else nanosurf.Spm.DataFilter.LineFit
        unit_str = "m" if channel == 1 else "V"
        line_str:str = self.spm_scan.GetLine(group, channel, line, filter, nanosurf.Spm.DataConversion.Physical)
        line_str = line_str.replace(',','.') # needed in case the numbers are formatted with a ',' as decimal separator (e.g. standard german windows number format setting)
        line_split_str = line_str.split(";")
        scan_data = [float(p) for p in line_split_str]
        return sci_channel.SciChannel(scan_data, unit=unit_str)

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
        