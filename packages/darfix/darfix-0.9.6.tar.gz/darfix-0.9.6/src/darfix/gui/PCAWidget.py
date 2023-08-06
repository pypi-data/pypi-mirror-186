__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "22/12/2020"

import numpy

from silx.gui import qt
from silx.gui.plot import Plot1D

from .operationThread import OperationThread


class PCAWidget(qt.QMainWindow):
    """
    Widget to apply PCA to a set of images and plot the eigenvalues found.
    """

    sigComputed = qt.Signal()

    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)

        self._plot = Plot1D()
        self._plot.setDataMargins(0.05, 0.05, 0.05, 0.05)
        self._plot.setGraphXLabel("Components")
        self._plot.setGraphYLabel("Singular values")
        self.setCentralWidget(self._plot)

    def _computePCA(self):
        try:
            self._thread = OperationThread(self, self._dataset.pca)
            self._thread.setArgs(return_vals=True, indices=self.indices)
            self._thread.finished.connect(self._updateData)
            self._thread.start()
        except Exception as e:
            raise e

    def setDataset(
        self, parent, dataset, indices=None, bg_indices=None, bg_dataset=None
    ):
        """
        Dataset setter.

        :param Dataset dataset: dataset
        """
        self._parent = parent
        self._dataset = dataset
        self.indices = indices
        self.bg_indices = bg_indices
        self.bg_dataset = bg_dataset
        self._plot.setGraphTitle(
            "Components representation of the dataset " + self._dataset.title
        )
        self._computePCA()

    def _updateDataset(self, widget, dataset):
        self._parent._updateDataset(widget, dataset)
        self._dataset = dataset

    def _updateData(self):
        """
        Plots the eigenvalues.
        """
        self._thread.finished.disconnect(self._updateData)
        vals = self._thread.data
        self._plot.show()
        self._plot.addCurve(numpy.arange(len(vals)), vals, symbol=".", linestyle=" ")
        self.sigComputed.emit()
