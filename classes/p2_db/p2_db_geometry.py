#!/usr/bin/env python3
# coding: utf-8

import os
import traceback
import pathlib

import sqlite3
from sqlite3 import Error

from classes.p2_database import ProjDatabase

class ProjTableGeometry(ProjDatabase):
    """The Class for Geometry Table Work. """
    ########################
    # Covered in Test 2a   #
    ########################

    def __init__(self, database) -> None:
        super().__init__(database)

        self.class_version = "0.0.5.dev"
        self.__str = "p2_db_geometry"
        self.__repr = "p2_db_geometry"
        self.__make_geometry_table()
        self.__set_default_geometry()


    ########################
    # Covered in Test 2b   #
    ########################
    def __str__(self) -> str:
        """ Return the __str__ Function. """
        return f"{self.__str}"

    ########################
    # Covered in Test 2c   #
    ########################
    def __repr__(self) -> str:
        """ Return the __repr__ Function. """
        return f"{self.__repr}"


####################################################################
#          Geometry related modules START                          #
####################################################################

    ########################
    # Covered in Test 2a   #
    ########################
    def __make_geometry_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Make the geometry table. """
        status = True
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            if not self.connection:
                raise Error("No Connection to database")
            self.cursor = self.connection.cursor()

            # Create the Geometry Table
            # ID Integer - Index Number
            # P1 Integer - X co-ordinate
            # P2 Integer - Y co-ordinate
            # P3 Integer - Width of the window to be set
            # P4 Integer - Height of the window to be set
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Geometry
                                (ID INTEGER NOT NULL DEFAULT 1 PRIMARY KEY,
                                P1  INTEGER NOT NULL  DEFAULT 0,
                                P2  INTEGER NOT NULL  DEFAULT 0,
                                P3  INTEGER NOT NULL  DEFAULT 0,
                                P4  INTEGER NOT NULL  DEFAULT 0) """)
            self.connection.commit()
        except Error as error_code:
            status = False
            self.module_error = float(self.module_index) + 0.0101
            self.module_error_message = \
                f"Unable to create {self.database_path} \
                Geometry Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

    ########################
    # Covered in Test 2g   #
    ########################
    def get_records_geometry(self) -> int:
        # sourcery skip: extract-method, inline-immediately-returned-variable
        """ Return number of geometry records. """
        status = -1
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()
            self.cursor.execute(""" SELECT COUNT(*) FROM Geometry """)
            self.connection.commit()
            status = len(self.cursor.fetchall())
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0102
            self.module_error_message = \
                f"Unable to get number of Geometry Records. \
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
    # Covered in Test 2h   #
    ########################
    def __set_default_geometry(self) -> bool:
        """ Set the default Geometry. """
        values = [0, 0, 600, 500]
        return self.update_geometry(values)

    ########################
    # Covered in Test 2h   #
    ########################
    def update_geometry(self, values: list = None) -> bool:   # type: ignore  # noqa: E501
        """ Update the Geometry Table. """
        status = False
        try:
            temp_t1 = values[0] or 0
            temp_t2 = values[1] or 0
            temp_t3 = values[2] or 600
            temp_t4 = values[3] or 500
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            self.cursor.execute(""" REPLACE INTO Geometry (ID, P1, P2, P3, P4) \
        VALUES (?, ?, ?, ?, ?) """, (1, temp_t1, temp_t2, temp_t3, temp_t4))
            self.connection.commit()
            status = True
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0103
            self.module_error_message = \
                f"Unable to add setting {self.fullfile} \
                Geometry Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

    ########################
    # Covered in Test 2i   #
    ########################
    def __get_geometry_record(self) -> list: # type: ignore
        # sourcery skip: use-named-expression
        """ Get the Geometry Record. """
        retval=[]
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()
            self.cursor.execute(""" \
                SELECT P1, P2, P3, P4 FROM Geometry \
                WHERE ID = 1 """)
            self.connection.commit()
            records = self.cursor.fetchone()
            if records:
                retval = [
                    records[0],
                    records[1],
                    records[2],
                    records[3]
                ]
            else:
                retval = [0, 0, 0, 0]
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0104
            self.module_error_message = \
                f"Unable to get setting {self.fullfile} \
                Geometry Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore
        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return retval

    ########################
    # Covered in Test 2i   #
    ########################
    def get_geometry_record(self) -> list:
        """ Return QRect. """
        return self.__get_geometry_record() or [0,0,0,0]

####################################################################
#          Geometry related modules END                            #
####################################################################