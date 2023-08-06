# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



from .petrelobject_grpc import PetrelObjectGrpc
from cegalprizm.pythontool.grpc import petrelinterface_pb2
import pandas as pd
import numpy as np
import typing
if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.petrelconnection import PetrelConnection
    from cegalprizm.pythontool.oophub.completionsset_hub import CompletionsSetHub

class CompletionsSetGrpc(PetrelObjectGrpc):
    def __init__(self, parent_well):
        petrel_connection: "PetrelConnection" = parent_well._borehole_object_link._plink
        parent_guid = parent_well._borehole_object_link._guid
        super(CompletionsSetGrpc, self).__init__('completionsset', parent_guid, petrel_connection)
        self._guid = parent_guid
        self._plink = petrel_connection
        self._invariant_content = {}
        self._channel = typing.cast("CompletionsSetHub", petrel_connection._service_completionsset)
        self._parent_well = parent_well

    def GetDataframe(self) -> pd.DataFrame:
        self._plink._opened_test()
        request = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid)
        responses = self._channel.GetCompletionsSetDataFrame(request)
        data = {}
        for response in responses:
            dataType = self.GetDataType(int(response.DataType))

            if(dataType is np.dtype('bool')):
                theData = self.GetBooleanSeriesFromStrings(response.values)
            else:
                theData = pd.Series(list(response.values), dtype=dataType)

            data[response.PropertyName] = theData

        df = pd.DataFrame(data)

        return df
    
    def GetCasingStrings(self):
        self._plink._opened_test()
        request = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid)
        responses = self._channel.GetCasingStrings(request)
        data = []
        for response in responses:
            data.append(response)
        return data
    
    def GetPerforations(self):
        self._plink._opened_test()
        request = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid)
        responses = self._channel.GetPerforations(request)
        data = []
        for response in responses:
            data.append(response)
        return data

    def AddPerforation(self, name: str, top_md: float, bottom_md: float):
        self._plink._opened_test()
        request = petrelinterface_pb2.CompletionsSet_AddPerforation_Request(
            Guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid),
            Name = name,
            TopMd = top_md,
            BottomMd = bottom_md,
        )
        response = self._channel.AddPerforation(request)
        return response
    
    def GetDataType(self, data_type_int):
        if(data_type_int == 3):
            dataType = np.dtype('str')
        elif(data_type_int == 1):
            dataType = np.dtype('float')
        elif(data_type_int == 4):
            dataType = np.dtype("datetime64[ns]")
        elif(data_type_int == 5):
            dataType = np.dtype('bool')
        return dataType

    def GetBooleanSeriesFromStrings(self, response_values):
        booleanSeries = pd.Series(list(), dtype=np.dtype('bool'))
        for index in range(len(response_values)):
            item = response_values[index]
            value = True
            if item == "False":
                value = False
            booleanSeries[index] = value
        return booleanSeries
