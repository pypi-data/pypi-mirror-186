__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "12/04/2022"

from silx.gui import qt
from silx.gui.colors import Colormap
from silx.gui.plot.StackView import StackViewMainWindow
import darfix
from darfix.core.dataset import Operation
from .operationThread import OperationThread


class BinningWidget(qt.QMainWindow):
    """
    Widget to bin the data for fastest processing
    """

    sigComputed = qt.Signal(float)

    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)

        self._scale = None

        widget = qt.QWidget()
        layout = qt.QGridLayout()

        self._scaleLE = qt.QLineEdit("1")
        validator = qt.QDoubleValidator()
        self._scaleLE.setValidator(validator)
        _buttons = qt.QDialogButtonBox(parent=self)
        self._okB = _buttons.addButton(_buttons.Ok)
        self._applyB = _buttons.addButton(_buttons.Apply)
        self._abortB = _buttons.addButton(_buttons.Abort)
        self._resetB = _buttons.addButton(_buttons.Reset)
        self._abortB.hide()

        self._applyB.clicked.connect(self._applyBinning)
        self._okB.clicked.connect(self.apply)
        self._resetB.clicked.connect(self.resetStack)
        self._abortB.clicked.connect(self.abort)

        self._sv = StackViewMainWindow()
        self._sv.setColormap(
            Colormap(
                name=darfix.config.DEFAULT_COLORMAP_NAME,
                normalization=darfix.config.DEFAULT_COLORMAP_NORM,
            )
        )
        layout.addWidget(qt.QLabel("Scale: "), 0, 0)
        layout.addWidget(self._scaleLE, 0, 1)
        layout.addWidget(self._sv, 1, 0, 1, 2)
        layout.addWidget(_buttons, 2, 0, 1, 2)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, scale):
        self._scale = scale
        self._scaleLE.setText(str(scale))

    def setDataset(
        self, parent, dataset, indices=None, bg_indices=None, bg_dataset=None
    ):
        """
        Dataset setter.

        :param Dataset dataset: dataset
        """
        self.parent = parent
        self._dataset = dataset
        self._update_dataset = dataset
        self.indices = indices
        self.bg_indices = bg_indices
        self.bg_dataset = bg_dataset
        self.setStack()
        self._thread = OperationThread(self, self._dataset.apply_binning)
        msg = qt.QMessageBox()
        msg.setIcon(qt.QMessageBox.Information)
        msg.setText(
            "Binning can be used to reduce the computation time of the operations in the workflow.\n"
            + "The scale is the factor to which the images will be rescaled.\n"
            + "After the correct parameters are found, you can remove the binning widget from the workflow"
            + " and execute it either with the GUI or using ewoks.\nBinning should be applied after any"
            + " ROI to have original images size and not the binned one.\n"
        )
        msg.setWindowTitle("Fit succeeded!")
        msg.setStandardButtons(qt.QMessageBox.Ok)
        msg.exec_()

    def _updateDataset(self, widget, dataset):
        self._dataset = dataset
        self._update_dataset = dataset
        self._parent._updateDataset(widget, dataset)

    def setStack(self, dataset=None):
        """
        Sets new data to the stack.
        Mantains the current frame showed in the view.

        :param Dataset dataset: if not None, data set to the stack will be from the given dataset.
        """
        if dataset is None:
            dataset = self._dataset
        nframe = self._sv.getFrameNumber()
        self._sv.setStack(dataset.get_data())
        self._sv.setFrameNumber(nframe)

    def _applyBinning(self):
        if not self._update_dataset.in_memory:
            self._abortB.show()
        self._applyB.setEnabled(False)
        self._okB.setEnabled(False)
        self.scale = float(self._scaleLE.text())
        self._thread.setArgs(self.scale)
        self._thread.finished.connect(self._updateData)
        self._thread.start()

    def _updateData(self):
        self._thread.finished.disconnect(self._updateData)
        self._applyB.setEnabled(True)
        self._abortB.hide()
        self._abortB.setEnabled(True)
        self._okB.setEnabled(True)
        if self._thread.data:
            self._update_dataset = self._thread.data
            self.setStack(self._update_dataset)

    def abort(self):
        self._abortB.setEnabled(False)
        self._update_dataset.stop_operation(Operation.BINNING)

    def apply(self):
        """
        Function that replaces the dataset data with the data shown in the stack of images.
        If the stack has a roi applied, it applies the same roi to the dark frames of the dataset.
        Signal emitted with the roi parameters.
        """
        if self.scale:
            self.sigComputed.emit(
                [self.scale] if type(self.scale) == int else self.scale
            )
        else:
            self.sigComputed.emit([])

    def getDataset(self):
        return self._update_dataset, self.indices, self.bg_indices, self.bg_dataset

    def resetStack(self):
        """
        Restores stack with the dataset data.
        """
        self._update_dataset = self._dataset
        self.setStack(self._dataset)

    def clearStack(self):
        """
        Clears stack.
        """
        self._sv.setStack(None)
