# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page99test.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Page99Test(object):
    def setupUi(self, Page99Test):
        if not Page99Test.objectName():
            Page99Test.setObjectName(u"Page99Test")
        Page99Test.resize(471, 351)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Page99Test.sizePolicy().hasHeightForWidth())
        Page99Test.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Page99Test)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayoutInfoTab = QGridLayout()
        self.gridLayoutInfoTab.setObjectName(u"gridLayoutInfoTab")
        self.labelInfoTitle = QLabel(Page99Test)
        self.labelInfoTitle.setObjectName(u"labelInfoTitle")
        self.labelInfoTitle.setAlignment(Qt.AlignCenter)

        self.gridLayoutInfoTab.addWidget(self.labelInfoTitle, 0, 0, 1, 1)

        self.labelInfoCopyright = QLabel(Page99Test)
        self.labelInfoCopyright.setObjectName(u"labelInfoCopyright")

        self.gridLayoutInfoTab.addWidget(self.labelInfoCopyright, 2, 0, 1, 1)

        self.labelInfoDetails = QLabel(Page99Test)
        self.labelInfoDetails.setObjectName(u"labelInfoDetails")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(98)
        sizePolicy1.setHeightForWidth(self.labelInfoDetails.sizePolicy().hasHeightForWidth())
        self.labelInfoDetails.setSizePolicy(sizePolicy1)
        self.labelInfoDetails.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.labelInfoDetails.setWordWrap(True)
        self.labelInfoDetails.setMargin(5)
        self.labelInfoDetails.setIndent(-4)

        self.gridLayoutInfoTab.addWidget(self.labelInfoDetails, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayoutInfoTab, 1, 1, 1, 1)


        self.retranslateUi(Page99Test)

        QMetaObject.connectSlotsByName(Page99Test)
    # setupUi

    def retranslateUi(self, Page99Test):
        Page99Test.setWindowTitle(QCoreApplication.translate("Page99Test", u"Page 99 Test", None))
#if QT_CONFIG(tooltip)
        Page99Test.setToolTip(QCoreApplication.translate("Page99Test", u"Page 99 Tool Tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Page99Test.setStatusTip(QCoreApplication.translate("Page99Test", u"Page 99 Status Tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Page99Test.setWhatsThis(QCoreApplication.translate("Page99Test", u"Page 99 Whats This", None))
#endif // QT_CONFIG(whatsthis)
        self.labelInfoTitle.setText(QCoreApplication.translate("Page99Test", u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Projectionist</span></h1></body></html>", None))
        self.labelInfoCopyright.setText(QCoreApplication.translate("Page99Test", u"<html><head/><body><p align=\"center\"><span style=\" font-size:small; font-weight:700;\">Copyright J2Casa 2023. All Rights Reserved</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.labelInfoDetails.setStatusTip(QCoreApplication.translate("Page99Test", u"Welcome Tab", None))
#endif // QT_CONFIG(statustip)
        self.labelInfoDetails.setText(QCoreApplication.translate("Page99Test", u"<html><head/><body><h4 align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt; font-weight:700;\">99 Test</span></h4></body></html>", None))
    # retranslateUi

