# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.




from cegalprizm.pythontool.petrelobject import PetrelObject
from cegalprizm.pythontool import grid

import typing

if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.grpc.zone_grpc import ZoneGrpc
    from cegalprizm.pythontool.grid import Grid

class Zone(PetrelObject):
    """A class holding information about a zone"""
    def __init__(self, petrel_object_link: "ZoneGrpc") -> None:
        super(Zone, self).__init__(petrel_object_link)
        self._zone_object_link = petrel_object_link

    def __str__(self) -> str:
        return 'Zone(petrel_name="{0}")'.format(self.petrel_name)

    @property
    def grid(self) -> 'Grid':
        """Returns the grid"""
        return grid.Grid(self._zone_object_link.GetParentGrid())

    @property
    def base_k(self) -> int:
        """Returns the BaseK"""
        return self._zone_object_link.GetBaseK()

    @property
    def top_k(self) -> int:
        """Returns the TopK"""
        return self._zone_object_link.GetTopK()

    @property
    def zones(self) -> 'Zones':
        """A readonly iterable collection of the zones for the zone

        Returns:
            cegalprizm.pythontool.Zones: the zones for the zone"""
        return Zones(self)

    @property
    def zone(self) -> 'Zone':
        """Returns the parent zone if zone is not top level zone"""
        parent_zone = self._zone_object_link.GetParentZone()
        if parent_zone is None:
            return None
        return Zone(parent_zone)

    def _get_zones(self):
        for zone in self._zone_object_link.GetZones():
            zone_py = Zone(zone)
            yield zone_py

    def _get_number_of_zones(self) -> int:
        return self._zone_object_link.GetNumberOfZones()

    def retrieve_history(self):
        print("History not available for individual Zone objects. Use the parent Grid object instead.")

class Zones(PetrelObject):
    """An iterable collection of :class:`cegalprizm.pythontool.Zone` objects."""

    def __init__(self, parent_obj: PetrelObject):
        self._parent_obj = parent_obj

    def __iter__(self) -> typing.Iterator[Zone]:
        for p in self._parent_obj._get_zones():
            yield p

    def __getitem__(self, idx: int) -> Zone:
        zones = list(self._parent_obj._get_zones())
        return zones[idx] # type: ignore

    def __len__(self) -> int:
        return self._parent_obj._get_number_of_zones()

    def __str__(self) -> str:
        return 'Zones({0}="{1}")'.format(self._parent_obj._petrel_object_link._sub_type, self._parent_obj)

    def retrieve_history(self):
        print("History not available for this object type. Use the parent Grid object instead.")

    def retrieve_stats(self):
        print("Stats not available for this object type.")