__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "22/12/2020"


from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output
from silx.gui.colors import Colormap
from darfix.gui.blindSourceSeparationWidget import BSSWidget
from darfix.core.process import BlindSourceSeparation


class BlindSourceSeparationWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "blind source separation"
    icon = "icons/bss.png"
    want_main_area = False
    ewokstaskclass = BlindSourceSeparation

    # Settings
    method = Setting(str(), schema_only=True)
    n_comp = Setting(int(), schema_only=True)

    # Inputs
    class Inputs:
        dataset = Input("dataset", tuple)
        colormap = Input("colormap", Colormap)

    # Outputs
    class Outputs:
        dataset = Output("dataset", tuple)
        colormap = Output("colormap", Colormap)

    def __init__(self):
        super().__init__()

        self._widget = BSSWidget(parent=self)
        self._widget.sigComputed.connect(self._updateSettings)
        self.controlArea.layout().addWidget(self._widget)

    def _updateSettings(self, method, n_comp):
        self.method = method.name
        self.n_comp = n_comp

    @Inputs.dataset
    def setDataset(self, _input):
        if _input is not None:
            dataset, update = _input
            self._widget.setDataset(*dataset)

            if update is None:
                self.open()
            self.Outputs.dataset.send(((self,) + dataset[1:], update))
            self.Outputs.colormap.send(
                self._widget.getDisplayComponentsWidget().getStackViewColormap()
            )

    @Inputs.colormap
    def setColormap(self, colormap):
        self._widget.getDisplayComponentsWidget().setStackViewColormap(colormap)

    def _updateDataset(self, widget, dataset):
        self._widget._updateDataset(widget, dataset)
