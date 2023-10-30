#!/usr/bin/env python3
# coding: utf-8

import os
import traceback
import pathlib

import sqlite3
from sqlite3 import Error

from classes.p2_database import ProjDatabase

class ProjTableApps(ProjDatabase):
    """The Class for Apps Database Work. """
    # Project Apps Database Functions.

    def __init__(self, database) -> None:
        super().__init__(database)

        self.class_version = "0.0.5.dev"
        self.__str = "p2_db_apps"
        self.__repr = "p2_db_apps"
        self.__make_apps_table()

    ########################
    # Covered in Test 3b   #
    ########################
    def __str__(self) -> str:
        """ Return the __str__ Function. """
        return f"{self.__str}"

    ########################
    # Covered in Test 3c   #
    ########################
    def __repr__(self) -> str:
        """ Return the __repr__ Function. """
        return f"{self.__repr}"

####################################################################
#          Apps related modules START                              #
####################################################################

    def __make_apps_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Make the apps table. """
        status = True
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            if not self.connection:
                raise Error("No Connection to database")
            self.cursor = self.connection.cursor()

            # Create the Apps Table
            # ID Integer - Index Number
            # P1 Text    - Name of the App
            # P2 Text    - Alias of the App
            # P3 Text    - Location of the App
            # P4 Text    - Version of the App at Creation
            # P5 Text    - Type of App
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Apps
                                (ID INTEGER NOT NULL DEFAULT 1 PRIMARY KEY,
                                P1  TEXT NOT NULL  DEFAULT '',
                                P2  TEXT NOT NULL  DEFAULT '',
                                P3  TEXT NOT NULL  DEFAULT '',
                                P4  TEXT NOT NULL  DEFAULT '',
                                P5  TEXT NOT NULL  DEFAULT '') """)
            self.connection.commit()
            self.cursor.execute(""" CREATE INDEX IF NOT EXISTS Apps1_idx ON Apps (P1) """)
            self.connection.commit()
            self.cursor.execute(""" CREATE INDEX IF NOT EXISTS Apps2_idx ON Apps (P2) """)
            self.connection.commit()
            self.cursor.execute(""" CREATE INDEX IF NOT EXISTS Apps5_idx ON Apps (P5) """)
            self.connection.commit()
        except Error as error_code:
            status = False
            self.module_error = float(self.module_index) + 0.0701
            self.module_error_message = \
                f"Unable to create {self.database_path} \
                Apps Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

    def get_records_apps(self) -> int:
        # sourcery skip: extract-method, inline-immediately-returned-variable
        """ Return number of Apps records. """
        status = -1
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()
            self.cursor.execute(""" SELECT COUNT(*) FROM Apps """)
            self.connection.commit()
            status = len(self.cursor.fetchall())
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0702
            self.module_error_message = \
                f"Unable to get number of Apps Records. \
                Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore
            status = -1
        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status # type: ignore

    def __set_default_apps(self) -> bool:
        """ Set the default apps. """
        return True

    def update_apps(self) -> bool:
        """ Set Fictitious apps function. """
        return True

    def __get_apps_record(self) -> bool:
        """ Get the Fictitious apps. """
        return True

    def get_apps_record(self) -> list:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Return AppUpdate Values. """
        retval = []
        self.__get_apps_record()
        return retval

####################################################################
#          Apps related modules END                                #
####################################################################
