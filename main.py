#!/usr/bin/env python3
# coding: utf-8

import sys
import traceback
import qdarktheme


from PySide6 import (
    QtCore
)

from PySide6.QtWidgets import (
    QApplication,
    QSystemTrayIcon,
    QMenu,
)

from PySide6.QtGui import (
    QAction,
    QIcon,
)

from PySide6.QtCore import (
    QCoreApplication,
)

from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton
)

from classes import (
    p2_splash,
    p2_logging
)

from classes.p2_db import(
    # p2_db_geometry,
    p2_db_logging,
    p2_db_splash,
    p2_db_theme
)

from mainwindow import MainWindow

from resources import buttonsGlassRound_rc  # noqa: F401

def setup_app() -> None:
    """Set the Application Information."""
    QtCore.QCoreApplication.setOrganizationName("J2Casa")
    QtCore.QCoreApplication.setOrganizationDomain("j2casa.com")
    QtCore.QCoreApplication.setApplicationName("Projectionist")
    QtCore.QCoreApplication.setApplicationVersion("3.0.0.dev")

def main():    # sourcery skip: remove-pass-body, remove-redundant-pass, swap-if-else-branches  # noqa: E501
    # trunk-ignore(ruff/D401)
    """Main Function to get us going."""
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

        if not QSystemTrayIcon.isSystemTrayAvailable():
            pass
        else:

            app.setQuitOnLastWindowClosed(False)

            tray_icon = QIcon(":/buttons/glassRound/glassButtonProjectionist.png")  # noqa: E501

            tray = QSystemTrayIcon()
            tray.setIcon(tray_icon)
            tray.setVisible(True)


            tray_menu = QMenu()
            action1 = QAction("Show")
            action1.triggered.connect(window.showNormal) # type: ignore
            action1.triggered.connect(window.activateWindow) # type: ignore
            action1.triggered.connect(window.raise_) # type: ignore
            action1.setIcon(QIcon(u":/buttons/glassRound/glassButtonProjectionist.png"))
            tray_menu.addAction(action1)

            action2 = QAction("Quit")
            action2.triggered.connect(app.quit) # type: ignore
            action2.setIcon(QIcon(":/buttons/glassRound/glassButtonQuit.png"))
            tray_menu.addAction(action2)

            tray.setContextMenu(tray_menu)

            print(f"window geometry 1. {window.geometry().getRect()}")

            # qdarktheme.setup_theme(p_settings.get_theme())
        window.show()
        if do_splash:
            use_splash.hide(window)

    except Exception as err:
        print("Unfortunately the Application has encountered an error \
and is unable to continue.")
        print(f"Exception {err=}, {type(err)=}")
        traceback.print_exc()
        traceback.print_exception() # type: ignore

    finally:
        print(f"window geometry 2. {window.geometry().getRect()}")
        sys.exit(app.exec()) # type: ignore



if __name__ == '__main__':
    """ Where it all starts from. """
    setup_app()
    main()

