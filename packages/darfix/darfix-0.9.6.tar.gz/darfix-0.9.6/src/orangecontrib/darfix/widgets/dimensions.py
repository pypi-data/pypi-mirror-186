__authors__ = ["H. Payno", "J. Garriga"]
__license__ = "MIT"
__date__ = "24/09/2019"


from silx.gui import qt
from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output
from darfix.core import utils
from darfix.core.dataset import Dimension
from darfix.gui.dimensionsWidget import DimensionWidget
from functools import partial
import logging
from darfix.core.process import DimensionDefinition

_logger = logging.getLogger(__file__)


class DimensionWidgetOW(OWWidget):
    """
    Widget used to define the calibration of the experimentation (select motor
    positions...)
    """

    name = "dimension definition"
    id = "orange.widgets.darfix.dimensiondefinition"
    description = "Define the dimension followed during the acquisition"
    icon = "icons/param_dims.svg"
    ewokstaskclass = DimensionDefinition

    priority = 4
    keywords = ["dataset", "calibration", "motor", "angle", "geometry"]

    # Inputs
    class Inputs:
        dataset = Input("dataset", tuple)

    # Outputs
    class Outputs:
        dataset = Output("dataset", tuple)

    want_main_area = False

    _dims = Setting(dict(), schema_only=True)

    def __init__(self):
        super().__init__()
        self._widget = DimensionWidget(parent=self)
        self.controlArea.layout().addWidget(self._widget)

        # buttons
        types = qt.QDialogButtonBox.Ok
        self.buttons = qt.QDialogButtonBox(parent=self)
        self.buttons.setStandardButtons(types)
        self.controlArea.layout().addWidget(self.buttons)

        self.buttons.accepted.connect(self.validate)
        self.buttons.button(qt.QDialogButtonBox.Ok).setEnabled(False)

        # connect Signal/SLOT
        _callbackValid = partial(
            self.buttons.button(qt.QDialogButtonBox.Ok).setEnabled, True
        )
        self._widget.fitSucceed.connect(_callbackValid)
        _callbackInvalid = partial(
            self.buttons.button(qt.QDialogButtonBox.Ok).setDisabled, True
        )
        self._widget.fitFailed.connect(_callbackInvalid)

        # expose API
        self.setDims = self._widget.setDims

    @property
    def _ndim(self):
        return self._widget.ndim

    @property
    def _dataset(self):
        return self._widget.dataset

    @Inputs.dataset
    def setDataset(self, _input):
        """
        Input signal to set the dataset.
        """
        if _input is not None:
            dataset, update = _input
            self.buttons.button(qt.QDialogButtonBox.Ok).setEnabled(False)
            try:
                self._widget.setDataset(*dataset)
                # load properties
                _dims = utils.convertDictToDim(self._dims)
                self._widget.setDims(_dims)
            except ValueError as e:
                qt.QMessageBox.warning(
                    self, "Fail to setup dimension definition", str(e)
                )
            else:
                if update is None:
                    self.open()
                elif update != self:
                    self.Outputs.dataset.send(
                        ((self,) + self._widget.getDataset(), update)
                    )

    def _updateDataset(self, widget, dataset):
        self._widget._updateDataset(widget, dataset)

    def validate(self):
        """
        Tries to fit the dimensions into the dataset.
        """
        self.Outputs.dataset.send(((self,) + self._widget.getDataset(), None))
        self.updateProperties()
        OWWidget.accept(self)

    def updateProperties(self):
        """
        Save dimensions to Settings.
        """
        self._dims = {}
        if self._widget.ndim == 0:
            return
        else:
            for _dim in self._widget.dims.values():
                assert isinstance(_dim, Dimension)
                axis = _dim.axis
                self._dims[axis] = _dim.to_dict()
