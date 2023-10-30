#!/usr/bin/env python3
# coding: utf-8
""" Projectionist Database Functions and Modules. """

import os
import traceback
import pathlib

import sqlite3
from sqlite3 import Error

from PySide6.QtCore import QRect

class ProjDatabase:
    """The Class for Database Work. """
    ########################
    # Covered in Test 1a   #
    ########################
    def __init__(self, database) -> None:
        # sourcery skip: aug-assign, remove-redundant-pass, remove-unnecessary-cast
        """ Init for Database Work. """
        super().__init__()

        self.class_version = "0.0.4.dev"
        self.module_index = "10"
        self.author_name = "Julian Bourne"
        self.__str = "p2_database"
        self.__repr = "p2_database"        
        # self.script_path = pathlib.Path(__file__).parent.resolve()
        # path = os.getcwd()
        # self.script_path = os.path.abspath(os.path.join(path, os.pardir))
        self.script_path = pathlib.Path(__file__).parent.resolve().parents[0]
        self.database_path = rf"{self.script_path}/db"
        self.database = database
        # print(f"Database Name 2 = {self.database}")

        self.fullfile = rf"{self.database_path}/{self.database}"
        self.module_error = 0.0
        self.module_error_message = "No Error"
        self.connection = None
        self.cursor = None

        self.db_good = self.check_database_exists()

    ########################
    # Covered in Test 1b   #
    ########################
    def __str__(self) -> str:
        """ Return the __str__ Function. """
        return f"{self.__str}"

    ########################
    # Covered in Test 1c   #
    ########################
    def __repr__(self) -> str:
        """ Return the __repr__ Function. """
        return f"{self.__repr}"

    ########################
    # Covered in Test 1d   #
    ########################
    def get_class_version(self) -> str:
        """Return the Version String of this Class."""
        return self.class_version

    ########################
    # Covered in Test 1e   #
    ########################
    def get_author_name(self) -> str:
        """Return the Author String of this Class."""
        return self.author_name

    ########################
    # Covered in Test 1f   #
    ########################
    def get_module_index(self) -> str:
        """Return the Module Index."""
        return self.module_index

####################################################################
#          Make the database location and name it                  #
####################################################################

    ########################
    # Covered in Test 1g   #
    ########################
    def check_database_exists(self) -> bool:
        """Check Database has been created and has default values. """
        looper = True
        # Internal Only Functions.
        looper = self.__make_database_location()
        looper = self.__make_database()
        return looper

    ########################
    # Covered in Test 1g   #
    ########################
    def __make_database_location(self) -> bool:
        """ Make database folder. """
        status = True
        try:
            if not os.path.exists(self.database_path):
                os.makedirs(self.database_path)
        except OSError as error_code:  # noqa: E999
            status = False
            self.module_error = float(self.module_index) + 0.0001
            self.module_error_message = \
            f"Unable to create {self.database_path} \
            folder. OSError {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore
        # finally:
        return status

    ########################
    # Covered in Test 1g   #
    ########################
    def __make_database(self) -> bool:  # sourcery skip: extract-method
        """ Make the database. """
        status = True
        try:
            if not os.path.isfile(self.fullfile):
                self.connection = sqlite3.connect(self.fullfile, timeout=10000)
        except Error as error_code:
            status = False
            self.module_error = float(self.module_index) + 0.0002
            self.module_error_message = \
            f"Unable to create {self.fullfile} \
            Database. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore
        finally:
            if self.connection:
                self.connection.close()
        return status

    ########################
    # Covered in Test 1h   #
    ########################
    def get_database_name(self) -> str:
        """ Return Name of Database. """
        return self.database

    ########################
    # Covered in Test 1i   #
    ########################
    def get_database_path(self) -> str:
        """ Return Name of Database. """
        return self.database_path

    ########################
    # Covered in Test 1j   #
    ########################
    def get_database_fullname(self) -> str:
        """ Return Name of Database. """
        return self.fullfile
