__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "08/04/2020"


from Orange.widgets.widget import OWWidget, Input, Output
from darfix.gui.PCAWidget import PCAWidget


class PCAWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "PCA"
    icon = "icons/pca.png"
    want_main_area = False

    # Inputs
    class Inputs:
        dataset = Input("dataset", tuple)

    # Outputs
    class Outputs:
        dataset = Output("dataset", tuple)

    def __init__(self):
        super().__init__()

        self._widget = PCAWidget(parent=self)
        self.controlArea.layout().addWidget(self._widget)

    @Inputs.dataset
    def setDataset(self, _input):
        if _input is not None:
            dataset, update = _input
            self._widget.setDataset(*dataset)
            if update is None:
                self.open()
            self.Outputs.dataset.send(((self,) + dataset[1:], update))

    def _updateDataset(self, widget, dataset):
        self._widget._updateDataset(widget, dataset)
