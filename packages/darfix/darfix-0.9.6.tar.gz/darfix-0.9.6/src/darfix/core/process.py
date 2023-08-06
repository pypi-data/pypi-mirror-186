"""
Module for defining processes to be used by the library `ewoks`. Each of
the processes defined here can be used (its corresponding widgets) within an
Orange workflow and later be converted to an Ewoks workflow without the GUI part needed.
"""

__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "16/07/2021"


import os
from collections import Mapping
from typing import Iterable, Union, Optional
from ewoksutils.import_utils import qualname
import numpy
import copy

from silx.gui import qt
from darfix.core import utils
from darfix.gui.blindSourceSeparationWidget import Method
from darfix.gui.grainPlotWidget import GrainPlotWidget
from darfix.gui.rsmHistogramWidget import RSMHistogramWidget
from darfix.gui.zSumWidget import ZSumWidget
from darfix.gui.rsmWidget import PixelSize
from darfix.core.data_selection import load_process_data
from darfix.io.utils import write_components
from ewokscore import Task
from ewokscore.graph import TaskGraph


def graph_data_selection(
    graph: TaskGraph,
    filenames: Union[str, Iterable[str]],
    root_dir: Optional[str] = None,
    in_memory: bool = True,
    dark_filename: Optional[str] = None,
    copy_files: bool = True,
):
    task_identifier = qualname(DataSelection)
    for node_attrs in graph.graph.nodes.values():
        if node_attrs.get("task_identifier") == task_identifier:
            default_inputs = node_attrs["default_inputs"] = list()
            default_inputs.append({"name": "root_dir", "value": root_dir})
            default_inputs.append({"name": "filenames", "value": filenames})
            default_inputs.append({"name": "dark_filename", "value": dark_filename})
            default_inputs.append({"name": "copy_files", "value": copy_files})
            default_inputs.append({"name": "in_memory", "value": in_memory})
            return
    raise RuntimeError(f"Workflow {graph} does not contain a 'DataSelection' task")


class DataSelection(
    Task,
    input_names=["filenames"],
    optional_input_names=["root_dir", "in_memory", "dark_filename", "copy_files"],
    output_names=["dataset"],
):
    """Simple util class to ignore a processing when executing without GUI"""

    def run(self):
        in_memory = self.inputs.in_memory
        if in_memory == self.MISSING_DATA:
            in_memory = True
        copy_files = self.inputs.copy_files
        if copy_files == self.MISSING_DATA:
            copy_files = True
        dark_filename = self.inputs.dark_filename
        if dark_filename == self.MISSING_DATA:
            dark_filename = None
        self.outputs.dataset = load_process_data(
            filenames=self.inputs.filenames,
            root_dir=self.inputs.root_dir,
            dark_filename=dark_filename,
            in_memory=in_memory,
            copy_files=copy_files,
        )


class DataCopy(
    Task,
    input_names=["dataset"],
    output_names=["dataset"],
):
    def run(self):
        self.outputs.dataset = copy.deepcopy(self.inputs.dataset)


class DataPassThrough(
    Task,
    input_names=["dataset"],
    output_names=["dataset"],
):
    def run(self):
        self.outputs.dataset = self.inputs.dataset


class NoiseRemoval(
    Task,
    input_names=["dataset"],
    optional_input_names=[
        "method",
        "background_type",
        "step",
        "chunks",
        "kernel_size",
        "bottom_threshold",
        "mask",
    ],
    output_names=["dataset"],
):
    def run(self):
        dataset, indices, li_indices, bg_dataset = self.inputs.dataset
        if self.inputs.method:
            step = int(self.inputs.step) if self.inputs.step else None
            chunks = self.inputs.chunks if self.inputs.chunks else None

            bg = None
            if self.inputs.background_type == "Dark data":
                bg = bg_dataset
            elif self.inputs.background_type == "Low intensity data":
                bg = li_indices

            dataset = dataset.apply_background_subtraction(
                indices=indices,
                method=self.inputs.method,
                background=bg,
                step=step,
                chunk_shape=chunks,
            )
        if self.inputs.kernel_size:
            dataset = dataset.apply_hot_pixel_removal(
                indices=indices, kernel=int(self.inputs.kernel_size)
            )

        if self.inputs.bottom_threshold:
            dataset = dataset.apply_threshold_removal(
                bottom=int(self.inputs.bottom_threshold)
            )

        if self.inputs.mask:
            dataset = dataset.apply_mask_removal(mask=self.inputs.mask)

        self.outputs.dataset = dataset, indices, li_indices, bg_dataset


