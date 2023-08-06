__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "20/11/2020"

import logging
from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Output

from silx.gui import qt

from darfix.gui.operationThread import OperationThread
from darfix.gui.datasetSelectionWidget import DatasetSelectionWidget
from darfix.core.process import DataSelection

_logger = logging.getLogger(__file__)


class DataSelectionWidgetOW(OWWidget):
    """
    Widget to select the data to be used in the dataset.
    """

    name = "data selection"
    icon = "icons/upload.svg"
    want_main_area = False
    ewokstaskclass = DataSelection

    # Outputs
    class Outputs:
        dataset = Output("dataset", tuple, bool)

    # Settings
    filenames = Setting(list(), schema_only=True)
    raw_filename = Setting(str(), schema_only=True)
    dark_filename = Setting(str(), schema_only=True)
    in_disk = Setting(bool(), schema_only=True)

    def __init__(self):
        super().__init__()

        self._widget = DatasetSelectionWidget()
        types = qt.QDialogButtonBox.Ok
        _buttons = qt.QDialogButtonBox(parent=self)
        _buttons.setStandardButtons(types)

        self.controlArea.layout().addWidget(self._widget)
        self.controlArea.layout().addWidget(_buttons)

        _buttons.accepted.connect(self._getDataset)

        self.__updatingData = False
        self.setDataset()

    def setDataset(self):
        self._widget.setRawFilenames(self.filenames)
        self._widget.setRawFilename(self.raw_filename)
        self._widget.setDarkFilename(self.dark_filename)
        if self.in_disk:
            self._widget._inDiskCB.setChecked(True)

    def _getDataset(self):
        if self.__updatingData:
            _logger.warning(
                "Another dataset is being loaded, please wait \
                            until it has finished"
            )
            return

        _logger.warning("create new dataset and emit them")
        # Create and start thread
        self._thread = OperationThread(self, self._widget.loadDataset)
        self._thread.finished.connect(self._sendSignal)
        self._thread.start()

        self.updateSettings()
        self.__updatingData = True
        self.information("Downloading dataset")

    def _updateDataset(self, widget, dataset):
        self._widget._updateDataset(dataset)
        self.Outputs.dataset.send(((self,) + self._widget.getDataset(), widget))

    def _sendSignal(self):
        """
        Function to emit the new dataset.
        Finishes the `downloading` state.
        """
        self._thread.finished.disconnect(self._sendSignal)
        self.__updatingData = False
        self.information()
        if self._thread.data:
            self.Outputs.dataset.send(((self,) + self._widget.getDataset(), None))
            self.close()

    def updateSettings(self):
        """
        Function to update the settings saved into the widget.
        """
        self.filenames = self._widget.getRawFilenames()
        self.raw_filename = self._widget.getRawFilename()
        self.dark_filename = self._widget.getDarkFilename()
        self.in_disk = self._widget._inDiskCB.isChecked()
