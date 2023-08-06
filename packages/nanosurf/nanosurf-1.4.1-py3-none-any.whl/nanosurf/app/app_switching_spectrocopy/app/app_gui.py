""" The GUI of the application framework
Copyright Nanosurf AG 2021
License - MIT
"""

from PySide2 import QtWidgets
from PySide2 import QtGui, QtWidgets, QtCore
import nanosurf as nsf
from app import app_common, module_base

control_layout_width = 200

class MenuSeparator(QtWidgets.QFrame):
    def __init__(self, hidden : bool = False, height: int = 1,  **kargs):
        super().__init__(*kargs)
        self.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        self.setStyleSheet(f"background-color:#{nsf.gui.nsf_colors.NSFColorHexStr.Orange};")
        self.setFixedHeight(height)
        self.setHidden(hidden)

class MenuButton(QtWidgets.QWidget):
  
    sig_on_menu_clicked = QtCore.Signal(int)
   
    def __init__(self, menutext: str, menuitem: int):
        super().__init__()
        self._setup_widgets(menutext)
        self.set_highlight(False)
        self.menuitem = menuitem
        self._button.clicked.connect(self._on_clicked)
    
    def set_highlight(self, highlight: bool = False):
        color = nsf.gui.nsf_colors.NSFColorHexStr.Orange if highlight else nsf.gui.nsf_colors.NSFColorHexStr.Soft_Gray
        self._marker_line.setStyleSheet(f"background-color:#{color};")

    def _on_clicked(self):
        self.sig_on_menu_clicked.emit(self.menuitem)

    def _setup_widgets(self, label_str: str):
        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        self._button = QtWidgets.QPushButton(label_str)
        self._marker_line = MenuSeparator(hidden=False, height=2)
        layout.addWidget(self._marker_line)
        layout.addWidget(self._button)
        self.setLayout(layout)      


class StdVSpacer(QtWidgets.QSpacerItem):
    def __init__(self):
        super().__init__(control_layout_width, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)

class AppWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def create_gui(self, ui_style_file : str, icon_file : str):
        # create main GUI layout
        style_sheet_str = self._read_style_sheet_into_str(ui_style_file)
        self.setStyleSheet(style_sheet_str)
        self.setWindowTitle(self.app.app_name_long)
        self.setWindowIcon(QtGui.QIcon(str(icon_file)))
        self.statusBar().showMessage("Ready")

        # setup general GUI layout
        # on the left will be a menu to open the modules stacked guis on the right
        self.mainScreen = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_menu = QtWidgets.QHBoxLayout()
        self.main_messagebox = nsf.gui.NSFInfoBox(hidden=True)
        self.main_stack = QtWidgets.QStackedLayout()
        self.main_stack.addWidget(QtWidgets.QLabel("Main screen"))

        self.menu_sep = MenuSeparator(hidden=True)
        self.status_sep = MenuSeparator(hidden=False)
        self.main_layout.addLayout(self.main_menu,0)
        self.main_layout.addWidget(self.menu_sep,1)
        self.main_layout.addWidget(self.main_messagebox,2)
        self.main_layout.addLayout(self.main_stack,3)
        self.main_layout.addWidget(self.status_sep,4)
        #self.main_layout.addSpacerItem(StdVSpacer())
        self.mainScreen.setLayout(self.main_layout)
        self.setCentralWidget(self.mainScreen)
        self.load_window_size()

    def show_message(self, msg: str, msg_type: app_common.MsgType = app_common.MsgType.Info):
        if msg_type == app_common.MsgType.Error:
            self.show_info_box(msg, background_color=nsf.gui.nsf_colors.NSFColorHexStr.Orange, text_color="")
        elif msg_type == app_common.MsgType.Warn:
            self.show_info_box(msg, '')
        else:
            self.statusBar().showMessage(msg)        

    def save_window_size(self):
        self.app.registry.setValue("geometry", self.saveGeometry())
        self.app.registry.setValue("windowState", self.saveState())
    
    def load_window_size(self):
        self.restoreGeometry(self.app.registry.value("geometry"))
        self.restoreState(self.app.registry.value("windowState"))

    def add_screen(self, module: module_base.ModuleBase):
        module_gui = module.gui
        if isinstance(module_gui, QtWidgets.QWidget):
            self.main_stack.addWidget(module_gui)
            # activate first screen 
            if self.main_stack.currentIndex() == 0:
                self.main_stack.setCurrentWidget(module_gui)

    def get_active_module_index(self) -> int:
        return self.main_stack.currentIndex() - 1

    def set_active_module_by_index(self, index: int):
        self.main_stack.setCurrentIndex(index+1)
        self._update_menu_button_highlight()

    def is_menu_visible(self) -> bool:
        return self.app.get_module_count() > 1

    def update_menu(self, modules: dict):
        mod_with_gui = 0
        for mod in modules.values():
            if mod.gui is not None:
                mod_with_gui += 1

        # show menu only if there are more than one modules with gui present
        if mod_with_gui > 1:
            #remove all menu items
            while self.main_menu.count():
                child = self.main_menu.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()

            # add menu items
            menuindex = 0
            for mod in modules.values():
                if mod.gui is not None:
                    menuitem = MenuButton(mod.name, menuindex)
                    menuitem.sig_on_menu_clicked.connect(self._on_menu_button_clicked)
                    self.main_menu.addWidget(menuitem)
                    menuindex += 1
            self.main_menu.addStretch() 

        self.menu_sep.setHidden(mod_with_gui <= 1)
        
    # internal use only

    def closeEvent(self, arg):
        """ capture close button from application window"""
        self.save_window_size()
        super().closeEvent(arg)

    def _read_style_sheet_into_str(self, style_file: str):
        style = ""
        with open(style_file) as f:
            style = f.read()
        return style
    
    def _on_menu_button_clicked(self, index: int):
        self.app.activate_module(index)

    def _update_menu_button_highlight(self):
        if self.is_menu_visible():
            active_index = self.get_active_module_index()
            for i in range(self.main_menu.count()-1):
                self.main_menu.itemAt(i).widget().set_highlight(i == active_index)

    def show_info_box(self, msg: str, background_color: str, text_color: str):
        self.main_messagebox.set_background_color(background_color)
        self.main_messagebox.set_text_color(text_color)
        self.main_messagebox.set_message(msg)
        self.main_messagebox.setHidden(False)
