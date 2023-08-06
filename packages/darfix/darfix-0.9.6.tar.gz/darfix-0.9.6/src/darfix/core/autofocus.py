__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "02/09/2019"


import numpy


def normalized_variance(img):
    """
    Computes the normalized variance autofocus function into the given image.
    """
    img = numpy.asanyarray(img)
    return img.var() / img.mean()
