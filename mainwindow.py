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
    Qt,
    QEvent
)


from classes import (
    p2_database
)

from pages import (
    page01intro,
    page99test
    # page02config
)

from mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """The MainWindow Class."""
    def __init__(self, app) -> None:
        super().__init__()
        self.setupUi(self)  # type: ignore
        self.app = app  # declare an app member

        self.p_database_name = f"{QtCore.QCoreApplication.applicationName()}.db"
        print(f"Database Name 3 = {self.p_database_name}")
        self.p_database = p2_database.ProjDatabase(self.p_database_name)
        self.p_database.check_database_exists()
        # self.current_theme = self.p_database.get_theme()

        self.R0C0_Context_Menu()

        self.pushButton_R0C0.setMenu(self.menu)

        self.page01intro  = page01intro.Page01Intro()
        self.page99test   = page99test.Page99Test()
        # self.page02config = page02config.Page02Config()

        self.stackedWidget.addWidget(self.page01intro) # index 1
        self.stackedWidget.addWidget(self.page99test) # index 2

        self.stackedWidget.setCurrentIndex(2)

        
        


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

