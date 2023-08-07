import os

from app.application import Application
from app.logz import create_logger
from app.login import login
from app.internal.control_editor import (
    excel_worksheet,
    data_load,
    db_update,
    delete_file,
)


class Test_Controller:

    logger = create_logger()

    def test_init(self):
        """Init"""
        with open("init.yaml", "r", encoding="utf-8") as file:
            data = file.read()
            self.logger.debug("init file: %s", data)
            assert len(data) > 5

    def test_control_editor_build(self):
        """Simple login test"""

        app = Application()
        self.logger.debug(os.getenv("REGSCALE_USER"))
        self.logger.debug(os.getenv("REGSCALE_PASSWORD"))

        jwt = login(os.getenv("REGSCALE_USER"), os.getenv("REGSCALE_PASSWORD"), app=app)
        self.logger.info(jwt)
        assert jwt is not None

    def test_control_editor_data_load(self):

        regscale_parent_id = 5
        regscale_module = "securityplans"
        path = os.path.join(os.getcwd() + r"\artifacts")

        # load workbook and upload data from regscale database

        data_load(regscale_parent_id, regscale_module, path)

    def test_control_editor_upload(self):
        regscale_parent_id = 5
        regscale_module = "securityplans"
        path = os.path.join(os.getcwd() + r"\artifacts")

        # Check file for changes and upload changes to regscale database and delete files

        db_update(regscale_parent_id, regscale_module, path)

    def test_control_editor_delete_files(self):

        path = os.path.join(os.getcwd() + r"\artifacts")

        # Delete files and folder created in current working directory if changes were made to "all_implementations" workbook

        delete_file(path)
