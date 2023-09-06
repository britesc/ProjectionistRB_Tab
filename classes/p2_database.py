#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import traceback

import sqlite3
from sqlite3 import Error

class ProjDatabase:
    """The Class for Database work."""
    def __init__(self) -> None:
        # sourcery skip: aug-assign, remove-redundant-pass, remove-unnecessary-cast
        """Init for Settings."""   
        super().__init__()
        self.class_version = "0.0.1.dev"
        self.module_index = "10"
        self.author_name = "Julian Bourne"
        self.database_path = r"db"
        self.database = r"projectionistTest.db"
        self.fullfile = rf"{self.database_path}/{self.database}"
        self.module_error = float(self.module_error)
        self.module_error_message = "No Error"
        self.connection = None
        self.cursor = None
        
        looper = True
        while looper:
            looper = self.__make_database_location()
            looper = self.__make_database()
            looper = self.__make_geometry_table()
            looper = self.__make_theme_table()
            looper = self.__make_splash_table()
            break

    def __make_database_location(self) -> bool:
        """Make database folder."""
        status = False
        try:
            if not os.path.exists(self.database_path):
                os.makedirs(self.database_path)
            status = True
        except OSError as error_code:  # noqa: E999
            self.module_error = float(self.module_error) + 0.0001
            self.module_error_message = f"Unable to create {self.database_path} folder. OSError {error_code}"  # noqa: E501
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc() # type: ignore
            traceback.print_exception() # type: ignore
        # finally:
        return status

    def __make_database(self) -> bool:  # sourcery skip: extract-method
        """Make the database."""
        status = False
        try:
            if not os.path.isfile(self.fullfile):
                self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            status = True    
        except Error as error_code:
            self.module_error = float(self.module_error) + 0.0002
            self.module_error_message = f"Unable to create {self.database_path} Database. Error {error_code}"  # noqa: E501
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc() # type: ignore
            traceback.print_exception() # type: ignore
        finally:
            if self.connection:
                self.connection.close()
        return status                

    def __make_geometry_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """Make the geometry table."""
        status = False
        try:
            self.connection = sqlite3.connect(self.database, timeout=10000)
            self.cursor = self.connection.cursor()

            # Create the Geometry Table
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS Geometry
            (ID INT NOT NULL  DEFAULT 1 PRIMARY KEY,
            P1  INT NOT NULL  DEFAULT 0,
            P2  INT NOT NULL  DEFAULT 0,
            P3  INT NOT NULL  DEFAULT 0,
            P4  INT NOT NULL  DEFAULT 0
            );''')
            self.connection.commit()            
        except Error as error_code:
            self.module_error = float(self.module_error) + 0.0003
            self.module_error_message = f"Unable to create {self.database_path} Geometry Table. Error {error_code}"  # noqa: E501
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc() # type: ignore
            traceback.print_exception() # type: ignore
            
        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()            
        return status        
        
    def __make_theme_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """Make the theme table."""

        status = False
        try:
            self.connection = sqlite3.connect(self.database, timeout=10000)
            self.cursor = self.connection.cursor()

            # Create the Theme Table
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS Theme 
            (ID INT  NOT NULL  DEFAULT 1 PRIMARY KEY,
            P1  TEXT NOT NULL  
            );''')  
            self.connection.commit()            
        except Error as error_code:
            self.module_error = float(self.module_error) + 0.0004
            self.module_error_message = f"Unable to create {self.database_path} Theme Table. Error {error_code}"  # noqa: E501
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc() # type: ignore
            traceback.print_exception() # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

    def __make_splash_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """Make the splash table."""

        status = False
        try:
            self.connection = sqlite3.connect(self.database, timeout=10000)
            self.cursor = self.connection.cursor()

            # Create the Splash Table
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS Splash 
            (ID INT  NOT NULL DEFAULT 1 PRIMARY KEY,
            P1  INT  NOT NULL DEFAULT 1 
            );''')
            self.connection.commit()
        except Error as error_code:
            self.module_error = float(self.module_error) + 0.0005
            self.module_error_message = f"Unable to create {self.database_path} Splash Table. Error {error_code}"  # noqa: E501
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc() # type: ignore
            traceback.print_exception() # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

    def __str__(self) -> str:
        """Return the __str__ Function."""
        return "P2_Settings"

    def __repr__(self) -> str:
        """Return the __repr__ Function."""
        return "P2_Settings"

    def get_class_version(self) -> str:
        """Return the Version String of this Class."""
        return self.class_version

    def get_author_name(self) -> str:
        """Return the Author String of this Class."""
        return self.author_name            

    def get_module_index(self) -> str:
        """Return the Module Index."""
        return self.module_index
