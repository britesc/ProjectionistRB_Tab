import qdarktheme

from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QFileDialog,
    QPushButton,
    QLineEdit 
)

from PySide6 import (
    QtCore,
    QtGui,
)
from PySide6.QtGui import QActionEvent

from pages.pageXXconfig import Ui_Page02Config


from wizards import (
    appwizard
)


class Page02Config(QWidget, Ui_Page02Config):
    """Create the Config Stacked Widget."""    
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  # type: ignore
    
        self.jSettings = j2_settings.J2_Settings()
        self.pfLocation = self.jSettings.getSetting("Project/Folder", "")
        self.HeaderDate = self.jSettings.getHeaderDate()
        self.YamlVersion = self.jSettings.getHeaderVersion()
        self.AppQuantity = self.jSettings.getHeaderQuantity()
        self.AppQuantityString = str(self.AppQuantity)
        self.AppWizard =  appwizard.AppWizard() 
        
                
        # Populate Home Folder Path                    
        self.lineEditDisplayProjectFolder.setText(self.pfLocation)
        
        # Populate Applications Wizard
        # Last Run
        self.labelTextLastRunWhen.setText(self.HeaderDate)
        self.labelTextVersionYAML.setText(self.YamlVersion)
        self.labelTextInstalledQuantity.setText(self.AppQuantityString)

        # Signals and Slots
        
        self.pushButtonWizardProjectFolder.clicked.connect(self.loadTheFileDialog)
        self.pushButtonWizardProjectFolder.setDefault(False)
        self.pushButtonWizardApplications.clicked.connect(self.loadTheAppWizard)
        self.pushButtonWizardApplications.setDefault(False)

        
    def loadTheFileDialog(self) -> None:
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.jSettings.setSetting("Project/Folder", folderpath)
        self.lineEditDisplayProjectFolder.setText(self.ProjectFolder)       
                
    def loadTheAppWizard(self) -> None:
        # self.AppWizard.show()
        print("loadTheAppWizard Called Why?")