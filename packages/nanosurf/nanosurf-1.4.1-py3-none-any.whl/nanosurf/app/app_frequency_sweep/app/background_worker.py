""" A base class for background tasks
Copyright Nanosurf AG 2021
License - MIT
"""
import sys
import time
import logging
from PySide2.QtCore import QThread, QObject, Signal
from app import module_base
from app import app_common

class WorkerData():
    """ Use this class as base class for own worker thread results"""
    pass

class SingleRunWorker(QObject):
    """ This class implements a long lasting activity in the background to not freeze the gui 
        (e.g. measuring some values over time) background 
        Subclass from this and implement do_work(). 
        
        The main thread then calls thread.start(). That's it.
        Signals emitted from worker thread to inform about its state
        Signal 'sig_finish' tells you when the work is done.

        The sub class can fire 'sig_new_data' to inform about the availability of new data.
        client can then call get_data() to read this.

        Text messages can be sent to the application by 'sig_message' any time.

        A running task can be asked if it's still running by task.is_running()
        A request to stop is done by: task.stop(wait=True|False)
        
        The user function in task.do_work() should implement the possibility to abort the work by checking regularly self.stop_request_flag 
        To check wether a task was aborted call: task.is_aborted()
    """
    sig_started = Signal()
    sig_new_data = Signal()
    sig_finished = Signal()

    def start(self):
        """ Start the worker activity. 
        'sig_started' is emitted to inform the real start of the worker activity"""
        if not self.is_running():
            self.stop_request_flag = False
            self.thread.start()
        else:
            self.logger.warning("Thread allready started")

    def stop(self, wait: bool = False, timeout : float = 10.0) -> bool:
        """ Send stop request to worker thread.  
            'sig_finished' is emitted when the worker thread has finished its job.

            Parameters
            ----------
            wait: bool
                If True the function waits until the worker thread has really finished
            timeout: float
                maximal wait time 

            Returns
            -------
            Bool:
                True if task could be stopped.
        """
        if self.is_running():
            self.stop_request_flag = True

            if wait:
                abort_waiting = False
                ticks = 0
                waiting_time = 0.0
                while self.is_running() and not abort_waiting:
                    ticks += 1
                    if ticks > 10:
                        waiting_time += 1.0
                        if waiting_time > timeout:
                            abort_waiting = True
                            self.logger.warning(f"Stop request was not served in {timeout}s")
                            self.thread.quit()
                    time.sleep(0.1)
        else:
            self.logger.warning("Thread allready stopped")
        return not self.is_running()

    def is_running(self) -> bool:
        return self.is_running_flag 

    def is_aborted(self) -> bool:
        return self.stop_request_flag and (not self.is_running_flag)

    def get_result(self) -> WorkerData:
        return self.resulting_data

    #--------------- for sub class only ------------------------------------------------------------

    def send_message(self, msg:str, msg_type : app_common.MsgType = app_common.MsgType.Info):
        self._sig_message.emit(msg, msg_type)
        self.logger.info(msg)       

    def do_work(self):
        """ This function has to be overwritten by sub class and do the long lasting background work"""
        raise NotImplementedError(f"Subclass of '{self.__class__.__name__}' has to implement '{sys._getframe().f_code.co_name}()'")

    #--------------- internal functions ------------------------------------------------------------

    _sig_ready_to_quit = Signal() # internal use
    _sig_message = Signal(str, int)
    
    def __init__(self, my_module: module_base.ModuleBase):
        """ setup the thread and wait until the task is started by thread.start()"""
        super().__init__()
        self.module = my_module
        self.logger = logging.getLogger(self.module.name)
        self.stop_request_flag = False
        self.is_running_flag = False
        self.resulting_data = WorkerData()
        self.thread = QThread()
        self._sig_ready_to_quit.connect(self.thread.quit)
        self._sig_message.connect(self.module.app.show_message)
        
        self.moveToThread(self.thread)
        self.thread.started.connect(self._background_worker)

    def _background_worker(self):
        """ this function is called at task start""" 

        # prepare 
        self.is_running_flag = True
        self.stop_request_flag = False
        self.module.app.activate_debugger_support_for_this_thread()
        self.sig_started.emit()

        # do the real stuff now
        self.do_work()
        
        # clean up
        self.is_running_flag = False
        self.sig_finished.emit()
        self._sig_ready_to_quit.emit()

