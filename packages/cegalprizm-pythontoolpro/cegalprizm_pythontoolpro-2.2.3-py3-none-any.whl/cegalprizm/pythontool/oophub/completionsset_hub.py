# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



from cegalprizm.pythontool.grpc.petrelinterface_pb2 import *
from .base_hub import BaseHub

class CompletionsSetHub(BaseHub):
    def GetCompletionsSetDataFrame(self, msg) -> CompletionsSet_GetData_Response:
        return self._server_streaming_wrapper("cegal.pythontool.CompletionsSet_GetCompletionsData", CompletionsSet_GetData_Response, msg) # type: ignore
    
    def GetCasingStrings(self, msg) -> PetrelObjectRef:
        return self._server_streaming_wrapper("cegal.pythontool.CompletionsSet_GetCasingStrings", PetrelObjectRef, msg) # type: ignore
    
    def GetPerforations(self, msg) -> PetrelObjectRef:
        return self._server_streaming_wrapper("cegal.pythontool.CompletionsSet_GetPerforations", PetrelObjectRef, msg)

    def AddPerforation(self, msg) -> PetrelObjectRef:
        return self._unary_wrapper("cegal.pythontool.CompletionsSet_AddPerforation", PetrelObjectRef, msg)
    
    def GetCasingStringEndDepth(self, msg) -> CompletionSet_CasingStrings_GetEndDepth_Response:
        return self._unary_wrapper("cegal.pythontool.CompletionSet_GetCasingStringEndDepth", CompletionSet_CasingStrings_GetEndDepth_Response, msg) # type: ignore
    
    def SetCasingStringEndDepth(self, msg) -> ProtoBool:
        return self._unary_wrapper("cegal.pythontool.CompletionSet_SetCasingStringEndDepth", ProtoBool, msg)
    
    def GetCasingStringStartDate(self, msg) -> CompletionSet_CasingStrings_GetStartDate_Response:
        return self._unary_wrapper("cegal.pythontool.CompletionSet_GetCasingStringStartDate", CompletionSet_CasingStrings_GetStartDate_Response, msg) # type: ignore
    
    def SetCasingStringStartDate(self, msg) -> ProtoBool:
        return self._unary_wrapper("cegal.pythontool.CompletionSet_SetCasingStringStartDate", ProtoBool, msg)

    def GetCasingStringEquipment(self, msg) -> CompletionSet_CasingStrings_GetEquipment_Response:
        return self._server_streaming_wrapper("cegal.pythontool.CompletionSet_GetAvailableCasingEquipment", CompletionSet_CasingStrings_GetEquipment_Response, msg)

    def GetCasingStringParts(self, msg) -> CompletionSet_CasingStrings_GetParts_Response:
        return self._server_streaming_wrapper("cegal.pythontool.CompletionSet_GetCasingStringParts", CompletionSet_CasingStrings_GetParts_Response, msg)

    def SetCasingStringPartDepth(self, msg) -> CompletionSet_CasingStrings_SetPartDepth_Response:
        return self._unary_wrapper("cegal.pythontool.CompletionSet_SetCasingPartDepth", CompletionSet_CasingStrings_SetPartDepth_Response, msg)

    def GetPerforationTopMd(self, msg) -> CompletionSet_Perforations_GetTopMd_Response:
        return self._unary_wrapper("cegal.pythontool.CompletionSet_GetPerforationTopMd", CompletionSet_Perforations_GetTopMd_Response, msg)
    
    def SetPerforationTopMd(self, msg) -> ProtoBool:
        return self._unary_wrapper("cegal.pythontool.CompletionSet_SetPerforationTopMd", ProtoBool, msg)

    def GetPerforationBottomMd(self, msg) -> CompletionSet_Perforations_GetBottomMd_Response:
        return self._unary_wrapper("cegal.pythontool.CompletionSet_GetPerforationBottomMd", CompletionSet_Perforations_GetBottomMd_Response, msg)

    def SetPerforationBottomMd(self, msg) -> ProtoBool:
        return self._unary_wrapper("cegal.pythontool.CompletionSet_SetPerforationBottomMd", ProtoBool, msg)

    def GetPerforationDate(self, msg) -> CompletionSet_Perforations_GetDate_Response:
        return self._unary_wrapper("cegal.pythontool.CompletionSet_GetPerforationDate", CompletionSet_Perforations_GetDate_Response, msg)

    def SetPerforationDate(self, msg) -> ProtoBool:
        return self._unary_wrapper("cegal.pythontool.CompletionSet_SetPerforationDate", ProtoBool, msg)

    def GetPerforationSkinFactor(self, msg) -> CompletionSet_Perforations_GetSkinFactor_Response:
        return self._unary_wrapper("cegal.pythontool.CompletionSet_GetPerforationSkinFactor", CompletionSet_Perforations_GetSkinFactor_Response, msg)

    def SetPerforationSkinFactor(self, msg) -> ProtoBool:
        return self._unary_wrapper("cegal.pythontool.CompletionSet_SetPerforationSkinFactor", ProtoBool, msg)