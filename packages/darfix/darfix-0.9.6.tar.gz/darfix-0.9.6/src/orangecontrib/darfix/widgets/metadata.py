__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "08/04/2020"


from Orange.widgets.widget import OWWidget, Input
from darfix.gui.metadataWidget import MetadataWidget
from darfix.core.process import DataPassThrough


class MetadataWidgetOW(OWWidget):
    """
    Widget to select the data to be used in the dataset.
    """

    name = "metadata"
    icon = "icons/metadata.svg"
    want_main_area = False
    ewokstaskclass = DataPassThrough

    # Inputs
    class Inputs:
        dataset = Input("dataset", tuple)

    def __init__(self):
        super().__init__()

        self._widget = MetadataWidget()
        self.controlArea.layout().addWidget(self._widget)

    @Inputs.dataset
    def setDataset(self, _input):
        if _input:
            dataset, update = _input
            if dataset:
                self._widget.setDataset(*dataset)
            else:
                self._widget.clearTable()
