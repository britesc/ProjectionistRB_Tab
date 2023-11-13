import os
import sys
import traceback
import qdarktheme

from PySide6 import (
    QtGui,
    QtCore
)

from PySide6.QtCore import (
    QSize,
    QFileInfo,
    QRect
)

from PySide6.QtGui import (
    QHideEvent,
    QShowEvent,
    QWindow,
    QAction,
    QIcon,
    QPixmap,
    QMouseEvent
)

from PySide6.QtWidgets import (
    QMainWindow,
    # QToolBar,
    QPushButton,
    QStatusBar,
    QApplication,
    QHeaderView,
    # QAbstractItemView,
    QTableWidget,
    QTableWidgetItem,
    # QVBoxLayout,
    # QHBoxLayout,
    # QTableView,
    QLabel,
    QMenu
)

from PySide6.QtCore import (
    Slot,
    Signal
)

from classes import (
    p2_database
)

from classes.p2_systray import p2_systray
# from main import main

from pages.page01 import page01intro
from pages.page02 import page02config
# from pages.page99 import page99test

from tabs.initial import initial

from mainwindow_ui import Ui_MainWindow

import pprint

class MainWindow(QMainWindow, Ui_MainWindow):
    """ The MainWindow Class. """
    def __init__(self, app) -> None:
        super().__init__()
        self.setupUi(self)  # type: ignore
        self.app = app  # declare an app member
        
        
        self.setMinimumSize(600, 510)
        self.setMaximumSize(600,510)
        
        self.p_database_name = f"{QtCore.QCoreApplication.applicationName()}.db"
        print(f"Database Name 3 = {self.p_database_name}")
        self.p_database = p2_database.ProjDatabase(self.p_database_name)
        self.p_database.check_database_exists()
        # self.current_theme = self.p_database.get_theme()

        self.R0C0_Context_Menu()

        self.pushButton_R0C0.setMenu(self.menu)

        self.page01intro  = page01intro.Page01Intro()
        # self.page99test   = page99test.Page99Test()
        self.page02config = page02config.Page02Config()

        self.stackedWidget.addWidget(self.page01intro) # index 1
        # self.stackedWidget.addWidget(self.page99test) # index 2
        self.stackedWidget.addWidget(self.page02config) # index 3
        self.stackedWidget.setCurrentIndex(0)
        print(f"Number of Pages {self.stackedWidget.count()}")
        print(f"Current Page {self.stackedWidget.currentIndex()}")

        initial_tab_setup = initial.tab_initial_setup()
        self.tabWidget_Ribbon_Bar.addTab(initial_tab_setup, "Initial Setup 1")
        initial_tab_setup.signal_pb_clicked.connect(self.signals_received)
        
        self.systray = p2_systray.ProjSysTray(app)
        
    def R0C0_Context_Menu(self) -> None:
        """Create the Context Menu."""
        self.menu = QMenu()

        R0C0_action_new = self.action_New
        R0C0_action_new.triggered.connect(self.R0C0_actionNew)  # type: ignore
        self.menu.addAction(R0C0_action_new)

        R0C0_action_open = self.action_Open
        R0C0_action_open.triggered.connect(self.R0C0_actionOpen)  # type: ignore
        self.menu.addAction(R0C0_action_open)

        R0C0_action_close = self.action_Close
        R0C0_action_close.triggered.connect(self.R0C0_actionClose)  # type: ignore
        self.menu.addAction(R0C0_action_close)

        R0C0_action_quit = self.action_Quit
        R0C0_action_quit.triggered.connect(self.R0C0_actionQuit)  # type: ignore
        self.menu.addAction(R0C0_action_quit)

        # self.pushButton_R0C0_Configuration_Theme.clicked.connect(self.p2_themes.toggle_theme)

    def R0C0_actionNew(self) -> None:
        print("Action New Clicked")

    def R0C0_actionOpen(self) -> None:
        print("Action Open Clicked")

    def R0C0_actionClose(self) -> None:
        print("Action Close Clicked")

    def R0C0_actionQuit(self) -> None:
        print("Action Quit Clicked")

    def initial_page_previous(self) -> None:
        """ Go to the next Stacked Widget Page. """

        self.current = self.stackedWidget.currentIndex()
        self.maximum = self.stackedWidget.count() - 1

        # print("initial_page_previous:")
        # print(f"self.current {self.current}")
        # print(f"self.maximum {self.maximum}")
        # print("")

        if self.current >  0:
            self.stackedWidget.setCurrentIndex(self.current - 1)

    def initial_page_next(self) -> None:
        """ Go to the next Stacked Widget Page. """

        self.current = self.stackedWidget.currentIndex()
        self.maximum = self.stackedWidget.count() - 1

        # print("initial_page_next:")
        # print(f"self.current {self.current}")
        # print(f"self.maximum {self.maximum}")
        # print("")

        if self.current <  self.maximum:
            self.stackedWidget.setCurrentIndex(self.current + 1)



    @Slot()
    def signals_received(self, sig) -> None:
        # print(f"Signal Received {sig}")
        match sig:
            case 10:
                self.hide()
            case 64:
                # print("Previous - Number 64 Received")
                self.initial_page_previous()
            case 65:
                # print("Next - Number 65 Received")
                self.initial_page_next()
            case _:
                pass

    def hideEvent(self, event: QHideEvent) -> None:
        print("Hide Event Triggered")
        self.systray.window_hide()
        return super().hideEvent(event)
    
    def showEvent(self, event: QShowEvent) -> None:
        print("Show Event Triggered")
        self.systray.window_show()      
        return super().showEvent(event)
    