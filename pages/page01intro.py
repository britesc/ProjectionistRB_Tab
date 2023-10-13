import qdarktheme

from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget
)

from pages.page01intro_ui import Ui_Page01Intro


class Page01Intro(QWidget, Ui_Page01Intro):
    """Create the Intro Stacked Widget."""
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.labelInfoTitle.setStyleSheet("font-size:xx-large; font-weight:700;")
        self.labelInfoDetails.setStyleSheet("font-size:medium; font-weight:700;")
        self.labelInfoCopyright.setStyleSheet("font-size:small; font-weight:700;")
        