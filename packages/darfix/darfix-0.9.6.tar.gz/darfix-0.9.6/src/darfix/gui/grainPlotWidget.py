__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "10/08/2021"

from matplotlib.colors import hsv_to_rgb
import numpy
import logging

from silx.gui import qt
from silx.gui.colors import Colormap
from silx.gui.plot import Plot2D
from silx.image.marchingsquares import find_contours
from silx.math.medianfilter import medfilt2d
from silx.utils.enum import Enum as _Enum
from silx.io.dictdump import dicttonx

from darfix.io.utils import create_nxdata_dict
from darfix.gui.utils import ChooseDimensionWidget
from .operationThread import OperationThread

_logger = logging.getLogger(__file__)


class Method(_Enum):
    """
    Different maps to show
    """

    COM = "Center of mass"
    FWHM = "FWHM"
    SKEWNESS = "Skewness"
    KURTOSIS = "Kurtosis"
    ORI_DIST = "Orientation distribution"
    MOSAICITY = "Mosaicity"


class GrainPlotWidget(qt.QMainWindow):
    """
    Widget to show a series of maps for the analysis of the data.
    """

    sigComputed = qt.Signal()

    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)

        self._methodCB = qt.QComboBox()
        self._methodCB.addItems(Method.values())
        for i in range(len(Method)):
            self._methodCB.model().item(i).setEnabled(False)
        self._methodCB.currentTextChanged.connect(self._updatePlot)
        self._plotWidget = qt.QWidget()
        plotsLayout = qt.QHBoxLayout()
        self._plotWidget.setLayout(plotsLayout)
        self._contoursPlot = Plot2D(parent=self)
        widget = qt.QWidget(parent=self)
        layout = qt.QVBoxLayout()
        self._levelsWidget = qt.QWidget()
        levelsLayout = qt.QGridLayout()
        levelsLabel = qt.QLabel("Number of levels:")
        self._levelsLE = qt.QLineEdit("20")
        self._levelsLE.setToolTip("Number of levels to use when finding the contours")
        self._levelsLE.setValidator(qt.QIntValidator())
        self._computeContoursB = qt.QPushButton("Compute")
        self._motorValuesCheckbox = qt.QCheckBox("Use motor values")
        self._motorValuesCheckbox.setChecked(True)
        self._motorValuesCheckbox.stateChanged.connect(self._checkboxStateChanged)
        self._centerDataCheckbox = qt.QCheckBox("Center angle values")
        self._centerDataCheckbox.setEnabled(False)
        self._centerDataCheckbox.stateChanged.connect(self._checkboxStateChanged)
        self._chooseDimensionWidget = ChooseDimensionWidget(
            self, vertical=False, values=False, _filter=False
        )
        self._chooseDimensionWidget.filterChanged.connect(self._updateMotorAxis)
        self._thirdMotorCB = qt.QComboBox(self)
        self._thirdMotorCB.currentIndexChanged.connect(self._updateThirdMotor)
        levelsLayout.addWidget(levelsLabel, 0, 0, 1, 1)
        levelsLayout.addWidget(self._levelsLE, 0, 1, 1, 1)
        levelsLayout.addWidget(self._motorValuesCheckbox, 0, 2, 1, 1)
        levelsLayout.addWidget(self._centerDataCheckbox, 0, 3, 1, 1)
        levelsLayout.addWidget(self._thirdMotorCB, 1, 2, 1, 1)
        levelsLayout.addWidget(self._computeContoursB, 1, 3, 1, 1)
        levelsLayout.addWidget(self._contoursPlot, 2, 0, 1, 4)
        self._levelsWidget.setLayout(levelsLayout)
        self._levelsWidget.hide()
        self._mosaicityPlot = Plot2D(parent=self)
        self._exportButton = qt.QPushButton("Export maps")
        self._exportButton.setEnabled(False)
        self._exportButton.clicked.connect(self.exportMaps)
        layout.addWidget(self._methodCB)
        layout.addWidget(self._chooseDimensionWidget)
        layout.addWidget(self._levelsWidget)
        layout.addWidget(self._plotWidget)
        layout.addWidget(self._mosaicityPlot)
        layout.addWidget(self._exportButton)
        self._plotWidget.hide()
        self._thirdMotorCB.hide()
        self._chooseDimensionWidget.hide()
        self._mosaicityPlot.hide()
        self._mosaicityPlot.getColorBarWidget().hide()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def setDataset(
        self, parent, dataset, indices=None, bg_indices=None, bg_dataset=None
    ):
        """
        Dataset setter.

        :param Dataset dataset: dataset
        """
        self._parent = parent
        self.dataset = dataset
        self.indices = indices
        self.bg_indices = bg_indices
        self.bg_dataset = bg_dataset
        self._mosaicity = None
        self._moments = None
        self.dimensions = [0, 1]
        state = self._methodCB.blockSignals(True)
        for i in range(len(Method)):
            self._methodCB.model().item(i).setEnabled(False)
        self._methodCB.blockSignals(state)
        if self.dataset.dims.ndim > 1 and self.dataset.dims.ndim < 4:
            self._curves = {}
            if self.dataset.dims.ndim == 3:
                # Update chooseDimensionWidget and thirdMotorCB
                state = self._chooseDimensionWidget.blockSignals(True)
                self._chooseDimensionWidget.setDimensions(self.dataset.dims)
                self._chooseDimensionWidget._updateState(True)
                self._chooseDimensionWidget.blockSignals(state)
                self._thirdMotorCB.clear()
                third_motor = self.dataset.dims.get(
                    int(
                        numpy.setdiff1d(
                            range(3), self._chooseDimensionWidget.dimension
                        )[0]
                    )
                )
                state = self._thirdMotorCB.blockSignals(True)
                self._thirdMotorCB.addItems(
                    numpy.array(third_motor.unique_values, dtype=str)
                )
                self._thirdMotorCB.blockSignals(state)
            self.ori_dist, self.hsv_key = self.dataset.compute_mosaicity_colorkey(
                third_motor=0
            )
            self._checkboxStateChanged()
            self._contoursPlot.getColorBarWidget().hide()
            self._curvesColormap = Colormap(
                name="temperature",
                vmin=numpy.min(self.ori_dist),
                vmax=numpy.max(self.ori_dist),
            )
            self._computeContoursB.clicked.connect(self._computeContours)
            self._methodCB.model().item(4).setEnabled(True)
            self._methodCB.setCurrentIndex(4)
        self._thread = OperationThread(self, self.dataset.apply_moments)
        self._thread.setArgs(self.indices)
        self._thread.finished.connect(self._updateData)
        self._thread.start()
        for i in reversed(range(self._plotWidget.layout().count())):
            self._plotWidget.layout().itemAt(i).widget().setParent(None)

        self._contoursPlot.setGraphTitle(
            self.dataset.title + "\n" + Method.ORI_DIST.value
        )
        self._mosaicityPlot.setGraphTitle(
            self.dataset.title + "\n" + Method.MOSAICITY.value
        )
        self._plots = []
        for axis, dim in self.dataset.dims:
            self._plots += [Plot2D(parent=self)]
            self._plots[-1].setGraphTitle(self.dataset.title + "\n" + dim.name)
            self._plots[-1].setDefaultColormap(Colormap(name="viridis"))
            self._plotWidget.layout().addWidget(self._plots[-1])

    def _updateData(self):
        """
        Updates the plots with the data computed in the thread
        """
        self._thread.finished.disconnect(self._updateData)
        if self._thread.data is not None:
            self._moments = self._thread.data
            self._updatePlot(self._methodCB.currentText())
            rg = len(Method) if self.dataset.dims.ndim > 1 else 4
            for i in range(rg):
                self._methodCB.model().item(i).setEnabled(True)
            self.mosaicity = self.compute_mosaicity()
            self._methodCB.setCurrentIndex(0)
            self._exportButton.setEnabled(True)
        else:
            print("\nComputation aborted")
            msg = qt.QMessageBox()
            msg.setIcon(qt.QMessageBox.Critical)
            msg.setText("Grain plot not working without dimensions")
            msg.setWindowTitle("Don't eat yellow snow!")
            msg.setStandardButtons(qt.QMessageBox.Ok)
            msg.exec_()

    def _updateDataset(self, widget, dataset):
        self._parent._updateDataset(widget, dataset)
        self.dataset = dataset

    def _checkboxStateChanged(self, state=None):
        """
        Update widgets linked to the checkbox state
        """
        self._centerDataCheckbox.setEnabled(not self._motorValuesCheckbox.isChecked())
        self._contoursPlot.remove(kind="curve")
        self._contoursPlot.resetZoom()
        scale = 100
        xdim = self.dataset.dims.get(self.dimensions[1])
        ydim = self.dataset.dims.get(self.dimensions[0])
        xscale = xdim.range[2]
        yscale = ydim.range[2]
        if self._motorValuesCheckbox.isChecked():
            self.ori_dist_origin = (xdim.range[0], ydim.range[0])
        elif self._centerDataCheckbox.isChecked():
            self.ori_dist_origin = (
                -xscale * int(xdim.size / 2),
                -yscale * int(ydim.size / 2),
            )
        else:
            self.ori_dist_origin = (0, 0)
        self._contoursPlot.addImage(
            hsv_to_rgb(self.hsv_key),
            xlabel=xdim.name,
            ylabel=ydim.name,
            origin=self.ori_dist_origin,
            scale=(xscale / scale, yscale / scale),
        )

    def _computeContours(self):
        """
        Compute contours map based on orientation distribution.
        """
        self._contoursPlot.remove(kind="curve")

        if self.ori_dist is not None:
            polygons = []
            levels = []
            for i in numpy.linspace(
                numpy.min(self.ori_dist),
                numpy.max(self.ori_dist),
                int(self._levelsLE.text()),
            ):
                polygons.append(find_contours(self.ori_dist, i))
                levels.append(i)

            colors = self._curvesColormap.applyToData(levels)
            xdim = self.dataset.dims.get(self.dimensions[1])
            ydim = self.dataset.dims.get(self.dimensions[0])
            self._curves = {}
            for ipolygon, polygon in enumerate(polygons):
                # iso contours
                for icontour, contour in enumerate(polygon):
                    if len(contour) == 0:
                        continue
                    # isClosed = numpy.allclose(contour[0], contour[-1])
                    x = contour[:, 1]
                    y = contour[:, 0]
                    xscale = xdim.range[2]
                    yscale = ydim.range[2]
                    x = self.ori_dist_origin[0] + x * xscale + xscale / 2
                    y = self.ori_dist_origin[1] + y * yscale + yscale / 2
                    legend = "poly{}.{}".format(icontour, ipolygon)
                    self._curves[legend] = {
                        "points": (x.copy(), y.copy()),
                        "color": colors[ipolygon],
                    }
                    self._contoursPlot.addCurve(
                        x=x,
                        y=y,
                        linestyle="-",
                        linewidth=2.0,
                        legend=legend,
                        resetzoom=False,
                        color=colors[ipolygon],
                    )

    def compute_mosaicity(self):
        """
        Compute mosaicity map depending on the selected dimensions, if any.
        """
        if self._moments is not None and self.dataset.dims.ndim > 1:
            com0 = self._moments[self.dimensions[0]][0]
            no_nans_indices = ~numpy.isnan(com0)
            min_com0 = numpy.min(
                com0[no_nans_indices] if len(com0[no_nans_indices]) > 0 else com0
            )
            com0[numpy.isnan(com0)] = min_com0
            norms0 = (com0 - min_com0) / numpy.ptp(com0)
            com1 = self._moments[self.dimensions[1]][0]
            no_nans_indices = ~numpy.isnan(com1)
            min_com1 = numpy.min(
                com1[no_nans_indices] if len(com1[no_nans_indices]) > 0 else com1
            )
            com1[numpy.isnan(com1)] = min_com1
            norms1 = (com1 - min_com1) / numpy.ptp(com1)

            mosaicity = hsv_to_rgb(
                numpy.stack(
                    (norms0, norms1, numpy.ones(self._moments[0].shape[1:])), axis=2
                )
            )
            return mosaicity

    def _updatePlot(self, method):
        """
        Update shown plots in the widget
        """
        method = Method(method)
        self._levelsWidget.hide()
        self._mosaicityPlot.hide()
        self._thirdMotorCB.hide()
        self._chooseDimensionWidget.hide()
        if method == Method.ORI_DIST:
            self._levelsWidget.show()
            self._plotWidget.hide()
            if self.dataset.dims.ndim == 3:
                self._chooseDimensionWidget.show()
                self._thirdMotorCB.show()
        elif method == Method.FWHM:
            self._plotWidget.show()
            for i, plot in enumerate(self._plots):
                self._addImage(plot, self._moments[i][1])
        elif method == Method.COM:
            self._plotWidget.show()
            for i, plot in enumerate(self._plots):
                self._addImage(plot, self._moments[i][0])
        elif method == Method.SKEWNESS:
            self._plotWidget.show()
            for i, plot in enumerate(self._plots):
                self._addImage(plot, self._moments[i][2])
        elif method == Method.KURTOSIS:
            self._plotWidget.show()
            for i, plot in enumerate(self._plots):
                self._addImage(plot, self._moments[i][3])
        elif method == Method.MOSAICITY:
            try:
                self._plotWidget.hide()
                self._addImage(self._mosaicityPlot, self.mosaicity)
                self._mosaicityPlot.show()
                if self.dataset.dims.ndim == 3:
                    self._chooseDimensionWidget.show()
            except Exception as e:
                _logger.error("Couldn't compute mosaicity: ", e)
        else:
            _logger.warning("Unexisting map method")

    def _updateMotorAxis(self):
        """
        Update dimensions used for orientation distribution and mosaicity maps.
        This is only used on datasets with more than two dimensions.
        """

        self.dimensions = self._chooseDimensionWidget.dimension
        self.ori_dist, self.hsv_key = self.dataset.compute_mosaicity_colorkey(
            dimensions=self.dimensions, third_motor=0
        )
        self.mosaicity = self.compute_mosaicity()

        self._thirdMotorCB.clear()
        third_motor = self.dataset.dims.get(
            int(numpy.setdiff1d(range(3), self.dimensions)[0])
        )

        self._curvesColormap = Colormap(
            name="temperature",
            vmin=numpy.min(self.ori_dist),
            vmax=numpy.max(self.ori_dist),
        )
        state = self._thirdMotorCB.blockSignals(True)
        self._thirdMotorCB.addItems(numpy.array(third_motor.unique_values, dtype=str))
        self._thirdMotorCB.blockSignals(state)
        self._checkboxStateChanged()
        self._updatePlot(self._methodCB.currentText())

    def _updateThirdMotor(self, index=-1):
        """
        Update orientation distribution according to the third motor chosen
        """
        if index > -1:
            self.ori_dist, self.hsv_key = self.dataset.compute_mosaicity_colorkey(
                dimensions=self._chooseDimensionWidget.dimension, third_motor=index
            )

            self._curvesColormap = Colormap(
                name="temperature",
                vmin=numpy.min(self.ori_dist),
                vmax=numpy.max(self.ori_dist),
            )
            self._updatePlot(self._methodCB.currentText())

    def _opticolor(self, img, minc, maxc):
        img = img.copy()
        Cnn = img[~numpy.isnan(img)]
        sortC = sorted(Cnn)
        Imin = sortC[int(numpy.floor(len(sortC) * minc))]
        Imax = sortC[int(numpy.floor(len(sortC) * maxc))]
        img[img > Imax] = Imax
        img[img < Imin] = Imin

        return medfilt2d(img)

    def exportMaps(self):
        """
        Creates dictionay with maps information and exports it to a nexus file
        """
        if self.dataset.transformation:
            axes = [
                self.dataset.transformation.yregular,
                self.dataset.transformation.xregular,
            ]
            axes_names = ["y", "x"]
            axes_long_names = [
                self.dataset.transformation.label,
                self.dataset.transformation.label,
            ]
        else:
            axes = None
            axes_names = None
            axes_long_names = None

        if self.dataset and self.dataset.dims.ndim > 1:
            nx = {
                "entry": {
                    Method.MOSAICITY.value: create_nxdata_dict(
                        self.mosaicity,
                        Method.MOSAICITY.value,
                        axes,
                        axes_names,
                        axes_long_names,
                        rgba=True,
                    ),
                    Method.ORI_DIST.value: {
                        "key": {
                            "image": hsv_to_rgb(self.hsv_key),
                            "origin": self._contoursPlot.getImage().getOrigin(),
                            "scale": self._contoursPlot.getImage().getScale(),
                            "xlabel": self._contoursPlot.getImage().getXLabel(),
                            "ylabel": self._contoursPlot.getImage().getYLabel(),
                            "image@interpretation": "rgba-image",
                        },
                        "curves": self._curves,
                    },
                    "@NX_class": "NXentry",
                    "@default": Method.MOSAICITY.value,
                },
                "@NX_class": "NXroot",
                "@default": "entry",
            }

            for axis, dim in self.dataset.dims:
                nx["entry"][dim.name] = {"@NX_class": "NXcollection"}
                for i in range(4):
                    nx["entry"][dim.name][Method.values()[i]] = create_nxdata_dict(
                        self._moments[axis][i],
                        Method.values()[i],
                        axes,
                        axes_names,
                        axes_long_names,
                    )
        else:
            nx = {
                "entry": {"@NX_class": "NXentry"},
                "@NX_class": "NXroot",
                "@default": "entry",
            }

            for i in range(4):
                nx["entry"][Method.values()[i]] = create_nxdata_dict(
                    self._moments[0][i],
                    Method.values()[i],
                    axes,
                    axes_names,
                    axes_long_names,
                )
            nx["entry"]["@default"] = Method.COM.value

        fileDialog = qt.QFileDialog()

        fileDialog.setFileMode(fileDialog.AnyFile)
        fileDialog.setAcceptMode(fileDialog.AcceptSave)
        fileDialog.setOption(fileDialog.DontUseNativeDialog)
        fileDialog.setDefaultSuffix(".h5")
        if fileDialog.exec_():
            dicttonx(nx, fileDialog.selectedFiles()[0])

    def _addImage(self, plot, image):
        if self.dataset.transformation is None:
            plot.addImage(image, xlabel="pixels", ylabel="pixels")
            return
        if self.dataset.transformation.rotate:
            image = numpy.rot90(image, 3)
        plot.addImage(
            image,
            origin=self.dataset.transformation.origin,
            scale=self.dataset.transformation.scale,
            xlabel=self.dataset.transformation.label,
            ylabel=self.dataset.transformation.label,
        )
