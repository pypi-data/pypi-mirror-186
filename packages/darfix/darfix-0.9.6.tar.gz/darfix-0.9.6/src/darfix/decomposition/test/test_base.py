__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "22/04/2020"

import numpy
import unittest

from darfix.decomposition.base import Base


class TestBase(unittest.TestCase):
    """Tests for `base.py`."""

    def setUp(self):
        self.images = numpy.random.random((100, 1000))

    def test_data(self):
        base = Base(self.images)
        numpy.testing.assert_equal(self.images, base.data)

    def test_indices(self):
        base = Base(self.images)
        numpy.testing.assert_equal(base.indices, numpy.arange(len(self.images)))

        base = Base(self.images, indices=numpy.arange(20))
        numpy.testing.assert_equal(base.indices, numpy.arange(20))

    def test_num_components(self):
        base = Base(self.images)
        self.assertEqual(base.num_components, 100)

        base = Base(self.images, num_components=10)
        self.assertEqual(base.num_components, 10)

    def test_W(self):
        base = Base(self.images, num_components=10)
        base.fit_transform()

        self.assertEqual(base.W.shape, (100, 10))

    def test_H(self):
        base = Base(self.images, num_components=10)
        base.fit_transform()

        self.assertEqual(base.H.shape, (10, 1000))

    def test_fit_transform(self):
        base = Base(self.images)
        base.fit_transform(compute_w=False)
        self.assertFalse(hasattr(base, "W"))
        self.assertTrue(hasattr(base, "H"))

        base = Base(self.images)
        base.fit_transform(compute_h=False)
        self.assertFalse(hasattr(base, "H"))
        self.assertTrue(hasattr(base, "W"))

    def test_frobenius_norm(self):
        base = Base(self.images)
        self.assertEqual(base.frobenius_norm(), None)

        base.fit_transform()
        self.assertNotEqual(base.frobenius_norm(), None)
