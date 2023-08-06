__authors__ = ["H.Payno", "J.Garriga"]
__license__ = "MIT"
__date__ = "14/10/2019"

import os
import tempfile

import fabio
import numpy
import string

from silx.resources import ExternalResources

from darfix.core.dataset import Dataset


utilstest = ExternalResources(
    project="darfix",
    url_base="http://www.edna-site.org/pub/darfix/testimages",
    env_key="DATA_KEY",
    timeout=60,
)


def random_generator(size=4, chars=string.printable):
    """
    Returns a string with random characters.
    """
    return "".join(chars[numpy.random.choice(len(chars))] for x in range(size))


def createRandomDataset(
    dims, nb_data_files=20, header=False, _dir=None, in_memory=True
):
    """Simple creation of a dataset in _dir with the requested number of data
    files and dark files.

    :param tuple of int dims: dimensions of the files.
    :param int nb_data_files: Number of data files to create.
    :param int nb_dark_files: Number of dark files to create.
    :param bool header: If True, a random header is created for every frame.
    :param str or None _dir: Directory to save the temporary files.

    :return :class:`Dataset`: generated instance of :class:`Dataset`
    """
    assert type(dims) is tuple and len(dims) == 2
    assert type(nb_data_files) is int
    # assert type(nb_ff_file) is int
    assert type(_dir) in (type(None), str)

    if _dir is None:
        _dir = tempfile.mkdtemp()

    if os.path.isdir(_dir) is False:
        raise ValueError("%s is not a directory" % _dir)

    if header:
        counter_mne = "a b c d e f g h"
        motor_mne = "obpitch y z mainx ffz m obx"
        # Create headers
        header = []
        # Dimensions for reshaping
        a = sorted(numpy.random.rand(2))
        b = [numpy.random.rand()] * numpy.array([1, 1.2, 1.4, 1.6, 1.8])
        c = sorted(numpy.random.rand(2))
        motors = numpy.random.rand(7)
        for i in numpy.arange(nb_data_files):
            header.append({})
            header[i]["HeaderID"] = i
            header[i]["counter_mne"] = counter_mne
            header[i]["motor_mne"] = motor_mne
            header[i]["counter_pos"] = ""
            header[i]["motor_pos"] = ""
            for count in counter_mne:
                header[i]["counter_pos"] += str(numpy.random.rand(1)[0]) + " "
            for j, m in enumerate(motor_mne.split()):
                if m == "z":
                    header[i]["motor_pos"] += (
                        str(a[int((i > 4 and i < 10) or i > 14)]) + " "
                    )
                elif m == "m":
                    header[i]["motor_pos"] += str(b[i % 5]) + " "
                elif m == "obpitch":
                    header[i]["motor_pos"] += str(c[int(i > 9)]) + " "
                else:
                    header[i]["motor_pos"] += str(motors[j]) + " "

            data_file = os.path.join(_dir, "data_file%04i.edf" % i)
            image = fabio.edfimage.EdfImage(
                data=numpy.random.random(dims), header=header[i]
            )
            image.write(data_file)
    else:
        for index in range(nb_data_files):
            data_file = os.path.join(_dir, "data_file%04i.edf" % index)
            image = fabio.edfimage.EdfImage(data=numpy.random.random(dims))
            image.write(data_file)

    dataset = Dataset(_dir=_dir, in_memory=in_memory)
    return dataset


def createDataset(data, filter_data=False, header=None, _dir=None, in_memory=True):
    """
    Create a dataset from a configuration

    :param numpy.ndarray data: Images to form the data.
    :param numpy.ndarray dark_frames: Images to form the dark frames.
    :param bool filter_data: If True, the dataset created will divide the data
        between the ones with no intensity (or very low) and the others.
    :param Union[None,array_like] header: List with a header per frame. If None,
        no header is added.
    :param str or None _dir: Directory to save the temporary files.

    :return :class:`Dataset`: generated instance of :class:`Dataset`.
    """
    assert type(_dir) in (type(None), str)
    assert len(data) > 0
    if header is not None:
        assert len(header) == len(data)

    if _dir is None:
        _dir = tempfile.mkdtemp()

    if os.path.isdir(_dir) is False:
        raise ValueError("%s is not a directory" % _dir)
    for index in range(len(data)):
        data_file = os.path.join(_dir, "data_file%04i.edf" % index)
        if header is not None:
            image = fabio.edfimage.EdfImage(data=data[index], header=header[index])
        else:
            image = fabio.edfimage.EdfImage(data=data[index])

        image.write(data_file)

    dataset = Dataset(_dir=_dir, in_memory=in_memory)

    return dataset
