__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "14/10/2021"

import logging
import os

from silx.gui import qt
from darfix.core.data_selection import load_process_data
from silx.gui.dialog.DataFileDialog import DataFileDialog

_logger = logging.getLogger(__file__)


class DatasetSelectionWidget(qt.QTabWidget):
    """
    Widget that creates a dataset from a list of files or from a single filename.
    It lets the user add the first filename of a directory of files, or to
    upload manually each of the files to be read.
    If both options are filled up, only the files in the list of filenames
    are read.
    """

    sigProgressChanged = qt.Signal(int)

    def __init__(self, parent=None):
        qt.QTabWidget.__init__(self, parent)

        self._ish5CB = qt.QCheckBox("Is hdf5?")

        # Raw data
        self._rawFilenameData = FilenameSelectionWidget(parent=self)
        self._rawFilesData = FilesSelectionWidget(parent=self)
        self._inDiskCB = qt.QCheckBox("Use data from disk", self)
        titleWidget = qt.QWidget(self)
        titleLayout = qt.QHBoxLayout()
        titleLabel = qt.QLabel("Workflow title:")
        self._titleLE = qt.QLineEdit("")
        titleLayout.addWidget(titleLabel)
        titleLayout.addWidget(self._titleLE)
        titleWidget.setLayout(titleLayout)
        rawData = qt.QWidget(self)
        rawData.setLayout(qt.QVBoxLayout())
        rawData.layout().addWidget(titleWidget)
        rawData.layout().addWidget(self._ish5CB)
        rawData.layout().addWidget(self._rawFilenameData)
        rawData.layout().addWidget(self._rawFilesData)
        rawData.layout().addWidget(self._inDiskCB)
        rawData.layout().addWidget(titleWidget)
        self.addTab(rawData, "raw data")

        self._isH5 = False
        self._inDisk = False

        # Dark data
        self._darkFilenameData = FilenameSelectionWidget(parent=self)
        self.addTab(self._darkFilenameData, "dark data")

        # Treated data
        self._treatedDirData = DirSelectionWidget(parent=self)
        self.addTab(self._treatedDirData, "treated data")

        self._dataset = None
        self.bg_dataset = None
        self.indices = None
        self.bg_indices = None

        self.getRawFilenames = self._rawFilesData.getFiles
        self.getRawFilename = self._rawFilenameData.getFilename
        self.getDarkFilename = self._darkFilenameData.getFilename
        self.setRawFilenames = self._rawFilesData.setFiles
        self.setRawFilename = self._rawFilenameData.setFilename
        self.setDarkFilename = self._darkFilenameData.setFilename
        self.getTreatedDir = self._treatedDirData.getDir
        self.setTreatedDir = self._treatedDirData.setDir

        self._ish5CB.stateChanged.connect(self.__isH5)
        self._inDiskCB.stateChanged.connect(self.__inDisk)

    def loadDataset(self) -> bool:
        """
        Loads the dataset from the filenames.
        """
        dark_filename = self._darkFilenameData.getFilename()
        root_dir = self._treatedDirData.getDir()
        filenames = self._rawFilesData.getFiles()
        if not filenames:
            filenames = self._rawFilenameData.getFilename()
        (
            self._dataset,
            self.indices,
            self.bg_indices,
            self.bg_dataset,
        ) = load_process_data(
            filenames,
            root_dir=root_dir,
            in_memory=not self._inDisk,
            dark_filename=dark_filename,
            isH5=self._isH5,
            title=self._titleLE.text(),
        )
        return self.dataset is not None and self.dataset.nframes != 0

    def _updateDataset(self, dataset):
        self._dataset = dataset

    @property
    def dataset(self):
        return self._dataset

    def getDataset(self):
        return self._dataset, self.indices, self.bg_indices, self.bg_dataset

    def updateProgress(self, progress):
        self.sigProgressChanged.emit(progress)

    def __isH5(self, isH5):
        self._isH5 = isH5
        self._rawFilenameData.isHDF5(isH5)
        if isH5:
            self._rawFilesData.hide()
        else:
            self._rawFilesData.show()

    def __inDisk(self, inDisk):
        self._inDisk = bool(inDisk)


