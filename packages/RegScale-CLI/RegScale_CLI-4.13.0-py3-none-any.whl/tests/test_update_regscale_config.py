#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from app.application import Application
from app.logz import create_logger
from app.utils.regscale_utils import update_regscale_config

sys.path.append("..")  # Adds higher directory to python modules path.


class Test_Update_Regscale_Config:
    logger = create_logger()

    domain_updated = "https://regscale.updateddomain.com:81"

    def test_init(self):
        """simple init test"""
        with open("init.yaml", "r") as f:
            data = f.read()
            self.logger.debug("init file: %s", data)
            assert len(data) > 5

    def test_update_regscale_config(self):
        """Test changing init.yaml"""
        app = Application()
        config = app.config
        assert "domain" in config
        # update existing param
        update_regscale_config("domain", self.domain_updated, app)
        assert config["domain"] == self.domain_updated
        # add new param
        update_regscale_config("new_param", "new_val", app)
        # test init.yaml file changed
        app_updated = Application()
        config_updated = app_updated.config
        assert config_updated["domain"] == self.domain_updated
        assert config_updated["new_param"] == "new_val"
