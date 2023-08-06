import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestMarkerCollectionAttributes:
    def test_markercollection_add_marker_readonly(self, welltops):
        welltops.readonly = True
        from cegalprizm.pythontool.exceptions import PythonToolException
        with pytest.raises(PythonToolException) as exceptionInfo:
            welltops.add_marker(None, None, 0.0)
        assert exceptionInfo.type is PythonToolException
        assert exceptionInfo.value.args[0] == "MarkerCollection is readonly"
        welltops.readonly = False

    def test_markercollection_add_attribute_readonly(self, welltops):
        welltops.readonly = True
        from cegalprizm.pythontool.exceptions import PythonToolException
        import numpy as np
        array = np.empty(0)
        with pytest.raises(PythonToolException) as exceptionInfo:
            welltops.add_attribute(array, "Something", "not used")
        assert exceptionInfo.type is PythonToolException
        assert exceptionInfo.value.args[0] == "MarkerCollection is readonly"
        welltops.readonly = False

    def test_markercollection_check_input_contains_data_raises_value_error(self, welltops):
        import numpy as np
        array = np.empty(0)
        with pytest.raises(ValueError) as error:
            welltops._check_input_contains_data(array)
        assert error.type is ValueError
        assert error.value.args[0] == "Input array does not contain any values"

    def test_markercollection_get_stratigraphy_droid_requires_stratigraphy(self, welltops):
        with pytest.raises(TypeError) as error:
            welltops._get_stratigraphy_droid("BAd INput")
        assert error.type is TypeError
        assert error.value.args[0] == "marker_stratigraphy must be a MarkerStratigrapy object as returned from markercollection.stratigraphies"

    def test_markercollection_stratigraphies_constructor_bad_input(self, welltops):
        from cegalprizm.pythontool.markercollection import MarkerStratigraphies
        with pytest.raises(TypeError) as error:
            bad = MarkerStratigraphies("Bad Parent")
        assert error.type is TypeError
        assert error.value.args[0] == "Parent must be MarkerCollection"

    def test_markercollection_stratigraphies_str_repr(self, welltops):
        strats = welltops.stratigraphies
        expected = "MarkerStratigraphies(marker collection=\"MarkerCollection(petrel_name=\"WellTops\")\")"
        assert str(strats) == expected
        assert repr(strats) == expected

    def test_markercollection_attributes_constructor_bad_input(self, welltops):
        from cegalprizm.pythontool.markercollection import MarkerAttributes
        with pytest.raises(TypeError) as error:
            bad = MarkerAttributes("Bad Parent")
        assert error.type is TypeError
        assert error.value.args[0] == "Parent must be MarkerCollection"

    def test_markercollection_attributes_str_repr(self, welltops):
        strats = welltops.attributes
        expected = "MarkerAttributes(marker collection=\"MarkerCollection(petrel_name=\"WellTops\")\")"
        assert str(strats) == expected
        assert repr(strats) == expected