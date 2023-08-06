__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "17/11/2020"

import unittest
import numpy

from darfix.core import mapping


class TestMapping(unittest.TestCase):

    """Tests for `mapping.py`"""

    def setUp(self):
        self.data = numpy.random.random(size=(3, 10, 10))

    def test_generator1(self):
        """Tests the correct creation of a generator without moments"""

        g = mapping.generator(self.data)

        img, moment = next(g)
        self.assertEqual(moment, None)
        numpy.testing.assert_array_equal(img, self.data[:, 0, 0])

    def test_generator2(self):
        """Tests the correct creation of a generator with moments"""

        moments = numpy.ones((3, 10, 10))
        g = mapping.generator(self.data, moments)

        img, moment = next(g)
        numpy.testing.assert_array_equal(moment, moments[:, 0, 0])
        numpy.testing.assert_array_equal(img, self.data[:, 0, 0])

    def test_fit_rocking_curve(self):
        """Tests the correct fit of a rocking curve"""

        samples = numpy.random.normal(size=10000) + numpy.random.random(10000)

        y, bins = numpy.histogram(samples, bins=100)

        y_pred, pars = mapping.fit_rocking_curve([y, None])
        rss = numpy.sum((y - y_pred) ** 2)
        tss = numpy.sum((y - y.mean()) ** 2)
        r2 = 1 - rss / tss

        self.assertGreater(r2, 0.9)
        self.assertEqual(len(pars), 4)

    def test_fit_data(self):
        """Tests the new data has same shape as initial data"""

        new_data, maps = mapping.fit_data(self.data)

        self.assertEqual(new_data.shape, self.data.shape)
        self.assertEqual(len(maps), 4)
        self.assertEqual(maps[0].shape, self.data[0].shape)

    def test_moments(self):
        """Tests the correct moments calculation"""

        values = [0.1, 0.2, 0.3]

        com, std, skews, kurt = mapping.compute_moments(values, self.data)

        self.assertEqual(com.shape, self.data.shape[1:])
        self.assertEqual(std.shape, self.data.shape[1:])
        self.assertEqual(skews.shape, self.data.shape[1:])
        self.assertEqual(kurt.shape, self.data.shape[1:])

    def test_rsm(self):
        """Tests RSM"""

        H, W = self.data.shape[1:]
        d = 0.1
        ffz = 10
        mainx = 5

        pix_arr = mapping.compute_rsm(H, W, d, ffz, mainx)

        self.assertEqual(pix_arr[0].shape, (H, W))
        self.assertEqual(pix_arr[1].shape, (H, W))

    def test_magnification(self):
        """Tests magnification"""

        H, W = self.data.shape[1:]
        d = 0.1
        obx = 10
        obpitch = 25.1
        mainx = 5

        pix_arr = mapping.compute_magnification(H, W, d, obx, obpitch, mainx)

        self.assertEqual(pix_arr[0].shape, (H, W))
        self.assertEqual(pix_arr[1].shape, (H, W))

    def test_magnification_uncentered(self):
        """Tests magnification uncentered"""

        H, W = self.data.shape[1:]
        d = 0.1
        obx = 10
        obpitch = 25.1
        mainx = 50  # Has to be big enough

        pix_arr = mapping.compute_magnification(
            H, W, d, obx, obpitch, mainx, center=False
        )

        self.assertEqual(pix_arr[0][0][0], 0)
        self.assertEqual(pix_arr[1][H - 1][0], 0)

    def test_peak_position(self):
        """Tests peak position map"""

        image = mapping.compute_peak_position(self.data)

        self.assertEqual(image[0, 1], numpy.argmax(self.data[:, 0, 1]))

    def test_peak_position_values(self):
        """Tests peak position map with values"""

        values = numpy.repeat([numpy.linspace(0.1, 1, 10)], 3).flatten()
        image = mapping.compute_peak_position(self.data, values)

        self.assertEqual(image[0, 0], values[numpy.argmax(self.data[:, 0, 0])])
