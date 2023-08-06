__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "10/08/2021"


from Orange.widgets.settings import Setting
from silx.gui import qt
from Orange.widgets.widget import OWWidget, Input, Output
from darfix.gui.magnificationWidget import MagnificationWidget
from darfix.gui.rsmWidget import RSMWidget
from darfix.core.process import Transformation


class TransformationWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "transformation"
    icon = "icons/axes.png"
    want_main_area = False
    ewokstaskclass = Transformation

    # Inputs
    class Inputs:
        dataset = Input("dataset", tuple)

    # Outputs
    class Outputs:
        dataset = Output("dataset", tuple)

    magnification = Setting(float(), schema_only=True)
    pixelSize = Setting(str(), schema_only=True)
    kind = Setting(bool(), schema_only=True)
    rotate = Setting(bool(), schema_only=True)
    orientation = Setting(int(), schema_only=True)

    def __init__(self):
        super().__init__()
        qt.QLocale.setDefault(qt.QLocale("en_US"))
        self._widget = None
        # Add combobox to choose between RSM and magnification (in one dimension case)
        self._methodCB = qt.QComboBox(self)
        self._methodCB.addItems(["RSM", "Magnification"])
        self._methodCB.hide()
        self.controlArea.layout().addWidget(self._methodCB)
        self._methodCB.currentTextChanged.connect(self._changeWidget)

    @Inputs.dataset
    def setDataset(self, _input):
        if _input is not None:
            if self._widget:
                self.controlArea.layout().removeWidget(self._widget)
                self._widget.hide()
            dataset, update = _input
            self._dataset = dataset
            if not dataset[1].dims.ndim:
                msg = qt.QMessageBox()
                msg.setIcon(qt.QMessageBox.Warning)
                msg.setText(
                    "This widget has to be used before selecting any region of \
                             interest and after selecting the dimensions"
                )
                msg.exec_()
            else:
                if dataset[1].dims.ndim == 1:
                    self._methodCB.show()
                    self._changeWidget("RSM")
                else:
                    self._methodCB.hide()
                    self._widget = MagnificationWidget(parent=self)
                    if self.magnification:
                        self._widget.magnification = self.magnification
                        self._widget.orientation = self.orientation

                    self._widget.sigComputed.connect(self._sendSignal)
                    self.controlArea.layout().addWidget(self._widget)
                    self._widget.setDataset(*dataset)

            if update is None:
                self.open()
            elif update != self._widget:
                self.Outputs.dataset.send(((self,) + self._widget.getDataset(), update))

    def _updateDataset(self, widget, dataset):
        self._widget._updateDataset(widget, dataset)
        if widget != self:
            self.Outputs.dataset.send(((self,) + self._widget.getDataset(), widget))

    def _changeWidget(self, method):
        """
        Change the widget displayed on the window
        """
        if self._widget:
            self.controlArea.layout().removeWidget(self._widget)
            self._widget.hide()
        if method == "RSM":
            self._widget = RSMWidget(parent=self)
            if self.pixelSize:
                self._widget.pixelSize = self.pixelSize
                self._widget.rotate = self.rotate
        else:
            self._widget = MagnificationWidget(parent=self)
            if self.magnification:
                self._widget.magnification = self.magnification
                self._widget.orientation = self.orientation
        self._widget.sigComputed.connect(self._sendSignal)
        self.controlArea.layout().addWidget(self._widget)
        self._widget.setDataset(*self._dataset)

    def _sendSignal(self):
        """
        Emits the signal with the new dataset.
        """
        if hasattr(self._widget, "magnification"):
            self.magnification = self._widget.magnification
            self.kind = False
            self.orientation = self._widget.orientation
        elif hasattr(self._widget, "pixelSize"):
            self.pixelSize = self._widget.pixelSize
            self.rotate = self._widget.rotate
            self.kind = True
        self.close()
        self.Outputs.dataset.send(((self,) + self._widget.getDataset(), None))
