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
    # Covered in Test 1    #
    ########################
    def __init__(self, database) -> None:
        # sourcery skip: aug-assign, remove-redundant-pass, remove-unnecessary-cast
        """ Init for Database Work. """
        super().__init__()

        self.class_version = "0.0.2.dev"
        self.module_index = "10"
        self.author_name = "Julian Bourne"
        # self.script_path = pathlib.Path(__file__).parent.resolve()
        # path = os.getcwd()
        # self.script_path = os.path.abspath(os.path.join(path, os.pardir))
        self.script_path = pathlib.Path(__file__).parent.resolve().parents[0]
        self.database_path = rf"{self.script_path}/db"
        self.database = database
        print(f"Database Name 2 = {self.database}")

        self.fullfile = rf"{self.database_path}/{self.database}"
        self.module_error = 0.0
        self.module_error_message = "No Error"
        self.connection = None
        self.cursor = None

    ########################
    # Covered in Test 2    #
    ########################
    def check_database_exists(self) -> None:
        """Check Database has been created and has default values. """
        looper = True
        while looper:
            # Internal Only Functions.
            looper = self.__make_database_location()
            looper = self.__make_database()
            looper = self.__make_geometry_table()
            looper = self.__make_theme_table()
            looper = self.__make_splash_table()
            looper = self.__make_debug_table()
            looper = self.__make_project_folder_table()
            looper = self.__make_app_update_table()
            looper = self.__make_apps_table()
            if self.get_records_geometry() < 1:
                looper = self.__set_default_geometry()
            if self.get_records_theme() < 1:
                looper = self.__set_default_theme()
            if self.get_records_splash() < 1:
                looper = self.__set_default_splash()
            if self.get_records_debug() < 1:
                looper = self.__set_default_debug()
            if self.get_records_app_update() < 1:
                looper = self.__set_default_app_update
            break


    def __str__(self) -> str:
        """ Return the __str__ Function. """
        return "p2_database"

    def __repr__(self) -> str:
        """ Return the __repr__ Function. """
        return "p2_database"

    def get_class_version(self) -> str:
        """ Return the Version String of this Class. """
        return self.class_version

    def get_author_name(self) -> str:
        """ Return the Author String of this Class. """
        return self.author_name

    def get_module_index(self) -> str:
        """ Return the Module Index. """
        return self.module_index

    def get_sqlite3_library_version(self) -> str:
        """ Return the Sqlite3 Library Version Number. """
        return sqlite3.sqlite_version

    def get_sqlite3_version(self) -> str:
        """ Return the Sqlite3 Version Number. """
        return sqlite3.version

####################################################################
#          Make the database location and name it                  #
####################################################################

    ########################
    # Covered in Test 2    #
    ########################
    def __make_database_location(self) -> bool:
        """ Make database folder. """
        status = False
        try:
            if not os.path.exists(self.database_path):
                os.makedirs(self.database_path)
            status = True
        except OSError as error_code:  # noqa: E999
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
    # Covered in Test 2    #
    ########################
    def __make_database(self) -> bool:  # sourcery skip: extract-method
        """ Make the database. """
        status = False
        try:
            if not os.path.isfile(self.fullfile):
                self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            status = True
        except Error as error_code:
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

####################################################################
#          Geometry related modules START                          #
####################################################################

    ########################
    # Covered in Test 2    #
    ########################
    def __make_geometry_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Make the geometry table. """
        status = False
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            if not self.connection:
                raise Error("No Connection to database")
            self.cursor = self.connection.cursor()

            # Create the Geometry Table
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Geometry
                                (ID integer NOT NULL DEFAULT 1 PRIMARY KEY,
                                P1  integer NOT NULL  DEFAULT 0,
                                P2  integer NOT NULL  DEFAULT 0,
                                P3  integer NOT NULL  DEFAULT 0,
                                P4  integer NOT NULL  DEFAULT 0) """)
            self.connection.commit()
        except Error as error_code:
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
    # Covered in Test 3    #
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
    # Covered in Test 2    #
    ########################
    def __set_default_geometry(self) -> bool:
        """ Set the default Geometry. """
        return self.update_geometry(0, 0, 600, 500)

    ########################
    # Covered in Test 2 7  #
    ########################
    def update_geometry(self, x: int = 0, y: int = 0, w: int = 600, h: int = 500) -> bool:   # type: ignore  # noqa: E501
        """ Update the Geometry Table. """
        status = False
        try:
            T1 = x or 0
            T2 = y or 0
            T3 = w or 600
            T4 = h or 500
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            self.cursor.execute(""" REPLACE INTO Geometry (ID, P1, P2, P3, P4) \
        VALUES (?, ?, ?, ?, ?) """, (1, T1, T2, T3, T4))
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
    # Covered in Test 11   #
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
    # Covered in Test 11   #
    ########################
    def get_geometry_record(self) -> QRect:
        """ Return QRect. """
        rect_list = self.__get_geometry_record()
        retval = None

        retval = QRect(
            rect_list[0],
            rect_list[1],
            rect_list[2],
            rect_list[3]
            )
        if not retval.isValid():
            retval = QRect(0,0,0,0)
        return retval

####################################################################
#          Geometry related modules END                            #
####################################################################

####################################################################
#          Theme related modules START                             #
####################################################################

    ########################
    # Covered in Test 2    #
    ########################
    def __make_theme_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Make the theme table. """

        status = False
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            # Create the Theme Table
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Theme
                                (ID integer NOT NULL DEFAULT 1 PRIMARY KEY,
                                P1  TEXT NOT NULL DEFAULT 'auto') """)
            self.connection.commit()
        except Error as error_code:
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
    # Covered in Test 4    #
    ########################
    def get_records_theme(self) -> int:
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
    def get_theme_record(self) -> str:
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

