import qdarktheme

from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget
)

from pages.page02.page02config_ui import Ui_Page02Config


class Page02Config(QWidget, Ui_Page02Config):
    """ Create the 02 Config Stacked Widget. """
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.labelTitle.setStyleSheet("font-size:xx-large; font-weight:700;")
        self.labelTextProjectFolder.setStyleSheet("font-size:medium; font-weight:700;")
        self.labelCopyright.setStyleSheet("font-size:small; font-weight:700;")
