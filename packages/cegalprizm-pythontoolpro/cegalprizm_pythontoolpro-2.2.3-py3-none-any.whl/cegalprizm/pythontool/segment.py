# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.




from cegalprizm.pythontool.petrelobject import PetrelObject
from cegalprizm.pythontool import primitives
from cegalprizm.pythontool import grid

import typing
if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.grpc.segment_grpc import SegmentGrpc
    from cegalprizm.pythontool.grid import Grid
    
class Segment(PetrelObject):
    """A class holding information about a segment"""
    def __init__(self, petrel_object_link: "SegmentGrpc") -> None:
        super(Segment, self).__init__(petrel_object_link)
        self._segment_object_link = petrel_object_link

    def __str__(self) -> str:
        return 'Segment(petrel_name="{0}")'.format(self.petrel_name)

    @property
    def grid(self) -> 'Grid':
        """Returns the grid"""
        return grid.Grid(self._segment_object_link.GetParentGrid())

    @property
    def cells(self) -> typing.Iterator[primitives.Indices]:
        """Returns the indices of the cells belonging to this segment"""
        return self._segment_object_link.GetCells()

    
    def is_cell_inside(self, cell_index: primitives.Indices) -> bool:
        """Check if a cell is inside a segment
        Args:
            cell_index: primitives.Indices (I, J, K). Only the I and J values are used to verify if the cell is inside the segment. The K value is ignored.
        Returns:
            bool: True if the cell is inside the segment
        """
        return self._segment_object_link.IsCellInside(cell_index)
    
    def retrieve_history(self):
        print("History not available for individual Segment objects. Use the parent Grid object instead.")

class Segments(PetrelObject):
    """An iterable collection of :class:`cegalprizm.pythontool.Segment` objects."""

    def __init__(self, parent_obj: PetrelObject):
        self._parent_obj = parent_obj

    def __iter__(self) -> typing.Iterator[Segment]:
        for p in self._parent_obj._get_segments():
            yield p

    def __getitem__(self, idx: int) -> Segment:
        segments = list(self._parent_obj._get_segments())
        return segments[idx] # type: ignore

    def __len__(self) -> int:
        return self._parent_obj._get_number_of_segments()

    def __str__(self) -> str:
        return 'Segments({0}="{1}")'.format(self._parent_obj._petrel_object_link._sub_type, self._parent_obj)

    def retrieve_history(self):
        print("History not available for this object type. Use the parent Grid object instead.")

    def retrieve_stats(self):
        print("Stats not available for this object type.")