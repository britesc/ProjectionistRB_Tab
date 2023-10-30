#!/usr/bin/env python3
# coding: utf-8

import os
import traceback
import pathlib

import sqlite3
from sqlite3 import Error

from classes.p2_database import ProjDatabase

class ProjTableLogging(ProjDatabase):
    """The Class for Logging Database Work. """
    # Logging Database Functions.

    def __init__(self, database) -> None:
        super().__init__(database)

        self.class_version = "0.0.5.dev"
        self.__str = "p2_db_logging"
        self.__repr = "p2_db_logging"
        self.__make_logging_table()
        self.__set_default_logging()

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
#          Logging related modules START                           #
####################################################################

    ########################
    # Covered in Test 2    #
    ########################
    def __make_logging_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Make the logging table. """
        status = True
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            # Create the Logging Table
            # ID Integer - Index Number
            # P1 Integer - Logging Value
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Logging
                                (ID INTEGER NOT NULL DEFAULT 1 PRIMARY KEY,
                                P1  INT  NOT NULL DEFAULT 0) """)
            self.connection.commit()
        except Error as error_code:
            status = False
            self.module_error = float(self.module_index) + 0.0401
            self.module_error_message = \
                f"Unable to create {self.fullfile} \
                Logging Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

    ########################
    # Covered in Test 3d   #
    ########################
    def get_records_logging(self) -> int:
        # sourcery skip: extract-method, inline-immediately-returned-variable
        """ Return number of logging records. """
        status = -1
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()
            self.cursor.execute(""" SELECT COUNT(*) FROM Logging """)
            self.connection.commit()
            status = len(self.cursor.fetchall())
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0402
            self.module_error_message = \
                f"Unable to get number of Logging Records. \
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
    def __set_default_logging(self) -> bool:
        """ Set the default Logging. """
        return self.update_logging(0)

    ########################
    # Covered in Test 2 10 #
    ########################
    def update_logging(self, logging: int = 0) -> bool:
        """ Update the Logging Table. """
        status = False
        try:
            T1 = logging
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            self.cursor.execute(""" \
                REPLACE INTO Logging \
                (ID, P1) \
                VALUES (?, ?) """, \
                (1, T1))
            self.connection.commit()
            status = True
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0403
            self.module_error_message = \
                f"Unable to add setting {self.fullfile} \
                Logging Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

    ########################
    # Covered in Test 13   #
    ########################
    def __get_logging_record(self) -> list:    # type: ignore
        # sourcery skip: use-named-expression
        """ Get the Logging Record. """
        retval=[]
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()
            self.cursor.execute(""" SELECT P1 FROM Logging WHERE ID = 1 """)
            self.connection.commit()
            records = self.cursor.fetchone()
            retval = [records[0]] if records else []
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0404
            self.module_error_message = \
                f"Unable to get setting {self.fullfile} \
                Logging Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore
        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return retval

    ########################
    # Covered in Test 13   #
    ########################
    def get_value_logging(self) -> int:
        """ Return Logging Value. """
        test_list = [0, 10, 20, 30, 40, 50]
        rec_list = self.__get_logging_record()
        retval = rec_list[0]
        exist_count = test_list.count(retval)
        if exist_count < 1:
            retval = 0
        return retval

####################################################################
#          Logging related modules END                               #
####################################################################
