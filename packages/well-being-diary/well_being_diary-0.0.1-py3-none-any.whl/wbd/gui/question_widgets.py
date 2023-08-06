from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets
from wbd import wbd_global
import logging
import abc
from string import Template


"""
class CustomQuestionWidgetAbstract(abc.ABC, QtWidgets.QWidget):
    @abc.abstractmethod
    def on_value_changed(self, i_new_value: str):
        # -Please note that the type is a string
        logging.debug("on_value_changed, i_new_value = " + str(i_new_value))
"""


class QuestionSliderCw(QtWidgets.QWidget):
    widget_update_signal = QtCore.Signal(str)
    # -str is the text to be added at the end of the entry text area (plaintextedit)
    WIDGET_PREFIX_STR = "[Slider_"
    WIDGET_SUFFIX_STR = "]"
    WIDGET_TEMPLATE_STR = WIDGET_PREFIX_STR + "${custom_value_str}" + WIDGET_SUFFIX_STR

    def __init__(self, i_title: str, i_min: int, i_max: int):
        super().__init__()

        self.vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbox_l2)

        self.title_qll = QtWidgets.QLabel(i_title)
        self.vbox_l2.addWidget(self.title_qll)

        self.slider = QtWidgets.QSlider()
        self.vbox_l2.addWidget(self.slider)
        self.slider.setMinimum(i_min)
        self.slider.setMaximum(i_max)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.valueChanged.connect(self.on_value_changed)

        self.show()

    def on_value_changed(self, i_new_value):
        new_value_as_str = str(i_new_value)
        logging.debug("i_new_value = " + new_value_as_str)

        template = Template(self.WIDGET_TEMPLATE_STR)
        to_send_str = template.substitute(
            custom_value_str=new_value_as_str
        )

        self.widget_update_signal.emit(to_send_str)


class QuestionCheckboxCw(QtWidgets.QWidget):
    widget_update_signal = QtCore.Signal(str)
    # -str is the text to be added at the end of the entry text area (plaintextedit)
    WIDGET_PREFIX_STR = "[Checkbox_"
    WIDGET_SUFFIX_STR = "]"
    WIDGET_TEMPLATE_STR = WIDGET_PREFIX_STR + "${custom_value_str}" + WIDGET_SUFFIX_STR

    def __init__(self, i_title: str):
        super().__init__()

        self.vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbox_l2)

        # self.title_qll = QtWidgets.QLabel("Title")
        # self.hbox_l2.addWidget(self.title_qll)

        self.checkbox = QtWidgets.QCheckBox(i_title)
        self.vbox_l2.addWidget(self.checkbox)
        self.checkbox.toggled.connect(self.on_value_changed)

        self.show()

    def on_value_changed(self, i_new_value):
        new_value_as_str = str(i_new_value)
        logging.debug("i_new_value = " + new_value_as_str)

        template = Template(self.WIDGET_TEMPLATE_STR)
        to_send_str = template.substitute(
            custom_value_str=new_value_as_str
        )

        self.widget_update_signal.emit(to_send_str)


