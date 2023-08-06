__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "15/09/2020"


import unittest
from silx.gui import qt
from orangecontrib.darfix.test.orangeWorkflowTest import OrangeWorkflowTest

try:
    from Orange.canvas.application.canvasmain import CanvasMainWindow
except ImportError:
    CanvasMainWindow = None
app = qt.QApplication.instance() or qt.QApplication([])


@unittest.skipUnless(
    CanvasMainWindow, "Only testing with orange versions older than 3.23.0"
)
class TestWorkflow(OrangeWorkflowTest):
    """
    Create workflow to test that the widgets are correctly displayed in the canvas.
    """

    def setUp(self):
        OrangeWorkflowTest.setUp(self)

        dataSelectionWidget = self.addWidget(
            "orangecontrib.darfix.widgets.dataselection.DataSelectionWidgetOW"
        )
        dataCopyWidget = self.addWidget(
            "orangecontrib.darfix.widgets.datacopy.DataCopyWidgetOW"
        )
        dataPartitionWidget = self.addWidget(
            "orangecontrib.darfix.widgets.datapartition.DataPartitionWidgetOW"
        )
        roiSelectionWidget = self.addWidget(
            "orangecontrib.darfix.widgets.roiselection.RoiSelectionWidgetOW"
        )
        noiseRemovalWidget = self.addWidget(
            "orangecontrib.darfix.widgets.noiseremoval.NoiseRemovalWidgetOW"
        )
        shiftCorrectionWidget = self.addWidget(
            "orangecontrib.darfix.widgets.shiftcorrection.ShiftCorrectionWidgetOW"
        )
        zsumWidget = self.addWidget("orangecontrib.darfix.widgets.zsum.ZSumWidgetOW")
        dimensionWidget = self.addWidget(
            "orangecontrib.darfix.widgets.dimensions.DimensionWidgetOW"
        )
        metadataWidget = self.addWidget(
            "orangecontrib.darfix.widgets.metadata.MetadataWidgetOW"
        )

        self.processOrangeEvents()

        self.link(dataSelectionWidget, "dataset", metadataWidget, "dataset")
        self.link(metadataWidget, "dataset", dataCopyWidget, "dataset")
        self.link(dataCopyWidget, "dataset", dataPartitionWidget, "dataset")
        self.link(dataPartitionWidget, "dataset", dimensionWidget, "dataset")
        self.link(dimensionWidget, "dataset", roiSelectionWidget, "dataset")
        self.link(roiSelectionWidget, "dataset", noiseRemovalWidget, "dataset")
        self.link(noiseRemovalWidget, "dataset", shiftCorrectionWidget, "dataset")
        self.link(shiftCorrectionWidget, "dataset", zsumWidget, "dataset")

        self.processOrangeEvents()

    def test(self):

        app.processEvents()

    def tearDown(self):
        OrangeWorkflowTest.tearDown(self)
