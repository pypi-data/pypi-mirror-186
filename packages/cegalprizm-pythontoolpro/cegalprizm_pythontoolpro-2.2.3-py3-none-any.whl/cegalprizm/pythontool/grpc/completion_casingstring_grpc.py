# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



from cegalprizm.pythontool.grpc import petrelinterface_pb2
from .petrelobject_grpc import PetrelObjectGrpc
import datetime
import typing
if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.petrelconnection import PetrelConnection
    from cegalprizm.pythontool.oophub.completionsset_hub import CompletionsSetHub

class CasingStringGrpc(PetrelObjectGrpc):
    def __init__(self, guid: str, petrel_connection: "PetrelConnection"):
        super(CasingStringGrpc, self).__init__('casing string', guid, petrel_connection)
        self._guid = guid
        self._plink = petrel_connection
        self._invariant_content = {}
        self._channel = typing.cast("CompletionsSetHub", petrel_connection._service_completionsset)

    def GetEndDepth(self):
        self._plink._opened_test()
        request = petrelinterface_pb2.PetrelObjectGuid(
            guid = self._guid
        )
        response = self._channel.GetCasingStringEndDepth(request)
        return response.EndDepth
    
    def SetEndDepth(self, new_depth: float) -> bool:
        self._plink._opened_test()
        request = petrelinterface_pb2.CompletionSet_CasingStrings_SetEndDepth_Request(
            guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid),
            EndDepth = new_depth,
        )
        response = self._channel.SetCasingStringEndDepth(request)
        return response.value
    
    def GetStartDate(self):
        self._plink._opened_test()
        request = petrelinterface_pb2.PetrelObjectGuid(
            guid = self._guid
        )
        response = self._channel.GetCasingStringStartDate(request)
       
        grpcDate: petrelinterface_pb2.Date = response.StartDate
        date = datetime.datetime(grpcDate.year, grpcDate.month, grpcDate.day, grpcDate.hour, grpcDate.minute, grpcDate.second)
        return date
    
    def SetStartDate(self, new_date: datetime.datetime) -> bool:
        self._plink._opened_test()
        grpcDate = petrelinterface_pb2.Date(
            year = new_date.year,
            month = new_date.month,
            day = new_date.day,
            hour = new_date.hour,
            minute = new_date.minute,
            second = new_date.second
        )
        request = petrelinterface_pb2.CompletionSet_CasingStrings_SetStartDate_Request(
            guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid),
            StartDate = grpcDate,
        )
        response = self._channel.SetCasingStringStartDate(request)
        return response.value

    def GetAvailableEquipment(self):
        self._plink._opened_test()
        request = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid)
        responses = self._channel.GetCasingStringEquipment(request)
        for response in responses:
            equipments = response.EquipmentName
        return equipments

    def GetCasingStringParts(self):
        self._plink._opened_test()
        request = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid)
        responses = self._channel.GetCasingStringParts(request)
        container = []
        for response in responses:
            container.append(response.name)
            container.append(response.depth)
        return container

    def SetCasingPartDepth(self, old_depth, new_depth) -> bool:
        self._plink._opened_test()
        request = petrelinterface_pb2.CompletionSet_CasingStrings_SetPartDepth_Request(
            Guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid),
            OldDepth = old_depth,
            NewDepth = new_depth
        )
        response = self._channel.SetCasingStringPartDepth(request)
        return response.NewDepth