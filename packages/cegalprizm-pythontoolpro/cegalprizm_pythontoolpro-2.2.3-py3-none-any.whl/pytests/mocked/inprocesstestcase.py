# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



import unittest
import cegalprizm.pythontool
from .mocks import *

class InprocessTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.bridge = cegalprizm.pythontool.PetrelLink(MockObjectFactory())
        prop = self.bridge.grid_properties["ThreeProp"]
        prop.readonly = False
        surfaceprop = self.bridge.surface_attributes["ThreeSurfaceProp"]
        surfaceprop.readonly = False
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()