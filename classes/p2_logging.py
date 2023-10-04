#!/usr/bin/env python3
# coding: utf-8

import os
import traceback
import logging
import datetime
import pathlib

from PySide6 import (
    QtCore
)


class ProjLogging:
    """The Class for Logging Work."""
    ########################
    # Covered in Test 1    #
    ########################
    def __init__(self, level) -> None:
        """ Init for Logging. """
        super().__init__()

        self.class_version = "0.0.1.dev"
        self.module_index = "12"
        self.author_name = "Julian Bourne"

        self.script_path = pathlib.Path(__file__).parent.resolve().parents[0]
        self.logging_path = rf"{self.script_path}/logs"
        self.debugstatus = level
        self.logdate = datetime.date.today()
        self.logfilename = f"{QtCore.QCoreApplication.applicationName()}.{self.logdate}.log"  # noqa: E501
        self.fullfile = rf"{self.logging_path}/{self.logfilename}"
        self.module_error = 0.0
        self.module_error_message = "No Error"
        self.level = None
        self.message = None
    ########################
    # Covered in Test 2    #
    ########################
    def __make_logging_location(self) -> bool:
        """Make logging folder."""
        status = False
        try:
            if not os.path.exists(self.logging_path):
                os.makedirs(self.logging_path)
            status = True
        except OSError as error_code:  # noqa: E999
            self.module_error = float(self.module_index) + 0.0001
            self.module_error_message = f"Unable to create {self.logging_path} folder. OSError {error_code}"  # noqa: E501
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc()  # type: ignore
            traceback.print_exception()  # type: ignore
        # finally:
        return status

    ########################
    # Covered in Test 2    #
    ########################
    def check_logging_exists(self) -> None:
        """Check Logging has been created."""
        looper = True
        while looper:
            looper = self.__make_logging_location()
            looper = self.__setup_logging()
            break

    ########################
    # Covered in Test 2    #
    ########################
    def __setup_logging(self) -> bool:
        # sourcery skip: extract-method, inline-immediately-returned-variable
        """Create the Logger."""
        status = False
        try:
            logging.basicConfig(
                filename=self.fullfile,
                encoding='utf-8',
                level=self.debugstatus,
                format='%(asctime)s %(name)s %(levelname)s: %(module)s %(funcName)s: %(lineno)s %(message)s',  # noqa: E501
                datefmt='%d/%m/%Y %H:%M:%S'
            )
            status = True
        except Exception as err:  # noqa: E722 , F841# type: ignore
            logging.error(f'Exception: {str(err)}')
            logging.error("Exception:", exc_info=True)            
            err.discard() # type: ignore
            self.module_error = float(self.module_index) + 0.0002
            self.module_error_message = f"Unable to create {self.logging_path} folder. Error {error_code}"  # noqa: E501, F821
            print(f"Error: {self.module_error} {self.module_error_message}")
            traceback.print_exc()  # type: ignore
            traceback.print_exception()  # type: ignore

            status = False
        finally:
            return status


    ########################
    # Covered in Test 3    #
    ########################
    def change_logging_level(self, level)-> None:
        """Change the logging level."""
        self.debugstatus = level
        logging.getLogger().setLevel(self.debugstatus)

    ########################
    # Covered in Test 4    #
    ########################
    def current_logging_level(self) -> int:
        """Get the current logging level."""
        return logging.root.level

    ########################
    # Covered in Test 5-9  #
    ########################
    def log_entry(self, level: str, message: str) -> None:
        """Create the log Entry."""
        self.level = level
        self.message = message
        match self.level:
            case "NOTSET":
                pass
            case "DEBUG":
                logging.debug(self.message)
            case "INFO":
                logging.info(self.message)
            case "WARNING":
                logging.warning(self.message)
            case "ERROR":
                logging.error(self.message)
            case "CRITICAL":
                logging.critical(self.message)
            case _:
                pass
