import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.completion_perforation import Perforation

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCompletionsPerforations:
    def test_perforation_get_by_name(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        perf = completions_set.perforations["Perforation 1"]
        assert isinstance(perf, Perforation)

    def test_perforation_get_by_name_when_multiple_with_same_name(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        list_of_perfs = completions_set.perforations["Perforation 2"]
        assert isinstance(list_of_perfs, list)
        assert all(isinstance(x, Perforation) for x in list_of_perfs)

    def test_perforation_get_by_name_bad_input(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        no_perforation = completions_set.perforations["NothingToSeeHere"]
        assert no_perforation is None

    def test_perforation_iterator(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        my_iterator = iter(completions_set.perforations)
        assert str(next(my_iterator)) == str(completions_set.perforations["Perforation 1"])
        assert str(next(my_iterator)) == str(completions_set.perforations["Perforation 2"][0])
        assert str(next(my_iterator)) == str(completions_set.perforations["Perforation 2"][1])
        with pytest.raises(StopIteration):
            assert next(my_iterator) == None

    def test_perforation_print_repr(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        perf = completions_set.perforations["Perforation 1"]
        expected = "Perforation(\"Perforation 1\")"
        assert str(perf) == expected
        assert repr(perf) == expected

    def test_perforation_get_set_top_md(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        perf = completions_set.perforations["Perforation 2"][0]
        old_depth = 8348.87
        assert perf.top_md == old_depth
        new_depth = 8383.83
        perf.top_md = new_depth
        assert perf.top_md == new_depth
        perf.top_md = old_depth
        assert perf.top_md == old_depth

    def test_perforation_get_set_bottom_md(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        perf = completions_set.perforations["Perforation 2"][0]
        old_depth = 8816.28
        assert perf.bottom_md == old_depth
        new_depth = 8888.99
        perf.bottom_md = new_depth
        assert perf.bottom_md == new_depth
        perf.bottom_md = old_depth
        assert perf.bottom_md == old_depth

    def test_perforation_get_set_date(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        import datetime
        perf = completions_set.perforations["Perforation 2"][0]
        old_date = datetime.datetime(1981,1,1)
        assert perf.start_date == old_date
        new_date = datetime.datetime(2001,8,8,12,35,25)
        perf.start_date = new_date
        assert perf.start_date == new_date
        perf.start_date = old_date
        assert perf.start_date == old_date

    def test_perforation_set_date_bad_input(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        perf = completions_set.perforations["Perforation 2"][0]
        with pytest.raises(Exception) as exceptionInfo:
            perf.start_date = "55 years ago"
        assert exceptionInfo.type is TypeError
        assert exceptionInfo.value.args[0] == "The new date must be a datetime.datetime object"

    def test_perforation_get_set_skin(self, completions_set, unsupported_version_2019):
        if unsupported_version_2019 == True:
            pytest.skip("Unsupported Petrel version: 2019")
        perf = completions_set.perforations["Perforation 2"][0]
        old_skin = 0.0
        assert perf.skin_factor == old_skin
        new_skin = 0.15
        perf.skin_factor = new_skin
        assert perf.skin_factor == new_skin
        perf.skin_factor = old_skin
        assert perf.skin_factor == old_skin

    # retrieve_history() returns null for perforation objects
    # def test_perforation_retrieve_history(sef, completions_set, unsupported_version_2019):
    #     if unsupported_version_2019 == True:
    #         pytest.skip("Unsupported Petrel version: 2019")
    #     perf = completions_set.perforations["Perforation 1"]
    #     history = perf.retrieve_history()
    #     assert history.empty != True
        