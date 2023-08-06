__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "05/10/2020"

import numpy


def convertDictToDim(_dict):

    from darfix.core.dataset import Dimension

    """
    Convert dictionary of dimensions from Settings to Dimension.
    """
    if len(_dict) > 0:
        _dims = {}
        for _axis, _dim in _dict.items():
            assert type(_dim) is dict
            _dims[_axis] = Dimension.from_dict(_dim)
        return _dims

    else:
        return {}


def wrapTo2pi(x):
    """
    Python implementation of Matlab method `wrapTo2pi`.
    Wraps angles in x, in radians, to the interval [0, 2*pi] such that 0 maps
    to 0 and 2*pi maps to 2*pi. In general, positive multiples of 2*pi map to
    2*pi and negative multiples of 2*pi map to 0.
    """
    xwrap = numpy.remainder(x - numpy.pi, 2 * numpy.pi)
    mask = numpy.abs(xwrap) > numpy.pi
    xwrap[mask] -= 2 * numpy.pi * numpy.sign(xwrap[mask])
    return xwrap + numpy.pi
