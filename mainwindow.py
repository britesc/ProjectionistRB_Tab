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

from sqlitedict import (
    SqliteDict
)

from classes import (
    p2_database
)

from mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """The MainWindow Class."""
    def __init__(self, app) -> None:
        super().__init__()
        self.setupUi(self)  # type: ignore
        self.app = app  # declare an app member
        self.p_database = p2_database.ProjDatabase()
        self.current_theme = self.p_database.get_theme()

        self.R0C0_Context_Menu()

        self.pushButton_R0C0.setMenu(self.menu)

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

