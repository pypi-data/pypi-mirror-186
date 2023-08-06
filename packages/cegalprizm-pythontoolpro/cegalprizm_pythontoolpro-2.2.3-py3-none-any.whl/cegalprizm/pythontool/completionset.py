# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



import pandas as pd
import typing
from cegalprizm.pythontool.completion_casingstring import CasingString
from cegalprizm.pythontool.completion_perforation import Perforation
from cegalprizm.pythontool.experimental import experimental_class
from cegalprizm.pythontool.grpc.completion_casingstring_grpc import CasingStringGrpc
from cegalprizm.pythontool.grpc.completion_perforation_grpc import PerforationGrpc
if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.grpc.completionset_grpc import CompletionsSetGrpc

@experimental_class
class CompletionsSet():
    """A class holding information about a completions set for a well."""

    def __init__(self, petrel_object_link: "CompletionsSetGrpc"):
        self._completionsset_object_link = petrel_object_link
    
    def __str__(self) -> str:
        """A readable representation"""
        return 'CompletionsSet(well_petrel_name="{0}")'.format(self._completionsset_object_link._parent_well.petrel_name)
    
    def __repr__(self) -> str:
        return self.__str__()

    def as_dataframe(self) -> pd.DataFrame:
        """ Gets a dataframe with information about a the active completions set for a well. 

        Returns:
            Dataframe: A dataframe with completions information. 
        """
        df = self._completionsset_object_link.GetDataframe()
        return df
    
    @property
    def casings(self):
        """ Gets an iterator with the casing strings for the completions set.
        
        Returns:
            An iterable collection of :class:`CasingString` objects for a completions set.
        """
        return CasingStrings(self)
    
    @property
    def perforations(self):
        """ Gets an iterator with the perforations for the completions set.
        
        Returns:
            An iterable collection of :class:`Perforation` objects for a completions set.
        """
        return Perforations(self)

    def add_perforation(self, name: str, top_md: float, bottom_md: float) -> Perforation:
        """ Adds a new perforation to the completions set.
        
        Args:
            name: The name of the new perforation as a string.
            top_md: The top MD of the new perforation as a float.
            bottom_md: The bottom MD of the new perforation as a float.

        Returns:
            The new perforation as a :class:`Perforation` object.
        """
        if(len(name) < 1):
            raise ValueError("name can not be an empty string")
        reference = self._completionsset_object_link.AddPerforation(name, top_md, bottom_md)
        grpc = PerforationGrpc(reference.guid, self._completionsset_object_link._plink)
        return Perforation(grpc)

class CasingStrings(object):
    """An iterable collection  of :class:`CasingString` objects for a completions set.
    """

    def __init__(self, parent):
        self._parent = parent
        if isinstance(parent, CompletionsSet):
            petrel_connection = parent._completionsset_object_link._plink
            grpcs = [
                CasingStringGrpc(petrelObjectRef.guid, petrel_connection)
                for petrelObjectRef in parent._completionsset_object_link.GetCasingStrings()
            ]
            self._casing_strings =  [
                CasingString(grpc)
                for grpc in grpcs
            ]
        else:
            raise TypeError("Parent must be a CompletionsSet object")
        
    def __len__(self) -> int:
        return len(self._casing_strings)

    def __iter__(self) -> typing.Iterator[CasingString]:
        return iter(self._casing_strings)
    
    def __getitem__(self, key):
        result = [x for x in self._casing_strings if x.petrel_name == key]
        if(len(result) == 0):
            return None
        elif len(result) == 1:
            return result[0]
        else:
            return result

    def __str__(self) -> str:
        return 'CasingStrings(CompletionsSet="{0}")'.format(self._parent)

    def __repr__(self) -> str:
        return str(self)
    
class Perforations(object):
    """An iterable collection  of :class:`Perforation` objects for a completions set.
    """

    def __init__(self, parent):
        self._parent = parent
        if isinstance(parent, CompletionsSet):
            petrel_connection = parent._completionsset_object_link._plink
            grpcs = [
                PerforationGrpc(petrelObjectRef.guid, petrel_connection)
                for petrelObjectRef in parent._completionsset_object_link.GetPerforations()
            ]
            self._perforations =  [
                Perforation(grpc)
                for grpc in grpcs
            ]
        else:
            raise TypeError("Parent must be a CompletionsSet object")
        
    def __len__(self) -> int:
        return len(self._perforations)

    def __iter__(self) -> typing.Iterator[Perforation]:
        return iter(self._perforations)
    
    def __getitem__(self, key):
        result = [x for x in self._perforations if x.petrel_name == key]
        if(len(result) == 0):
            return None
        elif len(result) == 1:
            return result[0]
        else:
            return result

    def __str__(self) -> str:
        return 'Perforations(CompletionsSet="{0}")'.format(self._parent)

    def __repr__(self) -> str:
        return str(self)