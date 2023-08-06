__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "20/11/2020"

from Orange.widgets.widget import OWWidget
from darfix.gui.lineProfileWidget import LineProfileWidget


class LineProfileWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "line profile"
    icon = "icons/line_profile.png"
    want_main_area = False

    def __init__(self):
        super().__init__()

        self._widget = LineProfileWidget(parent=self)
        self.controlArea.layout().addWidget(self._widget)
