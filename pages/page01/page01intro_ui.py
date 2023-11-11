# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page01intro.ui'
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
import buttonsGlassRound_rc
import png_rc
import readfiles_rc
import splash_rc

class Ui_Page01Intro(object):
    def setupUi(self, Page01Intro):
        if not Page01Intro.objectName():
            Page01Intro.setObjectName(u"Page01Intro")
        Page01Intro.resize(471, 351)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Page01Intro.sizePolicy().hasHeightForWidth())
        Page01Intro.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Page01Intro)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayoutPage = QGridLayout()
        self.gridLayoutPage.setObjectName(u"gridLayoutPage")
        self.labelTitle = QLabel(Page01Intro)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setText(u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Projectionist</span></h1></body></html>")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayoutPage.addWidget(self.labelTitle, 0, 0, 1, 1)

        self.labelDetails = QLabel(Page01Intro)
        self.labelDetails.setObjectName(u"labelDetails")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(98)
        sizePolicy1.setHeightForWidth(self.labelDetails.sizePolicy().hasHeightForWidth())
        self.labelDetails.setSizePolicy(sizePolicy1)
        self.labelDetails.setText(u"<html><head/><body><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Welcome to Projectionist.</span></h3><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight:700;\">In order to make use of this excellent application, it is first necessary to configure it.</span></h4><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight:700;\">It may also be necessary to add applications to the OS $PATH variable to ensure that they can be found and utilised correctly. This should be fairly easy to do.</span></h4><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight"
                        ":700;\">Once you are ready to commence the configuration, please click on the Configuration Tab and follow the instructions.</span></h4><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight:700;\">This application can been set to operate in a minimum size of 630 x 500, but can operate just as well or better in large sizes, including full screen.</span></h4></body></html>")
        self.labelDetails.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.labelDetails.setWordWrap(True)
        self.labelDetails.setMargin(5)
        self.labelDetails.setIndent(-4)

        self.gridLayoutPage.addWidget(self.labelDetails, 1, 0, 1, 1)

        self.labelCopyright = QLabel(Page01Intro)
        self.labelCopyright.setObjectName(u"labelCopyright")
        self.labelCopyright.setText(u"<html><head/><body><p align=\"center\" valign=\"bottom\"><span style=\" font-size:small; font-weight:700;\">Copyright J2Casa 2023. All Rights Reserved</span></p></body></html>")
        self.labelCopyright.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayoutPage.addWidget(self.labelCopyright, 2, 0, 1, 1, Qt.AlignBottom)


        self.gridLayout.addLayout(self.gridLayoutPage, 1, 1, 1, 1)


        self.retranslateUi(Page01Intro)

        QMetaObject.connectSlotsByName(Page01Intro)
    # setupUi

    def retranslateUi(self, Page01Intro):
        Page01Intro.setWindowTitle(QCoreApplication.translate("Page01Intro", u"Page 01 Intro", None))
#if QT_CONFIG(tooltip)
        Page01Intro.setToolTip(QCoreApplication.translate("Page01Intro", u"Page Tool Tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Page01Intro.setStatusTip(QCoreApplication.translate("Page01Intro", u"Page Status Tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Page01Intro.setWhatsThis(QCoreApplication.translate("Page01Intro", u"Page Whats This", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(statustip)
        self.labelDetails.setStatusTip(QCoreApplication.translate("Page01Intro", u"Welcome", None))
#endif // QT_CONFIG(statustip)
    # retranslateUi

