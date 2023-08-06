# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.




from cegalprizm.pythontool import PetrelObject
import datetime
import typing
if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.grpc.completion_perforation_grpc import PerforationGrpc

class Perforation(PetrelObject):
    """A class holding information about a Perforation"""

    def __init__(self, petrel_object_link: "PerforationGrpc"):
        super(Perforation, self).__init__(petrel_object_link)
        self._perforation_object_link = petrel_object_link

    def __str__(self) -> str:
        """A readable representation"""
        return 'Perforation("{0}")'.format(self.petrel_name)
    
    def __repr__(self) -> str:
        return str(self)

    @property
    def top_md(self) -> float:
        """The top MD of the perforation.
        
        Returns:
            float: The top MD of the perforation as a float value.
        """
        return self._perforation_object_link.GetTopMd()

    @top_md.setter
    def top_md(self, new_depth: float) -> None:
        ok = self._perforation_object_link.SetTopMd(new_depth)

    @property
    def bottom_md(self) -> float:
        """The bottom MD of the perforation.
        
        Returns:
            float: The bottom MD of the perforation as a float value.
        """
        return self._perforation_object_link.GetBottomMd()

    @bottom_md.setter
    def bottom_md(self, new_depth: float) -> None:
        ok = self._perforation_object_link.SetBottomMd(new_depth)


    @property
    def start_date(self) -> datetime.datetime:
        """The start date of the perforation.
        
        Returns:
            datetime.datetime: The start date of the perforation as a datetime object.
        """
        return self._perforation_object_link.GetDate()

    @start_date.setter
    def start_date(self, new_date: datetime.datetime) -> None:
        if not isinstance(new_date, datetime.datetime):
            raise TypeError("The new date must be a datetime.datetime object")
        return self._perforation_object_link.SetDate(new_date)

    @property
    def skin_factor(self) -> float:
        """The skin factor of the perforation.
        
        Returns:
            float: The skin factor of the perforation as a float value.
        """
        return self._perforation_object_link.GetSkinFactor()

    @skin_factor.setter
    def skin_factor(self, new_skin_factor: float) -> None:
        ok = self._perforation_object_link.SetSkinFactor(new_skin_factor)