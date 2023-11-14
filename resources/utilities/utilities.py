# trunk-ignore-all(black)
#!/usr/bin/env python3
# coding: utf-8

""" Contains Utility Functions.
    
    This file is used to contain functions and modules
    that can be used throughout the application and do not
    need to be class specific.
"""
import typing

from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,  
    QWidget,  
)    

from PySide6.QtCore import (
    QCoreApplication,
)

from PySide6 import (
    QtGui,
    QtCore
)

def findMainWindow() -> typing.Union[QMainWindow, None]:
    # sourcery skip: use-next
    """ Get the MainWindow Object. """
    # app = QApplication.instance()
    for widget in QApplication.topLevelWidgets():
        if isinstance(widget, QMainWindow):
            return widget
    return None    