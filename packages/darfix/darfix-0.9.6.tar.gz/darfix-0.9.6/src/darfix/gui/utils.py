__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "03/12/2020"


from silx.gui import qt


class ChooseDimensionDock(qt.QDockWidget):
    def __init__(self, parent=None, vertical=True, values=True, _filter=True):
        """
        Dock widget containing the ChooseDimensionWidget.
        """
        qt.QDockWidget.__init__(self, parent)
        self.widget = ChooseDimensionWidget(self, vertical, values, _filter)
        self.setWidget(self.widget)


class ChooseDimensionWidget(qt.QWidget):
    """
    Widget to choose a dimension from a dict and choose the value to filter
    the data. It can be included in other widget like StackView to filter the
    stack.
    """

    filterChanged = qt.Signal(list, list)
    stateDisabled = qt.Signal()

    def __init__(self, parent=None, vertical=True, values=True, _filter=True):
        qt.QWidget.__init__(self, parent)

        if vertical:
            self.setLayout(qt.QVBoxLayout())
        else:
            self.setLayout(qt.QHBoxLayout())
        self.show_values = values
        self.dimensionWidgets = []
        self.filter = _filter
        if _filter:
            self._checkbox = qt.QCheckBox("Filter by dimension", self)
            self._checkbox.stateChanged.connect(self._updateState)

    def setDimensions(self, dimensions):
        """
        Function that fills the corresponeding comboboxes with the dimension's
        name and possible values.

        :param array_like dimensions: List of `darfix.core.dataset.Dimension`
                                      elements.
        """
        self.dimensionWidgets = []
        for i in reversed(range(self.layout().count())):
            self.layout().itemAt(i).widget().setParent(None)
        self.dimensions = dimensions
        self.dimension = []
        self.value = [0 for i in range(self.dimensions.ndim - 1)]
        for i in range(dimensions.ndim - 1):
            self._addDimensionWidget()
            self.dimension.append(i)
            self.dimensionWidgets[-1][0].setCurrentIndex(i)

        status = self.blockSignals(True)
        self._updateDimension(0)
        if self.filter:
            self.blockSignals(status)
            self._updateState(self._checkbox.isChecked())
            self.layout().addWidget(self._checkbox)

    def _addDimensionWidget(self):
        """
        Add new widget to choose between different dimensions and values.
        """

        widget = qt.QWidget(self)
        layout = qt.QGridLayout()
        dimensionCB = qt.QComboBox()
        valueCB = None
        if self.show_values:
            dimensionLabel = qt.QLabel("Dimension: ")
            layout.addWidget(dimensionLabel, 0, 0)
            layout.addWidget(dimensionCB, 0, 1)
            valueLabel = qt.QLabel("Value: ")
            valueCB = qt.QComboBox()
            layout.addWidget(valueLabel, 1, 0)
            layout.addWidget(valueCB, 1, 1)
            valueCB.setEnabled(False)
            valueCB.currentIndexChanged.connect(self._updateValue)
        else:
            layout.addWidget(dimensionCB, 0, 0)
        self.dimensionWidgets.append([dimensionCB, valueCB])
        widget.setLayout(layout)
        self.layout().addWidget(widget)
        dimensionCB.setEnabled(False)

        for dimension in self.dimensions:
            dimensionCB.insertItem(dimension[0], dimension[1].name)
        dimensionCB.currentIndexChanged.connect(self._updateDimension)

    def _updateDimension(self, axis=-1):
        """
        Updates the selected dimension and set's the corresponding possible values.

        :param int axis: selected dimension's axis, only used to check valid call
            of the method.
        """
        if axis != -1 and axis is not None:
            self.dimension = []
            # Init values to 0
            self.value = [0 for i in range(self.dimensions.ndim - 1)]
            # Reset all dimensions
            for dimWidget in self.dimensionWidgets:
                # Prevent signals
                status = dimWidget[0].blockSignals(True)
                axis = dimWidget[0].currentIndex()
                # Enable / disable items in combobox
                for dimension in self.dimensions:
                    if dimension[0] in self.dimension:
                        dimWidget[0].model().item(dimension[0]).setEnabled(False)
                        # If axis is already in the dimensions list, set it to
                        # next available axis.
                        if axis == dimension[0]:
                            axis = (axis + 1) % self.dimensions.ndim
                            dimWidget[0].setCurrentIndex(axis)
                    else:
                        dimWidget[0].model().item(dimension[0]).setEnabled(True)
                dimWidget[0].blockSignals(status)
                if dimWidget[0].currentText() != "None":
                    self.dimension.append(axis)
                if self.show_values:
                    # Set values from new dimension
                    dimWidget[1].clear()
                    dimWidget[1].addItems(
                        map(str, self.dimensions.get(axis).unique_values)
                    )

            self.filterChanged.emit(self.dimension, self.value)

    def _updateValue(self, index=None):
        """
        Updates the selected value.

        :param int index: selected value's index.
        """
        if self.show_values and (index is not None or index != -1):
            self.value = []
            for dimWidget in self.dimensionWidgets:
                axis = dimWidget[1].currentIndex()
                self.value.append(axis)

            self.filterChanged.emit(self.dimension, self.value)

    def _updateState(self, state):
        """
        Updates the state of the widget.

        :param bool state: If True, the widget emit's a signal
                    with the selected dimension and value. Else,
                    a disabled signal is emitted.

        """
        for dimWidget in self.dimensionWidgets:
            dimWidget[0].setEnabled(state)
            if self.show_values:
                dimWidget[1].setEnabled(state)

        if state:
            self.filterChanged.emit(self.dimension, self.value)
        else:
            self.stateDisabled.emit()
