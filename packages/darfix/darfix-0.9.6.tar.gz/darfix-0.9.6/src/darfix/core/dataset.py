__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "08/12/2021"

import copy
import glob
import logging
import multiprocessing
import os
import threading
from functools import partial
from multiprocessing import Pool
from enum import IntEnum
from typing import Tuple
from numbers import Number

import h5py
import numpy

import fabio
import silx
from silx.io import utils
from silx.io import fabioh5
from silx.io.url import DataUrl

from darfix.core.dimension import AcquisitionDims, Dimension, POSITIONER_METADATA
from darfix.core.imageOperations import img2img_mean, chunk_image
from darfix.core.imageOperations import (
    background_subtraction,
    background_subtraction_2D,
)
from darfix.core.imageOperations import hot_pixel_removal_3D, hot_pixel_removal_2D
from darfix.core.imageOperations import threshold_removal, mask_removal
from darfix.core.imageOperations import Method
from darfix.core.imageRegistration import shift_detection, apply_shift
from darfix.core.mapping import (
    fit_data,
    fit_2d_data,
    compute_moments,
    compute_rsm,
    compute_magnification,
    calculate_RSM_histogram,
    rescale_data,
)
from darfix.core.roi import apply_2D_ROI, apply_3D_ROI
from darfix.core.utils import wrapTo2pi
from darfix.decomposition.ipca import IPCA
from darfix.decomposition.nmf import NMF
from darfix.decomposition.nica import NICA
from darfix.io import utils as io_utils

_logger = logging.getLogger(__file__)


class Operation(IntEnum):
    """
    Flags for different operations in Dataset
    """

    PARTITION = 0
    BS = 1
    HP = 2
    THRESHOLD = 3
    SHIFT = 4
    ROI = 5
    MOMENTS = 6
    FIT = 7
    BINNING = 8
    MASK = 9


