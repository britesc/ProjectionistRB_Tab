#!/usr/bin/env python3
# coding: utf-8

"""Main Test and debug application for database class."""
from PySide6 import (
    QtCore
)

from classes import (
    p2_database
)
def setup_app() -> None:
    """Set the Application Information."""
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
    print("\tTest 1 - Initialising Class as Db Test1")
    db_test = p2_database.ProjDatabase("Test1.db")

    print("\tTest 2 - check_database_exists")
    db_test.check_database_exists()
    print("")

    print("\tGet Records Tests")    
    # print("\tTest 3 - get_records_geometry")
    print(f"\tTest 3 - get_records_geometry = {db_test.get_records_geometry()}")

    # print("\tTest 4 - get_records_theme")
    print(f"\tTest 4 - get_records_theme = {db_test.get_records_theme()}")

    # print("\tTest 5 - get_records_splash")
    print(f"\tTest 5 - get_records_splash = {db_test.get_records_splash()}")

    # print("\tTest 6 - get_records_debug")
    print(f"\tTest 6 - get_records_debug = {db_test.get_records_debug()}")
    print("")

    print("\tUpdate Tests")    
    print("\tTest 7  - update_geometry (1,2,3,4)")
    db_test.update_geometry(1,2,3,4)

    print("\tTest 8  - update_theme 'dark'")
    db_test.update_theme("dark")

    print("\tTest 9  - update_splash 0")
    db_test.update_splash(0)

    print("\tTest 10 - update_debug 50")
    db_test.update_debug(50)
    print("")

    print("\tGet Records Test")
    # print("Test 11 - get_geometry_record")
    print(f"\tTest 11 - get_geometry_record = {db_test.get_geometry_record()}")

    # print("Test 12 - get_theme_record")
    print(f"\tTest 12 - get_theme_record = {db_test.get_theme_record()}")

    # print("Test 13 - get_debug_record")
    print(f"\tTest 13 - get_debug_record = {db_test.get_debug_record()}")  

    # print("Test 14 - get_splash_record")
    print(f"\tTest 14 - get_splash_record = {db_test.get_splash_record()}")  
    print("")

    print("Ending Tests")

# Run the Application.
if __name__ == '__main__':
    setup_app()
    main()
