__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "25/04/2022"


import numpy
from silx.gui import qt
from silx.gui.colors import Colormap
from silx.gui.plot import Plot2D
from silx.io.dictdump import dicttonx
from darfix.io.utils import create_nxdata_dict
from .rsmWidget import PixelSize
from .operationThread import OperationThread


class RSMHistogramWidget(qt.QMainWindow):
    """
    Widget to compute Reciprocal Space Map
    """

    sigComputed = qt.Signal()

    class _LineEditsWidget(qt.QWidget):
        def __init__(self, parent, dims=1, validator=None, placeholder=None):
            qt.QWidget.__init__(self, parent)
            self.setLayout(qt.QHBoxLayout())
            if placeholder:
                assert len(placeholder) == dims
            self._lineEdits = []
            for i in range(dims):
                lineEdit = qt.QLineEdit(parent=self)
                if placeholder:
                    lineEdit.setPlaceholderText(placeholder[i])
                if validator:
                    lineEdit.setValidator(validator)
                self._lineEdits.append(lineEdit)
                self.layout().addWidget(lineEdit)

            self.layout().setContentsMargins(0, 0, 0, 0)

        @property
        def value(self):
            values = []
            for le in self._lineEdits:
                values += [le.text() if le.text() != "" else None]
            return values

        def setValue(self, values):
            """
            :param int or None _range
            """
            assert type(values) is list

            for i, value in enumerate(values):
                self._lineEdits[i].setText(str(value))
                self._lineEdits[i].setCursorPosition(0)

    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)

        self._idx = [(2, 1), (2, 0), (1, 0)]

        widget = qt.QWidget(parent=self)
        layout = qt.QGridLayout()
        label = qt.QLabel("Q:")
        font = label.font()
        font.setBold(True)
        label.setFont(font)
        layout.addWidget(label, 0, 0, 1, 1)
        self._q = self._LineEditsWidget(self, 3, qt.QIntValidator(), ["h", "k", "l"])
        self._q.setValue([1, 0, 1])
        layout.addWidget(self._q, 0, 1, 1, 2)
        label = qt.QLabel("Pseudocubic lattice:")
        label.setFont(font)
        layout.addWidget(label, 1, 0, 1, 2)
        self._a = qt.QLineEdit()
        self._a.setValidator(qt.QDoubleValidator())
        self._a.setText("4.08")
        layout.addWidget(self._a, 1, 1, 1, 2)
        label = qt.QLabel("Map range:")
        label.setFont(font)
        layout.addWidget(label, 2, 0, 1, 2)
        self._map_range = qt.QLineEdit()
        self._map_range.setValidator(qt.QDoubleValidator())
        self._map_range.setText("0.008")
        layout.addWidget(self._map_range, 2, 1, 1, 2)
        label = qt.QLabel("Detector:")
        label.setFont(font)
        layout.addWidget(label, 3, 0, 1, 2)
        self._detector = qt.QComboBox()
        self._detector.addItems(PixelSize.names())
        layout.addWidget(self._detector, 3, 1, 1, 2)
        label = qt.QLabel("Units:")
        label.setFont(font)
        layout.addWidget(label, 4, 0, 1, 2)
        self._units = qt.QComboBox()
        self._units.addItems(["Poulsen", "Gorfman"])
        layout.addWidget(self._units, 4, 1, 1, 2)
        label = qt.QLabel("n:")
        label.setFont(font)
        layout.addWidget(label, 5, 0, 1, 1)
        self._n = self._LineEditsWidget(self, 3, qt.QIntValidator(), ["h", "k", "l"])
        self._n.setValue([0, 1, 0])
        layout.addWidget(self._n, 5, 1, 1, 2)
        label = qt.QLabel("Map shape:")
        label.setFont(font)
        layout.addWidget(label, 6, 0, 1, 1)
        self._map_shape = self._LineEditsWidget(
            self, 3, qt.QIntValidator(), ["x", "y", "z"]
        )
        self._map_shape.setValue([200, 200, 200])
        layout.addWidget(self._map_shape, 6, 1, 1, 2)
        label = qt.QLabel("Energy:")
        label.setFont(font)
        layout.addWidget(label, 7, 0, 1, 2)
        self._energy = qt.QLineEdit()
        self._energy.setValidator(qt.QDoubleValidator())
        self._energy.setText("17")
        layout.addWidget(self._energy, 7, 1, 1, 2)
        self._computeB = qt.QPushButton("Compute")
        layout.addWidget(self._computeB, 8, 2, 1, 1)
        self._computeB.clicked.connect(self._computeRSM)
        self._plotWidget = qt.QWidget()
        self._plotWidget.setLayout(qt.QHBoxLayout())
        layout.addWidget(self._plotWidget, 9, 0, 1, 3)
        self._plotWidget.hide()
        self._exportButton = qt.QPushButton("Export maps")
        self._exportButton.hide()
        layout.addWidget(self._exportButton, 10, 2, 1, 1)
        self._exportButton.clicked.connect(self.exportMaps)

        widget.setLayout(layout)
        widget.setMinimumWidth(650)
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
        self._update_dataset = dataset
        self._thread = OperationThread(self, self.dataset.apply_fit)
        for i in reversed(range(self._plotWidget.layout().count())):
            self._plotWidget.layout().itemAt(i).widget().setParent(None)

        self._plotWidget.hide()
        self._exportButton.hide()

        self._plots = []
        for i in range(len(self._idx)):
            self._plots += [Plot2D(parent=self)]
            self._plots[-1].setDefaultColormap(Colormap(name="viridis"))
            self._plotWidget.layout().addWidget(self._plots[-1])

        self._thread = OperationThread(self, self.dataset.compute_rsm)

    @property
    def q(self):
        return numpy.array(self._q.value, dtype=int)

    @q.setter
    def q(self, q):
        self._q.setValue(q)

    @property
    def a(self):
        return float(self._a.text())

    @a.setter
    def a(self, a):
        self._a.setText(str(a))

    @property
    def map_range(self):
        return float(self._map_range.text())

    @map_range.setter
    def map_range(self, map_range):
        self._map_range.setText(str(map_range))

    @property
    def detector(self):
        return self._detector.currentText()

    @detector.setter
    def detector(self, detector):
        self._detector.setCurrentText(detector)

    @property
    def units(self):
        return self._units.currentText()

    @units.setter
    def units(self, units):
        self._units.setCurrentText(units)

    @property
    def n(self):
        return numpy.array(self._n.value, dtype=int)

    @n.setter
    def n(self, n):
        self._n.setValue(n)

    @property
    def map_shape(self):
        return numpy.array(self._map_shape.value, dtype=int)

    @map_shape.setter
    def map_shape(self, map_shape):
        self._map_shape.setValue(map_shape)

    @property
    def energy(self):
        return float(self._energy.text())

    @energy.setter
    def energy(self, energy):
        self._energy.setText(str(energy))

    def _computeRSM(self):

        self._computeB.setEnabled(False)
        self._thread.setArgs(
            Q=self.q,
            a=self.a,
            map_range=self.map_range,
            pixel_size=numpy.array(PixelSize[self.detector].value, dtype=float),
            units=self.units.lower(),
            n=self.n,
            map_shape=self.map_shape,
            energy=self.energy,
        )
        self.sigComputed.emit()
        self._thread.finished.connect(self._updateData)
        self._thread.start()

    def _updateData(self):
        self._thread.finished.disconnect(self._updateData)
        self._computeB.setEnabled(True)

        if self._thread.data is not None:
            arr, edges = self._thread.data

            arr = numpy.nan_to_num(arr)

            self._projections = []

            if self._units.currentText().lower() == "poulsen":
                self.labels = [r"$q_{rock}$", r"$q_{\perp}$", r"$q_{||}$"]
            else:
                self.labels = ["h", "k", "l"]

            for idx, (i, j) in enumerate(self._idx):
                self._projections += [numpy.sum(arr, axis=idx)]
                xscale = (edges[i][-1] - edges[i][0]) / len(edges[i])
                yscale = (edges[j][-1] - edges[j][0]) / len(edges[j])
                self._plots[idx].addImage(
                    self._projections[-1],
                    scale=(xscale, yscale),
                    origin=(edges[i][0], edges[j][0]),
                    xlabel=self.labels[i],
                    ylabel=self.labels[j],
                )

            self.edges = edges

            self._plotWidget.show()
            self._exportButton.show()

        else:
            print("\nComputation aborted")

    def exportMaps(self):
        """
        Creates dictionay with maps information and exports it to a nexus file
        """
        entry = "entry"

        nx = {
            entry: {"@NX_class": "NXentry"},
            "@NX_class": "NXroot",
            "@default": "entry",
        }

        for idx, (j, i) in enumerate(self._idx):
            axis = [self.edges[i][:-1], self.edges[j][:-1]]
            nx["entry"][str(idx)] = create_nxdata_dict(
                self._projections[idx],
                self.labels[i] + "_" + self.labels[j],
                axis,
                axes_names=[self.labels[i], self.labels[j]],
            )

        fileDialog = qt.QFileDialog()

        fileDialog.setFileMode(fileDialog.AnyFile)
        fileDialog.setAcceptMode(fileDialog.AcceptSave)
        fileDialog.setOption(fileDialog.DontUseNativeDialog)
        fileDialog.setDefaultSuffix(".h5")
        if fileDialog.exec_():
            dicttonx(nx, fileDialog.selectedFiles()[0])
