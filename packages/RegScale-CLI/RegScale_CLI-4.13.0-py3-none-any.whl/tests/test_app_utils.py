#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from app.utils.app_utils import str_to_date, uncamel_case

# from app.application import Application
# from app.internal.login import is_licensed, login
from app.logz import create_logger

sys.path.append("..")  # Adds higher directory to python modules path.


class Test_App_Utils:
    logger = create_logger()

    def test_init(self):
        """simple init test"""
        with open("init.yaml", "r") as f:
            data = f.read()
            self.logger.debug("init file: %s", data)
            assert len(data) > 5

    def test_uncamel_case(self):
        """Simple uncamel case test"""
        txt_cc = "lowerCaseCamel"
        txt_tc = "Lower Case Camel"

        self.logger.debug(f"Testing '{txt_cc}'")
        assert uncamel_case(txt_cc) == txt_tc

        txt_cc = "UpperCaseCamel"
        txt_tc = "Upper Case Camel"

        self.logger.debug(f"Testing '{txt_cc}'")
        assert uncamel_case(txt_cc) == txt_tc

    # def test_application(self):
    #     """simple test of config"""
    #     app = Application()
    #     config = app.config
    #     assert "domain" in config
    #     assert "token" in config

    # def test_license(self):
    #     app = Application()
    #     license = is_licensed(app)
    #     assert license
