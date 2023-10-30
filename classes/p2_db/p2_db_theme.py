#!/usr/bin/env python3
# coding: utf-8

import os
import traceback
import pathlib

import sqlite3
from sqlite3 import Error

from classes.p2_database import ProjDatabase

class ProjTableTheme(ProjDatabase):
    """The Class for Theme Database Work. """
    ########################
    # Covered in Test 4a   #
    ########################

    def __init__(self, database) -> None:
        super().__init__(database)
        
        self.class_version = "0.0.5.dev"
        self.__str = "p2_db_theme"
        self.__repr = "p2_db_theme"
        self.__make_theme_table()
        self.__set_default_theme()

    ########################
    # Covered in Test 4b   #
    ########################
    def __str__(self) -> str:
        """ Return the __str__ Function. """
        return f"{self.__str}"

    ########################
    # Covered in Test 4c   #
    ########################
    def __repr__(self) -> str:
        """ Return the __repr__ Function. """
        return f"{self.__repr}"

####################################################################
#          Theme related modules START                             #
####################################################################

    ########################
    # Covered in Test 2    #
    ########################
    def __make_theme_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Make the theme table. """
        status = True
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            # Create the Theme Table
            # ID Integer - Index Number
            # P1 Text    - Name of the Theme
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Theme
                                (ID INTEGER NOT NULL DEFAULT 1 PRIMARY KEY,
                                P1  TEXT NOT NULL DEFAULT 'auto') """)
            self.connection.commit()
        except Error as error_code:
            status = False
            self.module_error = float(self.module_index) + 0.0201
            self.module_error_message = \
                f"Unable to create {self.fullfile} \
                Theme Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

    ########################
    # Covered in Test 3b   #
    ########################
    def get_quantity_records_theme(self) -> int:
        # sourcery skip: extract-method, inline-immediately-returned-variable
        """ Return number of theme records. """
        status = -1
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()
            self.cursor.execute(""" SELECT COUNT(*) FROM Theme """)
            self.connection.commit()
            status = len(self.cursor.fetchall())
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0202
            self.module_error_message = \
                f"Unable to get number of Theme Records. \
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

    ########################
    # Covered in Test 2    #
    ########################
    def __set_default_theme(self) -> bool:
        """ Set the default Theme. """
        return self.update_theme("auto")

    ########################
    # Covered in Test 2 8  #
    ########################
    def update_theme(self, theme: str ="auto") -> bool:
        """ Update the Theme Table. """
        status = False
        try:
            T1 = theme
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            self.cursor.execute(""" \
                REPLACE INTO Theme (ID, P1) \
                VALUES (?, ?) """, \
                (1, T1))
            self.connection.commit()
            status = True
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0203
            self.module_error_message = \
                f"Unable to add setting {self.fullfile} \
                Theme Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

    ########################
    # Covered in Test 12   #
    ########################
    def __get_theme_record(self) -> list:    # type: ignore
        # sourcery skip: use-named-expression
        """ Get the Theme Record. """
        retval=[]
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()
            self.cursor.execute(""" SELECT P1 FROM Theme WHERE ID = 1 """)
            self.connection.commit()
            records = self.cursor.fetchone()
            retval = [records[0]] if records else ["auto"]
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0204
            self.module_error_message = \
            f"Unable to get setting {self.fullfile} \
            Theme Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore
        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return retval

    ########################
    # Covered in Test 12   #
    ########################
    def get_value_theme(self) -> str:
        """ Return Theme. """
        test_list = ["auto", "dark", "light"]
        rec_list = self.__get_theme_record()
        retval = rec_list[0]
        exist_count = test_list.count(retval)
        if exist_count < 1:
            retval = "auto"
        return retval

####################################################################
#          Theme related modules END                               #
####################################################################
