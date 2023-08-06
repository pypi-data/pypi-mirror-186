__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "11/12/2020"


# import numpy

from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output
from silx.gui.colors import Colormap

# from silx.gui import qt
from darfix.gui.roiSelectionWidget import ROISelectionWidget
from darfix.core.process import RoiSelection


class RoiSelectionWidgetOW(OWWidget):

    name = "roi selection"
    icon = "icons/roi.png"
    want_main_area = False
    ewokstaskclass = RoiSelection

    # Inputs/Outputs
    class Inputs:
        dataset = Input("dataset", tuple)
        colormap = Input("colormap", Colormap)

    class Outputs:
        dataset = Output("dataset", tuple)
        colormap = Output("colormap", Colormap)

    # Settings
    roi_origin = Setting(list(), schema_only=True)
    roi_size = Setting(list(), schema_only=True)

    def __init__(self):
        super().__init__()

        self._widget = ROISelectionWidget(parent=self)
        # self._button = qt.QPushButton('Ok', parent=self)
        # self._button.setEnabled(False)
        self.controlArea.layout().addWidget(self._widget)
        # self.controlArea.layout().addWidget(self._button)
        self._widget.sigComputed.connect(self._sendSignal)

        # self._button.pressed.connect(self._createRoi)

    @Inputs.dataset
    def setDataset(self, _input):
        if _input is not None:
            dataset, update = _input
            self._widget.setDataset(*dataset)
            # Set saved roi
            if len(self.roi_origin) and len(self.roi_size):
                self._widget.setRoi(origin=self.roi_origin, size=self.roi_size)

            if update is None:
                self.open()
            elif update != self:
                self.Outputs.dataset.send(((self,) + self._widget.getDataset(), update))

    @Inputs.colormap
    def setColormap(self, colormap):
        self._widget.setStackViewColormap(colormap)

    def _updateDataset(self, widget, dataset):
        self._widget._updateDataset(widget, dataset)

    def _sendSignal(self, roi_origin=[], roi_size=[]):
        """
        Emits the signal with the new dataset.
        """
        self.close()
        self.roi_origin = roi_origin
        self.roi_size = roi_size
        self.Outputs.dataset.send(((self,) + self._widget.getDataset(), None))
        self.Outputs.colormap.send(self._widget.getStackViewColormap())
