#!/usr/bin/env python3
# coding: utf-8

"""Main Test and logging application for database class."""
from PySide6 import (
    QtCore
)

from classes import (
    p2_logging
)

def setup_app() -> None:
    """Create the Application Information."""
    QtCore.QCoreApplication.setOrganizationName("J2Casa")
    QtCore.QCoreApplication.setOrganizationDomain("j2casa.com")
    QtCore.QCoreApplication.setApplicationName("Projectionist")
    QtCore.QCoreApplication.setApplicationVersion("2.0.0.dev")

def main():
    """Call the Main Function to get us going."""  
    print("Starting Tests.")
    print("")
    print("\tSetting Script Path.")
    print("")

    print("\tConstruction Tests")
    print("\tTest 1 - Initialising Class as log_test")
    log_test = p2_logging.ProjLogging("logging")

    print("\tTest 2 - check_logging_exists")
    log_test.check_logging_exists()
    print("")

    print("\tTest 3 - change_logging_level")
    log_test.change_logging_level("logging")
    print("")

    print("\tTest 4 - current_logging_level")
    print(f"\tCurrent Level = {log_test.current_logging_level()}")    
    print("")
    
    print("\tTest 5 - log_entry at CRITICAL level")
    log_test.change_logging_level("CRITICAL")
    log_test.log_entry("logging",    "T5 - Logging Message")
    log_test.log_entry("INFO",     "T5 - Info Message")
    log_test.log_entry("WARNING",  "T5 - Warning Message")
    log_test.log_entry("ERROR",    "T5 - Error Message")
    log_test.log_entry("CRITICAL", "T5 - Critical Message")

    print("\tTest 6 - log_entry at ERROR level")
    log_test.change_logging_level("ERROR")
    log_test.log_entry("logging",    "T6 - Logging Message")
    log_test.log_entry("INFO",     "T6 - Info Message")
    log_test.log_entry("WARNING",  "T6 - Warning Message")
    log_test.log_entry("ERROR",    "T6 - Error Message")
    log_test.log_entry("CRITICAL", "T6 - Critical Message")

    print("\tTest 7 - log_entry at WARNING level")
    log_test.change_logging_level("WARNING")
    log_test.log_entry("logging",    "T7 - Logging Message")
    log_test.log_entry("INFO",     "T7 - Info Message")
    log_test.log_entry("WARNING",  "T7 - Warning Message")
    log_test.log_entry("ERROR",    "T7 - Error Message")
    log_test.log_entry("CRITICAL", "T7 - Critical Message")

    print("\tTest 8 - log_entry at INFO level")
    log_test.change_logging_level("INFO")
    log_test.log_entry("logging",    "T8 - Logging Message")
    log_test.log_entry("INFO",     "T8 - Info Message")
    log_test.log_entry("WARNING",  "T8 - Warning Message")
    log_test.log_entry("ERROR",    "T8 - Error Message")
    log_test.log_entry("CRITICAL", "T8 - Critical Message")

    print("\tTest 9 - log_entry at logging level")
    log_test.change_logging_level("logging")
    log_test.log_entry("logging",    "T9 - Logging Message")
    log_test.log_entry("INFO",     "T9 - Info Message")
    log_test.log_entry("WARNING",  "T9 - Warning Message")
    log_test.log_entry("ERROR",    "T9 - Error Message")
    log_test.log_entry("CRITICAL", "T9 - Critical Message")
    


    print("Ending Tests")

# Run the Application.
if __name__ == '__main__':
    setup_app()
    main()
