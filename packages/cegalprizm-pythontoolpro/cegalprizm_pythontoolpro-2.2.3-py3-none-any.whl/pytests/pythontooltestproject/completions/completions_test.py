import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCompletions:
    def test_well_with_completions_returns_completions(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        assert completions_set is not None

    def test_well_without_completions_returns_none(self, completions_set_none):
        assert completions_set_none is None

    def test_completions_set_print_repr(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        expected = "CompletionsSet(well_petrel_name=\"Well_Good\")"
        assert str(completions_set) == expected
        assert repr(completions_set) == expected

    def test_completions_set_casings_len(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        assert len(completions_set.casings) >= 3

    def test_completions_set_casings_print_repr(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        expected = "CasingStrings(CompletionsSet=\"CompletionsSet(well_petrel_name=\"Well_Good\")\")"
        assert str(completions_set.casings) == expected
        assert repr(completions_set.casings) == expected

    def test_completions_set_casings_constructor_bad_input(self, completions_set):
        from cegalprizm.pythontool.completionset import CasingStrings
        with pytest.raises(TypeError) as error:
            bad = CasingStrings("Bad Parent")
        assert error.type is TypeError
        assert error.value.args[0] == "Parent must be a CompletionsSet object"

    def test_completions_set_perforations_len(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        assert len(completions_set.perforations) >= 3

    def test_completions_set_perforations_print_repr(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        expected = "Perforations(CompletionsSet=\"CompletionsSet(well_petrel_name=\"Well_Good\")\")"
        assert str(completions_set.perforations) == expected
        assert repr(completions_set.perforations) == expected

    def test_completions_set_perforations_constructor_bad_input(self, completions_set):
        from cegalprizm.pythontool.completionset import Perforations
        with pytest.raises(TypeError) as error:
            bad = Perforations("Bad Parent")
        assert error.type is TypeError
        assert error.value.args[0] == "Parent must be a CompletionsSet object"

    def test_completions_set_add_perforation_no_name(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        with pytest.raises(ValueError) as error:
            newPerforation = completions_set.add_perforation("", 1234, 5678)
            assert newPerforation is None
        assert error.type is ValueError
        assert error.value.args[0] == "name can not be an empty string"

    def test_completions_set_add_perforation_bad_input(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        with pytest.raises(TypeError) as error:
            badPerforation = completions_set.add_perforation("Hello", "Hello", "Hello")
            assert badPerforation is None
        assert error.type is TypeError
        assert error.value.args[0] == "'Hello' has type str, but expected one of: int, float"

    def test_completions_set_add_perforation(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        newPerforation = completions_set.add_perforation("NewPerforation1", 8888, 8898.99)
        assert newPerforation is not None
        assert str(newPerforation) == str(completions_set.perforations["NewPerforation1"])
        import datetime
        newDate = datetime.datetime(2010,11,12,13,14,15)
        newPerforation.start_date = newDate
        assert completions_set.perforations["NewPerforation1"].start_date == newDate