####################################################################
#          Splash related modules START                            #
####################################################################

    ########################
    # Covered in Test 2    #
    ########################
    def __make_splash_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Make the splash table. """

        status = False
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            # Create the Splash Table
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Splash
                                (ID integer NOT NULL DEFAULT 1 PRIMARY KEY,
                                P1  INT  NOT NULL DEFAULT 1) """)
            self.connection.commit()
        except Error as error_code:
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
    # Covered in Test 5    #
    ########################
    def get_records_splash(self) -> int:
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
    def get_splash_record(self) -> int:
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

####################################################################
#          Debug related modules START                             #
####################################################################

    ########################
    # Covered in Test 2    #
    ########################
    def __make_debug_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Make the debug table. """

        status = False
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            # Create the Splash Table
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Debug
                                (ID integer NOT NULL DEFAULT 1 PRIMARY KEY,
                                P1  INT  NOT NULL DEFAULT 0) """)
            self.connection.commit()
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0401
            self.module_error_message = \
                f"Unable to create {self.fullfile} \
                Debug Table. Error {error_code}"
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc(None) # type: ignore
            traceback.print_exception(None) # type: ignore

        finally:
            if self.connection:
                self.cursor = None
                self.connection.close()
        return status

    ########################
    # Covered in Test 6    #
    ########################
    def get_records_debug(self) -> int:
        # sourcery skip: extract-method, inline-immediately-returned-variable
        """ Return number of debug records. """
        status = -1
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()
            self.cursor.execute(""" SELECT COUNT(*) FROM Debug """)
            self.connection.commit()
            status = len(self.cursor.fetchall())
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0402
            self.module_error_message = \
                f"Unable to get number of Debug Records. \
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
    def __set_default_debug(self) -> bool:
        """ Set the default Debug. """
        return self.update_debug(0)

    ########################
    # Covered in Test 2 10 #
    ########################
    def update_debug(self, debug: int = 0) -> bool:
        """ Update the Debug Table. """
        status = False
        try:
            T1 = debug
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            self.cursor.execute(""" \
                REPLACE INTO Debug \
                (ID, P1) \
                VALUES (?, ?) """, \
                (1, T1))
            self.connection.commit()
            status = True
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0403
            self.module_error_message = \
                f"Unable to add setting {self.fullfile} \
                Debug Table. Error {error_code}"
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
    def __get_debug_record(self) -> list:    # type: ignore
        # sourcery skip: use-named-expression
        """ Get the Debug Record. """
        retval=[]
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()
            self.cursor.execute(""" SELECT P1 FROM Debug WHERE ID = 1 """)
            self.connection.commit()
            records = self.cursor.fetchone()
            retval = [records[0]] if records else []
        except Error as error_code:
            self.module_error = float(self.module_index) + 0.0404
            self.module_error_message = \
                f"Unable to get setting {self.fullfile} \
                Debug Table. Error {error_code}"
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
    def get_debug_record(self) -> int:
        """ Return Debug Value. """
        test_list = [0, 10, 20, 30, 40, 50]
        rec_list = self.__get_debug_record()
        retval = rec_list[0]
        exist_count = test_list.count(retval)
        if exist_count < 1:
            retval = 0
        return retval

####################################################################
#          Debug related modules END                               #
####################################################################

####################################################################
#          Project Folder related modules START                          #
####################################################################

    def __make_project_folder_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Make the project folder table. """

        status = False
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            self.cursor = self.connection.cursor()

            # Create the Project Folder Table
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS PFolder
                                (ID integer NOT NULL DEFAULT 1 PRIMARY KEY,
                                P1  TEXT NOT NULL) """)
            self.connection.commit()
        except Error as error_code:
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

####################################################################
#          App Update related modules  START                               #
####################################################################

    def __make_app_update_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Make the app_update table. """

        status = False
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
                                P1  TEXT    NOT NULL DEFAULT "Zero" INDEX,
                                P2  INTEGER NOT NULL DEFAULT 0,
                                P3  INTEGER NOT NULL DEFAULT 2440587,
                                P4  INTEGER NOT NULL DEFAULT 2440587
                                ) """)
            self.connection.commit()
        except Error as error_code:
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

####################################################################
#          Apps related modules START                              #
####################################################################

    def __make_apps_table(self) -> bool:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
        """ Make the apps table. """
        status = False
        try:
            self.connection = sqlite3.connect(self.fullfile, timeout=10000)
            if not self.connection:
                raise Error("No Connection to database")
            self.cursor = self.connection.cursor()

            # Create the Apps Table
            # ID Integer
            # P1 Text    - Name of the App
            # P2 Text    - Alias of the App
            # P3 Text    - Location of the App
            # P4 Text    - Version of the App at Creation
            # P5 Text    - Type of App

            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Apps
                                (ID integer NOT NULL DEFAULT 1 PRIMARY KEY,
                                P1  TEXT NOT NULL  DEFAULT "" INDEX,
                                P2  TEXT NOT NULL  DEFAULT "" INDEX,
                                P3  TEXT NOT NULL  DEFAULT "",
                                P4  TEXT NOT NULL  DEFAULT "",
                                P5  TEXT NOT NULL  DEFAULT "" INDEX) """)
            self.connection.commit()
        except Error as error_code:
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

####################################################################
#          Apps related modules END                                #
####################################################################
