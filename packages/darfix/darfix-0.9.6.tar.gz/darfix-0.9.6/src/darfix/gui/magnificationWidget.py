__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "28/10/2021"


from silx.gui import qt
from silx.utils.enum import Enum as _Enum


class Value(_Enum):
    """
    Methods available to compute the background.
    """

    PIXEL_2X = 3.75
    PIXEL_10X = 0.75


class Orientation(_Enum):
    VERTICAL = "Vertical"
    HORIZONTAL = "Horizontal"


class MagnificationWidget(qt.QMainWindow):
    """
    Widget to apply magnification transformation to the data axes.
    """

    sigComputed = qt.Signal()

    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)

        widget = qt.QWidget()
        layout = qt.QVBoxLayout()

        self._magnification = Value.PIXEL_2X.value
        self._checkbox2x = qt.QCheckBox("2x magnification")
        self._checkbox10x = qt.QCheckBox("10x magnification")
        self._checkboxManual = qt.QCheckBox("Manual magnification:")
        self._topographyCheckbox = qt.QCheckBox("Topography (obpitch)")
        self._centerAxesCheckbox = qt.QCheckBox("Center axes")
        self._centerAxesCheckbox.setChecked(True)
        self._orientationCB = qt.QComboBox()
        self._orientationCB.addItems(Orientation.values())
        topographyAxis = qt.QLabel("Topography axis: ")
        self._manualLE = qt.QLineEdit(parent=self)
        self._manualLE.setEnabled(False)
        validator = qt.QDoubleValidator()
        validator.setBottom(0)
        self._manualLE.setValidator(validator)
        self._okButton = qt.QPushButton("Ok")
        self._okButton.setEnabled(False)
        self._okButton.pressed.connect(self._saveMagnification)
        layout.addWidget(self._checkbox2x)
        layout.addWidget(self._checkbox10x)
        layout.addWidget(self._checkboxManual)
        layout.addWidget(self._manualLE)
        layout.addWidget(self._topographyCheckbox, alignment=qt.Qt.AlignRight)
        self._topographyWidget = qt.QWidget()
        topographyLayout = qt.QHBoxLayout()
        topographyLayout.addWidget(topographyAxis)
        topographyLayout.addWidget(self._orientationCB)
        self._topographyWidget.setLayout(topographyLayout)
        self._topographyWidget.hide()
        self._topographyWidget.setMaximumHeight(40)
        layout.addWidget(self._topographyWidget, alignment=qt.Qt.AlignRight)
        layout.addWidget(self._okButton)
        layout.addWidget(self._centerAxesCheckbox)

        # self._okButton.pressed.connect(self._saveMagnification)
        self._checkbox2x.stateChanged.connect(self._check2x)
        self._checkbox10x.stateChanged.connect(self._check10x)
        self._checkboxManual.stateChanged.connect(self._checkManual)
        self._topographyCheckbox.stateChanged.connect(self._checkTopography)

        self._checkbox2x.setChecked(True)
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def setDataset(
        self, parent, dataset, indices=None, bg_indices=None, bg_dataset=None
    ):
        """
        Dataset setter.

        :param Dataset dataset: dataset
        """
        self.parent = parent
        self.dataset = dataset
        self.indices = indices
        self.bg_indices = bg_indices
        self.bg_dataset = bg_dataset

        if not self.dataset.dims:
            msg = qt.QMessageBox()
            msg.setIcon(qt.QMessageBox.Warning)
            msg.setText(
                "This widget has to be used before selecting any region of \
                         interest and after selecting the dimensions"
            )
            msg.exec_()
        else:
            self._okButton.setEnabled(True)

    @property
    def magnification(self):
        return self._magnification

    @property
    def orientation(self):
        if self._topographyCheckbox.isChecked():
            return self._orientationCB.currentIndex()
        else:
            return -1

    @orientation.setter
    def orientation(self, orientation):
        if orientation != -1:
            self._topographyCheckbox.setChecked(True)
            self._orientationCB.setCurrentIndex(orientation)

    @magnification.setter
    def magnification(self, magnification):
        self._magnification = magnification
        if self.magnification == Value.PIXEL_2X.value:
            self._check2x(True)
            self._checkbox2x.setChecked(True)
        elif self.magnification == Value.PIXEL_10X.value:
            self._checkbox10x.setChecked(True)
            self._check10x(True)
        else:
            self._manualLE.setText(str(self._magnification))
            self._checkManual(True)
            self._checkboxManual.setChecked(True)

    def getDataset(self):
        return self.dataset, self.indices, self.bg_indices, self.bg_dataset

    def _updateDataset(self, widget, dataset):
        self.parent._updateDataset(widget, dataset)
        self.dataset = dataset

    def _checkManual(self, checked):
        if checked:
            self._checkbox2x.setChecked(False)
            self._checkbox10x.setChecked(False)
            self._manualLE.setEnabled(True)
        else:
            self._manualLE.setEnabled(False)

    def _check2x(self, checked):
        if checked:
            self._checkbox10x.setChecked(False)
            self._checkboxManual.setChecked(False)
            self._manualLE.setEnabled(False)

    def _check10x(self, checked):
        if checked:
            self._checkbox2x.setChecked(False)
            self._checkboxManual.setChecked(False)
            self._manualLE.setEnabled(False)

    def _checkTopography(self, checked):
        if checked:
            self._topographyWidget.show()
        else:
            self._topographyWidget.hide()

    def _saveMagnification(self):

        if self._checkbox2x.isChecked():
            magnification = Value.PIXEL_2X.value
        elif self._checkbox10x.isChecked():
            magnification = Value.PIXEL_10X.value
        else:
            magnification = self._manualLE.text()
            if magnification == "":
                msg = qt.QMessageBox()
                msg.setIcon(qt.QMessageBox.Warning)
                msg.setText(
                    "Magnification value has to be entered when choosing manual"
                )
                msg.exec_()
                return
        self._magnification = float(magnification)

        self.dataset.compute_transformation(
            self.magnification,
            topography=[
                self._topographyCheckbox.isChecked(),
                self._orientationCB.currentIndex(),
            ],
            center=self._centerAxesCheckbox.isChecked(),
        )

        self.sigComputed.emit()
