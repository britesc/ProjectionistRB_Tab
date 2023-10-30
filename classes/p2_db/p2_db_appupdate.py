#!/usr/bin/env python3
# coding: utf-8

import os
import traceback
import pathlib

import sqlite3
from sqlite3 import Error

from classes.p2_database import ProjDatabase

class ProjTableAppUpdate(ProjDatabase):
    """The Class for AppUpdate Database Work. """
    # AppUpdate Database Functions.

    def __init__(self, database) -> None:
        super().__init__(database)

        self.class_version = "0.0.5.dev"
        self.__str = "p2_db_appupdate"
        self.__repr = "p2_db_appupdate"
        self.__make_app_update_table()

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
#          App Update related modules  START                       #
####################################################################

    def __make_app_update_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Make the app_update table. """
        status = True
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            # Create the App Update Table
            # ID Integer
            # P1 Text    - Header Version
            # P2 Integer - Header Quantity
            # P3 Integer - Julian Date of File
            # P4 Integer - Julian Date of Install
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS AppUpdate
                                (ID INTEGER NOT NULL DEFAULT 1 PRIMARY KEY,
                                P1  TEXT    NOT NULL DEFAULT '' ,
                                P2  INTEGER NOT NULL DEFAULT 0,
                                P3  INTEGER NOT NULL DEFAULT 2440587,
                                P4  INTEGER NOT NULL DEFAULT 2440587
                                ) """)
            self.connection.commit()
            self.cursor.execute(""" CREATE INDEX IF NOT EXISTS AppUpdate1_idx ON AppUpdate (P1) """)
            self.connection.commit()
        except Error as error_code:
            status = False
            self.module_error = float(self.module_index) + 0.0601
            self.module_error_message = \
                f"Unable to create {self.fullfile} \
                App Update Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

    ########################
    # Covered in Test 3f   #
    ########################
    def get_records_app_update(self) -> int:
        # sourcery skip: extract-method, inline-immediately-returned-variable
        """ Return number of AppUpdate records. """
        status = -1
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()
            self.cursor.execute(""" SELECT COUNT(*) FROM AppUpdate """)
            self.connection.commit()
            status = len(self.cursor.fetchall())
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0602
            self.module_error_message = \
                f"Unable to get number of AppUpdate Records. \
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

    def __set_default_app_update(self) -> bool:
        """ Set the default Geometry. """
        return True

    def update_app_update(self) -> bool:
        """ Set Fictitious app update function. """
        return True

    def __get_app_update_record(self) -> bool:
        """ Get the Fictitious app update. """
        return True

    def get_app_update_record(self) -> list:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Return AppUpdate Values. """
        retval = []
        self.__get_app_update_record()
        return retval

####################################################################
#          App Update related modules END                          #
####################################################################
