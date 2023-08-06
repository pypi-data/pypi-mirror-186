import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestMarkerCollectionDataframe:
    def test_markercollection_dataframe_petrel_index(self, welltops):
        dataframe = welltops.as_dataframe()
        assert dataframe['Petrel index'][101] == 102

    def test_markercollection_dataframe_md(self, welltops):
        dataframe = welltops.as_dataframe()
        assert dataframe['MD'][2] == 1805.45

    def test_markercollection_dataframe_fluvial_facies(self, welltops):
        dataframe = welltops.as_dataframe()
        assert dataframe['Fluvial facies'][8] == 99.0

    def test_markercollection_dataframe_uc_markers_false_petrel_index(self, welltops):
        dataframe = welltops.as_dataframe(False)
        assert dataframe['Petrel index'][0] == 4

    def test_markercollection_dataframe_uc_markers_false_well_id(self, welltops):
        dataframe = welltops.as_dataframe(False)
        assert dataframe['Well identifier (Well name)'][4] == 'B1'

    def test_markercollection_dataframe_uc_markers_false_md(self, welltops):
        dataframe = welltops.as_dataframe(False)
        assert dataframe['MD'][0] == 2012.93

    def test_markercollection_dataframe_uc_markers_true_md(self, welltops):
        dataframe = welltops.as_dataframe(True)
        assert dataframe['MD'][2] == 1805.45

    def test_markercollection_dataframe_strat_filter_md(self, welltops):
        stratigraphy = welltops.stratigraphies["Base Cretaceous"]
        dataframe = welltops.as_dataframe(True, stratigraphy)
        assert dataframe['MD'][0] == 1858.55
        assert dataframe['MD'][1] == 1879.35

    def test_markercollection_dataframe_well_filter(self, welltops, wellb1):
        dataframe = welltops.as_dataframe(True, None, wellb1)
        assert dataframe['MD'][0] == 1831.03
        assert dataframe['MD'][1] == 1864.8

    def test_markercollection_dataframe_strat_and_well_filter(self, welltops, wellb1):
        stratigraphy = welltops.stratigraphies["Top Ness"]
        dataframe = welltops.as_dataframe(True, stratigraphy, wellb1)
        assert dataframe['MD'][0] == 1949.68
        assert dataframe['MD'][1] == 1949.68