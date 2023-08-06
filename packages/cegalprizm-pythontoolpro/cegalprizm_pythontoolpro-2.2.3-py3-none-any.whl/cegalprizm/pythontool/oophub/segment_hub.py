# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



from cegalprizm.pythontool.grpc.petrelinterface_pb2 import *
from .base_hub import BaseHub


class SegmentHub(BaseHub):
    def GetSegment(self, msg) -> PetrelObjectRef:
        return self._wrapper("cegal.pythontool.GetSegment", PetrelObjectRef, msg) # type: ignore

    def Segment_GetParentGrid(self, msg) -> Segment_GetParentGrid_Response:
        return self._wrapper("cegal.pythontool.Segment_GetParentGrid", Segment_GetParentGrid_Response, msg) # type: ignore

    def Segment_GetCells(self, msg) -> Indices2Array:
        return self._wrapper("cegal.pythontool.Segment_GetCells", Indices2Array, msg) # type: ignore
    
    def Segment_IsCellInside(self, msg) -> Segment_IsCellInside_Response:
        return self._wrapper("cegal.pythontool.Segment_IsCellInside", Segment_IsCellInside_Response, msg) # type: ignore