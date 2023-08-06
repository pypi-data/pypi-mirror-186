# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



import typing
import string
import numpy as np
import pandas as pd
from cegalprizm.pythontool import exceptions, PetrelObject
from cegalprizm.pythontool.borehole import Well
from cegalprizm.pythontool.markerattribute import MarkerAttribute
from cegalprizm.pythontool.grpc.markerattribute_grpc import MarkerAttributeGrpc
from cegalprizm.pythontool.markerstratigraphy import MarkerStratigraphy
from cegalprizm.pythontool.exceptions import UserErrorException

if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.grpc.markercollection_grpc import MarkerCollectionGrpc

class MarkerCollection(PetrelObject):
    """A class holding information about a MarkerCollection.
    """

    def __init__(self, petrel_object_link: "MarkerCollectionGrpc"):
        super(MarkerCollection, self).__init__(petrel_object_link)
        self._markercollection_object_link = petrel_object_link
        
    def __str__(self) -> str:
        """A readable representation"""
        return 'MarkerCollection(petrel_name="{0}")'.format(self.petrel_name)

    @property
    def name(self):
        """The name of the MarkerCollection.
        
        Returns:
            string: Name of the MarkerCollection as a string.
        """
        return self._markercollection_object_link.GetName()
 
    @name.setter
    def name(self, value: string) -> None:
        ok = self._markercollection_object_link.SetName(value)

    def as_dataframe(self, include_unconnected_markers: bool = True, marker_stratigraphy: MarkerStratigraphy = None, well: Well = None) -> pd.DataFrame:
        """Gets a dataframe with information about Markers in the MarkerCollection.
        
        Args:
            include_unconnected_markers: Flag to include markers where the borehole does not exist in the project. Defaults to true.
            marker_stratigraphy: Limit dataframe to include only markers for one specified MarkerStratigraphy (as returned by markercollection.stratigraphies). Defaults to None.
            well: Limit dataframe to include only markers for a specified Well (as returned by petrelconnection.wells). Defaults to None.

        Returns:
            Dataframe: A dataframe with Marker information, similar to the Well tops spreadsheet in Petrel.
        """
        stratigraphy_droid = self._get_stratigraphy_droid(marker_stratigraphy)
        self._check_well(well)
        
        df = self._markercollection_object_link.GetDataFrameValues(include_unconnected_markers, stratigraphy_droid, well)
        return df

    def _as_dataframe_for_attribute(self, attribute_droid: str, include_unconnected_markers: bool = True, marker_stratigraphy: MarkerStratigraphy = None, well: Well = None) -> pd.DataFrame:
        stratigraphy_droid = self._get_stratigraphy_droid(marker_stratigraphy)
        self._check_well(well)
        df = self._markercollection_object_link.GetDataFrameValuesForAttribute(attribute_droid, include_unconnected_markers, stratigraphy_droid, well)
        return df

    def _as_array_for_attribute(self, attribute_droid: str, include_unconnected_markers: bool = True, marker_stratigraphy: MarkerStratigraphy = None, well: Well = None) -> np.array:
        stratigraphy_droid = self._get_stratigraphy_droid(marker_stratigraphy)
        self._check_well(well)
        array = self._markercollection_object_link.GetArrayValuesForAttribute(attribute_droid, include_unconnected_markers, stratigraphy_droid, well)
        return array

    def _set_values_for_attribute(self, attribute_droid: str, data: np.array, include_unconnected_markers: bool, marker_stratigraphy: MarkerStratigraphy = None, well: Well = None) -> None:

        self._check_input_contains_data(data)

        currentArray = self._as_array_for_attribute(attribute_droid, include_unconnected_markers, marker_stratigraphy, well)
        self._check_input_data_has_correct_length(data, len(currentArray))
        
        currentPropType = self._markercollection_object_link.GetPropTypeForValue(currentArray[0])
        self._check_input_has_expected_data_type(data, currentPropType)

        indices = self._create_indices(data)

        stratigraphy_droid = self._get_stratigraphy_droid(marker_stratigraphy)
        self._check_well(well)

        self._markercollection_object_link.SetPropertyValues(attribute_droid, indices, data, include_unconnected_markers, stratigraphy_droid, well)

    def add_marker(self, well: Well, marker_stratigraphy: MarkerStratigraphy, measured_depth: float):
        """Add a new Marker to the MarkerCollection.
        
        Input:
            well: A Well object as returned from petrelconnection.wells.
            marker_stratigraphy: A MarkerStratigraphy object as returned by markercollection.stratigraphies.
            measured_depth: A float value as the measured depth of the new Marker

        Raises:
            PythonToolException: if the MarkerCollection is read-only
            TypeError: if the well parameter is not a Well object or marker_stratigraphy parameter is not a MarkerStratigraphy object
        """

        if self.readonly:
            raise exceptions.PythonToolException("MarkerCollection is readonly")

        if marker_stratigraphy is None:
            raise TypeError("marker_stratigraphy must be a MarkerStratigrapy object as returned from markercollection.stratigraphies")

        stratigraphy_droid = self._get_stratigraphy_droid(marker_stratigraphy)

        if not isinstance(well, Well):
            raise TypeError("well argument must be a Well object as returned from petrelconnection.wells")
        
        self._markercollection_object_link.AddMarker(well, stratigraphy_droid, measured_depth)

    def add_attribute(self, data: np.array, name: string, data_type: string, include_unconnected_markers: bool = True, marker_stratigraphy: MarkerStratigraphy = None, well: Well = None) -> None:
        """Add a new MarkerAttribute to a MarkerCollection by specifying the data as a numpy array and the name and data_type of the attribute as strings.
           The include_unconnected_markers flag is used for verifying that the length of the provided array matches the expected amount of data. 
           If set to False the attribute will still be added to all markers, but with default values for all unconnected markers.
           If an empty array is passed in the attribute will be added to all markers with default values. For boolean attributes the default value is False.
        
        **Example**:

        Add a new continuous attribute to a markercollection and set values only for the connected markers.

        .. code-block:: python

          import numpy as np
          new_attribute_values = np.array([1.1, 2.2, 3.3])
          markercollection.add_attribute(new_attribute_values, 'MyNewAttribute', 'continuous', False)

        Args:
            data: A numpy array of attributes with format as returned by MarkerAttribute.as_array() 
            name: A string specifying the name of the new attribute
            data_type: A string specifying the data_type. Supported strings are: string | bool | continuous | discrete
            include_unconnected_markers: A boolean flag to include markers where the borehole does not exist in the project. Defaults to True.
            marker_stratigraphy: Limit array to include only markers for one specified MarkerStratigraphy (as returned by markercollection.stratigraphies). Defaults to None.
            well: Limit array to include only markers for a specified Well (as returned by petrelconnection.wells). Defaults to None.

        Raises:
            PythonToolException: if the MarkerCollection is read-only
            ValueError: if the data_type is not 'string | bool | continuous | discrete'
            UserErrorException: if column already exist
        """
        if self.readonly:
            raise exceptions.PythonToolException("MarkerCollection is readonly")

        expectedPropType = self._markercollection_object_link.GetPropTypeFromString(data_type)
        if expectedPropType is None:
            raise ValueError("Unsupported data_type, supported values are: string | bool | continuous | discrete")

        if len(data) > 0:
            stratigraphy_droid = self._get_stratigraphy_droid(marker_stratigraphy)
            self._check_well(well)
            firstAttribute = next(iter(self.attributes))
            firstAttributeArray = self._as_array_for_attribute(firstAttribute._droid, include_unconnected_markers, marker_stratigraphy, well)
            self._check_input_data_has_correct_length(data, len(firstAttributeArray))
            self._check_input_has_expected_data_type(data, expectedPropType)
            indices = self._create_indices(data)
            ok = self._markercollection_object_link.AddAttribute(name, indices, data, include_unconnected_markers, stratigraphy_droid, well)
        else:
            ok = self._markercollection_object_link.AddEmptyAttribute(name, expectedPropType)
      
        if not ok:
            raise UserErrorException("Something went wrong while adding the attribute.")

    @property
    def attributes(self) -> dict:
        """Get a list of MarkerCollection attributes"""
        return MarkerAttributes(self)

    @property
    def stratigraphies(self) -> dict:
        """Get a list of MarkerCollection stratigraphies"""
        return MarkerStratigraphies(self)


    ## Helper methods
    def _check_input_has_expected_data_type(self, data: np.array, expectedPropType) -> None:
        for i in range(len(data)):
            propType = self._markercollection_object_link.GetPropTypeForValue(data[i])
            # Prop type is an int
            if propType != expectedPropType:
                raise ValueError("Input data type does not match expected data type")

    def _check_input_contains_data(self, data: np.array) -> None:
        if len(data) < 1: # No data
            raise ValueError("Input array does not contain any values")

    def _check_input_data_has_correct_length(self, data: np.array, requiredLength) -> None:
        if len(data) != requiredLength:
            raise ValueError("Number of elements in array must match number of markers in markercollection")

    def _create_indices(self, data: np.array) -> list:
        indices = []
        for i in range(len(data)):
            indices.append(i)
        return indices
    
    def _get_stratigraphy_droid(self, marker_stratigraphy: MarkerStratigraphy) -> str:
        stratigraphy_droid = ""
        if marker_stratigraphy is not None:
            if not isinstance(marker_stratigraphy, MarkerStratigraphy):
                raise TypeError("marker_stratigraphy must be a MarkerStratigrapy object as returned from markercollection.stratigraphies")
            stratigraphy_droid = marker_stratigraphy._droid
        return stratigraphy_droid

    def _check_well(self, well):
        if well is not None:
            if not isinstance(well, Well):
                raise ValueError("well argument must be a Well object as returned from petrelconnection.wells")

