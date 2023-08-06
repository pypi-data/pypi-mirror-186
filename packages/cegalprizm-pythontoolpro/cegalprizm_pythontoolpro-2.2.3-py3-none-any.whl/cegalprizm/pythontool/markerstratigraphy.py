# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.




class MarkerStratigraphy:
    """A class holding information about a MarkerStratigraphy"""

    def __init__(self, name: str, droid: str, parent_markercollection):
        self._name = name
        self._parent_markercollection = parent_markercollection
        self._droid = droid

    def __str__(self) -> str:
        """A readable representation"""
        return 'MarkerStratigraphy("{0}")'.format(self._name)

    def __repr__(self) -> str:
        return str(self)

    def _get_name(self) -> str:
        return self._name

    @property
    def markercollection(self):
        return self._parent_markercollection