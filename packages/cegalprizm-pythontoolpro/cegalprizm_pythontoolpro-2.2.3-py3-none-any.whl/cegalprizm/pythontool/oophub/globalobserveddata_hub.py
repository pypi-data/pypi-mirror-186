# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



from cegalprizm.pythontool.grpc.petrelinterface_pb2 import *
from .base_hub import BaseHub

class GlobalObservedDataSetsHub(BaseHub):
    def GetGlobalObservedDataSet(self, msg) -> PetrelObjectRef:
        return self._unary_wrapper("cegal.pythontool.GlobalObservedDataSet_GetGlobalObservedDataSet", PetrelObjectRef, msg) # type: ignore

    def GlobalObservedDataSet_CreateObservedDataSet(self, msg) -> GlobalObservedDataSet_CreateObservedDataSet_Response:
        return self._unary_wrapper("cegal.pythontool.GlobalObservedDataSet_CreateObservedDataSet", GlobalObservedDataSet_CreateObservedDataSet_Response, msg) # type: ignore