#!/usr/bin/env python3
# coding: utf-8

import sys
import traceback
import qdarktheme


from PySide6.QtWidgets import (
    QApplication,
    QSystemTrayIcon,
    QMenu
)    

from PySide6.QtGui import (
    QAction,
    QIcon
)

from PySide6 import (
    QtCore
)

from classes import (
    p2_database,
    p2_splash
)

from mainwindow import MainWindow


import resources.buttonsGlassRound_rc  # noqa: F401

def setup_app() -> None:
    """Set the Application Information."""
    QtCore.QCoreApplication.setOrganizationName("J2Casa")
    QtCore.QCoreApplication.setOrganizationDomain("j2casa.com")
    QtCore.QCoreApplication.setApplicationName("Projectionist")
    QtCore.QCoreApplication.setApplicationVersion("3.0.0.dev")

def main():  # sourcery skip: remove-pass-body, remove-redundant-pass, swap-if-else-branches  # noqa: E501
    # trunk-ignore(ruff/D401)
    """Main Function to get us going."""
    try:
        app = QApplication(sys.argv)
        window = MainWindow(app)

        p_database_name = f"{QtCore.QCoreApplication.applicationName()}.db"
        print(f"Database Name 1 = {p_database_name}")
        p_database = p2_database.ProjDatabase(p_database_name)
        p_database.check_database_exists()

        do_splash = p_database.get_records_splash()
        do_theme  = p_database.get_records_theme()
        do_debug  = p_database.get_records_debug()
        del p_database

        if do_splash:
            use_splash = p2_splash.ProjSplash(app)
            use_splash.show(3)



        if not QSystemTrayIcon.isSystemTrayAvailable():
            pass
        else:

            app.setQuitOnLastWindowClosed(False)

            tray_icon = QIcon(u":/buttons/glassRound/glassButtonProjectionist.png")  # noqa: E501

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
            action2.setIcon(QIcon(u":/buttons/glassRound/glassButtonQuit.png"))
            tray_menu.addAction(action2)

            tray.setContextMenu(tray_menu)

            print(f"window geometry {window.geometry().getRect()}")

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
        print(f"window geometry {window.geometry().getRect()}")
        sys.exit(app.exec()) # type: ignore



if __name__ == '__main__':
    """Where it all starts from."""
    setup_app()
    main()
