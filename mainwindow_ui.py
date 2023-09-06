# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)
import resources.buttonsGlassRound_rc
import resources.png_rc
import resources.readfiles_rc
import resources.splash_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1197, 589)
        icon = QIcon()
        icon.addFile(u":/Images/png/projectionist.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_New = QAction(MainWindow)
        self.action_New.setObjectName(u"action_New")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/glassRound/glassButtonNew.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_New.setIcon(icon1)
        self.action_Open = QAction(MainWindow)
        self.action_Open.setObjectName(u"action_Open")
        icon2 = QIcon()
        icon2.addFile(u":/buttons/glassRound/glassButtonOpen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Open.setIcon(icon2)
        self.action_Close = QAction(MainWindow)
        self.action_Close.setObjectName(u"action_Close")
        icon3 = QIcon()
        icon3.addFile(u":/buttons/glassRound/glassButtonClose.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Close.setIcon(icon3)
        self.action_Quit = QAction(MainWindow)
        self.action_Quit.setObjectName(u"action_Quit")
        icon4 = QIcon()
        icon4.addFile(u":/buttons/glassRound/glassButtonExit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Quit.setIcon(icon4)
        self.action_Help_Master = QAction(MainWindow)
        self.action_Help_Master.setObjectName(u"action_Help_Master")
        icon5 = QIcon()
        icon5.addFile(u":/buttons/glassRound/glassButtonHelp2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Help_Master.setIcon(icon5)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_1_Top = QVBoxLayout()
        self.verticalLayout_1_Top.setObjectName(u"verticalLayout_1_Top")
        self.horizontalLayout_RibbonBar = QHBoxLayout()
        self.horizontalLayout_RibbonBar.setObjectName(u"horizontalLayout_RibbonBar")
        self.gridLayout_1_Left = QGridLayout()
        self.gridLayout_1_Left.setSpacing(0)
        self.gridLayout_1_Left.setObjectName(u"gridLayout_1_Left")
        self.pushButton_R0C0 = QPushButton(self.centralwidget)
        self.pushButton_R0C0.setObjectName(u"pushButton_R0C0")
        self.pushButton_R0C0.setMinimumSize(QSize(64, 64))
        self.pushButton_R0C0.setMaximumSize(QSize(64, 64))
        self.pushButton_R0C0.setAutoFillBackground(False)
        self.pushButton_R0C0.setIcon(icon)
        self.pushButton_R0C0.setIconSize(QSize(64, 64))
        self.pushButton_R0C0.setFlat(True)

        self.gridLayout_1_Left.addWidget(self.pushButton_R0C0, 0, 0, 2, 2)

        self.pushButton_R0C2 = QPushButton(self.centralwidget)
        self.pushButton_R0C2.setObjectName(u"pushButton_R0C2")
        self.pushButton_R0C2.setMinimumSize(QSize(32, 32))
        self.pushButton_R0C2.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Left.addWidget(self.pushButton_R0C2, 0, 2, 1, 1)

        self.pushButton_R0C3 = QPushButton(self.centralwidget)
        self.pushButton_R0C3.setObjectName(u"pushButton_R0C3")
        self.pushButton_R0C3.setMinimumSize(QSize(32, 32))
        self.pushButton_R0C3.setMaximumSize(QSize(32, 32))
        icon6 = QIcon()
        icon6.addFile(u":/Images/png/arrowdown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_R0C3.setIcon(icon6)
        self.pushButton_R0C3.setIconSize(QSize(16, 16))
        self.pushButton_R0C3.setFlat(True)

        self.gridLayout_1_Left.addWidget(self.pushButton_R0C3, 0, 3, 1, 1)

        self.pushButton_R1C2 = QPushButton(self.centralwidget)
        self.pushButton_R1C2.setObjectName(u"pushButton_R1C2")
        self.pushButton_R1C2.setMinimumSize(QSize(32, 32))
        self.pushButton_R1C2.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Left.addWidget(self.pushButton_R1C2, 1, 2, 1, 1)

        self.pushButton_R1C3 = QPushButton(self.centralwidget)
        self.pushButton_R1C3.setObjectName(u"pushButton_R1C3")
        self.pushButton_R1C3.setMinimumSize(QSize(32, 32))
        self.pushButton_R1C3.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Left.addWidget(self.pushButton_R1C3, 1, 3, 1, 1)

        self.pushButton_R2C0 = QPushButton(self.centralwidget)
        self.pushButton_R2C0.setObjectName(u"pushButton_R2C0")
        self.pushButton_R2C0.setMinimumSize(QSize(32, 32))
        self.pushButton_R2C0.setMaximumSize(QSize(32, 32))
        icon7 = QIcon()
        icon7.addFile(u":/Images/png/help2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_R2C0.setIcon(icon7)
        self.pushButton_R2C0.setIconSize(QSize(32, 32))
        self.pushButton_R2C0.setFlat(True)

        self.gridLayout_1_Left.addWidget(self.pushButton_R2C0, 2, 0, 1, 1)

        self.pushButton_R2C1 = QPushButton(self.centralwidget)
        self.pushButton_R2C1.setObjectName(u"pushButton_R2C1")
        self.pushButton_R2C1.setMinimumSize(QSize(32, 32))
        self.pushButton_R2C1.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Left.addWidget(self.pushButton_R2C1, 2, 1, 1, 1)

        self.pushButton_R2C2 = QPushButton(self.centralwidget)
        self.pushButton_R2C2.setObjectName(u"pushButton_R2C2")
        self.pushButton_R2C2.setMinimumSize(QSize(32, 32))
        self.pushButton_R2C2.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Left.addWidget(self.pushButton_R2C2, 2, 2, 1, 1)

        self.pushButton_R2C3 = QPushButton(self.centralwidget)
        self.pushButton_R2C3.setObjectName(u"pushButton_R2C3")
        self.pushButton_R2C3.setMinimumSize(QSize(32, 32))
        self.pushButton_R2C3.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Left.addWidget(self.pushButton_R2C3, 2, 3, 1, 1)

        self.pushButton_R3C0 = QPushButton(self.centralwidget)
        self.pushButton_R3C0.setObjectName(u"pushButton_R3C0")
        self.pushButton_R3C0.setMinimumSize(QSize(32, 32))
        self.pushButton_R3C0.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Left.addWidget(self.pushButton_R3C0, 3, 0, 1, 1)

        self.pushButton_R3C1 = QPushButton(self.centralwidget)
        self.pushButton_R3C1.setObjectName(u"pushButton_R3C1")
        self.pushButton_R3C1.setMinimumSize(QSize(32, 32))
        self.pushButton_R3C1.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Left.addWidget(self.pushButton_R3C1, 3, 1, 1, 1)

        self.pushButton_R3C2 = QPushButton(self.centralwidget)
        self.pushButton_R3C2.setObjectName(u"pushButton_R3C2")
        self.pushButton_R3C2.setMinimumSize(QSize(32, 32))
        self.pushButton_R3C2.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Left.addWidget(self.pushButton_R3C2, 3, 2, 1, 1)

        self.pushButton_R3C3 = QPushButton(self.centralwidget)
        self.pushButton_R3C3.setObjectName(u"pushButton_R3C3")
        self.pushButton_R3C3.setMinimumSize(QSize(32, 32))
        self.pushButton_R3C3.setMaximumSize(QSize(32, 32))
        icon8 = QIcon()
        icon8.addFile(u":/Images/png/arrowup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_R3C3.setIcon(icon8)
        self.pushButton_R3C3.setFlat(True)

        self.gridLayout_1_Left.addWidget(self.pushButton_R3C3, 3, 3, 1, 1)


        self.horizontalLayout_RibbonBar.addLayout(self.gridLayout_1_Left)

        self.tabWidget_Ribbon_Bar = QTabWidget(self.centralwidget)
        self.tabWidget_Ribbon_Bar.setObjectName(u"tabWidget_Ribbon_Bar")

        self.horizontalLayout_RibbonBar.addWidget(self.tabWidget_Ribbon_Bar)


        self.verticalLayout_1_Top.addLayout(self.horizontalLayout_RibbonBar)


        self.verticalLayout_2.addLayout(self.verticalLayout_1_Top)

        self.verticalLayout_2_Bottom = QVBoxLayout()
        self.verticalLayout_2_Bottom.setObjectName(u"verticalLayout_2_Bottom")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_Home = QWidget()
        self.page_Home.setObjectName(u"page_Home")
        self.stackedWidget.addWidget(self.page_Home)
        self.page_Edit = QWidget()
        self.page_Edit.setObjectName(u"page_Edit")
        self.stackedWidget.addWidget(self.page_Edit)

        self.verticalLayout_2_Bottom.addWidget(self.stackedWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout_2_Bottom)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 999)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton_R0C0.setDefault(False)
        self.tabWidget_Ribbon_Bar.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Projectionist", None))
        self.action_New.setText(QCoreApplication.translate("MainWindow", u"&New", None))
#if QT_CONFIG(tooltip)
        self.action_New.setToolTip(QCoreApplication.translate("MainWindow", u"Open New...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_New.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_Open.setText(QCoreApplication.translate("MainWindow", u"&Open", None))
#if QT_CONFIG(tooltip)
        self.action_Open.setToolTip(QCoreApplication.translate("MainWindow", u"Open...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_Close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
#if QT_CONFIG(shortcut)
        self.action_Close.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.action_Quit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
#if QT_CONFIG(tooltip)
        self.action_Quit.setToolTip(QCoreApplication.translate("MainWindow", u"Quit", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Quit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_Help_Master.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(tooltip)
        self.action_Help_Master.setToolTip(QCoreApplication.translate("MainWindow", u"Open Help...", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_R0C0.setText("")
        self.pushButton_R0C2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_R0C3.setText("")
        self.pushButton_R1C2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_R1C3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_R2C0.setText("")
        self.pushButton_R2C1.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_R2C2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_R2C3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_R3C0.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_R3C1.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_R3C2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_R3C3.setText("")
    # retranslateUi

