import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestMarkerCollectionAttributes:
    def test_markercollection_attributes_repr(self, welltops):
        assert welltops is not None
        assert welltops.attributes is not None
        z = welltops.attributes["Z"]
        assert z is not None
        represent = repr(welltops.attributes["Z"])
        assert represent == "MarkerAttribute(\"Z\")"

    def test_markercollection_attributes_readonly(self, welltops):
        welltops.readonly = True
        from cegalprizm.pythontool.exceptions import PythonToolException
        import numpy as np
        array = np.empty(2)
        with pytest.raises(PythonToolException) as exceptionInfo:
            welltops.attributes["Z"].set_values(array)
        assert exceptionInfo.type is PythonToolException
        assert exceptionInfo.value.args[0] == "MarkerCollection is readonly"
        welltops.readonly = False

    def test_markercollection_attributes_parent(self, welltops):
        z = welltops.attributes["Z"]
        assert z.markercollection == welltops

    def test_markercollection_attributes_len(self, welltops):
        assert len(welltops.attributes) >= 29

    def test_markercollection_attributes_get_none(self, welltops):
        assert welltops.attributes[None] is None

    