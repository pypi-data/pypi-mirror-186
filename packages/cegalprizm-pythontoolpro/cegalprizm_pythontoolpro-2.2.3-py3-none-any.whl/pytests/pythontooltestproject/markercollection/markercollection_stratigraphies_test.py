import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestMarkerCollectionStratigraphies:
    def test_markercollection_stratigraphies_repr(self, welltops):
        assert welltops is not None
        assert welltops.stratigraphies is not None
        strat = welltops.stratigraphies["Base Cretaceous"]
        assert strat is not None
        represent = repr(strat)
        assert represent == "MarkerStratigraphy(\"Base Cretaceous\")"

    def test_markercollection_stratigraphies_parent(self, welltops):
        strat = welltops.stratigraphies["Base Cretaceous"]
        assert strat.markercollection == welltops

    def test_markercollection_stratigraphies_bad_key(self, welltops):
        with pytest.raises(KeyError) as error:
            welltops.stratigraphies["Bad Key"]
        assert error.type is KeyError
        assert error.value.args[0] == "Cannot find unique stratigraphy name Bad Key"

    def test_markercollection_stratigraphies_len(self, welltops):
        assert len(welltops.stratigraphies) == 9