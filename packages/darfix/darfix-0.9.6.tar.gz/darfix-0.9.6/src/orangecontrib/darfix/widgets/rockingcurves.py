__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "11/12/2020"


from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input
from silx.gui.colors import Colormap
from darfix.gui.rockingCurvesWidget import RockingCurvesWidget
from darfix.core.process import RockingCurves


class RockingCurvesWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "rocking curves"
    icon = "icons/curves.png"
    want_main_area = False
    ewokstaskclass = RockingCurves

    # Inputs
    class Inputs:
        dataset = Input("dataset", tuple)
        colormap = Input("colormap", Colormap)

    int_thresh = Setting(str())

    def __init__(self):
        super().__init__()

        self._widget = RockingCurvesWidget(parent=self)
        self._widget.sigFitted.connect(self._fit)
        self.controlArea.layout().addWidget(self._widget)
        if self.int_thresh:
            self._widget.intThresh = self.int_thresh

    @Inputs.dataset
    def setDataset(self, _input):
        if _input is not None:
            dataset, update = _input
            self._widget.setDataset(*dataset)
            if update is None:
                self.open()

    @Inputs.colormap
    def setColormap(self, colormap):
        self._widget.setStackViewColormap(colormap)

    def _fit(self):
        self.int_thresh = self._widget.intThresh
