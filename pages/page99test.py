import qdarktheme

from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget
)

from pages.page99test_ui import Ui_Page99Test


class Page99Test(QWidget, Ui_Page99Test):
    """Create the 99 Test Stacked Widget."""
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.labelInfoTitle.setStyleSheet("font-size:xx-large; font-weight:700;")
        self.labelInfoDetails.setStyleSheet("font-size:medium; font-weight:700;")
        self.labelInfoCopyright.setStyleSheet("font-size:small; font-weight:700;")
        