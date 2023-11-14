#!/usr/bin/env python3
# coding: utf-8
""" System Tray. """

import os
import traceback
import pathlib

from PySide6.QtWidgets import (
    QApplication,
    QSystemTrayIcon,
    QMenu,
)

from PySide6.QtGui import (
    QAction,
    QIcon,
    QHideEvent,
    QShowEvent,    
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
from resources.utilities import utilities

import buttonsGlassRound_rc

class ProjSysTray:
    """The Class for System Tray. """
    def __init__(self, app) -> None:
        # sourcery skip: aug-assign, remove-pass-body, remove-redundant-pass, remove-unnecessary-cast
        """ Init for System Tray. """
        super().__init__()
        

        self.class_version = "0.0.4.dev"
        self.module_index = "21"
        self.author_name = "Julian Bourne"

        tv = utilities.findMainWindow()
        # if tv:
        #     print(f"Found MainWindow {tv}")
        # else:
        #     print("Unable to find MainWindow")

        if not QSystemTrayIcon.isSystemTrayAvailable():
            pass
        else:

            app.setQuitOnLastWindowClosed(False)

            self.tray_icon = QIcon(":buttons/buttons/glassRound/glassButtonProjectionist.png")  # noqa: E501

            self.tray = QSystemTrayIcon()
            self.tray.setIcon(self.tray_icon)
            self.tray.setVisible(True)

            self.tray_menu = QMenu()
            self.action1 = QAction("Show")
            self.action1.triggered.connect(tv.showNormal) # type: ignore
            self.action1.triggered.connect(tv.activateWindow) # type: ignore
            self.action1.triggered.connect(tv.raise_) # type: ignore
            self.action1.setIcon(QIcon(u":buttons/buttons/glassRound/glassButtonShow.png"))
            self.action1.setVisible(False)
            self.tray_menu.addAction(self.action1)

            self.action2 = QAction("Hide")
            self.action2.triggered.connect(tv.hide) # type: ignore
            self.action2.setIcon(QIcon(u":buttons/buttons/glassRound/glassButtonHide.png"))
            self.action2.setVisible(True)
            self.tray_menu.addAction(self.action2)

            self.action3 = QAction("Quit")
            self.action3.triggered.connect(app.quit) # type: ignore
            self.action3.setIcon(QIcon(":buttons/buttons/glassRound/glassButtonExit.png"))
            self.tray_menu.addAction(self.action3)

            self.tray.setContextMenu(self.tray_menu)
            
    def window_hide(self) -> None:
        # print("1. window_hide Triggered")
        self.action1.setVisible(True)
        self.action2.setVisible(False)
        return
    
    def window_show(self) -> None:
        # print("1. window_show Triggered")
        self.action1.setVisible(False)
        self.action2.setVisible(True)
        return
                