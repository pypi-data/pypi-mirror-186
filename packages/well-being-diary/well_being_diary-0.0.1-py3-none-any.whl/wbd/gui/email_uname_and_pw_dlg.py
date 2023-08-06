
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui
import sys


class EmailUnamePwDlg(QtWidgets.QDialog):
    """
    Inspiration: Answer by lou here:
    https://stackoverflow.com/questions/18196799/how-can-i-show-a-pyqt-modal-dialog-and-get-data-out-of-its-controls-once-its-clo
    """
    def __init__(self, i_parent=None):
        super().__init__(i_parent)

        vbox = QtWidgets.QVBoxLayout(self)

        self.description_qll = QtWidgets.QLabel("Please enter your username and password")
        vbox.addWidget(self.description_qll)

        self.uname_qle = QtWidgets.QLineEdit(self)
        self.uname_qle.setText("tord@disroot.org")
        vbox.addWidget(self.uname_qle)

        self.pw_qle = QtWidgets.QLineEdit(self)
        self.pw_qle.setEchoMode(QtWidgets.QLineEdit.Password)
        vbox.addWidget(self.pw_qle)

        self.button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal,
            self
        )
        vbox.addWidget(self.button_box)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        # -accept and reject are "slots" built into Qt

    @staticmethod
    def get_email_uname_pw_dialog():
        dialog = EmailUnamePwDlg()
        dialog_result = dialog.exec_()
        if dialog_result == QtWidgets.QDialog.Accepted:
            return (dialog.uname_qle.text(), dialog.pw_qle.text())
        else:
            return None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    confirmation_result_bool = EmailUnamePwDlg.get_email_uname_pw_dialog()
    print("confirmation_result_bool = " + str(confirmation_result_bool))
    sys.exit(app.exec_())
