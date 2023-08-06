import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCompletionsAsDataframe:
    def test_completions_dataframe_not_none(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        df = completions_set.as_dataframe()
        assert df is not None

    def test_completions_dataframe_names_types(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        df = completions_set.as_dataframe()
        assert df["Well name"][0] == "Well_Good"
        assert df["Category"][0] == "Casing"
        assert df["Category"][7] == "Workovers"
        assert df["Type"][0] == "Casing string"
        assert df["Type"][1] == "Casing part"
        assert df["Type"][7] == "Perforation"
        assert df["Name"][0] == "Casing 1"
        assert df["Name"][1] == "Casing 1:1"
        assert df["Name"][7] == "Perforation 1"

    def test_completions_dataframe_depths(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        df = completions_set.as_dataframe()
        assert df["Top MD"][1] == 331.00
        assert df["Bottom MD"][1] == 1574.44
        assert df["Top MD"][8] == 8348.87
        assert df["Bottom MD"][8] == 8816.28

    def test_completions_dataframe_diameters(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        df = completions_set.as_dataframe()
        import numpy as np
        assert np.isnan(df["Outer Diameter"][0]) == True
        assert np.isnan(df["Inner Diameter"][0]) == True
        assert df["Outer Diameter"][1] == 7.0
        assert df["Inner Diameter"][1] == 6.456
        assert df["Outer Diameter"][2] == 5.5
        assert df["Inner Diameter"][2] == 4.892

    def test_completions_dataframe_dates(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        import datetime
        df = completions_set.as_dataframe()
        assert df["Start Date"][1] == datetime.datetime(1980,1,1)
        assert df["Start Date"][8] == datetime.datetime(1981,1,1)

    def test_completions_dataframe_isvalid(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        df = completions_set.as_dataframe()
        assert df["Is Valid"][1] == True
        assert df["Is Valid"][7] == True
        # Make first perforation invalid (set top md below bottom md)
        perforation = completions_set.perforations["Perforation 1"]
        original_top_md = perforation.top_md
        perforation.top_md = 20000
        df = completions_set.as_dataframe()
        assert df["Is Valid"][7] == False
        # Set back depth to leave project in clean state
        perforation.top_md = original_top_md
        df = completions_set.as_dataframe()
        assert df["Is Valid"][7] == True
