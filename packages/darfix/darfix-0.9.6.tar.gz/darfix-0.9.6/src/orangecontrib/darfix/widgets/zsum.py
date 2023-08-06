__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "20/07/2021"


from silx.gui.colors import Colormap
from Orange.widgets.widget import OWWidget, Input
from darfix.gui.zSumWidget import ZSumWidget
from darfix.core.process import ZSum


class ZSumWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "z sum"
    icon = "icons/zsum.svg"
    want_main_area = False
    ewokstaskclass = ZSum

    # Inputs
    class Inputs:
        dataset = Input("dataset", tuple)
        colormap = Input("colormap", Colormap)

    def __init__(self):
        super().__init__()

        self._widget = ZSumWidget(parent=self)
        self.controlArea.layout().addWidget(self._widget)

    @Inputs.dataset
    def setDataset(self, _input):
        if _input is not None:
            dataset, update = _input
            self._widget.setDataset(*dataset)
            if update is None:
                self.open()

    @Inputs.colormap
    def setColormap(self, colormap):
        self._widget.setColormap(colormap)
