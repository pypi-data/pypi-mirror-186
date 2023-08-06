""" The application entry point
Copyright Nanosurf AG 2021
License - MIT
"""

import sys
import nanosurf as nsf

from app import app_base
from modules.scan_module import module as scan_func
from modules.scan_module import gui as scan_gui

MyCompany = "Nanosurf"
MyAppNameShort = "PythonScanDemo"
MyAppNameLong = "Nanosurf Python Imaging and Library Demo"

class MyAppSettings(app_base.AppSettings):
    """ Settings defined here as PropVal are stored persistently in a ini-file"""
    AppHelloMsg = nsf.PropVal("Welcome to scan and library usage demo.")
    
class MyApp(app_base.ApplicationBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings = MyAppSettings()

    def do_startup(self):
        """ Insert any module used in this app. 
            If more than one module is added, a menu bar is shown in the app window
        """
        self.add_module(scan_func.ScanModule(self, scan_gui.ScanScreen()), "Scan Demo")
        # use self.add_module() again for second and more modules used in this application

        # here we apply a setting value just for fun
        self.show_message(self.settings.AppHelloMsg.value)
        
    def do_shutdown(self):
        """ Handle cleaning up stuff here"""
        pass

if __name__ == "__main__":
    App = MyApp(MyCompany, MyAppNameShort, MyAppNameLong, [])
    App.start_app()
    sys.exit(App.exec_())

