__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "21/09/2021"


from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output
from silx.gui import qt
from silx.gui.colors import Colormap
from darfix.gui.shiftCorrectionWidget import ShiftCorrectionDialog
from darfix.core.process import ShiftCorrection


class ShiftCorrectionWidgetOW(OWWidget):
    """
    Widget to make the shift correction of a dataset.
    """

    name = "shift correction"
    icon = "icons/shift_correction.svg"
    want_main_area = False
    ewokstaskclass = ShiftCorrection

    # Inputs
    class Inputs:
        dataset = Input("dataset", tuple)
        colormap = Input("colormap", Colormap)

    # Outputs
    class Outputs:
        dataset = Output("dataset", tuple)
        colormap = Output("colormap", Colormap)

    # Settings
    shift = Setting(list(), schema_only=True)

    def __init__(self):
        super().__init__()
        qt.QLocale.setDefault(qt.QLocale("en_US"))

        self._widget = ShiftCorrectionDialog(parent=self)
        self._widget.okSignal.connect(self._sendSignal)
        self.controlArea.layout().addWidget(self._widget)

    @Inputs.dataset
    def setDataset(self, _input):
        if _input is not None:
            dataset, update = _input
            self._widget.setDataset(*dataset)
            if len(self.shift):
                self._widget.mainWindow.shift = self.shift

            if update is None:
                self.open()
            elif update != self:
                self.Outputs.dataset.send(
                    ((self,) + self._widget.mainWindow.getDataset(), update)
                )

    @Inputs.colormap
    def setColormap(self, colormap):
        self._widget.setStackViewColormap(colormap)

    def _updateDataset(self, widget, dataset):
        self._widget.mainWindow._updateDataset(widget, dataset)

    def _sendSignal(self):
        """
        Function to emit the new dataset.
        """
        self.shift = self._widget.mainWindow.shift.tolist()
        self.Outputs.dataset.send(
            ((self,) + self._widget.mainWindow.getDataset(), None)
        )
        self.Outputs.colormap.send(self._widget.mainWindow.getStackViewColormap())
        self.close()
