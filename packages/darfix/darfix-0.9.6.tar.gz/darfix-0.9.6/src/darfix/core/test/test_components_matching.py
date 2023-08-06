__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "20/01/2020"


import unittest

import numpy

from silx.opencl.common import ocl

from darfix.core.componentsMatching import ComponentsMatching, Method
from skimage import data


class TestComponentsMatching(unittest.TestCase):

    """Tests for `componentsMatching.py`."""

    def setUp(self):
        self.components1 = numpy.array([data.moon(), data.camera(), data.gravel()])

        self.components2 = numpy.array(
            [self.components1[2], self.components1[0], self.components1[1]]
        )
        self.componentsMatching = ComponentsMatching(
            components=[self.components1, self.components2]
        )

    def test_euclidean_distance(self):
        ed = self.componentsMatching.euclidean_distance(
            self.components1[0], self.components2[1]
        )

        self.assertEqual(ed, 0)

        ed = self.componentsMatching.euclidean_distance(
            self.components1[1], self.components2[1]
        )

        self.assertNotEqual(ed, 0)

    @unittest.skipUnless(ocl, "PyOpenCl is missing")
    def test_sift_match(self):
        final_matches, matches = self.componentsMatching.match_components(
            method=Method.sift_feature_matching
        )
        self.assertEqual(final_matches[0], 1)

    def test_orb_match(self):
        final_matches, matches = self.componentsMatching.match_components(
            method=Method.orb_feature_matching
        )
        self.assertEqual(final_matches[0], 1)

    def test_draw_matches0(self):
        final_matches, matches = self.componentsMatching.match_components(
            method=Method.orb_feature_matching
        )
        stack = self.componentsMatching.draw_matches(
            final_matches, matches, displayMatches=True
        )
        self.assertEqual(stack[0].shape, (512, 1024))
        stack = self.componentsMatching.draw_matches(
            final_matches, matches, displayMatches=False
        )
        self.assertEqual(stack[1].shape, (512, 1024))

    def test_draw_matches1(self):
        final_matches, matches = self.componentsMatching.match_components(
            method=Method.euclidean_distance
        )
        stack = self.componentsMatching.draw_matches(final_matches, matches)
        self.assertEqual(stack[2].shape, (512, 1024))

    @unittest.skipUnless(ocl, "PyOpenCl is missing")
    def test_draw_matches2(self):
        final_matches, matches = self.componentsMatching.match_components(
            method=Method.sift_feature_matching
        )
        stack = self.componentsMatching.draw_matches(final_matches, matches)
        self.assertEqual(stack[2].shape, (512, 1024))
