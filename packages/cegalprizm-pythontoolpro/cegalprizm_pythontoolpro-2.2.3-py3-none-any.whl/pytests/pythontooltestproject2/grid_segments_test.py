import pytest
import io
import os
import sys
parent_dir = os.path.abspath("..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject2
from contextlib import redirect_stdout

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestGridSegments:
    def test_segment_count(self, grid):
        assert len(grid.segments) == 3

    def test_segment_petrel_names(self, grid):
        for index, segment in enumerate(grid.segments):
            assert segment.petrel_name == "Segment " + str(index + 1)

    def test_segment_paths(self, grid):
        for index, segment in enumerate(grid.segments):
            assert segment.path == "Models/Segmented model/Segmented grid/Segment filter/Segment " + str(index + 1)

    def test_segment_readonly(self, grid):
        for segment in grid.segments:
            assert segment.readonly == True

    def test_segment_print(self, grid):
        with io.StringIO() as buffer, redirect_stdout(buffer):
            print(grid.segments[0])
            output = buffer.getvalue().strip('\n')
            assert output == 'Segment(petrel_name="Segment 1")'

    def test_segment_droid(self, grid):
        assert grid.segments[1].droid == "f31abc94-a808-4495-9894-c05e82186d8a+Segment: Segment 2"

    def test_segment_cell_print(self, grid):
        with io.StringIO() as buffer, redirect_stdout(buffer):
            print(grid.segments[1].cells[1])
            output = buffer.getvalue().strip('\n')
            assert output == 'Indices(i=2, j=66, k=None)'

    def test_segment_cell_ijk(self, grid):
        assert grid.segments[1].cells[1].i == 2
        assert grid.segments[1].cells[1].j == 66
        assert grid.segments[1].cells[1].k == None

    def test_segments_cell_count(self, grid):
        assert len(grid.segments[0].cells) == 1550
        assert len(grid.segments[1].cells) == 566
        assert len(grid.segments[2].cells) == 390

    def test_segment_is_cell_inside_is_true(self, grid):
        assert grid.segments[1].is_cell_inside(grid.segments[1].cells[1]) == True
    
    def test_segment_is_cell_inside_is_false(self, grid):
        assert grid.segments[1].is_cell_inside(grid.segments[0].cells[1]) == False

    def test_segment_parent(self, grid):
        assert grid.segments[0].grid.droid == grid.droid

