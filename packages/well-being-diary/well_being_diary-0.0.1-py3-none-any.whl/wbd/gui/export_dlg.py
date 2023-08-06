
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui
import sys
import time
import wbd.model


class ExportDlg(QtWidgets.QDialog):
    """
    Inspiration: Answer by lou here:
    https://stackoverflow.com/questions/18196799/how-can-i-show-a-pyqt-modal-dialog-and-get-data-out-of-its-controls-once-its-clo
    """
    def __init__(self, i_parent = None):
        super().__init__(i_parent)

        vbox = QtWidgets.QVBoxLayout(self)

        self.description_qll = QtWidgets.QLabel("Please choose what to export")
        vbox.addWidget(self.description_qll)

        # Using active filtering

        # Exporting all

        self.export_type_qbg = QtWidgets.QButtonGroup()

        self.active_filters_qrb = QtWidgets.QRadioButton("Active filter")
        vbox.addWidget(self.active_filters_qrb)
        self.export_type_qbg.addButton(self.active_filters_qrb)

        self.all_qrb = QtWidgets.QRadioButton("All")
        vbox.addWidget(self.all_qrb)
        self.export_type_qbg.addButton(self.all_qrb)

        # Dialog buttons
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
    def open_export_dialog() -> bool:
        dialog = ExportDlg()
        dialog_result = dialog.exec_()
        confirmation_result_bool = False
        if dialog_result == QtWidgets.QDialog.Accepted:
            confirmation_result_bool = True
            if dialog.active_filters_qrb.isChecked():
                wbd.model.export_to_csv(wbd.model.ExportTypeEnum.active_filters)
            elif dialog.all_qrb.isChecked():
                wbd.model.export_to_csv(wbd.model.ExportTypeEnum.all)
            else:
                pass  # -no radiobutton selected
        return confirmation_result_bool


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    confirmation_result_bool = ExportDlg.open_export_dialog()
    print("confirmation_result_bool = " + str(confirmation_result_bool))
    sys.exit(app.exec_())
