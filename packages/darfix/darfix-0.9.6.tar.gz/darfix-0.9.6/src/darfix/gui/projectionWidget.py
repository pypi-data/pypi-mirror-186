__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "09/12/2021"


from silx.gui import qt
from silx.gui.colors import Colormap
from silx.gui.plot.StackView import StackViewMainWindow

import darfix
from darfix.gui.utils import ChooseDimensionWidget
from .operationThread import OperationThread


class ProjectionWidget(qt.QMainWindow):
    """
    Widget to apply a projection to the chosen dimension.
    """

    sigComputed = qt.Signal()

    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)

        self._dimension = None

        self._sv = StackViewMainWindow()
        self._sv.setColormap(
            Colormap(name=darfix.config.DEFAULT_COLORMAP_NAME, normalization="linear")
        )
        self._chooseDimensionWidget = ChooseDimensionWidget(
            self, vertical=False, values=False, _filter=False
        )
        self._projectButton = qt.QPushButton("Project data")
        self._projectButton.setEnabled(False)
        types = qt.QDialogButtonBox.Ok
        self._buttons = qt.QDialogButtonBox(parent=self)
        self._buttons.setStandardButtons(types)
        self._buttons.setEnabled(False)
        layout = qt.QGridLayout()
        layout.addWidget(self._chooseDimensionWidget, 0, 0, 1, 2)
        layout.addWidget(self._projectButton, 1, 1)
        layout.addWidget(self._sv, 2, 0, 1, 2)
        layout.addWidget(self._buttons, 3, 1)
        self._sv.hide()
        widget = qt.QWidget()
        widget.setLayout(layout)

        self._buttons.accepted.connect(self.sigComputed.emit)
        self._projectButton.clicked.connect(self._projectData)

        self.setCentralWidget(widget)

    def setDataset(
        self, parent, dataset, indices=None, bg_indices=None, bg_dataset=None
    ):
        """
        Dataset setter.

        :param Dataset dataset: dataset
        """
        if dataset is not None:
            self._parent = parent
            self._dataset = dataset
            self._update_dataset = dataset
            self.indices = indices
            self.bg_indices = bg_indices
            self.bg_dataset = bg_dataset
            self._projectButton.setEnabled(True)
            if self._dataset.dims.ndim > 1:
                self._buttons.setEnabled(True)

            self._chooseDimensionWidget.setDimensions(self._dataset.dims)
            self._chooseDimensionWidget._updateState(True)
            for i in range(1, self._dataset.dims.ndim - 1):
                self._chooseDimensionWidget.dimensionWidgets[i][0].addItem("None")
            self._thread = OperationThread(self, self._dataset.project_data)
            if self._dataset.title != "":
                self._sv.setTitleCallback(lambda idx: self._dataset.title)

    def getDataset(self, update=None):
        return self._update_dataset, self.indices, self.bg_indices, self.bg_dataset

    def clearStack(self):
        self._sv.setStack(None)
        self._projectButton.setEnabled(False)

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        self._dimension = dimension

    def _projectData(self):
        self._projectButton.setEnabled(False)
        self.dimension = [self._chooseDimensionWidget.dimension[0]]
        for i in range(1, len(self._chooseDimensionWidget.dimension)):
            self.dimension += [self._chooseDimensionWidget.dimension[i]]
        self._thread.setArgs(dimension=self.dimension, indices=self.indices)
        self._thread.finished.connect(self._updateData)
        self._thread.start()

    def _updateDataset(self, widget, dataset):
        self._parent._updateDataset(widget, dataset)
        self._dataset = dataset

    def _updateData(self):
        self._projectButton.setEnabled(True)
        self._thread.finished.disconnect(self._updateData)
        if self._thread.data:
            del self._update_dataset
            self._update_dataset = self._thread.data
            self.indices, self.bg_indices = None, None
            self._sv.show()
            self._sv.setStack(self._update_dataset.get_data())
