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

from PySide6.QtCore import (
    QCoreApplication
)


from classes import (
    p2_settings
)

from mainwindow import MainWindow

# trunk-ignore(ruff/F401)
import resources.buttonsGlassRound_rc  # noqa: F401


def setup_app() -> None:
    # trunk-ignore(ruff/D401)
    """Setup the Application Information."""
    QCoreApplication.setOrganizationName("J2Casa")
    QCoreApplication.setOrganizationDomain("j2casa.com")
    QCoreApplication.setApplicationName("Projectionist")    
    QCoreApplication.setApplicationVersion("2.0.0.dev")

def main():  # sourcery skip: remove-pass-body, remove-redundant-pass, swap-if-else-branches  # noqa: E501
    # trunk-ignore(ruff/D401)
    """Main Function to get us going."""
    try:
        app = QApplication(sys.argv)
        window = MainWindow(app)
        p_settings = p2_settings.P2_Settings()
        

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

            p_settings.create_tables()
            

            # settings.save_geometry(window.geometry())
            # settings.save_theme("dark")
            # settings.save_splash(True)
            
            # print(f"Geometry {settings.get_geometry()}")
            # print(f"Theme {settings.get_theme()}")
            # print(f"Splash {settings.get_splash()}")
        
            print(f"window geometry {window.geometry().getRect()}")
            
            qdarktheme.setup_theme(p_settings.get_theme()) 
            
        
        window.show()

    except Exception as err:
        print("Unfortunately the Application has encountered an error \
and is unable to continue.")
        print(f"Exception {err=}, {type(err)=}")
        traceback.print_exc()
        traceback.print_exception() # type: ignore

    finally:
        sys.exit(app.exec()) # type: ignore



if __name__ == '__main__':
    """Where it all starts from."""
    setup_app()
    main()
