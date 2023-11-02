# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page02config.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import buttonsGlassRound_rc
import png_rc
import readfiles_rc
import splash_rc

class Ui_Page02Config(object):
    def setupUi(self, Page02Config):
        if not Page02Config.objectName():
            Page02Config.setObjectName(u"Page02Config")
        Page02Config.resize(474, 360)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Page02Config.sizePolicy().hasHeightForWidth())
        Page02Config.setSizePolicy(sizePolicy)
        Page02Config.setWindowTitle(u"Page 02 Config")
#if QT_CONFIG(tooltip)
        Page02Config.setToolTip(u"Page 02 Tool Tip")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Page02Config.setStatusTip(u"Page 02 Status Tip")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Page02Config.setWhatsThis(u"Page 02 Whats This")
#endif // QT_CONFIG(whatsthis)
        self.gridLayout = QGridLayout(Page02Config)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayoutPage = QGridLayout()
        self.gridLayoutPage.setObjectName(u"gridLayoutPage")
        self.labelTitle = QLabel(Page02Config)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setText(u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Configuration</span></h1></body></html>")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayoutPage.addWidget(self.labelTitle, 0, 0, 1, 1)

        self.groupBoxProjectFolder = QGroupBox(Page02Config)
        self.groupBoxProjectFolder.setObjectName(u"groupBoxProjectFolder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(5)
        sizePolicy1.setHeightForWidth(self.groupBoxProjectFolder.sizePolicy().hasHeightForWidth())
        self.groupBoxProjectFolder.setSizePolicy(sizePolicy1)
        self.groupBoxProjectFolder.setTitle(u"Project Folder Wizard")
        self.groupBoxProjectFolder.setFlat(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBoxProjectFolder)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayoutlabelTextProjectFolder = QVBoxLayout()
        self.verticalLayoutlabelTextProjectFolder.setObjectName(u"verticalLayoutlabelTextProjectFolder")
        self.labelTextProjectFolder = QLabel(self.groupBoxProjectFolder)
        self.labelTextProjectFolder.setObjectName(u"labelTextProjectFolder")
        self.labelTextProjectFolder.setText(u"<html><head/><body><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight:700;\">Please use the Wizard to locate your Master Project Folder.</span></h4></body></html>")
        self.labelTextProjectFolder.setMargin(1)

        self.verticalLayoutlabelTextProjectFolder.addWidget(self.labelTextProjectFolder)


        self.verticalLayout_4.addLayout(self.verticalLayoutlabelTextProjectFolder)

        self.verticalLayoutlineEditDisplayProjectFolder = QVBoxLayout()
        self.verticalLayoutlineEditDisplayProjectFolder.setObjectName(u"verticalLayoutlineEditDisplayProjectFolder")
        self.lineEditDisplayProjectFolder = QLineEdit(self.groupBoxProjectFolder)
        self.lineEditDisplayProjectFolder.setObjectName(u"lineEditDisplayProjectFolder")
        self.lineEditDisplayProjectFolder.setReadOnly(True)
        self.lineEditDisplayProjectFolder.setPlaceholderText(u"Master Project Folder Location")

        self.verticalLayoutlineEditDisplayProjectFolder.addWidget(self.lineEditDisplayProjectFolder)


        self.verticalLayout_4.addLayout(self.verticalLayoutlineEditDisplayProjectFolder)

        self.verticalLayoutButtonsProjectFolder = QVBoxLayout()
        self.verticalLayoutButtonsProjectFolder.setObjectName(u"verticalLayoutButtonsProjectFolder")
        self.horizontalLayoutButtonsProjectFolder = QHBoxLayout()
        self.horizontalLayoutButtonsProjectFolder.setObjectName(u"horizontalLayoutButtonsProjectFolder")
        self.horizontalSpacerProjectFolder = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutButtonsProjectFolder.addItem(self.horizontalSpacerProjectFolder)

        self.pushButtonWizardProjectFolder = QPushButton(self.groupBoxProjectFolder)
        self.pushButtonWizardProjectFolder.setObjectName(u"pushButtonWizardProjectFolder")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButtonWizardProjectFolder.sizePolicy().hasHeightForWidth())
        self.pushButtonWizardProjectFolder.setSizePolicy(sizePolicy2)
        self.pushButtonWizardProjectFolder.setMinimumSize(QSize(48, 48))
        self.pushButtonWizardProjectFolder.setMaximumSize(QSize(48, 48))
#if QT_CONFIG(tooltip)
        self.pushButtonWizardProjectFolder.setToolTip(u"Location Wizard")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonWizardProjectFolder.setStatusTip(u"Project Folder Location Wizard")
#endif // QT_CONFIG(statustip)
        icon = QIcon()
        icon.addFile(u":/buttons/glassRound/glassButtonWizard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonWizardProjectFolder.setIcon(icon)
        self.pushButtonWizardProjectFolder.setIconSize(QSize(48, 48))
#if QT_CONFIG(shortcut)
        self.pushButtonWizardProjectFolder.setShortcut(u"Ctrl+Alt+1")
#endif // QT_CONFIG(shortcut)
        self.pushButtonWizardProjectFolder.setFlat(True)

        self.horizontalLayoutButtonsProjectFolder.addWidget(self.pushButtonWizardProjectFolder)

        self.horizontalLayoutButtonsProjectFolder.setStretch(0, 97)

        self.verticalLayoutButtonsProjectFolder.addLayout(self.horizontalLayoutButtonsProjectFolder)


        self.verticalLayout_4.addLayout(self.verticalLayoutButtonsProjectFolder)


        self.gridLayoutPage.addWidget(self.groupBoxProjectFolder, 1, 0, 1, 1)

        self.groupBoxLocateApps = QGroupBox(Page02Config)
        self.groupBoxLocateApps.setObjectName(u"groupBoxLocateApps")
        sizePolicy1.setHeightForWidth(self.groupBoxLocateApps.sizePolicy().hasHeightForWidth())
        self.groupBoxLocateApps.setSizePolicy(sizePolicy1)
        self.groupBoxLocateApps.setTitle(u"Applications Locations Wizard")
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxLocateApps)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayoutApplicatiosWizardText = QVBoxLayout()
        self.verticalLayoutApplicatiosWizardText.setObjectName(u"verticalLayoutApplicatiosWizardText")
        self.labelTextApplicationsWizard = QLabel(self.groupBoxLocateApps)
        self.labelTextApplicationsWizard.setObjectName(u"labelTextApplicationsWizard")
        self.labelTextApplicationsWizard.setText(u"<html><head/><body><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight:700;\">Please locate applications using the Wizard.</span></h4></body></html>\n"
"")
        self.labelTextApplicationsWizard.setWordWrap(True)
        self.labelTextApplicationsWizard.setMargin(1)

        self.verticalLayoutApplicatiosWizardText.addWidget(self.labelTextApplicationsWizard)


        self.verticalLayout_2.addLayout(self.verticalLayoutApplicatiosWizardText)

        self.verticalLayoutApplicatiosWizardDetails = QVBoxLayout()
        self.verticalLayoutApplicatiosWizardDetails.setObjectName(u"verticalLayoutApplicatiosWizardDetails")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelTextLastRun = QLabel(self.groupBoxLocateApps)
        self.labelTextLastRun.setObjectName(u"labelTextLastRun")
        self.labelTextLastRun.setText(u"Last Run:")

        self.horizontalLayout.addWidget(self.labelTextLastRun)

        self.labelTextLastRunWhen = QLabel(self.groupBoxLocateApps)
        self.labelTextLastRunWhen.setObjectName(u"labelTextLastRunWhen")
        self.labelTextLastRunWhen.setText(u"Never")
        self.labelTextLastRunWhen.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelTextLastRunWhen)

        self.labelTextVersion = QLabel(self.groupBoxLocateApps)
        self.labelTextVersion.setObjectName(u"labelTextVersion")
        self.labelTextVersion.setText(u"Version:")

        self.horizontalLayout.addWidget(self.labelTextVersion)

        self.labelTextVersionYAML = QLabel(self.groupBoxLocateApps)
        self.labelTextVersionYAML.setObjectName(u"labelTextVersionYAML")
        self.labelTextVersionYAML.setText(u"0.0.0")

        self.horizontalLayout.addWidget(self.labelTextVersionYAML)

        self.labelTextInstalled = QLabel(self.groupBoxLocateApps)
        self.labelTextInstalled.setObjectName(u"labelTextInstalled")
        self.labelTextInstalled.setText(u"Installed:")

        self.horizontalLayout.addWidget(self.labelTextInstalled)

        self.labelTextInstallledQuantity = QLabel(self.groupBoxLocateApps)
        self.labelTextInstallledQuantity.setObjectName(u"labelTextInstallledQuantity")
        self.labelTextInstallledQuantity.setText(u"None")

        self.horizontalLayout.addWidget(self.labelTextInstallledQuantity)

        self.horizontalSpacerConfigureWizard = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacerConfigureWizard)


        self.verticalLayoutApplicatiosWizardDetails.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayoutApplicatiosWizardDetails)

        self.verticalLayoutButtonsApplications = QVBoxLayout()
        self.verticalLayoutButtonsApplications.setObjectName(u"verticalLayoutButtonsApplications")
        self.horizontalLayoutButtonsApplications = QHBoxLayout()
        self.horizontalLayoutButtonsApplications.setObjectName(u"horizontalLayoutButtonsApplications")
        self.horizontalSpacerApplications = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutButtonsApplications.addItem(self.horizontalSpacerApplications)

        self.pushButtonWizardApplications = QPushButton(self.groupBoxLocateApps)
        self.pushButtonWizardApplications.setObjectName(u"pushButtonWizardApplications")
        self.pushButtonWizardApplications.setMinimumSize(QSize(48, 48))
        self.pushButtonWizardApplications.setMaximumSize(QSize(48, 48))
        self.pushButtonWizardApplications.setIcon(icon)
        self.pushButtonWizardApplications.setIconSize(QSize(48, 48))
        self.pushButtonWizardApplications.setFlat(True)

        self.horizontalLayoutButtonsApplications.addWidget(self.pushButtonWizardApplications)


        self.verticalLayoutButtonsApplications.addLayout(self.horizontalLayoutButtonsApplications)


        self.verticalLayout_2.addLayout(self.verticalLayoutButtonsApplications)


        self.gridLayoutPage.addWidget(self.groupBoxLocateApps, 2, 0, 1, 1)

        self.labelCopyright = QLabel(Page02Config)
        self.labelCopyright.setObjectName(u"labelCopyright")
        self.labelCopyright.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-size:small; font-weight:700;\">Copyright J2Casa 2023. All Rights Reserved</span></p></body></html>")

        self.gridLayoutPage.addWidget(self.labelCopyright, 3, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayoutPage, 1, 1, 1, 1)


        self.retranslateUi(Page02Config)

        QMetaObject.connectSlotsByName(Page02Config)
    # setupUi

    def retranslateUi(self, Page02Config):
        self.pushButtonWizardProjectFolder.setText("")
        self.pushButtonWizardApplications.setText("")
        pass
    # retranslateUi

