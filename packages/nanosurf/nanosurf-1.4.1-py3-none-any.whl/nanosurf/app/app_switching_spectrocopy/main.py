""" Application template to be used to build own nice python applications
Copyright Nanosurf AG 2021
License - MIT
"""

import sys
import nanosurf.lib.datatypes.prop_val as prop_val

from app import app_base
from modules.switching_spec_module import module as switching_spec_func
from modules.switching_spec_module import gui as switching_gui

MyCompany = "Nanosurf"
MyAppNameShort = "SwitchingSpectroscopy"
MyAppNameLong = "Switching spectroscopy application"

class MyAppSettings(app_base.AppSettings):
    """ Settings defined here as PropVal are stored persistently in a ini-file"""
    AppHelloMsg = prop_val.PropVal(f"Welcome to {MyAppNameLong}")
    
class MyApp(app_base.ApplicationBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings = MyAppSettings()

    def do_startup(self):
        """ Insert any module used in this app. 
            If more than one module is added, a menu bar is shown in the app window
        """
        self.add_module(switching_spec_func.SwitchingSpecModule(self, switching_gui.SwitchingSpecScreen()), "Switching Spectroscopy")
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