class RoiSelection(
    Task,
    input_names=["dataset"],
    optional_input_names=["roi_origin", "roi_size"],
    output_names=["dataset"],
):
    def run(self):
        dataset, indices, li_indices, bg_dataset = self.inputs.dataset
        origin = numpy.flip(self.inputs.roi_origin) if self.inputs.roi_origin else []
        size = numpy.flip(self.inputs.roi_size) if self.inputs.roi_size else []
        if len(origin) and len(size):
            dataset = dataset.apply_roi(origin=origin, size=size)
            if bg_dataset:
                bg_dataset = bg_dataset.apply_roi(origin=origin, size=size)
        self.outputs.dataset = dataset, indices, li_indices, bg_dataset


class DataPartition(
    Task,
    input_names=["dataset"],
    optional_input_names=["bins", "n_bins"],
    output_names=["dataset"],
):
    def run(self):
        dataset, indices, li_indices, bg_dataset = self.inputs.dataset
        bins = self.inputs.bins if self.inputs.bins else None
        nbins = self.inputs.n_bins if self.inputs.n_bins else 1
        indices, li_indices = dataset.partition_by_intensity(bins, nbins)
        self.outputs.dataset = dataset, indices, li_indices, bg_dataset


class DimensionDefinition(
    Task, input_names=["dataset", "_dims"], output_names=["dataset"]
):
    def run(self):
        dataset, indices, li_indices, bg_dataset = self.inputs.dataset
        assert isinstance(self.inputs._dims, Mapping)
        dims = utils.convertDictToDim(self.inputs._dims)
        if dataset is not None and len(dataset.data.metadata) > 0:
            for axis, dim in dims.items():
                assert type(axis) is int
                dataset.add_dim(axis=axis, dim=dim)
            try:
                dataset = dataset.reshape_data()
                for axis, dimension in dataset.dims:
                    if dataset.dims.ndim > 1:
                        metadata = numpy.swapaxes(dataset.data.metadata, 0, axis)[0]
                    else:
                        metadata = dataset.data.metadata
                    values = []
                    for data in metadata:
                        try:
                            values += [
                                data.get_value(
                                    kind=dimension.kind, name=dimension.name
                                )[0]
                            ]
                        except KeyError:
                            values += ["0"]
                    dimension.set_unique_values(values)
            except ValueError:
                for axis, dimension in dataset.dims:
                    values = numpy.unique(
                        self.dataset.get_dimensions_values()[dimension.name]
                    )
                    dimension.set_unique_values(values)
                dataset = dataset.reshape_data()
        self.outputs.dataset = dataset, indices, li_indices, bg_dataset


class ShiftCorrection(
    Task,
    input_names=["dataset"],
    optional_input_names=["shift"],
    output_names=["dataset"],
):
    def run(self):
        dataset, indices, li_indices, bg_dataset = self.inputs.dataset
        if not self.inputs.shift:
            raise ValueError("Shift not defined")
        frames = numpy.arange(dataset.get_data(indices=indices).shape[0])
        dataset = dataset.apply_shift(
            numpy.outer(self.inputs.shift, frames), indices=indices
        )
        self.outputs.dataset = dataset, indices, li_indices, bg_dataset


class BlindSourceSeparation(
    Task,
    input_names=["dataset", "method"],
    optional_input_names=["n_comp"],
    output_names=["dataset"],
):
    def run(self):
        dataset, indices, li_indices, bg_dataset = self.inputs.dataset
        n_comp = self.inputs.n_comp if self.inputs.n_comp else None
        method = Method[self.inputs.method]
        if method == Method.PCA:
            comp, W = dataset.pca(n_comp, indices=indices)
        elif method == Method.NICA:
            comp, W = dataset.nica(n_comp, indices=indices)
        elif method == Method.NMF:
            comp, W = dataset.nmf(n_comp, indices=indices)
        elif method == Method.NICA_NMF:
            comp, W = dataset.nica_nmf(n_comp, indices=indices)
        else:
            raise ValueError("BSS method not managed")
        n_comp = comp.shape[0]
        shape = dataset.get_data()[0].shape
        comp = comp.reshape(n_comp, shape[0], shape[1])
        if li_indices is not None:
            # If filter data is activated, the matrix W has reduced dimensionality, so reshaping is not possible
            # Create empty array with shape the total number of frames
            W = numpy.zeros((dataset.nframes, n_comp))
            # Set actual values of W where threshold of filter is True
            W[indices] = W
            W = W
        write_components(
            os.path.join(dataset.dir, "components.h5"),
            "entry",
            dataset.get_dimensions_values(),
            W,
            comp,
            1,
        )
        self.outputs.dataset = dataset, indices, li_indices, bg_dataset


