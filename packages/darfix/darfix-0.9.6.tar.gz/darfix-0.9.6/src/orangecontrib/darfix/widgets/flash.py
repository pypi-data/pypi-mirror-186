__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "12/08/2019"


from Orange.widgets.widget import OWWidget, Input, Output


class FlashWidgetOW(OWWidget):

    """
    Widget that creates a new dataset from a given one, and copies its data.
    """

    name = "flash"
    icon = "icons/flash.svg"
    want_main_area = False

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
            self.dataset, update = _input
            self.dataset[0]._updateDataset(self.dataset[0], self.dataset[1])
            self.Outputs.dataset.send(((self,) + self.dataset[1:], None))

    def _updateDataset(self, widget, dataset):
        self.Outputs.dataset.send(((self, dataset) + self.dataset[2:], widget))

    def setVisible(self, visible):
        pass
