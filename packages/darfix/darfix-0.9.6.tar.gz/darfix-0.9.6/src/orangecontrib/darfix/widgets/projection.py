__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "09/12/2021"


from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets.settings import Setting
from darfix.gui.projectionWidget import ProjectionWidget
from darfix.core.process import Projection


class ProjectionWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "projection"
    # icon = "icons/projection.png"
    want_main_area = False
    ewokstaskclass = Projection

    # Inputs
    class Inputs:
        dataset = Input("dataset", tuple)

    # Outputs
    class Outputs:
        dataset = Output("dataset", tuple)

    dimension = Setting(int)

    def __init__(self):
        super().__init__()

        self._widget = ProjectionWidget(parent=self)
        self._widget.sigComputed.connect(self._sendSignal)
        self.controlArea.layout().addWidget(self._widget)

    @Inputs.dataset
    def setDataset(self, _input):
        if _input is not None:
            dataset, update = _input
            self._widget.setDataset(*dataset)

            if update is None:
                self.open()
            elif update != self:
                self.Outputs.dataset.send(
                    ((self,) + self._widget.mainWindow.getDataset(), update)
                )

            if self.dimension:
                self._widget.dimension = self.dimension

    def _updateDataset(self, widget, dataset):
        self._widget._updateDataset(widget, dataset)

    def _sendSignal(self):
        """
        Function to emit the new dataset.
        """
        self.dimension = self._widget.dimension
        self.Outputs.dataset.send(((self,) + self._widget.getDataset(), None))
        self.close()
