#!/usr/bin/env python3
# coding: utf-8

import os
import traceback
import pathlib

import sqlite3
from sqlite3 import Error

from classes.p2_database import ProjDatabase

class ProjTableSplash(ProjDatabase):
    """The Class for Splash Database Work. """
    ########################
    # Covered in Test 3a   #
    ########################

    def __init__(self, database) -> None:
        super().__init__(database)

        self.class_version = "0.0.5.dev"
        self.__str = "p2_db_splash"
        self.__repr = "p2_db_splash"
        self.__make_splash_table()
        self.__set_default_splash()

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
#          Splash related modules START                            #
####################################################################

    ########################
    # Covered in Test 2    #
    ########################
    def __make_splash_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Make the splash table. """
        status = True
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            # Create the Splash Table
            # ID Integer - Index Number
            # P1 Integer - Show or Hide 1 or 0
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Splash
                                (ID INTEGER NOT NULL DEFAULT 1 PRIMARY KEY,
                                P1  INT  NOT NULL DEFAULT 1) """)
            self.connection.commit()
        except Error as error_code:
            status = False
            self.module_error = float(self.module_index) + 0.0301
            self.module_error_message = \
                f"Unable to create {self.fullfile} \
                Splash Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

    ########################
    # Covered in Test 3c   #
    ########################
    def get_quantity_records_splash(self) -> int:
        # sourcery skip: extract-method, inline-immediately-returned-variable
        """ Return number of splash records. """
        status = -1
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()
            self.cursor.execute(""" SELECT COUNT(*) FROM Splash """)
            self.connection.commit()
            status = len(self.cursor.fetchall())
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0302
            self.module_error_message = \
                f"Unable to get number of Splash Records. \
                Error {error_code}"  # noqa: E501
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
    def __set_default_splash(self) -> bool:
        """ Set the default Splash. """
        return self.update_splash(1)
    ########################
    # Covered in Test 2 9  #
    ########################
    def update_splash(self, splash: int = 1) -> bool:
        """ Update the Splash Table. """
        status = False
        try:
            T1 = splash
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            self.cursor.execute(""" \
                REPLACE INTO Splash \
                (ID, P1) \
                VALUES (?, ?) """, \
                (1, T1))
            self.connection.commit()
            status = True
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0303
            self.module_error_message = \
                f"Unable to add setting {self.fullfile} \
                Splash Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

    ########################
    # Covered in Test 14   #
    ########################
    def __get_splash_record(self) -> list: # type: ignore
        # sourcery skip: use-named-expression
        """ Get the Splash Record. """
        retval=[]
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()
            self.cursor.execute(""" SELECT P1 FROM Splash WHERE ID = 1 """)
            self.connection.commit()
            records = self.cursor.fetchone()
            retval = [records[0]] if records else []
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0304
            self.module_error_message = \
                f"Unable to get setting {self.fullfile} \
                Splash Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore
        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return retval

    ########################
    # Covered in Test 14   #
    ########################
    def get_value_splash(self) -> int:
        """ Return Splash Value. """
        test_list = [0, 1]
        rec_list = self.__get_splash_record()
        retval = rec_list[0]
        exist_count = test_list.count(retval)
        if exist_count < 1:
            retval = 0
        return retval

####################################################################
#          Splash related modules END                              #
####################################################################
        