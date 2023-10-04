#!/usr/bin/env python3
# coding: utf-8
from time import time

from PySide6.QtWidgets import QSplashScreen
from PySide6.QtGui import QPixmap


class ProjSplash:
    """The Class for Splash Work."""

    def __init__(self, app) -> None:
        """ Init for Splash. """
        super().__init__()
        self.app = app
        self.class_version = "0.0.3.dev"
        self.module_index = "12"
        self.author_name = "Julian Bourne"
        
        pixmap = QPixmap(u"resources/Images/png/splash.png")
        self.splash = QSplashScreen(pixmap)

    def __str__(self) -> str:
        """ Return the __str__ Function. """
        return "p2_splash"

    def __repr__(self) -> str:
        """ Return the __repr__ Function. """
        return "p2_splash"

    def get_class_version(self) -> str:
        """Return the Version String of this Class."""
        return self.class_version

    def get_author_name(self) -> str:
        """Return the Author String of this Class."""
        return self.author_name

    def get_module_index(self) -> str:
        """Return the Module Index."""
        return self.module_index

    def show(self, duration: int) -> None:
        """ Display the Splash Screen. """
        self.splash.show()

        while duration > 0:
            self.__splash_sleep(duration)

            self.app.processEvents()
            duration -= 1

    def hide(self, window) -> None:
        """ Hide the Splash Screen. """
        self.app.processEvents()
        self.splash.finish(window)

    def __splash_sleep(self, secs) -> None:
        """ Create an Alternative to Python Sleep. """
        init_time = time()
        while time() < init_time+secs:
            pass