class FilesSelectionWidget(qt.QWidget):
    """
    Widget used to get one or more files from the computer and add them to a list.
    """

    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)

        self._files = []

        self.setLayout(qt.QVBoxLayout())
        self._table = self._init_table()
        self._addButton = qt.QPushButton("Add")
        self._rmButton = qt.QPushButton("Remove")
        self.layout().addWidget(self._table)
        self.layout().addWidget(self._addButton)
        self.layout().addWidget(self._rmButton)
        self._addButton.clicked.connect(self._addFiles)
        self._rmButton.clicked.connect(self._removeFiles)

    def _init_table(self):

        table = qt.QTableWidget(0, 1, parent=self)
        table.horizontalHeader().hide()
        # Resize horizontal header to fill all the column size
        if hasattr(table.horizontalHeader(), "setSectionResizeMode"):  # Qt5
            table.horizontalHeader().setSectionResizeMode(0, qt.QHeaderView.Stretch)
        else:  # Qt4
            table.horizontalHeader().setResizeMode(0, qt.QHeaderView.Stretch)

        return table

    def _addFiles(self):
        """
        Opens the file dialog and let's the user choose one or more files.
        """
        dialog = qt.QFileDialog(self)
        dialog.setFileMode(qt.QFileDialog.ExistingFiles)

        if not dialog.exec_():
            dialog.close()
            return

        for file in dialog.selectedFiles():
            self.addFile(file)

    def _removeFiles(self):
        """
        Removes the selected items from the table.
        """
        selectedItems = self._table.selectedItems()
        if selectedItems is not None:
            for item in selectedItems:
                self._files.remove(item.text())
                self._table.removeRow(item.row())

    def addFile(self, file):
        """
        Adds a file to the table.

        :param str file: filepath to add to the table.
        """
        assert os.path.isfile(file)
        item = qt.QTableWidgetItem()
        item.setText(file)
        row = self._table.rowCount()
        self._table.setRowCount(row + 1)
        self._table.setItem(row, 0, item)
        self._files.append(file)

    def getFiles(self):
        return self._files

    def setFiles(self, files):
        """
        Adds a list of files to the table.

        :param array_like files: List to add
        """
        for file in files:
            self.addFile(file)

    def getDir(self):
        if len(self._files):
            return os.path.dirname(self._files[0])
        return None


class DirSelectionWidget(qt.QWidget):
    """
    Widget used to obtain a filename (manually or from a file)
    """

    dirChanged = qt.Signal()

    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)

        self._dir = qt.QLineEdit("", parent=self)
        self._dir.editingFinished.connect(self.dirChanged)
        self._addButton = qt.QPushButton("Upload directory", parent=self)
        # self._okButton =  qt.QPushButton("Ok", parent=self)
        self._addButton.pressed.connect(self._uploadDir)
        # self._okButton.pressed.connect(self.close)
        self.setLayout(qt.QHBoxLayout())

        self.layout().addWidget(self._dir)
        self.layout().addWidget(self._addButton)
        # self.layout().addWidget(self._okButton)

    def _uploadDir(self):
        """
        Loads the file from a FileDialog.
        """
        fileDialog = qt.QFileDialog()
        fileDialog.setOption(qt.QFileDialog.ShowDirsOnly)
        fileDialog.setFileMode(qt.QFileDialog.Directory)
        if fileDialog.exec_():
            self._dir.setText(fileDialog.directory().absolutePath())
            self.dirChanged.emit()
        else:
            _logger.warning("Could not open directory")

    def getDir(self):
        return str(self._dir.text())

    def setDir(self, _dir):
        self._dir.setText(str(_dir))


class FilenameSelectionWidget(qt.QWidget):
    """
    Widget used to obtain a filename (manually or from a file)
    """

    filenameChanged = qt.Signal()

    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)
        self._isH5 = False
        self._filename = None
        self._filenameLE = qt.QLineEdit("", parent=self)
        self._addButton = qt.QPushButton("Upload file", parent=self)
        # self._okButton =  qt.QPushButton("Ok", parent=self)
        self._addButton.pressed.connect(self._uploadFilename)
        # self._okButton.pressed.connect(self.close)
        self.setLayout(qt.QHBoxLayout())

        self.layout().addWidget(self._filenameLE)
        self.layout().addWidget(self._addButton)
        # self.layout().addWidget(self._okButton)

    def isHDF5(self, isH5):
        self._isH5 = isH5

    def _uploadFilename(self):
        """
        Loads the file from a FileDialog.
        """
        if self._isH5:
            fileDialog = DataFileDialog()
            if fileDialog.exec_():
                self._filename = fileDialog.selectedDataUrl().path()
                self._filenameLE.setText(self._filename)
                self.filenameChanged.emit()
            else:
                _logger.warning("Could not open file")
        else:
            fileDialog = qt.QFileDialog()
            fileDialog.setFileMode(qt.QFileDialog.ExistingFile)
            if fileDialog.exec_():
                self._filenameLE.setText(fileDialog.selectedFiles()[0])
                self._filename = fileDialog.selectedFiles()[0]
                self.filenameChanged.emit()
            else:
                _logger.warning("Could not open file")

    def getFilename(self):
        return str(self._filenameLE.text())

    def setFilename(self, filename):
        self._filename = filename
        self._filenameLE.setText(str(filename))