class RockingCurves(
    Task,
    input_names=["dataset"],
    optional_input_names=["int_thresh", "dimension"],
    output_names=["dataset"],
):
    def run(self):
        dataset, indices, li_indices, bg_dataset = self.inputs.dataset
        int_thresh = float(self.inputs.int_thresh) if self.inputs.int_thresh else None
        dataset = dataset.apply_fit(indices=indices, int_thresh=int_thresh)
        self.outputs.dataset = dataset, indices, li_indices, bg_dataset


class GrainPlot(Task, input_names=["dataset"], output_names=["dataset"]):
    def run(self):
        app = qt.QApplication([])
        widget = GrainPlotWidget()
        if self.inputs.dataset:
            widget.setDataset(*(None,) + self.inputs.dataset)
        widget.setAttribute(qt.Qt.WA_DeleteOnClose)
        widget.show()
        app.exec_()
        self.outputs.dataset = self.inputs.dataset[1:]


class Transformation(
    Task,
    input_names=["dataset"],
    optional_input_names=[
        "magnification",
        "pixelSize",
        "kind",
        "rotate",
        "orientation",
    ],
    output_names=["dataset"],
):
    def run(self):
        dataset, indices, li_indices, bg_dataset = self.inputs.dataset
        magnification = self.inputs.magnification if self.inputs.magnification else None
        orientation = self.inputs.orientation if self.inputs.orientation else None
        pixelSize = self.inputs.pixelSize if self.inputs.pixelSize else None
        kind = self.inputs.kind if self.inputs.kind else None
        rotate = self.inputs.rotate if self.inputs.rotate else None
        if dataset and dataset.dims.ndim:
            if dataset.dims.ndim == 1 and kind:
                dataset.compute_transformation(
                    PixelSize[pixelSize].value, kind="rsm", rotate=rotate
                )
            else:
                if orientation == -1 or orientation is None:
                    dataset.compute_transformation(magnification, topography=[False, 0])
                else:
                    dataset.compute_transformation(
                        magnification, topography=[True, orientation]
                    )
        self.outputs.dataset = dataset, indices, li_indices, bg_dataset


class ZSum(
    Task,
    input_names=["dataset"],
    optional_input_names=["plot"],
    output_names=["dataset"],
):
    def run(self):
        self.outputs.dataset = self.inputs.dataset
        if self.inputs.plot:
            app = qt.QApplication([])
            widget = ZSumWidget()
            if self.inputs.dataset:
                widget.setDataset((None,) + self.inputs.dataset)
            widget.setAttribute(qt.Qt.WA_DeleteOnClose)
            widget.show()
            app.exec_()


class Projection(
    Task,
    input_names=["dataset"],
    optional_input_names=["dimension"],
    output_names=["dataset"],
):
    def run(self):
        dataset, indices, li_indices, bg_dataset = self.inputs.dataset
        dimension = self.inputs.dimension
        if dimension:
            dataset = dataset.project_data(dimension=dimension, indices=indices)
        self.outputs.dataset = dataset, indices, li_indices, bg_dataset


class RSMHistogram(
    Task,
    input_names=["dataset"],
    optional_input_names=[
        "q",
        "a",
        "map_range",
        "detector",
        "units",
        "n",
        "map_shape",
        "energy",
    ],
    output_names=["dataset"],
):
    def run(self):
        app = qt.QApplication([])
        widget = RSMHistogramWidget()
        if self.inputs.dataset:
            widget.setDataset(*(None,) + self.inputs.dataset)
        widget.setAttribute(qt.Qt.WA_DeleteOnClose)
        # TODO: Only show computed maps?
        if self.inputs.q:
            widget.q = self.inputs.q
        if self.inputs.a:
            widget.a = self.inputs.a
        if self.inputs.map_range:
            widget.map_range = self.inputs.map_range
        if self.inputs.detector:
            widget.detector = self.inputs.detector
        if self.inputs.units:
            widget.units = self.inputs.units
        if self.inputs.n:
            widget.n = self.inputs.n
        if self.inputs.map_shape:
            widget.map_shape = self.inputs.map_shape
        if self.inputs.energy:
            widget.energy = self.inputs.energy
        widget.show()
        app.exec_()
        self.outputs.dataset = self.inputs.dataset[1:]
