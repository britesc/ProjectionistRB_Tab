#!/usr/bin/env python3
# coding: utf-8

"""
Projectionist main startup code.

Includes
--------
import sys
import traceback
import qdarktheme

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication

from classes import p2_splash
from classes import  p2_logging
from classes.p2_db import p2_db_geometry
from classes.p2_db import p2_db_logging
from classes.p2_db import p2_db_splash
from classes.p2_db import p2_db_theme

from resources.utilities import utilities
from mainwindow import MainWindow
import buttonsGlassRound_rc

Methods
-------
setup_app() -> None:
    Set the Application Information.
    
main() -> None:
    Start the Main Function to get us going.
    
"""

import sys
import traceback
import qdarktheme


from PySide6 import (
    QtCore
)

from PySide6.QtWidgets import (
    QApplication
    # QSystemTrayIcon,
    # QMenu,
)

# from PySide6.QtGui import (
#     QAction,
#     QIcon,
# )

# from PySide6.QtCore import (
#     QCoreApplication,
# )

# from PySide6.QtWidgets import (
#     QMainWindow,
#     QPushButton
# )

# from PySide6.QtCore import (
#     Slot,
#     Signal
# )

from classes import (
    p2_splash,
    p2_logging
)

from classes.p2_db import(
    p2_db_geometry,
    p2_db_logging,
    p2_db_splash,
    p2_db_theme
)

from resources.utilities import utilities

from mainwindow import MainWindow

import buttonsGlassRound_rc  # noqa: F401

def setup_app() -> None:
    """ Set the Application Information. """
    QtCore.QCoreApplication.setOrganizationName("J2Casa")
    QtCore.QCoreApplication.setOrganizationDomain("j2casa.com")
    QtCore.QCoreApplication.setApplicationName("Projectionist")
    QtCore.QCoreApplication.setApplicationVersion("3.0.0.dev")

def main() -> None:  # sourcery skip: extract-method, remove-pass-body, remove-redundant-pass, swap-if-else-branches
    """ Start the Main Function to get us going. """
    try:
        app = QApplication(sys.argv)
        window = MainWindow(app)

        p_database_name = f"{QtCore.QCoreApplication.applicationName()}.db"

        use_splash = False
        use_logging  = False

        splash_db = p2_db_splash.ProjTableSplash(p_database_name)
        do_splash = splash_db.get_value_splash() # Tells us to use or not Splash
        if do_splash:
            use_splash = p2_splash.ProjSplash(app)
            use_splash.show(3)
        del splash_db

        theme_db = p2_db_theme.ProjTableTheme(p_database_name)
        if do_theme := theme_db.get_value_theme():
            qdarktheme.setup_theme(do_theme)
        del theme_db

        logging_db = p2_db_logging.ProjTableLogging(p_database_name)
        if do_logging := logging_db.get_value_logging():
            use_logging = p2_logging.ProjLogging(do_logging)
            use_logging.log_entry("INFO", "Logging Started")
        del logging_db

        window.show()
        if do_splash:
            use_splash.hide(window) # type: ignore

    except Exception as err:
        print("Unfortunately the Application has encountered an error \
and is unable to continue.")
        print(f"Exception {err=}, {type(err)=}")
        traceback.print_exc()
        traceback.print_exception() # type: ignore

    finally:
        temp_rect = window.geometry().getRect()  # type: ignore
        temp_list = utilities.convertRectToList(temp_rect)  # type: ignore
        geometry_db = p2_db_geometry.ProjTableGeometry(p_database_name)  # type: ignore
        geometry_db.update_geometry(temp_list)
        del geometry_db
        sys.exit(app.exec()) # type: ignore

if __name__ == '__main__':
    """ Where it all starts from. """
    setup_app()
    main()

