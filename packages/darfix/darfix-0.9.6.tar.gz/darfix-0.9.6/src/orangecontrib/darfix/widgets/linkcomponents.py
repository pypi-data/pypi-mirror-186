__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "20/11/2020"

from Orange.widgets.widget import OWWidget
from darfix.gui.linkComponentsWidget import LinkComponentsWidget


class LinkComponentsWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "link components"
    icon = "icons/link.png"
    want_main_area = False

    def __init__(self):
        super().__init__()

        self._widget = LinkComponentsWidget(parent=self)
        self.controlArea.layout().addWidget(self._widget)
