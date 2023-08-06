# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



import typing
from cegalprizm.pythontool import primitives
from .petrelobject_grpc import PetrelObjectGrpc
from cegalprizm.pythontool.grpc import grid_grpc, petrelinterface_pb2
from .petrelobject_grpc import PetrelObjectGrpc
if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.petrelconnection import PetrelConnection
    from cegalprizm.pythontool.oophub.segment_hub import SegmentHub


class SegmentGrpc(PetrelObjectGrpc):

    def __init__(self, guid: str, petrel_connection: "PetrelConnection", sub_type: str = 'segment'):
        super(SegmentGrpc, self).__init__(sub_type, guid, petrel_connection)
        self._guid = guid
        self._plink = petrel_connection
        self._channel = typing.cast('SegmentHub', petrel_connection._service_segment)

    def GetParentGrid(self):
        self._plink._opened_test()
        request = petrelinterface_pb2.Segment_GetParentGrid_Request(
            guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid)
        )
        response = self._channel.Segment_GetParentGrid(request)
        return grid_grpc.GridGrpc(response.guid.guid, self._plink)

    def GetCells(self):
        self._plink._opened_test()
        request = petrelinterface_pb2.Segment_GetCells_Request(
            guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid)
        )
        response = self._channel.Segment_GetCells(request)
        indices_array = response.indices_array
        array_length = len(indices_array)
        indices = [primitives.Indices] * array_length
        for index in range(array_length):
            indices[index] = primitives.Indices(indices_array[index].i, indices_array[index].j, None)
        return indices

    def IsCellInside(self, cell_index: primitives.Indices):
        index = petrelinterface_pb2.Primitives.Indices2(i = cell_index.i, j = cell_index.j)
        self._plink._opened_test()
        request = petrelinterface_pb2.Segment_IsCellInside_Request(
            guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid),
            index = index
        )
        response = self._channel.Segment_IsCellInside(request)
        return response.cellIsInsideSegment