class MarkerStratigraphies(object):
    """An iterable collection of :class:`MarkerStratigraphy`
    objects for the MarkerStratigraphies in the MarkerCollection"""

    def __init__(self, parent):
        self._parent = parent
        if isinstance(parent, MarkerCollection):
            mc = parent
            self._marker_stratigraphies = [
                MarkerStratigraphy(name, droid, mc)
                for droid, name in mc._markercollection_object_link.GetStratigraphies().items()
            ]
        else:
            raise TypeError("Parent must be MarkerCollection")

    def __len__(self) -> int:
        return len(self._marker_stratigraphies)

    def __iter__(self) -> typing.Iterator[str]:
        return iter(self._marker_stratigraphies)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._marker_stratigraphies[key]
        elif isinstance(key, str):
            stratigraphies = []
            for strat in self._marker_stratigraphies:
                if strat._get_name() == key:
                    stratigraphies.append(strat)
            
            if len(stratigraphies) == 1:
                return stratigraphies[0]
            else:
                raise KeyError("Cannot find unique stratigraphy name " + key)

    def __str__(self) -> str:
        return 'MarkerStratigraphies({0}="{1}")'.format(self._parent._petrel_object_link._sub_type, self._parent)

    def __repr__(self) -> str:
        return str(self)

class MarkerAttributes(object):
    """An iterable collection of :class:`MarkerAttribute`
    objects for the MarkerAttributes in the MarkerCollection"""

    def __init__(self, parent):
        self._parent = parent
        if isinstance(parent, MarkerCollection):
            mc = parent
            petrel_connection = parent._petrel_object_link._plink
            grpcs = [
                MarkerAttributeGrpc(petrelObjectRef.guid, petrel_connection, petrelObjectRef.petrel_name)
                for petrelObjectRef in mc._markercollection_object_link.GetAttributes()
            ]
            self._marker_attributes = [
                MarkerAttribute(grpc, mc)
                for grpc in grpcs
            ]
        else:
            raise TypeError("Parent must be MarkerCollection")

    def __len__(self) -> int:
        return len(self._marker_attributes)

    def __iter__(self) -> typing.Iterator[MarkerAttribute]:
        return iter(self._marker_attributes)

    def __getitem__(self, key):
        index = None
        i = 0
        while i < len(self._marker_attributes):
            if key == self._marker_attributes[i]._get_name():
                index = i
            i += 1
        if index is None:
            return None
        return self._marker_attributes[index]

    def __str__(self) -> str:
        return 'MarkerAttributes({0}="{1}")'.format(self._parent._petrel_object_link._sub_type, self._parent)

    def __repr__(self) -> str:
        return str(self)