class Dataset:
    """Class to define a dataset from a series of data files.
    The idea of this class is to make life easier for the user when using darfix.
    Most of the operations on darfix need to use all the data to be computed,
    having a wrapper like Dataset allows to execute the operations on that same data
    without having to load the data at each step.
    This is not a God object: Operations on the source data (e.g. blind source separation, hot pixel removal,
    shift correction) are implemented as pure transformations acting on this entity,
    such that there are no side effects and the operations can be chained together to define
    a computational workflow.
    Although it is a complex class due to the next things:
    - The data can be loaded on memory or on disk. When the data is on disk,
    the core operations are called using chunks of the data to reduce its size on memory.
    - A Dataset allows the user to use only part of the data for certain operations,
    which allows to have a much faster processing of those. This is done using the
    `indices` and `bg_indices` attributes.
    - It also allows, for certain operations and at certain cases, to stop a running operation.
    This is done with the attributes `running_data` and `operations_state`, which
    contain the `Data` object with the data being modified and a list of the operations
    to stop.
    - The `dims` attribute is a dictionary containing the dimensions that
    shape the data. Several operations can be applied on only part of the data
    depending on the dimensions shape.

    :param _dir: Global directory to use and save all the data in the different
        operations.
    :type _dir: str
    :param data: If not None, sets the Data array with the data of the dataset
        to use, default None
    :type data: :class:`Data`, optional
    :param raw_folder: Path to the folder that contains the data, defaults to
        None
    :type raw_folder: Union[None,str], optional
    :param filenames: Ordered list of filenames, defaults to None.
    :type filenames: Union[Generator,Iterator,List], optional
    :param dims: Dimensions dictionary
    :type dims: AcquisitionDims, optional
    :param transformation: Axes to use when displaying the images
    :type transformation: ndarray, optional
    :param in_memory: If True, data is loaded into memory, else, data is read in
        chunks depending on the algorithm to apply, defaults to False.
    :type in_memory: bool, optional
    :param copy_files: If True, creates a new treated data folder and doesn't replace
        the directory files.
    :type copy_files: bool, optional
    """

    def __init__(
        self,
        _dir,
        data=None,
        first_filename=None,
        filenames=None,
        dims=None,
        transformation=None,
        in_memory=True,
        copy_files=False,
        isH5=False,
        title="",
    ):

        self._data = None
        self._frames_intensity = []
        self._lock = threading.Lock()
        self.running_data = None
        self.moments_dims = {}
        self.operations_state = numpy.zeros(len(Operation))
        self._dir = _dir
        self._transformation = transformation
        self._title = title
        if copy_files:
            self._dir = os.path.join(self._dir, "treated")
            if not os.path.isdir(self._dir):
                try:
                    os.mkdir(self._dir)
                except PermissionError:
                    raise PermissionError(
                        "Add a directory in the Treated Data tab with WRITE permission"
                    )

        if dims is None:
            self.__dims = AcquisitionDims()
        else:
            assert isinstance(
                dims, AcquisitionDims
            ), "Attribute dims has to be of class AcquisitionDims"
            self.__dims = dims
        # Keys: dimensions names, values: dimensions values
        self._dimensions_values = {}
        self._in_memory = in_memory
        self._isH5 = isH5

        if data is not None:
            self._data = data
        else:
            if filenames is None and first_filename is None:
                filenames = sorted(
                    [x for x in glob.glob(os.path.join(_dir, "*")) if os.path.isfile(x)]
                )
            self.filenames = filenames
            self.first_filename = first_filename

            metadata = []
            data_urls = []

            if self._isH5:
                url = DataUrl(first_filename)
                with silx.io.open(url.file_path()) as h5:
                    for i in range(h5[url.data_path()].shape[0]):
                        data_urls.append(
                            DataUrl(
                                file_path=url.file_path(),
                                data_path=url.data_path(),
                                data_slice=i,
                                scheme="silx",
                            )
                        )
                        metadata.append("For now there is no metadata")
            else:
                with fabio.open_series(
                    filenames=filenames, first_filename=first_filename
                ) as series:
                    for frame in series.frames():
                        filename = frame.file_container.filename
                        data_urls.append(DataUrl(file_path=filename, scheme="fabio"))
                        fabio_reader = fabioh5.EdfFabioReader(file_name=filename)
                        metadata.append(fabio_reader)
                        fabio_reader.close()
            self._data = Data(
                numpy.array(data_urls), metadata=metadata, in_memory=self._in_memory
            )

    def stop_operation(self, operation):
        """
        Method used for cases where threads are created to apply functions to the dataset.
        If method is called, the flag concerning the stop is set to 0 so that if the concerned
        operation is running in another thread it knows to stop.

        :param int operation: operation to stop
        :type int: Union[int, `Operation`]
        """
        if self.operations_state[operation]:
            self._lock.acquire()
            self.operations_state[operation] = 0
            self._lock.release()
        if self.running_data is not None:
            self.running_data.stop_operation(operation)

    @property
    def transformation(self):
        return self._transformation

    @transformation.setter
    def transformation(self, value):
        self._transformation = value

    @property
    def title(self):
        return self._title

    @property
    def dir(self):
        return self._dir

    def compute_frames_intensity(self, kernel=(3, 3), sigma=20):
        """
        Returns for every image a number representing its intensity. This number
        is obtained by first blurring the image and then computing its variance.
        """
        _logger.info("Computing intensity per frame")
        io_utils.advancement_display(0, self.nframes, "Computing intensity")
        frames_intensity = []
        self._lock.acquire()
        self.operations_state[Operation.PARTITION] = 1
        self._lock.release()

        for i in range(self.nframes):
            import cv2

            if not self.operations_state[Operation.PARTITION]:
                return
            frames_intensity += [
                cv2.GaussianBlur(self.get_data(i), kernel, sigma).var()
            ]
            io_utils.advancement_display(i + 1, self.nframes, "Computing intensity")
        self._frames_intensity = frames_intensity
        self._lock.acquire()
        self.operations_state[Operation.PARTITION] = 0
        self._lock.release()
        return self._frames_intensity

    def partition_by_intensity(self, bins=None, bottom_bin=None, top_bin=None):
        """
        Function that computes the data from the set of urls.
        If the filter_data flag is activated it filters the data following the next:
        -- First, it computes the intensity for each frame, by calculating the variance after
        passing a gaussian filter.
        -- Second, computes the histogram of the intensity.
        -- Finally, saves the data of the frames with an intensity bigger than a threshold.
        The threshold is set to be the second bin of the histogram.

        :param int num_bins: Number of bins to use as threshold.
        """
        frames_intensity = (
            self._frames_intensity
            if self._frames_intensity
            else self.compute_frames_intensity()
        )
        if frames_intensity is None:
            return
        values, bins = numpy.histogram(
            frames_intensity, self.nframes if bins is None else bins
        )
        frames_intensity = numpy.asanyarray(frames_intensity)
        if top_bin is None:
            top_bin = len(bins) - 1
        if bottom_bin is None:
            bottom_bin = 0

        bottom_threshold = frames_intensity >= bins[bottom_bin]
        top_threshold = frames_intensity <= bins[top_bin]
        threshold = numpy.array(
            [a and b for a, b in zip(bottom_threshold, top_threshold)]
        )
        return numpy.flatnonzero(threshold), numpy.flatnonzero(~threshold)

    @property
    def in_memory(self):
        return self._in_memory

    @in_memory.setter
    def in_memory(self, in_memory):
        """
        Removes data from memory and sets that from now on data will be read from disk.
        """
        if self._in_memory is not in_memory:
            self._in_memory = in_memory
            self._data = Data(self.data.urls, self.data.metadata, self._in_memory)

    @property
    def data(self):
        return self._data

    def get_data(self, indices=None, dimension=None, return_indices=False):
        """
        Returns the data corresponding to certains indices and given some dimensions values.
        The data is always flattened to be a stack of images.

        :param array_like indices: If not None, data is filtered using this array.
        :param array_like dimension: If not None, return only the data corresponding to
            the given dimension. Dimension is a 2d vector, where the first component is
            a list of the axis and the second is a list of the indices of the values to extract.
            The dimension and value list length can be up to the number of dimensions - 1.
            The call get_data(dimension=[[1, 2], [2, 3]]) is equivalent to data[:, 2, 3] when data
            is in memory.
            The axis of the dimension is so that lower the axis, fastest the dimension (higher changing
            value).

        :return: Array with the new data.
        """
        if dimension is not None and len(self._data.shape) > 3:
            # Make sure dimension and value are lists
            if type(dimension[0]) is int:
                dimension[0] = [dimension[0]]
                dimension[1] = [dimension[1]]
            data = self.data
            indices = numpy.arange(self.nframes) if indices is None else indices
            # Init list of bool indices
            bool_indices = numpy.zeros(self.data.flatten().shape[:-2], dtype=bool)
            bool_indices[indices] = True
            bool_indices = bool_indices.reshape(self.data.shape[:-2])
            indx = numpy.arange(self.nframes).reshape(self.data.shape[:-2])
            # For every axis, get corresponding elements
            for i, dim in enumerate(sorted(dimension[0])):
                # Flip axis to be consistent with the data shape
                axis = self.dims.ndim - dim - 1
                data = data.take(indices=dimension[1][i], axis=axis)
                bool_indices = bool_indices.take(indices=dimension[1][i], axis=axis)
                indx = indx.take(indices=dimension[1][i], axis=axis)
            data = data[bool_indices]
            indx = indx[bool_indices]
            if return_indices:
                return data.flatten(), indx.flatten()
            return data.flatten()
        else:
            data = self.data.flatten()
            if return_indices:
                return (
                    (data, numpy.arange(len(data)))
                    if indices is None
                    else (data[indices], indices)
                )
            return data if indices is None else data[indices]

    @property
    def nframes(self):
        """
        Return number of frames
        """
        if self.data is None:
            return 0
        else:
            return len(self.data.flatten())

    def to_memory(self, indices):
        """
        Method to load only part of the data into memory.
        Returns a new dataset with the data corresponding to given indices into memory.
        The new indices array has to be given, if all the data has to be set into
        memory please set `in_memory` to True instead, this way no new dataset will be
        created.

        :param array_like indices: Indices of the new dataset.
        """
        if not self._in_memory:
            data = self.get_data(indices)
            new_data = Data(data.urls, data.metadata, True)
        else:
            new_data = self.get_data(indices)
        return Dataset(
            _dir=self._dir,
            data=new_data,
            dims=self.__dims,
            in_memory=True,
            title=self.title,
        )

    @property
    def dims(self):
        return self.__dims

    @dims.setter
    def dims(self, _dims):
        assert isinstance(_dims, AcquisitionDims), (
            "Dimensions dictionary has " "to be of class `AcquisitionDims`"
        )
        self.__dims = _dims

    def clear_dims(self):
        self.__dims = AcquisitionDims()

    def add_dim(self, axis, dim):
        """
        Adds a dimension to the dimension's dictionary.

        :param int axis: axis of the dimension.
        :param `Dimension` dim: dimension to be added.
        """
        self.__dims.add_dim(axis, dim)

    def remove_dim(self, axis):
        """
        Removes a dimension from the dimension's dictionary.

        :param int axis: axis of the dimension.
        """
        self.__dims.remove_dim(axis)

    def zsum(self, indices=None, dimension=None):
        data = self.get_data(indices, dimension)
        return data.sum(axis=0)

    def reshape_data(self):
        """
        Function that reshapes the data to fit the dimensions.
        """
        if self.__dims.ndim == 1 and self.__dims.get(0).size == self.nframes:
            return self
        elif self.__dims.ndim > 1:
            try:
                shape = list(self.__dims.shape)
                shape.append(self.get_data().shape[-2])
                shape.append(self.get_data().shape[-1])
                data = self.get_data().reshape(shape)
                return Dataset(
                    _dir=self.dir,
                    data=data,
                    dims=self.__dims,
                    in_memory=self._in_memory,
                    title=self.title,
                )
            except Exception:
                raise ValueError(
                    "Failed to reshape data into dimensions {} \
                                  Try using another tolerance or size values.".format(
                        " ".join(self.__dims.get_names())
                    )
                )
        else:
            raise ValueError("Not enough dimensions where found")

    def find_dimensions(self, kind, tolerance=1e-9):
        """
        Goes over all the headers from a given kind and finds the dimensions
        that move (have more than one value) along the data.

        Note: Before, only the dimensions that could fit where shown, now it
        shows all the dimensions and let the user choose the valid ones.

        :param int kind: Type of metadata to find the dimensions.
        :param float tolerance: Tolerance that will be used to compute the
            unique values.
        """
        self.__dims.clear()
        self._dimensions_values = {}
        if self._isH5:
            return False
        keys = numpy.array(list(self.data.metadata[0].get_keys(kind)))
        values = numpy.array(
            [self.get_metadata_values(kind=kind, key=key) for key in keys]
        )
        # Unique values for each key.
        unique_values = [
            numpy.unique(value, return_index=True, return_counts=True)
            for value in values
        ]
        dimensions = []
        dataset_size = len(self.data.metadata)
        # For every key that has more than one different value, creates a new Dimension.
        for i, value in enumerate(unique_values):
            if value[2][0] != dataset_size:
                try:
                    dimension = Dimension(kind, keys[i], tolerance=tolerance)
                    dimension.set_unique_values(
                        numpy.array(values[i][numpy.sort(value[1])], dtype=float)
                    )
                    # Value that tells when does the change of value occur. It is used to know the order
                    # of the reshaping.
                    dimension.changing_value = self.__compute_changing_value(values[i])
                    dimensions.append(dimension)
                except ValueError:
                    _logger.warning("Couldn't convert to float")

        for dimension in sorted(
            dimensions, key=lambda x: x.changing_value, reverse=True
        ):
            self.__dims.add_dim(axis=self.__dims.ndim, dim=dimension)
            _logger.info(
                "Dimension {} of size {} has been added for reshaping".format(
                    dimension.name, dimension.size
                )
            )
        return True

    def get_metadata_values(self, kind, key, indices=None, dimension=None):

        values = []
        missing_value = False
        for data in self.get_data(indices, dimension).metadata:
            try:
                values += [data.get_value(kind=kind, name=key)[0]]
            except KeyError:
                missing_value = True
                if len(values):
                    values += [values[-1]]
                else:
                    values = ["0"]

        if missing_value:
            import warnings

            warnings.warn(
                "Missing value(s) filled to previous value for kind {} and key {}".format(
                    key, kind
                )
            )

        return values

    def __compute_changing_value(self, values, changing_value=1):
        """
        Recursive method used to calculate how fast is a dimension. The speed of a dimension is the number of
        times the dimension changes of value while moving through the dataset.
        """
        if len(numpy.unique(values)) > 1:
            return self.__compute_changing_value(
                values[: int(len(values) / 2)], changing_value + 1
            )
        else:
            return changing_value

    def get_dimensions_values(self, indices=None):
        """
        Returns all the metadata values of the dimensions.
        The values are assumed to be numbers.

        :returns: array_like
        """
        if not self._dimensions_values or indices is not None:
            for dimension in self.__dims:
                self._dimensions_values[dimension[1].name] = self.get_metadata_values(
                    kind=dimension[1].kind, key=dimension[1].name, indices=indices
                )
        return self._dimensions_values

    def compute_mosaicity_colorkey(
        self, dimensions=[0, 1], scale=100, indices=None, third_motor=None
    ):
        """
        Computes a mosaicity colorkey from the dimensions, and returns also the
        orientation distribution image.
        """
        # only work with 2 dimensions
        assert len(dimensions) == 2, "Only works with two motors"
        if self.__dims and self.__dims.ndim > 1:
            new_shape = []
            dims_list = []
            for axis in dimensions:
                dim = self.__dims.get(axis)
                dims_list += [numpy.linspace(-1, 1, dim.size * scale)]
                new_shape += [dim.size]
            dims_list.reverse()
            mesh = numpy.meshgrid(*dims_list)
            data = numpy.arctan2(mesh[0], mesh[1])
            normalized_data = wrapTo2pi(data) / numpy.pi / 2
            sqr = numpy.sqrt(
                numpy.power(mesh[0], 2) + numpy.power(mesh[1], 2)
            ) / numpy.sqrt(2)
            hsv_key = numpy.stack(
                (
                    normalized_data,
                    sqr,
                    numpy.ones((len(dims_list[1]), len(dims_list[0]))),
                ),
                axis=2,
            )

            ori_dist = numpy.zeros(new_shape[0] * new_shape[1])
            _slice1 = ori_dist.shape[0] * third_motor
            _slice2 = ori_dist.shape[0] * (third_motor + 1)
            ori_dist[indices] = self.get_data(indices).sum(axis=1)[_slice1:_slice2]
            return ori_dist.reshape(numpy.flip(new_shape)).T, hsv_key
        return None, None

    def apply_background_subtraction(
        self,
        background=None,
        method="median",
        indices=None,
        step=None,
        chunk_shape=[100, 100],
        _dir=None,
    ):
        """
        Applies background subtraction to the data and saves the new data
        into disk.

        :param background: Data to be used as background. If None, data with indices `indices` is used.
            If Dataset, data of the dataset is used. If array, use data with indices in the array.
        :type background: Union[None, array_like, Dataset]
        :param method: Method to use to compute the background.
        :type method: Method
        :param indices: Indices of the images to apply background subtraction.
            If None, the background subtraction is applied to all the data.
        :type indices: Union[None, array_like]
        :param int step: Distance between images to be used when computing the median.
            Parameter used only when flag in_memory is False and method is `Method.median`.
            If `step` is not None, all images with distance of `step`, starting at 0,
            will be loaded into memory for computing the median, if the data loading throws
            a MemoryError, the median computation is tried with `step += 1`.
        :param chunk_shape: Shape of the chunk image to use per iteration.
            Parameter used only when flag in_memory is False and method is `Method.median`.
        :type chunk_shape: array_like
        :returns: dataset with data of same size as `self.data` but with the
            modified images. The urls of the modified images are replaced with
            the new urls.
        :rtype: Dataset
        """

        _dir = self.dir if _dir is None else _dir

        if not os.path.isdir(_dir):
            os.mkdir(_dir)

        temp_dir = os.path.join(_dir, "temp_dir")

        if not os.path.isdir(temp_dir):
            os.mkdir(temp_dir)

        method = Method.from_value(method)

        self.running_data = self.get_data(indices)

        self._lock.acquire()
        self.operations_state[Operation.BS] = 1
        self._lock.release()

        if background is None:
            bg_data = self.running_data
            if indices is None:
                _logger.info(
                    "Computing background from " + method.name + " of raw data"
                )
            else:
                _logger.info(
                    "Computing background from "
                    + method.name
                    + " of high intensity data"
                )
        elif isinstance(background, Dataset):
            bg_data = background.data
            _logger.info(
                "Computing background from " + method.name + " of `background` set"
            )
        else:
            bg_data = self.get_data(background)
            _logger.info(
                "Computing background from " + method.name + " of low intensity data"
            )

        if self._in_memory:
            new_data = background_subtraction(self.running_data, bg_data, method).view(
                Data
            )
            new_data.save(os.path.join(temp_dir, "data.hdf5"))
            urls = new_data.urls
        else:
            bg = numpy.zeros(self.running_data[0].shape, self.running_data.dtype)
            if method == Method.mean:
                if bg_data.in_memory:
                    numpy.mean(bg_data, out=bg, axis=0)
                else:
                    io_utils.advancement_display(
                        0, len(bg_data), "Computing mean image"
                    )
                    for i in range(len(bg_data)):
                        if not self.operations_state[Operation.BS]:
                            return
                        bg = img2img_mean(bg_data[i], bg, i)
                        io_utils.advancement_display(
                            i + 1, len(bg_data), "Computing mean image"
                        )
            elif method == Method.median:
                if bg_data.in_memory:
                    numpy.median(bg_data, out=bg, axis=0)
                else:
                    if step is not None:
                        bg_indices = numpy.arange(0, len(bg_data), step)
                        try:
                            numpy.median(
                                Data(
                                    bg_data.urls[bg_indices],
                                    bg_data.metadata[bg_indices],
                                ),
                                out=bg,
                                axis=0,
                            )
                        except MemoryError:
                            if not self.operations_state[Operation.BS]:
                                return
                            print("MemoryError, trying with step {}".format(step + 1))
                            return self.apply_background_subtraction(
                                background, method, indices, step + 1
                            )
                    else:
                        start = [0, 0]
                        img = self.running_data[0]
                        bg = numpy.empty(img.shape, img.dtype)
                        chunks_1 = int(numpy.ceil(img.shape[0] / chunk_shape[0]))
                        chunks_2 = int(numpy.ceil(img.shape[1] / chunk_shape[1]))
                        io_utils.advancement_display(
                            0,
                            chunks_1 * chunks_2 * len(bg_data),
                            "Computing median image",
                        )
                        for i in range(chunks_1):
                            for j in range(chunks_2):
                                if not self.operations_state[Operation.BS]:
                                    return
                                c_images = []
                                cpus = multiprocessing.cpu_count()
                                with Pool(cpus - 1) as p:
                                    c_images = p.map(
                                        partial(chunk_image, start, chunk_shape),
                                        bg_data,
                                    )
                                io_utils.advancement_display(
                                    i * chunks_2 + j + 1,
                                    chunks_1 * chunks_2,
                                    "Computing median image",
                                )
                                numpy.median(
                                    c_images,
                                    out=bg[
                                        start[0] : start[0] + chunk_shape[0],
                                        start[1] : start[1] + chunk_shape[1],
                                    ],
                                    axis=0,
                                )
                                start[1] = chunk_shape[1] * (j + 1)
                            start[0] = chunk_shape[0] * (i + 1)
                            start[1] = 0

            if not self.operations_state[Operation.BS]:
                return
            urls = self.running_data.apply_funcs(
                [(background_subtraction_2D, [bg])],
                save=os.path.join(temp_dir, "data.hdf5"),
                text="Applying background subtraction",
                operation=Operation.BS,
            )
            if urls is None:
                return

        self._lock.acquire()
        self.operations_state[Operation.BS] = 0
        self._lock.release()

        # Set urls as shape and dimension of original urls.
        if indices is not None:
            new_urls = numpy.array(self.get_data().urls, dtype=object)
            new_urls[indices] = urls
            new_data = Data(
                new_urls.reshape(self.data.urls.shape),
                self.data.metadata,
                self._in_memory,
            )
        else:
            new_data = Data(
                urls.reshape(self.data.urls.shape), self.data.metadata, self._in_memory
            )

        new_data.save(os.path.join(_dir, "data.hdf5"), indices=indices)

        try:
            os.remove(os.path.join(temp_dir, "data.hdf5"))
            os.rmdir(temp_dir)
        except OSError as e:
            _logger.warning("Error: %s" % (e.strerror))

        return Dataset(
            _dir=_dir,
            data=new_data,
            dims=self.__dims,
            transformation=self.transformation,
            in_memory=self._in_memory,
            title=self.title,
        )

    def apply_hot_pixel_removal(self, kernel=3, indices=None, _dir=None):
        """
        Applies hot pixel removal to Data, and saves the new data
        into disk.

        :param int kernel: size of the kernel used to find the hot
            pixels.
        :param indices: Indices of the images to apply background subtraction.
            If None, the hot pixel removal is applied to all the data.
        :type indices: Union[None, array_like]
        :return: dataset with data of same size as `self.data` but with the
            modified images. The urls of the modified images are replaced with
            the new urls.
        :rtype: Dataset
        """

        self.running_data = self.get_data(indices)

        _dir = self.dir if _dir is None else _dir

        if not os.path.isdir(_dir):
            os.mkdir(_dir)

        temp_dir = os.path.join(_dir, "temp_dir")

        if not os.path.isdir(temp_dir):
            os.mkdir(temp_dir)

        if self._in_memory:
            new_data = hot_pixel_removal_3D(self.running_data, kernel).view(Data)
            new_data.save(os.path.join(temp_dir, "data.hdf5"))
            urls = new_data.urls
        else:
            urls = self.running_data.apply_funcs(
                [(hot_pixel_removal_2D, [kernel])],
                save=os.path.join(temp_dir, "data.hdf5"),
                text="Applying hot pixel removal",
                operation=Operation.HP,
            )
            if urls is None:
                return

        if indices is not None:
            new_urls = numpy.array(self.get_data().urls, dtype=object)
            new_urls[indices] = urls
            new_data = Data(
                new_urls.reshape(self.data.urls.shape),
                self.data.metadata,
                self._in_memory,
            )
        else:
            new_data = Data(
                urls.reshape(self.data.urls.shape), self.data.metadata, self._in_memory
            )

        new_data.save(os.path.join(_dir, "data.hdf5"), indices=indices)
        try:
            os.remove(os.path.join(temp_dir, "data.hdf5"))
            os.rmdir(temp_dir)
        except OSError as e:
            _logger.warning("Error: %s" % (e.strerror))

        return Dataset(
            _dir=_dir,
            data=new_data,
            dims=self.__dims,
            transformation=self.transformation,
            in_memory=self._in_memory,
            title=self.title,
        )

    def apply_threshold_removal(self, bottom=None, top=None, indices=None, _dir=None):
        """
        Applies bottom threshold to Data, and saves the new data
        into disk.

        :param int bottom: bottom threshold to apply.
        :param int top: top threshold to apply.
        :param indices: Indices of the images to apply background subtraction.
            If None, the hot pixel removal is applied to all the data.
        :type indices: Union[None, array_like]
        :return: dataset with data of same size as `self.data` but with the
            modified images. The urls of the modified images are replaced with
            the new urls.
        :rtype: Dataset
        """

        self.running_data = self.get_data(indices)

        _dir = self.dir if _dir is None else _dir

        if not os.path.isdir(_dir):
            os.mkdir(_dir)

        temp_dir = os.path.join(_dir, "temp_dir")

        if not os.path.isdir(temp_dir):
            os.mkdir(temp_dir)

        if self._in_memory:
            new_data = threshold_removal(self.running_data, bottom, top).view(Data)
            new_data.save(os.path.join(temp_dir, "data.hdf5"))
            urls = new_data.urls
        else:
            urls = self.running_data.apply_funcs(
                [(threshold_removal, [bottom, top])],
                save=os.path.join(temp_dir, "data.hdf5"),
                text="Applying threshold",
                operation=Operation.THRESHOLD,
            )
            if urls is None:
                return
        if indices is not None:
            new_urls = numpy.array(self.get_data().urls, dtype=object)
            new_urls[indices] = urls
            new_data = Data(
                new_urls.reshape(self.data.urls.shape),
                self.data.metadata,
                self._in_memory,
            )
        else:
            new_data = Data(
                urls.reshape(self.data.urls.shape), self.data.metadata, self._in_memory
            )

        new_data.save(os.path.join(_dir, "data.hdf5"), indices=indices)
        try:
            os.remove(os.path.join(temp_dir, "data.hdf5"))
            os.rmdir(temp_dir)
        except OSError as e:
            _logger.warning("Error: %s" % (e.strerror))

        return Dataset(
            _dir=_dir,
            data=new_data,
            dims=self.__dims,
            transformation=self.transformation,
            in_memory=self._in_memory,
            title=self.title,
        )

    def apply_mask_removal(self, mask, indices=None, _dir=None):
        """
        Applies mask to Data, and saves the new data into disk.

        :param nd.array mask: Mask to apply with 0's on the mask.
        :param indices: Indices of the images to apply background subtraction.
            If None, the hot pixel removal is applied to all the data.
        :type indices: Union[None, array_like]
        :return: dataset with data of same size as `self.data` but with the
            modified images. The urls of the modified images are replaced with
            the new urls.
        :rtype: Dataset
        """

        if not numpy.any(mask):
            return self

        self.running_data = self.get_data(indices)

        _dir = self.dir if _dir is None else _dir

        if not os.path.isdir(_dir):
            os.mkdir(_dir)

        temp_dir = os.path.join(_dir, "temp_dir")

        if not os.path.isdir(temp_dir):
            os.mkdir(temp_dir)

        if self._in_memory:
            new_data = mask_removal(self.running_data, mask).view(Data)
            new_data.save(os.path.join(temp_dir, "data.hdf5"))
            urls = new_data.urls
        else:
            urls = self.running_data.apply_funcs(
                [(mask_removal, [mask])],
                save=os.path.join(temp_dir, "data.hdf5"),
                text="Removing mask",
                operation=Operation.MASK,
            )
            if urls is None:
                return
        if indices is not None:
            new_urls = numpy.array(self.get_data().urls, dtype=object)
            new_urls[indices] = urls
            new_data = Data(
                new_urls.reshape(self.data.urls.shape),
                self.data.metadata,
                self._in_memory,
            )
        else:
            new_data = Data(
                urls.reshape(self.data.urls.shape), self.data.metadata, self._in_memory
            )

        new_data.save(os.path.join(_dir, "data.hdf5"), indices=indices)
        try:
            os.remove(os.path.join(temp_dir, "data.hdf5"))
            os.rmdir(temp_dir)
        except OSError as e:
            _logger.warning("Error: %s" % (e.strerror))

        return Dataset(
            _dir=_dir,
            data=new_data,
            dims=self.__dims,
            transformation=self.transformation,
            in_memory=self._in_memory,
            title=self.title,
        )

    def apply_roi(
        self, origin=None, size=None, center=None, indices=None, roi_dir=None
    ):
        """
        Applies a region of interest to the data.

        :param origin: Origin of the roi
        :param size: [Height, Width] of the roi.
        :param center: Center of the roi
        :type origin: Union[2d vector, None]
        :type center: Union[2d vector, None]
        :type size: Union[2d vector, None]
        :param indices: Indices of the images to apply background subtraction.
            If None, the roi is applied to all the data.
        :type indices: Union[None, array_like]
        :param roi_dir: Directory path for the new dataset
        :type roi_dir: str
        :returns: dataset with data with roi applied.
            Note: To preserve consistence of shape between images, if `indices`
            is not None, only the data modified is returned.
        :rtype: Dataset
        """

        roi_dir = self.dir if roi_dir is None else roi_dir
        if not os.path.isdir(roi_dir):
            os.mkdir(roi_dir)

        self.running_data = self.get_data(indices)
        if self._in_memory:
            new_data = (
                apply_3D_ROI(self.running_data, origin, size, center).view(Data).copy()
            )
            new_data.save(os.path.join(roi_dir, "data.hdf5"), new_shape=new_data.shape)
        else:
            shape = numpy.append(
                [self.running_data.shape[0]],
                apply_2D_ROI(self.running_data[0], origin, size, center).shape,
            )
            urls = self.running_data.apply_funcs(
                [(apply_2D_ROI, [origin, size, center])],
                save=os.path.join(roi_dir, "data.hdf5"),
                text="Applying roi",
                operation=Operation.ROI,
                new_shape=shape,
            )
            if urls is None:
                return
            new_data = Data(urls, self.running_data.metadata, self._in_memory)

        transformation = self.transformation
        if transformation is not None:
            transformation = Transformation(
                transformation.kind,
                apply_2D_ROI(transformation.x, origin, size, center),
                apply_2D_ROI(transformation.y, origin, size, center),
                transformation.rotate,
            )

        if indices is None:
            shape = list(self.data.shape)[:-2]
            shape.append(new_data.shape[-2])
            shape.append(new_data.shape[-1])
            new_data = new_data.reshape(shape)
        return Dataset(
            _dir=roi_dir,
            data=new_data,
            dims=self.__dims,
            transformation=transformation,
            in_memory=self._in_memory,
            title=self.title,
        )

    def find_shift(self, dimension=None, steps=50, indices=None):
        """
        Find shift of the data or part of it.

        :param dimension: Parametes with the position of the data in the reshaped
            array.
        :type dimension: Union[None, tuple, array_like]
        :param float h_max: See `core.imageRegistration.shift_detection`
        :param float h_step: See `core.imageRegistration.shift_detection`
        :param indices: Boolean index list with True in the images to apply the shift to.
            If None, the hot pixel removal is applied to all the data.
        :type indices: Union[None, array_like]
        :returns: Array with shift per frame.
        """
        return shift_detection(self.get_data(indices, dimension), steps)

    def find_shift_along_dimension(self, dimension, steps=50, indices=None):
        shift = []
        for value in range(self.dims.get(dimension[0]).size):
            shift.append(self.find_shift([dimension[0], value], steps, indices))
        return numpy.array(shift)

    def apply_shift_along_dimension(
        self,
        shift,
        dimension,
        shift_approach="fft",
        indices=None,
        callback=None,
        _dir=None,
    ):

        dataset = self
        for value in range(self.dims.get(dimension[0]).size):
            data, rindices = self.get_data(
                indices=indices, dimension=[dimension[0], value], return_indices=True
            )
            frames = numpy.arange(
                self.get_data(indices=indices, dimension=[dimension[0], value]).shape[0]
            )
            dataset = dataset.apply_shift(
                numpy.outer(shift[value], frames),
                [dimension[0], value],
                shift_approach,
                indices,
                callback,
                _dir,
            )

        return dataset

    def apply_shift(
        self,
        shift,
        dimension=None,
        shift_approach="fft",
        indices=None,
        callback=None,
        _dir=None,
    ):
        """
        Apply shift of the data or part of it and save new data into disk.

        :param array_like shift: Shift per frame.
        :param dimension: Parametes with the position of the data in the reshaped
            array.
        :type dimension: Union[None, tuple, array_like]
        :param Union['fft', 'linear'] shift_approach: Method to use to apply the shift.
        :param indices: Boolean index list with True in the images to apply the shift to.
            If None, the hot pixel removal is applied to all the data.
        :type indices: Union[None, array_like]
        :param Union[function, None] callback: Callback
        :returns: dataset with data of same size as `self.data` but with the
            modified images. The urls of the modified images are replaced with
            the new urls.
        """
        assert len(shift) > 0, "Shift list can't be empty"

        if not numpy.any(shift):
            return self

        _dir = self.dir if _dir is None else _dir

        if not os.path.isdir(_dir):
            os.mkdir(_dir)

        data, rindices = self.get_data(indices, dimension, return_indices=True)
        self._lock.acquire()
        self.operations_state[Operation.SHIFT] = 1
        self._lock.release()
        try:
            filename = os.path.join(_dir, "data.hdf5")
            _file = h5py.File(filename, "a")
        except OSError:
            if os.path.exists(filename):
                os.remove(filename)
            _file = h5py.File(filename, "w")
        dataset_name = "dataset"
        if "dataset" not in _file:
            _file.create_dataset(
                "dataset", self.get_data().shape, dtype=self.data.dtype
            )
        elif self.get_data().shape != _file["dataset"].shape:
            del _file["dataset"]
            _file.create_dataset(
                "dataset", self.get_data().shape, dtype=self.data.dtype
            )
        else:
            dataset_name = "update_dataset"
            _file.copy("dataset", "update_dataset")

        io_utils.advancement_display(0, len(data), "Applying shift")
        if dimension is not None:
            # Convert dimension and value into list
            if type(dimension[0]) is int:
                dimension[0] = [dimension[0]]
                dimension[1] = [dimension[1]]
            urls = []
            for i, idx in enumerate(rindices):
                if not self.operations_state[Operation.SHIFT]:
                    if "update_dataset" in _file:
                        del _file["update_dataset"]
                    return
                img = apply_shift(data[i], shift[:, i], shift_approach)
                if shift[:, i].all() > 1:
                    shift_approach = "linear"
                _file[dataset_name][idx] = img
                urls.append(
                    DataUrl(
                        file_path=_dir + "/data.hdf5",
                        data_path="/dataset",
                        data_slice=idx,
                        scheme="silx",
                    )
                )
                io_utils.advancement_display(i + 1, len(rindices), "Applying shift")

            # Replace specific urls that correspond to the modified data
            new_urls = numpy.array(self.data.urls, dtype=object)
            copy_urls = new_urls
            if indices is not None:
                # Create array of booleans to know which indices we have
                bool_indices = numpy.zeros(self.get_data().shape[:-2], dtype=bool)
                bool_indices[indices] = True
                bool_indices = bool_indices.reshape(self.data.shape[:-2])
                for i, dim in enumerate(sorted(dimension[0])):
                    # Flip axis to be consistent with the data shape
                    axis = self.dims.ndim - dim - 1
                    copy_urls = numpy.swapaxes(copy_urls, 0, axis)[dimension[1][i], :]
                    bool_indices = numpy.swapaxes(bool_indices, 0, axis)[
                        dimension[1][i], :
                    ]
                copy_urls[bool_indices] = urls
            else:
                for i, dim in enumerate(sorted(dimension[0])):
                    # Flip axis to be consistent with the data shape
                    axis = self.dims.ndim - dim - 1
                    copy_urls = numpy.swapaxes(copy_urls, 0, axis)[dimension[1][i], :]
                copy_urls[:] = urls
        else:
            urls = []
            for i, idx in enumerate(rindices):
                if not self.operations_state[Operation.SHIFT]:
                    if "update_dataset" in _file:
                        del _file["update_dataset"]
                    return
                if shift[:, i].all() > 1:
                    shift_approach = "linear"
                img = apply_shift(data[i], shift[:, i], shift_approach)
                _file[dataset_name][idx] = img
                urls.append(
                    DataUrl(
                        file_path=_dir + "/data.hdf5",
                        data_path="/dataset",
                        data_slice=idx,
                        scheme="silx",
                    )
                )
                io_utils.advancement_display(i + 1, len(data), "Applying shift")
            if indices is not None:
                new_urls = numpy.array(self.data.urls, dtype=object).flatten()
                numpy.put(new_urls, indices, urls)
            else:
                new_urls = numpy.array(urls)

        self._lock.acquire()
        self.operations_state[Operation.SHIFT] = 0
        self._lock.release()

        if dataset_name == "update_dataset":
            del _file["dataset"]
            _file["dataset"] = _file["update_dataset"]
            del _file["update_dataset"]

        _file.close()
        data = Data(
            new_urls.reshape(self.data.urls.shape),
            self.data.metadata,
            in_memory=self._in_memory,
        )
        return Dataset(
            _dir=_dir,
            data=data,
            dims=self.__dims,
            transformation=self.transformation,
            in_memory=self._in_memory,
            title=self.title,
        )

    def find_and_apply_shift(
        self,
        dimension=None,
        steps=100,
        shift_approach="fft",
        indices=None,
        callback=None,
    ):
        """
        Find the shift of the data or part of it and apply it.

        :param dimension: Parametes with the position of the data in the reshaped
            array.
        :type dimension: Union[None, tuple, array_like]
        :param float h_max: See `core.imageRegistration.shift_detection`
        :param float h_step: See `core.imageRegistration.shift_detection`
        :param Union['fft', 'linear'] shift_approach: Method to use to apply the shift.
        :param indices: Indices of the images to find and apply the shift to.
            If None, the hot pixel removal is applied to all the data.
        :type indices: Union[None, array_like]
        :param Union[function, None] callback: Callback
        :returns: Dataset with the new data.
        """
        shift = self.find_shift(dimension, steps, indices=indices)
        return self.apply_shift(shift, dimension, indices=indices)

    def _waterfall_nmf(
        self, num_components, iterations, vstep=None, hstep=None, indices=None
    ):
        """
        This method is used as a way to improve the speed of convergence of
        the NMF method. For this, it uses a waterfall model where at every step
        the output matrices serve as input for the next.
        That is, the method starts with a smaller resized images of the data,
        and computes the NMF decomposition. The next step is the same but with
        bigger images, and using as initial H and W the precomputed matrices.
        The last step is done using the actual size of the images.
        This way, the number of iterations with big images can be diminished, and
        the method converges faster.

        :param int num_components: Number of components to find.
        :param array_like iterations: Array with number of iterations per step of the waterfall.
            The size of the array sets the size of the waterfall.
        :param Union[None, array_like] indices: If not None, apply method only to indices of data.
        """

        from skimage.transform import resize
        import shutil

        W = None
        H = None
        shape = numpy.asarray(self.get_data(0).shape)
        first_size = (shape / (len(iterations) + 1)).astype(int)
        size = first_size

        if not os.path.isdir(os.path.join(self.dir, "waterfall")):
            os.mkdir(os.path.join(self.dir, "waterfall"))

        _logger.info("Starting waterfall NMF")

        for i in range(len(iterations)):
            new_urls = []
            if indices is None:
                indices = range(self.nframes)
            for j in indices:
                filename = os.path.join(self.dir, "waterfall", str(j) + ".npy")
                numpy.save(filename, resize(self.get_data(j), size))
                new_urls.append(DataUrl(file_path=filename, scheme="fabio"))
            data = Data(new_urls, self.get_data(indices).metadata, self._in_memory)
            dataset = Dataset(
                _dir=os.path.join(self.dir, "waterfall"),
                data=data,
                in_memory=self._in_memory,
            )
            if vstep:
                v_step = vstep * (len(iterations) - i)
            if hstep:
                h_step = hstep * (len(iterations) - i)
            H, W = dataset.nmf(
                num_components, iterations[i], W=W, H=H, vstep=v_step, hstep=h_step
            )
            size = first_size * (i + 2)
            H2 = numpy.empty((H.shape[0], size[0] * size[1]))
            for row in range(H.shape[0]):
                H2[row] = resize(H[row].reshape((i + 1) * first_size), size).flatten()
            H = H2

        try:
            shutil.rmtree(os.path.join(self.dir, "waterfall"))
        except Exception as e:
            print(
                "Failed to delete %s. Reason: %s"
                % (os.path.join(self.dir, "waterfall"), e)
            )

        H = resize(H, (num_components, shape[0] * shape[1]))

        return H, W

    def pca(self, num_components=None, chunk_size=500, indices=None, return_vals=False):
        """
        Compute Principal Component Analysis on the data.
        The method, first converts, if not already, the data into an hdf5 file object
        with the images flattened in the rows.

        :param num_components: Number of components to find.
            If None, it uses the minimum between the number of images and the
            number of pixels.
        :type num_components: Union[None, int]
        :param chunk_size: Number of chunks for which the whitening must be computed,
            incrementally, defaults to None
        :type chunksize: Union[None, int], optional
        :param indices: If not None, apply method only to indices of data, defaults to None
        :type indices: Union[None, array_like], optional
        :param return_vals: If True, returns only the singular values of PCA, else returns
            the components and the mixing matrix, defaults to False
        :type return_vals: bool, optional

        :return: (H, W): The components matrix and the mixing matrix.
        """
        bss_dir = os.path.join(self.dir, "bss")
        if not os.path.isdir(bss_dir):
            os.mkdir(bss_dir)
        if self._in_memory:
            from sklearn import decomposition

            model = decomposition.PCA(n_components=num_components)
            try:
                if indices is not None:
                    W = model.fit_transform(self.data.convert_to_hdf5(bss_dir)[indices])
                else:
                    W = model.fit_transform(self.data.convert_to_hdf5(bss_dir)[:, :])
            finally:
                self.data._file.close()

            H, vals, W = model.components_, model.singular_values_, W
        else:
            model = IPCA(
                self.data.convert_to_hdf5(bss_dir),
                chunk_size,
                num_components,
                indices=indices,
            )
            file = h5py.File(os.path.join(bss_dir, "ipca.hdf5"), "w")
            H, W, vals = None, None, None
            try:
                file["W"] = numpy.random.random(
                    (model.num_samples, model.num_components)
                )
                file["H"] = numpy.random.random(
                    (model.num_components, model.num_features)
                )
                model.fit_transform(W=file["W"], H=file["H"])
            finally:
                file.close()
                self.data._file.close()

            H, vals, W = model.H, model.singular_values, model.W
        return vals if return_vals else (H, W)

    def nica(
        self,
        num_components,
        chunksize=None,
        num_iter=500,
        error_step=None,
        indices=None,
    ):
        """
        Compute Non-negative Independent Component Analysis on the data.
        The method, first converts, if not already, the data into an hdf5 file object
        with the images flattened in the rows.

        :param num_components: Number of components to find
        :type num_components: Union[None, int]
        :param chunksize: Number of chunks for which the whitening must be computed,
            incrementally, defaults to None
        :type chunksize: Union[None, int], optional
        :param num_iter: Number of iterations, defaults to 500
        :type num_iter: int, optional
        :param error_step: If not None, find the error every error_step and compares it
            to check for convergence. TODO: not able for huge datasets.
        :param indices: If not None, apply method only to indices of data, defaults to None
        :type indices: Union[None, array_like], optional

        :return: (H, W): The components matrix and the mixing matrix.
        """
        bss_dir = os.path.join(self.dir, "bss")
        if not os.path.isdir(bss_dir):
            os.mkdir(bss_dir)

        if self._in_memory:
            chunksize = None
        model = NICA(
            self.data.convert_to_hdf5(bss_dir),
            num_components,
            chunksize,
            indices=indices,
        )
        try:
            model.fit_transform(max_iter=num_iter, error_step=error_step)
            return numpy.abs(model.H), numpy.abs(model.W)
        finally:
            self.data._file.close()

    def nmf(
        self,
        num_components,
        num_iter=100,
        error_step=None,
        waterfall=None,
        H=None,
        W=None,
        vstep=100,
        hstep=1000,
        indices=None,
        init=None,
    ):
        """
        Compute Non-negative Matrix Factorization on the data.
        The method, first converts, if not already, the data into an hdf5 file object
        with the images flattened in the rows.

        :param num_components: Number of components to find
        :type num_components: Union[None, int]
        :param num_iter: Number of iterations, defaults to 100
        :type num_iter: int, optional
        :param error_step: If not None, find the error every error_step and compares it
            to check for convergence, defaults to None
            TODO: not able for huge datasets.
        :type error_step: Union[None, int], optional
        :param waterfall: If not None, NMF is computed using the waterfall method.
            The parameter should be an array with the number of iterations per
            sub-computation, defaults to None
        :type waterfall: Union[None, array_like], optional
        :param H: Init matrix for H of shape (n_components, n_samples), defaults to None
        :type H: Union[None, array_like], optional
        :param W: Init matrix for W of shape (n_features, n_components), defaults to None
        :type W: Union[None, array_like], optional
        :param indices: If not None, apply method only to indices of data, defaults to None
        :type indices: Union[None, array_like], optional

        :return: (H, W): The components matrix and the mixing matrix.
        """
        bss_dir = os.path.join(self.dir, "bss")
        if not os.path.isdir(bss_dir):
            os.mkdir(bss_dir)

        if self._in_memory:
            from sklearn import decomposition

            model = decomposition.NMF(
                n_components=num_components, init=init, max_iter=num_iter
            )
            if indices is not None:
                X = self.data.convert_to_hdf5(bss_dir)[indices]
            else:
                X = self.data.convert_to_hdf5(bss_dir)
            if numpy.any(X[:, :] < 0):
                _logger.warning("Setting negative values to 0 to compute NMF")
                X[X[:, :] < 0] = 0
            try:
                if H is not None:
                    H = H.astype(X.dtype)
                if W is not None:
                    W = W.astype(X.dtype)
                W = model.fit_transform(X, W=W, H=H)
                return model.components_, W
            finally:
                self.data._file.close()
        else:
            if waterfall is not None:
                H, W = self._waterfall_nmf(
                    num_components, waterfall, vstep, hstep, indices=indices
                )

            model = NMF(
                self.data.convert_to_hdf5(bss_dir), num_components, indices=indices
            )
            try:
                model.fit_transform(
                    max_iter=num_iter,
                    H=H,
                    W=W,
                    vstep=vstep,
                    hstep=hstep,
                    error_step=error_step,
                )
                return model.H, model.W
            finally:
                self.data._file.close()

    def nica_nmf(
        self,
        num_components,
        chunksize=None,
        num_iter=500,
        waterfall=None,
        error_step=None,
        vstep=100,
        hstep=1000,
        indices=None,
    ):
        """
        Applies both NICA and NMF to the data. The init H and W for NMF are the
        result of NICA.
        """
        H, W = self.nica(num_components, chunksize, num_iter, indices=indices)

        # Initial NMF factorization: X = F0 * G0
        W = numpy.abs(W)
        H = numpy.abs(H)

        return self.nmf(
            min(num_components, H.shape[0]),
            num_iter,
            error_step,
            waterfall,
            H,
            W,
            vstep,
            hstep,
            indices=indices,
            init="custom",
        )

    def apply_moments(self, indices=None, chunk_shape=[500, 500]):
        """
        Compute the COM, FWHM, skewness and kurtosis of the data for very dimension.

        :param indices: If not None, apply method only to indices of data, defaults to None
        :type indices: Union[None, array_like], optional
        :param chunk_shape: Shape of the chunk image to use per iteration.
            Parameter used only when flag in_memory is False.
        :type chunk_shape: array_like, optional
        """

        if not self.dims.ndim:
            return None
        self.running_data = self.get_data(indices)
        if indices is None:
            indices = range(self.nframes)
        for axis, dim in self.dims:
            # Get motor values per image of the stack
            values = self.get_dimensions_values(indices)[dim.name]
            if self._in_memory:
                # Data in memory
                com, std, skew, kurt = compute_moments(values, self.running_data)
            else:
                # Data in disk
                start = [0, 0]
                img = self.running_data[0]
                moments = numpy.empty(
                    (4, img.shape[0], img.shape[1]), dtype=numpy.float64
                )
                chunks_1 = int(numpy.ceil(img.shape[0] / chunk_shape[0]))
                chunks_2 = int(numpy.ceil(img.shape[1] / chunk_shape[1]))
                io_utils.advancement_display(
                    0, chunks_1 * chunks_2 * len(self.running_data), "Computing moments"
                )
                for i in range(chunks_1):
                    for j in range(chunks_2):
                        c_images = []
                        cpus = multiprocessing.cpu_count()
                        with Pool(cpus - 1) as p:
                            c_images = p.map(
                                partial(chunk_image, start, chunk_shape),
                                self.running_data,
                            )
                        io_utils.advancement_display(
                            i * chunks_2 + j + 1,
                            chunks_1 * chunks_2,
                            "Computing moments",
                        )
                        com, std, skew, kurt = compute_moments(values, c_images)
                        moments[0][
                            start[0] : start[0] + chunk_shape[0],
                            start[1] : start[1] + chunk_shape[1],
                        ] = com
                        moments[1][
                            start[0] : start[0] + chunk_shape[0],
                            start[1] : start[1] + chunk_shape[1],
                        ] = std
                        moments[2][
                            start[0] : start[0] + chunk_shape[0],
                            start[1] : start[1] + chunk_shape[1],
                        ] = skew
                        moments[3][
                            start[0] : start[0] + chunk_shape[0],
                            start[1] : start[1] + chunk_shape[1],
                        ] = kurt
                        start[1] = chunk_shape[1] * (j + 1)
                    start[0] = chunk_shape[0] * (i + 1)
                    start[1] = 0
                com, std, skew, kurt = moments[0], moments[1], moments[2], moments[3]
            self.moments_dims[axis] = numpy.array(
                [com, std, skew, kurt], dtype=numpy.float64
            )

        return self.moments_dims

    def apply_fit(
        self, indices=None, int_thresh=None, chunk_shape=[100, 100], _dir=None
    ):
        """
        Fits the data around axis 0 and saves the new data into disk.

        :param indices: Indices of the images to fit.
            If None, the fit is done to all the data.
        :type indices: Union[None, array_like]
        :param int_thresh: see `mapping.fit_pixel`
        :type int_thresh: Union[None, float]
        :param chunk_shape: Shape of the chunk image to use per iteration.
            Parameter used only when flag in_memory is False.
        :type chunk_shape: array_like
        :returns: dataset with data of same size as `self.data` but with the
            modified images. The urls of the modified images are replaced with
            the new urls.
        :rtype: Dataset
        """

        _dir = self.dir if _dir is None else _dir
        _dir = os.path.join(_dir, "fit")

        if not os.path.isdir(_dir):
            os.mkdir(_dir)

        self._lock.acquire()
        self.operations_state[Operation.FIT] = 1
        self._lock.release()

        urls = []
        values = None
        shape = None
        data = self.get_data(indices)
        # Fit can only be done if rocking curves are at least of size 3
        if len(data) < 3:
            _logger.warning("Not enough values for fitting")
            return self
        if indices is None:
            indices = range(data.shape[0])

        if self.dims.ndim == 2:
            xdim = self.dims.get(0)
            ydim = self.dims.get(1)
            values = [
                self.get_metadata_values(kind=xdim.kind, key=xdim.name),
                self.get_metadata_values(kind=ydim.kind, key=ydim.name),
            ]
            shape = [xdim.size, ydim.size]
            _fit = fit_2d_data
            data = self.get_data()
            maps = numpy.empty((7,) + data[0].shape)
        else:
            data = self.get_data(indices)
            _fit = fit_data
            if self.dims.ndim > 0:
                values = self.get_metadata_values(
                    kind=self.dims.get(0).kind,
                    key=self.dims.get(0).name,
                    indices=indices,
                )
            else:
                values = None
            maps = numpy.empty((4,) + data[0].shape)
        if not data.in_memory:
            # Use chunks to load the data into memory
            start = [0, 0]
            chunks_1 = int(numpy.ceil(data.shape[1] / chunk_shape[0]))
            chunks_2 = int(numpy.ceil(data.shape[2] / chunk_shape[1]))
            img = numpy.empty((data.shape[1], data.shape[2]))
            io_utils.advancement_display(
                0, chunks_1 * chunks_2 * len(data), "Fitting rocking curves"
            )
            for i in range(chunks_1):
                for j in range(chunks_2):
                    if not self.operations_state[Operation.FIT]:
                        return
                    # Use multiprocessing to chunk the images
                    cpus = multiprocessing.cpu_count()
                    with Pool(cpus - 1) as p:
                        c_images = p.map(partial(chunk_image, start, chunk_shape), data)
                    fitted_data, chunked_maps = _fit(
                        numpy.asarray(c_images),
                        values=values,
                        shape=shape,
                        indices=indices,
                        int_thresh=int_thresh,
                    )
                    for k in range(len(fitted_data)):
                        filename = os.path.join(
                            _dir, "data_fit_" + str(indices[k]).zfill(4) + ".npy"
                        )
                        if (i, j) != (0, 0):
                            # If chunk is not the first, load image from disk
                            img = numpy.load(filename)
                        else:
                            urls.append(DataUrl(file_path=filename, scheme="fabio"))
                        img[
                            start[0] : start[0] + chunk_shape[0],
                            start[1] : start[1] + chunk_shape[1],
                        ] = fitted_data[k]
                        numpy.save(filename, img)
                        io_utils.advancement_display(
                            i * chunks_2 * len(data) + j * len(data) + k + 1,
                            chunks_1 * chunks_2 * len(data),
                            "Fitting rocking curves",
                        )
                    maps[
                        :,
                        start[0] : start[0] + chunk_shape[0],
                        start[1] : start[1] + chunk_shape[1],
                    ] = chunked_maps
                    start[1] = chunk_shape[1] * (j + 1)
                start[0] = chunk_shape[0] * (i + 1)
                start[1] = 0
        else:
            fitted_data, maps = _fit(
                data,
                values=values,
                shape=shape,
                int_thresh=int_thresh,
                indices=indices,
                _tqdm=True,
            )
            for i, image in enumerate(fitted_data):
                filename = os.path.join(
                    _dir, "data_fit" + str(indices[i]).zfill(4) + ".npy"
                )
                numpy.save(filename, image)
                urls.append(DataUrl(file_path=filename, scheme="fabio"))
        self._lock.acquire()
        self.operations_state[Operation.FIT] = 0
        self._lock.release()

        if indices is not None:
            # Replace only fitted data urls
            new_urls = numpy.array(self.data.urls, dtype=object).flatten()
            numpy.put(new_urls, indices, urls)
        else:
            new_urls = numpy.array(urls)

        data = Data(
            new_urls.reshape(self.data.urls.shape),
            self.data.metadata,
            in_memory=self._in_memory,
        )  # to modify
        return (
            Dataset(
                _dir=_dir,
                data=data,
                dims=self.__dims,
                transformation=self.transformation,
                in_memory=self._in_memory,
                title=self.title,
            ),
            maps,
        )

    def compute_transformation(
        self, d, kind="magnification", rotate=False, topography=[False, 0], center=True
    ):

        """
        Computes transformation matrix.
        Depending on the kind of transformation, computes either RSM or magnification
        axes to be used on future widgets.

        :param d: Size of the pixel
        :type d: float
        :param kind: Transformation to apply, either 'magnification' or 'rsm'
        :type kind: str
        :param rotate: To be used only with kind='rsm', if True the images with
            transformation are rotated 90 degrees.
        :type rotate: bool
        :param topography: To be used only with kind='magnification', if True
            obpitch values are divided by its sine.
        :type topography: bool
        """

        H, W = self.get_data(0).shape
        self.rotate = rotate

        if self.dims.ndim == 1 and kind == "rsm":
            ffz = self.get_metadata_values(POSITIONER_METADATA, "ffz")[0]
            mainx = -self.get_metadata_values(POSITIONER_METADATA, "mainx")[0]
            x, y = compute_rsm(H, W, d, ffz, mainx, rotate)
        else:
            obx = self.get_metadata_values(POSITIONER_METADATA, "obx")[0]
            obpitch = numpy.unique(
                self.get_metadata_values(POSITIONER_METADATA, "obpitch")
            )
            obpitch = obpitch[len(obpitch) // 2]
            mainx = -self.get_metadata_values(POSITIONER_METADATA, "mainx")[0]
            x, y = compute_magnification(
                H, W, d, obx, obpitch, mainx, topography, center
            )
        self.transformation = Transformation(kind, x, y, rotate)

    def project_data(self, dimension, indices=None, _dir=None):

        """
        Applies a projection to the data.
        The new Dataset will have the same size as the chosen dimension, where
        the data is projected on.

        :param dimension: Dimensions to project the data onto
        :type dimension: array_like
        :param indices: Indices of the images to use for the projection.
            If None, the projection is done using all data.
        :type indices: Union[None, array_like]
        :param str _dir: Directory filename to save the new data
        """

        _dir = self.dir if _dir is None else _dir
        if not os.path.isdir(_dir):
            os.mkdir(_dir)

        dims = AcquisitionDims()
        if len(dimension) == 1:
            axis = self.dims.ndim - dimension[0] - 1
            dim = self.dims.get(dimension[0])
            data = []
            for i in range(dim.size):
                _sum = self.zsum(indices=indices, dimension=[dimension[0], i])
                if len(_sum):
                    data += [_sum]
            dims.add_dim(0, dim)
        elif len(dimension) == 2:
            axis = int(numpy.setdiff1d(range(self.dims.ndim), dimension)[0])
            dim1 = self.dims.get(dimension[0])
            dim2 = self.dims.get(dimension[1])
            dims.add_dim(0, dim1)
            dims.add_dim(1, dim2)
            data = []
            for i in range(dim1.size):
                for j in range(dim2.size):
                    _sum = self.zsum(indices=indices, dimension=[dimension, [i, j]])
                    if len(_sum):
                        data += [_sum]
        else:
            return ValueError("Only 1D and 2D projection is allowed")
        dim = self.dims.get(axis)
        data = numpy.array(data).view(Data)
        metadata = numpy.swapaxes(self.data.metadata, self.dims.ndim - 1, axis)
        for i in range(self.dims.ndim - len(dimension)):
            metadata = metadata[0]
        data.save(
            os.path.join(_dir, "project_" + dim.name + ".hdf5"),
            in_memory=self._in_memory,
        )
        data.metadata = metadata

        dataset = Dataset(
            _dir=_dir,
            data=data,
            dims=dims,
            transformation=self.transformation,
            in_memory=self._in_memory,
            title=self.title,
        )

        return dataset.reshape_data()

    def compute_rsm(
        self,
        Q,
        a,
        map_range,
        pixel_size,
        units,
        n,
        map_shape,
        energy=17,
        transformation=None,
    ):

        diffry = self.get_metadata_values(POSITIONER_METADATA, "diffry")
        if transformation is None:
            transformation = self.transformation
        elif self.transformation is None:
            raise ValueError(
                "Transformation has to first be computed using the Transformation Widget (before any ROI)"
            )

        return calculate_RSM_histogram(
            data=self.get_data(),
            diffry_values=diffry,
            twotheta=transformation.y,
            eta=transformation.x,
            Q=Q,
            a=a,
            map_range=map_range,
            units=units,
            map_shape=map_shape,
            n=n,
            E=energy,
        )

    def apply_binning(self, scale, _dir=None):

        _dir = self.dir if _dir is None else _dir
        if not os.path.isdir(_dir):
            os.mkdir(_dir)

        data = rescale_data(self.get_data(), scale)
        shape = data.shape
        data = data.view(Data)
        data.save(
            os.path.join(_dir, "binned_data.hdf5"),
            in_memory=self._in_memory,
            new_shape=shape,
        )
        data.metadata = self.data.metadata
        shape = list(self.data.shape)[:-2]
        shape.append(data.shape[-2])
        shape.append(data.shape[-1])
        data = data.reshape(shape)

        return Dataset(
            _dir=_dir,
            data=data,
            dims=self.dims,
            transformation=self.transformation,
            in_memory=True,
            title=self.title,
        )

    def __deepcopy__(self, memo):
        """
        Create copy of the dataset. The data numpy array is also copied using
        deep copy. The rest of the attributes are the same.
        """
        dataset = type(self)(
            self.dir,
            data=self.data,
            dims=self.__dims,
            in_memory=self.in_memory,
            copy_files=True,
        )
        dataset.dims = copy.deepcopy(self.__dims, memo)
        return dataset


class Data(numpy.ndarray):
    """
    Class to structure the data and link every image with its corresponding url and
    metadata. It inherits from numpy.ndarray and Overrides the necessary methods,
    taking into account the `in_memory` attribute.

    :param urls: Array with the urls of the data
    :type urls: array_like
    :param metadata: Array with the metadata of the data
    :type metadata: array_like
    :param in_memory: If True, the data is loaded into memory, default True
    :type in_memory: bool, optional
    """

    def __new__(cls, urls, metadata, in_memory=True, data=None):
        urls = numpy.asarray(urls)
        if in_memory:
            if data is None or urls.shape != data.shape[:-2]:
                # Create array as stack of images
                # Create array as stack of images
                img = utils.get_data(urls.flatten()[0])
                data = numpy.empty(
                    (urls.flatten().shape[0], img.shape[0], img.shape[1]), img.dtype
                )
                for i, url in enumerate(urls.flatten()):
                    data[i] = utils.get_data(url)
            shape = list(urls.shape)
            shape.append(data.shape[-2])
            shape.append(data.shape[-1])
            obj = data.reshape(shape).view(cls)
        else:
            # Access image one at a time using url
            obj = super(Data, cls).__new__(cls, urls.shape)

        obj.in_memory = in_memory
        obj.urls = urls
        obj.metadata = numpy.asarray(metadata)
        obj._file = None

        obj._lock = threading.Lock()
        obj.operations = numpy.zeros(len(Operation))

        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.urls = getattr(obj, "urls", None)
        self.metadata = getattr(obj, "metadata", None)
        self.in_memory = getattr(obj, "in_memory", None)

    def __getitem__(self, indices):
        """
        Return self[indices]
        """
        if self.in_memory:
            data = super(Data, self).__getitem__(indices)
            if len(data.shape) < 3:
                data = data.view(numpy.ndarray)
            else:
                if isinstance(indices, tuple):
                    data.urls = self.urls[indices[0]]
                    data.metadata = self.metadata[indices[0]]
                else:
                    data.urls = self.urls[indices]
                    data.metadata = self.metadata[indices]
            return data
        if isinstance(indices, tuple):
            if not isinstance(self.urls[indices[0]], numpy.ndarray):
                return utils.get_data(self.urls[indices[0]])[indices[1], indices[2]]
            else:
                return Data(
                    self.urls[indices[0]], self.metadata[indices], self.in_memory
                )
        else:
            if not isinstance(self.urls[indices], numpy.ndarray):
                return utils.get_data(self.urls[indices])
            else:
                return Data(self.urls[indices], self.metadata[indices], self.in_memory)

    def __reduce__(self):
        # Get the parent's __reduce__ tuple
        pickled_state = super(Data, self).__reduce__()
        # Create our own tuple to pass to __setstate__
        new_state = pickled_state[2] + ((self.urls, self.metadata, self.in_memory),)
        # Return a tuple that replaces the parent's __setstate__ tuple with our own
        return (pickled_state[0], pickled_state[1], new_state)

    def __setstate__(self, state):
        self.urls, self.metadata, self.in_memory = state[-1]  # Set the attributes
        super(Data, self).__setstate__(state[0:-1])

    def stop_operation(self, operation):
        """
        Method used for cases where threads are created to apply functions to the data.
        If method is called, the flag concerning the stop is set to 0 so that if the concerned
        operation is running in another thread it knows to stop.

        :param int operation: operation to stop
        :type int: Union[int, `Operation`]
        """
        if hasattr(self, "operations") and self.operations[operation]:
            self._lock.acquire()
            self.operations[operation] = 0
            self._lock.release()

    @property
    def shape(self):
        """
        Tuple of array dimensions.
        """
        if self.in_memory:
            return super(Data, self).shape
        else:
            if not super(Data, self).shape[0]:
                return super(Data, self).shape
            data = self.flatten()[0]
            shape = list(super(Data, self).shape)
            shape.append(data.shape[0])
            shape.append(data.shape[1])
            return tuple(shape)

    @property
    def ndim(self):
        """
        Number of array dimensions.
        """
        if self.in_memory:
            return super(Data, self).ndim
        else:
            return super(Data, self).ndim + 2

    def apply_funcs(
        self,
        funcs=[],
        indices=None,
        save=False,
        text="",
        operation=None,
        new_shape=None,
    ):
        """
        Method that applies a series of functions into the data. It can save the images
        into disk or return them.

        :param funcs: List of tupples. Every tupples contains the function to
            apply and its parameters, defaults to []
        :type funcs: array_like, optional
        :param indices: Indices of the data to apply the functions to,
            defaults to None
        :type indices: Union[None, array_like], optional
        :param save: If True, saves the images into disk, defaults to False
        :type save: bool
        :param str text: Text to show in the advancement display.
        :param int operation: operation to stop
        :type int: Union[int, `Operation`]

        :returns: Array with the new urls (if data was saved)
        """
        if indices is None:
            indices = range(len(self))
        if isinstance(indices, int):
            indices = [indices]
        urls = []
        io_utils.advancement_display(0, len(self.urls.flatten()), text)

        if not hasattr(self, "operations"):
            self.operations = numpy.zeros(len(Operation))
            self._lock = threading.Lock()
        self._lock.acquire()
        self.operations[operation] = 1
        self._lock.release()

        try:
            _file = h5py.File(save, "a")
        except OSError:
            if os.path.exists(save):
                os.remove(save)
            _file = h5py.File(save, "w")

        dataset_name = "dataset"
        new_shape = self.shape if new_shape is None else tuple(new_shape)
        if "dataset" in _file:
            if new_shape != _file["dataset"].shape:
                _file.create_dataset("update_dataset", new_shape, dtype=self.dtype)
            else:
                _file.create_dataset(
                    "update_dataset",
                    shape=_file["dataset"].shape,
                    dtype=_file["dataset"].dtype,
                )
                for i, img in enumerate(_file["dataset"]):
                    _file["update_dataset"][i] = img
            dataset_name = "update_dataset"
        else:
            _file.create_dataset("dataset", new_shape, dtype=self.dtype)

        for i in indices:
            if operation is not None and not self.operations[operation]:
                if "update_dataset" in _file:
                    del _file["update_dataset"]
                return
            #     if save:
            #         for j in indices:
            #             if j != i:
            #                 filename = save + str(j).zfill(4) + ".npy"
            #                 os.remove(filename)
            #             else:
            #                 break
            #     return
            img = self[int(i)]
            for f, args in funcs:
                img = f(*([img] + args))
            if save:
                _file[dataset_name][i] = img
                urls.append(
                    DataUrl(
                        file_path=save,
                        data_path="/dataset",
                        data_slice=i,
                        scheme="silx",
                    )
                )
                # filename = save + str(i).zfill(4) + ".npy"
                # numpy.save(filename, img)
                # urls.append(DataUrl(file_path=filename, scheme='fabio'))
            io_utils.advancement_display(i + 1, len(self.urls.flatten()), text)
        self._lock.acquire()
        self.operations[operation] = 0
        self._lock.release()

        if dataset_name == "update_dataset":
            del _file["dataset"]
            _file["dataset"] = _file["update_dataset"]
            del _file["update_dataset"]

        _file.close()
        return numpy.array(urls)

    def save(self, path, indices=None, new_shape=None, in_memory=True):
        """
        Save the data into `path` folder and replace Data urls.
        TODO: check if urls already exist and, if so, modify only urls[indices].

        :param path: Path to the folder
        :type path: str
        :param indices: the indices of the values to save, defaults to None
        :type indices: Union[None,array_like], optional
        """
        if not hasattr(self, "in_memory") or self.in_memory is None:
            self.in_memory = True
        urls = []

        if indices is None:
            data = self.flatten() if self.urls is not None else self
            indices = numpy.arange(len(data))
        else:
            data = self.flatten()[indices] if self.urls is not None else self[indices]

        try:
            _file = h5py.File(path, "a")
        except OSError:
            if os.path.exists(path):
                os.remove(path)
            _file = h5py.File(path, "w")

        if len(self.shape) > 3:
            shape = self.flatten().shape
        else:
            shape = self.shape
        new_shape = shape if new_shape is None else tuple(new_shape)
        if "dataset" not in _file:
            _file.create_dataset("dataset", new_shape, dtype=self.dtype)
        elif new_shape != _file["dataset"].shape:
            del _file["dataset"]
            _file.create_dataset("dataset", new_shape, dtype=self.dtype)

        for i, j in enumerate(indices):
            _file["dataset"][j] = data[i]
            urls.append(
                DataUrl(
                    file_path=path, data_path="/dataset", data_slice=j, scheme="silx"
                )
            )
        #     filename = path + str(i).zfill(4) + ".npy"
        #     numpy.save(filename, img)
        #     urls.append(DataUrl(file_path=filename, scheme='fabio'))
        _file.close()
        urls = numpy.asarray(urls)
        if self.urls is not None:
            new_urls = self.urls.flatten()
            new_urls[indices] = urls
            self.urls = new_urls.reshape(self.urls.shape)
        else:
            self.urls = numpy.asarray(urls)

    def convert_to_hdf5(self, _dir):
        """
        Converts the data into an HDF5 file, setting flattened images in the rows.
        TODO: pass filename per parameter?

        :param _dir: Directory in which to save the HDF5 file.
        :type _dir: str

        :return: Hdf5 file
        :rtype: `h5py.File`
        """
        try:
            filename = os.path.join(_dir, "data.hdf5")
            self._file = h5py.File(filename, "a")
        except OSError:
            if os.path.exists(filename):
                os.remove(filename)
            self._file = h5py.File(filename, "w")
        data = self.flatten()
        shape = data[0].shape[0] * data[0].shape[1]
        if "dataset" in self._file:
            if self._file["dataset"].shape == (len(data), shape):
                return self._file["dataset"]
            else:
                del self._file["dataset"]
        self._file.create_dataset("dataset", (len(data), shape))
        for i in range(len(data)):
            self._file["dataset"][i] = data[i].flatten()

        return self._file["dataset"]

    def reshape(self, shape, order="C"):
        """
        Returns an array containing the same data with a new shape of urls and metadata.
        Shape also contains image shape at the last two positions (unreshapable).

        :param shape: New shape, should be compatible with the original shape.
        :type shape: int or tuple of ints.
        :return: new Data object with urls and metadata reshaped to shape.
        """
        data = None
        if self.in_memory:
            data = super(Data, self).reshape(shape, order=order).view(numpy.ndarray)
        return Data(
            self.urls.reshape(shape[:-2], order=order),
            self.metadata.reshape(shape[:-2], order=order),
            self.in_memory,
            data=data,
        )

    def sum(self, axis=None, **kwargs):
        """
        Sum of array elements over a given axis.

        :param axis: Only axis accepted are 0 or 1.
            With 0, the sum is done around the z axis, so a resulting image is returned.
            With 1, every images has its pixels summed and the result is a list with
            the intensity of each image.
            With None, a float is the result of the sum of all the pixels and all
            the images.
        :type axis: Union[None, int]

        :return: Summed data
        :rtype: Union[float, list]
        """
        data = self.flatten()
        if self.in_memory:
            if axis == 0:
                return super(Data, data).sum(axis=axis).view(numpy.ndarray)
            elif axis == 1:
                return super(Data, data).view(numpy.ndarray).sum(axis=1).sum(axis=1)
            elif axis is None:
                return super(Data, data).sum()
            else:
                raise TypeError("Axis must be None, 0 or 1")
        else:
            if axis == 0:
                if data.size == 0:
                    return numpy.array([])
                elif not data.shape[0]:
                    return numpy.zeros(data[0].shape)
                zsum = numpy.array(data[0], dtype=numpy.float64)
                for i in range(1, len(data)):
                    zsum += data[i]
                return zsum
            elif axis == 1:
                return numpy.array([i.sum() for i in data])
            elif axis is None:
                img_sum = 0
                for i in data:
                    img_sum += i.sum()
                return img_sum
            else:
                raise TypeError("Axis must be None, 0 or 1")

    def take(self, indices, axis=None, out=None, mode="raise"):
        """
        Take elements from urls and metadata from an array along an axis.

        :param indices: the indices of the values to extract
        :type indices: array_like
        :param axis: the axis over which to select values, defaults to None
        :type axis: Union[N one, int], optional

        :return: Flattened data.
        :rtype: :class:`Data`
        """
        urls = numpy.take(self.urls, indices, axis, mode=mode)
        metadata = numpy.take(self.metadata, indices, axis, mode=mode)
        data = None
        if self.in_memory:
            data = super(Data, self).take(indices, axis, mode=mode).view(numpy.ndarray)
        return Data(urls, metadata, self.in_memory, data=data)

    def flatten(self):
        """
        :return: new data with flattened urls and metadata (but not images).
        :rtype: :class:`Data`
        """
        if len(super(Data, self).shape) < 2:
            return self
        data = None
        urls = self.urls.flatten()
        if self.in_memory:
            data = (
                super(Data, self)
                .reshape((len(urls), self.shape[-2], self.shape[-1]))
                .view(numpy.ndarray)
            )
        return Data(urls, self.metadata.flatten(), self.in_memory, data=data)


class Transformation:
    def __init__(self, kind: str, x: numpy.ndarray, y: numpy.ndarray, rotate: bool):
        self.x = x  # shape (sy, sx)
        self.y = y  # shape (sy, sx)
        self.rotate = rotate
        self.kind = kind

    @property
    def shape(self) -> Tuple[int, int]:
        return self.x.shape

    @property
    def sx(self) -> int:
        return self.shape[1]

    @property
    def sy(self) -> int:
        return self.shape[0]

    @property
    def label(self) -> str:
        return "degrees" if self.kind == "rsm" else "µm"

    @property
    def xregular(self) -> numpy.ndarray:
        return self.xscale * numpy.arange(self.sx) + self.xorigin

    @property
    def yregular(self) -> numpy.ndarray:
        return self.yscale * numpy.arange(self.sy) + self.yorigin

    @property
    def xorigin(self) -> Number:
        return self.x[0][0]

    @property
    def yorigin(self) -> Number:
        return self.y[0][0]

    @property
    def origin(self) -> Tuple[Number, Number]:
        return self.xorigin, self.yorigin

    @property
    def xscale(self) -> Number:
        x = self.x
        return (x[-1][-1] - x[0][0]) / self.sx

    @property
    def yscale(self) -> Number:
        y = self.y
        return (y[-1][-1] - y[0][0]) / self.sy

    @property
    def scale(self) -> Tuple[Number, Number]:
        return self.xscale, self.yscale
