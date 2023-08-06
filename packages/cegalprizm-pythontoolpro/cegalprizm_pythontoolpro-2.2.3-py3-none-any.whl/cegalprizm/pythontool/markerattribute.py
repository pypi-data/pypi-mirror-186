# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



import pandas as pd
import numpy as np
from cegalprizm.pythontool.markerstratigraphy import MarkerStratigraphy
from cegalprizm.pythontool.borehole import Well
from cegalprizm.pythontool import exceptions, PetrelObject

import typing
if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.grpc.markerattribute_grpc import MarkerAttributeGrpc

class MarkerAttribute(PetrelObject):
    """A class holding information about a MarkerAttribute"""

    def __init__(self, petrel_object_link: "MarkerAttributeGrpc", parent_markercollection):
        super(MarkerAttribute, self).__init__(petrel_object_link)
        self._markerattribute_object_link = petrel_object_link
        self._parent_markercollection = parent_markercollection
        self._name = petrel_object_link._unique_name
        self._droid = petrel_object_link.GetDroidString()

    def __str__(self) -> str:
        """A readable representation"""
        return 'MarkerAttribute("{0}")'.format(self._name)

    def __repr__(self) -> str:
        return str(self)

    def _get_name(self) -> str:
        return self._name

    def as_dataframe(self, include_unconnected_markers: bool = True, marker_stratigraphy: MarkerStratigraphy = None, well: Well = None) -> pd.DataFrame:
        """ Gets a dataframe with information about a MarkerAttribute in the MarkerCollection. 
        
        Args:
            include_unconnected_markers: Flag to include markers where the borehole does not exist in the project. Defaults to true.
            marker_stratigraphy: Limit dataframe to include only markers for one specified MarkerStratigraphy (as returned my markercollection.stratigraphies). Defaults to None.
            well: Limit dataframe to include only markers for a specified Well (as returned by petrelconnection.wells). Defaults to None.

        Returns:
            Dataframe: A dataframe with MarkerAttribute information together with Petrel index, Well identifier and Surface information. 
        """
        df = self._parent_markercollection._as_dataframe_for_attribute(self._droid, include_unconnected_markers, marker_stratigraphy, well)
        return df

    def as_array(self, include_unconnected_markers: bool = True, marker_stratigraphy: MarkerStratigraphy = None, well: Well = None) -> np.array:
        """ Gets a numpy array with the values for MarkerAttribute in the MarkerCollection. 
        
        Args:
            include_unconnected_markers: Flag to include markers where the borehole does not exist in the project. Defaults to true.
            marker_stratigraphy: Limit array to include only markers for one specified MarkerStratigraphy (as returned my markercollection.stratigraphies). Defaults to None.
            well: Limit array to include only markers for a specified Well (as returned by petrelconnection.wells). Defaults to None.

        Returns:
            Array: A numpy array with the values for the MarkerAttribute.
        """
        array = self._parent_markercollection._as_array_for_attribute(self._droid, include_unconnected_markers, marker_stratigraphy, well)
        return array

    def set_values(self, data: np.array, include_unconnected_markers: bool = True, marker_stratigraphy: MarkerStratigraphy = None, well: Well = None) -> None:
        """Attribute values are written to Petrel. The data parameter must be a numpy array.
           The length of the array must match the number of selected markers in the markercollection.

        **Example**:

        Set a new numpy array as the values of a specified attribute and write the new data back to Petrel.

        .. code-block:: python

          import numpy as np
          new_attribute_values = np.array([1.1, 2.2, 3.3])
          my_attribute = markercollection.attributes['my attribute']
          my_attribute.set_values(new_attribute_values, False)

        Args:
            data: A numpy array of attributes with format as returned by as_array() 
            include_unconnected_markers: A boolean flag to include markers where the borehole does not exist in the project. Defaults to True.
            marker_stratigraphy: Limit array to include only markers for one specified MarkerStratigraphy (as returned my markercollection.stratigraphies). Defaults to None.
            well: Limit array to include only markers for a specified Well (as returned by petrelconnection.wells). Defaults to None.

        Raises:
            PythonToolException: if the parent MarkerCollection is read-only
            ValueError: if the data input is empty
        """
        if self._parent_markercollection.readonly:
            raise exceptions.PythonToolException("MarkerCollection is readonly")

        if len(data) < 1:
            raise ValueError("Input array does not contain any values")
        
        return self._parent_markercollection._set_values_for_attribute(self._droid, data, include_unconnected_markers, marker_stratigraphy, well)

    @property
    def markercollection(self):
        return self._parent_markercollection