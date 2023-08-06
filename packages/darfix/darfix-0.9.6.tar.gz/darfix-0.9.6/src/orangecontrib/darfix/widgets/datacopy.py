__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "12/08/2019"


import copy

from Orange.widgets.widget import OWWidget, Input, Output
from darfix.core.process import DataCopy


class DataCopyWidgetOW(OWWidget):

    """
    Widget that creates a new dataset from a given one, and copies its data.
    """

    name = "data copy"
    icon = "icons/copy.svg"
    want_main_area = False
    ewokstaskclass = DataCopy

    # Inputs
    class Inputs:
        dataset = Input("dataset", tuple)

    # Outputs
    class Outputs:
        dataset = Output("dataset", tuple)

    def __init__(self):
        super().__init__()

    @Inputs.dataset
    def setDataset(self, _input):
        if _input is not None:
            # Copy and send new dataset
            dataset, update = _input
            if not update:
                self.cp_dataset = copy.deepcopy(dataset[1:])
                self.Outputs.dataset.send(((self,) + self.cp_dataset, None))

    def _updateDataset(self, widget, dataset):
        self.Outputs.dataset.send(((self, dataset) + self.cp_dataset[1:], widget))

    def setVisible(self, visible):
        pass
