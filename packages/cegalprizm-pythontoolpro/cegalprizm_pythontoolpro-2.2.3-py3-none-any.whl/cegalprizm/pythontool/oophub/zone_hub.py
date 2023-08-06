# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



from cegalprizm.pythontool.grpc.petrelinterface_pb2 import *
from .base_hub import BaseHub


class ZoneHub(BaseHub):
    def GetZone(self, msg) -> PetrelObjectRef:
        return self._wrapper("cegal.pythontool.GetZone", PetrelObjectRef, msg) # type: ignore

    def Zone_GetParentGrid(self, msg) -> Zone_GetParentGrid_Response:
        return self._wrapper("cegal.pythontool.Zone_GetParentGrid", Zone_GetParentGrid_Response, msg) # type: ignore

    def Zone_GetBaseK(self, msg) -> Zone_GetBaseK_Response:
        return self._wrapper("cegal.pythontool.Zone_GetBaseK", Zone_GetBaseK_Response, msg) # type: ignore

    def Zone_GetTopK(self, msg) -> Zone_GetTopK_Response:
        return self._wrapper("cegal.pythontool.Zone_GetTopK", Zone_GetTopK_Response, msg) # type: ignore

    def Zone_GetNumberOfZones(self, msg) -> Zone_GetNumberOfZones_Response:
        return self._wrapper("cegal.pythontool.Zone_GetNumberOfZones", Zone_GetNumberOfZones_Response, msg) # type: ignore

    def Zone_GetZones(self, msg) -> Zone_GetZones_Response:
        return self._wrapper("cegal.pythontool.Zone_GetZones", Zone_GetZones_Response, msg) # type: ignore

    def Zone_GetParentZone(self, msg) -> Zone_GetParentZone_Response:
        return self._wrapper("cegal.pythontool.Zone_GetParentZone", Zone_GetParentZone_Response, msg) # type: ignore