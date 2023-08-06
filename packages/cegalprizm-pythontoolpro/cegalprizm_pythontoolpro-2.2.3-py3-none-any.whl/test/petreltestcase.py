# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



import os
import typing
import unittest
from cegalprizm.hub import Hub
import pathlib

def getPersonalFolderPath() -> str:
    import win32com
    from win32com.shell import shell, shellcon
    # picks up the path equivalent to csharp Environment.SpecialFolder.Personal=Environment.SpecialFolder.MyDocuments
    return shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0) 

class PetreltestUnitCase(unittest.TestCase):
    _project: typing.Optional[str] = None
    _project_name: typing.Optional[str] = None   

    def getPetrelProjectPath(project_name)-> str:
        if not project_name:
             raise RuntimeError("self._project_name must be set by child class before running tests")

        # on devops agent
        if os.environ.get("USERNAME").lower() == "vmadministrator": 
            directory = os.environ.get("BUILD_ARTIFACTSTAGINGDIRECTORY")
            project_path = os.path.join(directory, "PetrelUnitTestFramework", project_name, project_name + ".pet")
            pet_file = pathlib.Path(project_path)
            if not pet_file.exists():
                raise RuntimeError("Test project does not exists in the expected location on the agent. Expected file: " + project_path )
            return project_path # project is downloaded and unzipped earlier in the pipeline stage that runs these python tests

        # running locally
        path = os.environ.get("BBR_UNIT_TEST_FRAMEWORK_FOLDER")
        if path is None:
            path = getPersonalFolderPath()
        project_path = os.path.join(path, "PetrelUnitTestFramework", "1", project_name, project_name + ".pet")
        pet_file = pathlib.Path(project_path)
        if not pet_file.exists():
            raise RuntimeError("Test project does not exists in the expected location on your computer. Expected file: " + project_path)
        return project_path

    def setUp(self) -> None:
        super().setUp()

    @classmethod
    def setUpClass(cls):
        project_path = cls.getPetrelProjectPath(cls._project_name)
        cls._h = Hub()
        cls._ptx = cls._h.default_petrel_ctx()
        try:
            if not pathlib.Path(project_path) == pathlib.Path(cls._ptx.project_info().path):
                cls._ptx.load_project(path = project_path, read_only=False)
        except Exception as e:
            cls._ptx.load_project(path = project_path, read_only=False)