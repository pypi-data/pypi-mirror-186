from PySide6 import QtWidgets
from PySide6 import QtCore
import traceback
import sys
import enum
import logging


class ExceptionType(enum.Enum):
    warning = 1
    error = 2


class ExceptionDlg(QtWidgets.QDialog):
    """
    Inspiration: Answer by lou here:
    https://stackoverflow.com/questions/18196799/how-can-i-show-a-pyqt-modal-dialog-and-get-data-out-of-its-controls-once-its-clo
    """
    def __init__(self, i_exception_type: ExceptionType, i_title: str, i_description: str, i_stack_trace: str=None, i_parent=None):
        super().__init__(i_parent)

        title_str = i_exception_type.name.capitalize() + ": " + i_title
        self.setWindowTitle(title_str)

        vbox = QtWidgets.QVBoxLayout(self)

        self.exception_type_qll = QtWidgets.QLabel(title_str)
        new_font = self.exception_type_qll.font()
        new_font.setPointSize(18)
        self.exception_type_qll.setFont(new_font)
        vbox.addWidget(self.exception_type_qll)

        self.description_title_qll = QtWidgets.QLabel("Description")
        new_font = self.description_title_qll.font()
        new_font.setPointSize(14)
        self.description_title_qll.setFont(new_font)
        vbox.addWidget(self.description_title_qll)

        self.description_qll = QtWidgets.QLabel(i_description)
        vbox.addWidget(self.description_qll)

        if i_stack_trace is not None:
            self.call_stack_title_qll = QtWidgets.QLabel("Call Stack")
            new_font = self.call_stack_title_qll.font()
            new_font.setPointSize(14)
            self.call_stack_title_qll.setFont(new_font)
            vbox.addWidget(self.call_stack_title_qll)

            self.call_stack_qpte = QtWidgets.QPlainTextEdit()
            self.call_stack_qpte.setReadOnly(True)
            self.call_stack_qpte.setPlainText(i_stack_trace)
            vbox.addWidget(self.call_stack_qpte)

        # Dialog buttons
        self.button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok,
            QtCore.Qt.Horizontal,
            self
        )
        vbox.addWidget(self.button_box)
        self.button_box.accepted.connect(self.accept)
        # -accept is a "slot" built into Qt


def warning(i_title: str, i_description: str=""):
    descr_str = i_title
    if i_description:
        descr_str = i_description
    dialog = ExceptionDlg(ExceptionType.warning, i_title, descr_str)
    dialog_result_unused = dialog.exec_()
    logging.warning(i_title + " - " + descr_str)
    raise RuntimeWarning

    """
    Logging, exceptions, etc:
    Idea: silent errors
    Idea: Raising exception
    """


def error(i_title: str, i_description: str=""):
    descr_str = i_title
    if i_description:
        descr_str = i_description
    stack_str = ''.join(traceback.format_stack())
    dialog = ExceptionDlg(ExceptionType.error, i_title, descr_str, stack_str)
    dialog_result_unused = dialog.exec_()
    logging.error(i_title + " - " + descr_str + "\n" + stack_str)
    raise RuntimeError
    # -Do we need to raise this runtimeerror? There is already stack output to stdout


#######def file_size_sanity_check(i_file_path: str, i_min_size_bytes: int):


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    warning("Title", "Description")
    sys.exit(app.exec_())

