#!/usr/bin/env python3
# coding: utf-8

import sys

from PySide6.QtCore import Signal, Slot, QObject

from PySide6.QtWidgets import (
    QWidget
)

from PySide6 import QtTest


from tabs.initial import initial_ui

class tab_initial_setup(QWidget, initial_ui.Ui_tab_initial_setup):
    signal_pb_clicked = Signal(int)    
    def __init__(self) -> None:
        super().__init__()
        # self.ui = initial_ui
        self.setupUi(self)  # type: ignore
        self.pushButtonExit.clicked.connect(self.button_pushed_exit)
        self.pushButton_navigation_previous.clicked.connect(self.button_pushed_previous)
        self.pushButton_navigation_next.clicked.connect(self.button_pushed_next)
        

    @Slot()
    def button_pushed_exit(self) -> None:
        print("Quit Clicked")  
        # sys.exit()
        self.signal_pb_clicked.emit(10)

    @Slot()  
    def button_pushed_previous(self) -> None:
        # print("Previous Signal Emitted")
        self.signal_pb_clicked.emit(64)

        
    @Slot()  
    def button_pushed_next(self) -> None:
        # print("Next Signal Emitted")
        self.signal_pb_clicked.emit(65)

        
                