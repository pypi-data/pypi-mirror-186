""" The base class for functional modules
Copyright Nanosurf AG 2021
License - MIT
"""
import sys
import logging
from PySide2 import QtWidgets, QtCore

control_layout_width = 200

class CtrlSpacer(QtWidgets.QSpacerItem):
    def __init__(self):
        super().__init__(control_layout_width,40, QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.MinimumExpanding)

class ModuleBase(QtCore.QObject):
    def __init__(self, app, gui):
        super().__init__()
        self.app = app
        self.ui = gui
        self.settings = None
        self.__name = ""
        self.logger = logging.getLogger(self.__name)
 
    def start(self):
        self.app.load_settings(self)

        self.do_start()
        if self.ui != None:
            self.ui.create_screen(self)

    @property
    def gui(self):
        return self.ui

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        self.logger = logging.getLogger(self.__name)

    def stop(self):
        self.do_stop()
        self.app.save_settings(self)

    def do_start(self):
        raise NotImplementedError(f"Subclass of '{self.__class__.__name__}' has to implement '{sys._getframe().f_code.co_name}()'")

    def do_stop(self):
        raise NotImplementedError(f"Subclass of '{self.__class__.__name__}' has to implement '{sys._getframe().f_code.co_name}()'")

class ModuleScreen(QtWidgets.QWidget):
    def __init__(self):
        self.module = None
        super().__init__()

    def create_screen(self, module: ModuleBase):
        """
        lets create the gui. Creates all GUI elements but no action yet. 
        This is done later in ConnectGUI()
        """
        self.module = module
        self.do_setup_screen(module)

    def do_setup_screen(self, module: ModuleBase):
        raise NotImplementedError(f"Subclass of '{self.__class__.__name__}' has to implement '{sys._getframe().f_code.co_name}()'")

