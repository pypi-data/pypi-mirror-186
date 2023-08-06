from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui


class HelpCompositeWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        vbox = QtWidgets.QVBoxLayout()
        self.setLayout(vbox)

        helptext_qll = QtWidgets.QLabel("Help text")
        helptext_qll.setWordWrap(True)

        vbox.addWidget(helptext_qll)
