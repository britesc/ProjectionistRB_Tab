#!/usr/bin/env python3
# coding: utf-8

import os
import traceback
import pathlib

import sqlite3
from sqlite3 import Error

from classes.p2_database import ProjDatabase

class ProjTablePFolder(ProjDatabase):
    """The Class for Project Folder Database Work. """
    # Project Folder Database Functions.

    def __init__(self, database) -> None:
        super().__init__(database)

        self.class_version = "0.0.5.dev"
        self.__str = "p2_db_pfolder"
        self.__repr = "p2_db_pfolder"      
        self.__make_project_folder_table()

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
#          Project Folder related modules START                    #
####################################################################

    def __make_project_folder_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Make the project folder table. """
        status = True
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            # Create the Project Folder Table
            # ID Integer - Index Number
            # P1 Text    - Name of the Project Folder
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS PFolder
                                (ID INTEGER NOT NULL DEFAULT 1 PRIMARY KEY,
                                P1  TEXT NOT NULL) """)
            self.connection.commit()
        except Error as error_code:
            status = False
            self.module_error = float(self.module_index) + 0.0501
            self.module_error_message = \
                f"Unable to create {self.fullfile} \
                Project Folder Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

    ########################
    # Covered in Test 3e   #
    ########################
    def get_records_project_folder(self) -> int:
        # sourcery skip: extract-method, inline-immediately-returned-variable
        """ Return number of project folder records. """
        status = -1
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()
            self.cursor.execute(""" SELECT COUNT(*) FROM PFolder """)
            self.connection.commit()
            status = len(self.cursor.fetchall())
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0502
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

    def update_project_folder(self, theme: str ="") -> bool:
        """ Update the PFolder Table. """
        status = False
        try:
            T1 = theme
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            self.cursor.execute(""" \
                REPLACE INTO PFolder \
                (ID, P1) \
                VALUES (?, ?) """, \
                (1, T1))
            self.connection.commit()
            status = True
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0503
            self.module_error_message = \
                f"Unable to add setting {self.fullfile} \
                PFolder Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

####################################################################
#          Project Folder related modules END                      #
####################################################################
