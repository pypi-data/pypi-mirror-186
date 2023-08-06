""" Application for performing Frequency Sweeps with Nanosurf Software
Compatible with Nanosurf software CX_3.10.3.5 and newer, Nanosurf python package 1.2.2 and DriveAFM
Author: Hans Gunstheimer
Copyright Nanosurf AG 2022
License - MIT
"""

import sys
import nanosurf.lib.datatypes.prop_val as prop_val

from app import app_base
from modules.frequency_sweep_module import sweep_module as sweep_func
from modules.frequency_sweep_module import sweep_gui as sweep_gui

MyCompany = "Nanosurf AG"
MyAppNameShort = "FrequencySweep"
MyAppNameLong = "Frequency Sweep Application"

class MyAppSettings(app_base.AppSettings):
    """ Settings defined here as PropVal are stored persistently in a ini-file"""
    AppHelloMsg = prop_val.PropVal("Welcome to the Nanosurf Frequency Sweep App")
    
class MyApp(app_base.ApplicationBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings = MyAppSettings()

    def do_startup(self):
        """ Insert any module used in this app. 
            If more than one module is added, a menu bar is shown in the app window
        """
        self.add_module(sweep_func.FrequencySweepModule(self, sweep_gui.SweepScreen()), "Sweep Module")

        # here we apply a setting value just for fun
        self.show_message(self.settings.AppHelloMsg.value)
        
    def do_shutdown(self):
        """ Handle cleaning up stuff here"""
        pass

if __name__ == "__main__":
    App = MyApp(MyCompany, MyAppNameShort, MyAppNameLong, [])
    App.start_app()
    sys.exit(App.exec_())
