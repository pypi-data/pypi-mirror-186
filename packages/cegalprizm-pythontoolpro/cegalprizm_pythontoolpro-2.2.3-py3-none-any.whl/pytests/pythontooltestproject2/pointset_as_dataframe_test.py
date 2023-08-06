import pytest
import os
import sys
parent_dir = os.path.abspath("..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject2

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestPointSets_as_dataframe_PythonToolTestProject2:

    def test_pointset_as_dataframe_show_units_False(self, pointset_custom_property_units):
        pointset = pointset_custom_property_units
        pointset_df = pointset.as_dataframe(show_units=False)
        assert pointset_df.columns[3] == "TWT auto"
        assert pointset_df.columns[4] == "Continuous"
        assert pointset_df.columns[5] == "Date"
        assert pointset_df.columns[6] == "Derived from DEPTH"
        assert pointset_df.columns[7] == "Dip angle"
        assert pointset_df.columns[8] == "Dip azimuth"
        assert pointset_df.columns[9] == "Vp time (1)"
        assert pointset_df.columns[10] == "Vp time (2)"

    def test_pointset_as_dataframe_show_units_True(self, pointset_custom_property_units):
        pointset = pointset_custom_property_units
        pointset_df = pointset.as_dataframe(show_units=True)
        assert pointset_df.columns[3] == "TWT auto [ms]"
        assert pointset_df.columns[4] == "Continuous [260degR/1000ft]"
        assert pointset_df.columns[5] == "Date [ ]"
        assert pointset_df.columns[6] == "Derived from DEPTH [ft]"
        assert pointset_df.columns[7] == "Dip angle [deg]"
        assert pointset_df.columns[8] == "Dip azimuth [deg]"
        assert pointset_df.columns[9] == "Vp time (1) [ft.g/(s.cm3)]"
        assert pointset_df.columns[10] == "Vp time (2) [m/s]"