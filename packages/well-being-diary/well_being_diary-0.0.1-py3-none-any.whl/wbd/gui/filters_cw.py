import logging
from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6 import QtCore
import wbd.model
import wbd.wbd_global
import wbd.gui.list_widget


class FiltersCw(QtWidgets.QWidget):
    filters_changed_signal = QtCore.Signal()
    activated_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()

        self.updating_gui_bool = False

        vbox1 = QtWidgets.QVBoxLayout()
        self.setLayout(vbox1)

        hbox_l3 = QtWidgets.QHBoxLayout()
        vbox1.addLayout(hbox_l3)

        self.title_qll = QtWidgets.QLabel("Diary Filters")
        hbox_l3.addWidget(self.title_qll)
        hbox_l3.addStretch(1)

        self.activate_qpb = QtWidgets.QPushButton("Show Diary")
        self.activate_qpb.clicked.connect(self.on_activate_clicked)
        hbox_l3.addWidget(self.activate_qpb)

        # Filters
        # self.filters_qbg.buttonToggled.connect(self.on_filter_checkbox_toggled)
        # ..tag
        hbox_l2 = QtWidgets.QHBoxLayout()
        vbox1.addLayout(hbox_l2)
        self.tag_filter_qcb = QtWidgets.QCheckBox("Tag")
        self.tag_filter_qcb.toggled.connect(self.on_tag_checkbox_toggled)
        hbox_l2.addWidget(self.tag_filter_qcb)
        self.tag_name_qll = QtWidgets.QLabel("<i>-</i>")
        hbox_l2.addWidget(self.tag_name_qll)
        hbox_l2.addStretch(1)
        self.set_tag_qpb = QtWidgets.QPushButton("Set")
        self.set_tag_qpb.clicked.connect(self.on_set_tag_clicked)
        hbox_l2.addWidget(self.set_tag_qpb)
        # ..search
        hbox_l2 = QtWidgets.QHBoxLayout()
        vbox1.addLayout(hbox_l2)
        self.search_filter_qcb = QtWidgets.QCheckBox("Search")
        self.search_filter_qcb.toggled.connect(self.on_search_checkbox_toggled)
        hbox_l2.addWidget(self.search_filter_qcb)
        self.search_qle = QtWidgets.QLineEdit()
        self.search_qle.textChanged.connect(self.on_search_text_changed)  # textEdited
        self.search_qle.setPlaceholderText("Search")
        hbox_l2.addWidget(self.search_qle)
        # ..rating
        hbox_l2 = QtWidgets.QHBoxLayout()
        vbox1.addLayout(hbox_l2)
        self.rating_filter_qcb = QtWidgets.QCheckBox("Rating")
        self.rating_filter_qcb.toggled.connect(self.on_rating_checkbox_toggled)
        hbox_l2.addWidget(self.rating_filter_qcb)
        self.rating_filter_qsr = QtWidgets.QSlider()
        self.rating_filter_qsr.setOrientation(QtCore.Qt.Horizontal)
        self.rating_filter_qsr.setMinimum(0)
        self.rating_filter_qsr.setMaximum(3)
        #########self.rating_filter_qsr.setValue(0)
        self.rating_filter_qsr.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.rating_filter_qsr.setTickInterval(1)
        self.rating_filter_qsr.setSingleStep(1)
        self.rating_filter_qsr.setPageStep(1)
        self.rating_filter_qsr.valueChanged.connect(self.on_rating_slider_changed)
        hbox_l2.addWidget(self.rating_filter_qsr)
        # ..date range
        hbox_l2 = QtWidgets.QHBoxLayout()
        vbox1.addLayout(hbox_l2)
        self.date_filter_qcb = QtWidgets.QCheckBox("Date range")
        hbox_l2.addWidget(self.date_filter_qcb)
        self.date_filter_qcb.toggled.connect(self.on_date_checkbox_toggled)
        self.start_date_qde = QtWidgets.QDateEdit(QtCore.QDate.currentDate())
        # self.start_date_qde.setDate(QtCore.QDateTime.)
        self.start_date_qde.setCalendarPopup(True)
        self.start_date_qde.dateChanged.connect(self.on_start_or_end_date_changed)
        hbox_l2.addWidget(self.start_date_qde)
        self.end_date_qde = QtWidgets.QDateEdit(QtCore.QDate.currentDate())
        self.end_date_qde.setCalendarPopup(True)
        self.end_date_qde.dateChanged.connect(self.on_start_or_end_date_changed)
        hbox_l2.addWidget(self.end_date_qde)

        # ..presets
        # vbox_l2 = QtWidgets.QVBoxLayout()
        hbox_l2 = QtWidgets.QHBoxLayout()
        vbox1.addLayout(hbox_l2)

        self.preset_title_qll = QtWidgets.QLabel("Filter presets")
        hbox_l2.addWidget(self.preset_title_qll)

        self.clear_filters_qpb = QtWidgets.QPushButton("Clear filters")
        hbox_l2.addWidget(self.clear_filters_qpb)
        self.clear_filters_qpb.clicked.connect(self.on_clear_filters_clicked)

        presets_hbox_l2 = QtWidgets.QHBoxLayout()
        vbox1.addLayout(presets_hbox_l2)
        self.presets_qlw = wbd.gui.list_widget.ListWidget(wbd.model.FilterPresetM)
        # QtWidgets.QListWidget()
        # TODO: If screen is small we could have this as a QComboBox?
        self.presets_qlw.currentRowChanged.connect(self.on_presets_row_changed)
        presets_hbox_l2.addWidget(self.presets_qlw)
        vbox_l3 = QtWidgets.QVBoxLayout()
        presets_hbox_l2.addLayout(vbox_l3)
        self.new_preset_name_qle = QtWidgets.QLineEdit()
        vbox_l3.addWidget(self.new_preset_name_qle)
        self.add_new_preset_qpb = QtWidgets.QPushButton("Add")
        self.add_new_preset_qpb.clicked.connect(self.on_add_new_preset_clicked)
        vbox_l3.addWidget(self.add_new_preset_qpb)

    def on_clear_filters_clicked(self):
        wbd.wbd_global.active_state.filters.reset()

        self.update_gui()
        self.filters_changed_signal.emit()

    def on_add_new_preset_clicked(self):
        if self.updating_gui_bool:
            return
        title_str = self.new_preset_name_qle.text()
        # tag_title_str = self.tag_name_qll.text()
        # tag_id_int = wbd.model.TagM.get_tag_by_title(tag_title_str)
        wbd.model.FilterPresetM.add(
            title_str,
            wbd.wbd_global.active_state.filters.tag_active_bool,
            wbd.wbd_global.active_state.filters.tag_id_int,
            wbd.wbd_global.active_state.filters.search_active_bool,
            wbd.wbd_global.active_state.filters.search_term_str,
            wbd.wbd_global.active_state.filters.rating_active_bool,
            wbd.wbd_global.active_state.filters.rating_int,
            wbd.wbd_global.active_state.filters.datetime_active_bool,
            wbd.wbd_global.active_state.filters.start_datetime_string,
            wbd.wbd_global.active_state.filters.end_datetime_string
        )
        self.update_gui()
        # self.presets_qlw.setCurrentRow()

    def on_presets_row_changed(self, i_current_row: int):
        if self.updating_gui_bool:
            return
        if i_current_row == -1:
            return
        current_row_item: QtWidgets.QListWidgetItem = self.presets_qlw.item(i_current_row)
        filter_preset = wbd.model.FilterPresetM.get_by_title(current_row_item.text())
        ######wbd.model.active_filters = filter_preset
        wbd.wbd_global.active_state.filters.tag_active_bool = filter_preset.tag_active_bool
        wbd.wbd_global.active_state.filters.tag_id_int = filter_preset.tag_id_int
        wbd.wbd_global.active_state.filters.search_active_bool = filter_preset.search_active_bool
        wbd.wbd_global.active_state.filters.search_term_str = filter_preset.search_term_str
        wbd.wbd_global.active_state.filters.rating_active_bool = filter_preset.rating_active_bool
        wbd.wbd_global.active_state.filters.rating_int = filter_preset.rating_int
        wbd.wbd_global.active_state.filters.datetime_active_bool = filter_preset.datetime_active_bool
        wbd.wbd_global.active_state.filters.start_datetime_string = filter_preset.start_datetime_string
        wbd.wbd_global.active_state.filters.end_datetime_string = filter_preset.end_datetime_string

        self.update_gui()
        self.filters_changed_signal.emit()

    def on_activate_clicked(self):
        if self.updating_gui_bool:
            return
        self.activated_signal.emit()

    # Date (start and end)

    def on_date_checkbox_toggled(self, i_checked: bool):
        if self.updating_gui_bool:
            return
        wbd.wbd_global.active_state.filters.datetime_active_bool = i_checked

        start_qdate: QtCore.QDate = self.start_date_qde.date()
        wbd.wbd_global.active_state.filters.start_datetime_string = start_qdate.toString(wbd.wbd_global.QT_DATETIME_FORMAT_STR)

        end_qdate: QtCore.QDate = self.end_date_qde.date()
        wbd.wbd_global.active_state.filters.end_datetime_string = end_qdate.toString(wbd.wbd_global.QT_DATETIME_FORMAT_STR)

        self.filters_changed_signal.emit()

    def on_start_or_end_date_changed(self):
        if self.updating_gui_bool:
            return
        wbd.wbd_global.active_state.filters.datetime_active_bool = True

        start_qdate: QtCore.QDate = self.start_date_qde.date()
        wbd.wbd_global.active_state.filters.start_datetime_string = start_qdate.toString(wbd.wbd_global.QT_DATE_ONLY_FORMAT_STR)
        logging.debug("wbd.wbd_global.active_state.filters.start_datetime_string = " + wbd.wbd_global.active_state.filters.start_datetime_string)

        end_qdate: QtCore.QDate = self.end_date_qde.date()
        wbd.wbd_global.active_state.filters.end_datetime_string = end_qdate.toString(wbd.wbd_global.QT_DATE_ONLY_FORMAT_STR)
        logging.debug("wbd.wbd_global.active_state.filters.end_datetime_string = " + wbd.wbd_global.active_state.filters.end_datetime_string)

        self.filters_changed_signal.emit()

    # Search text

    def on_search_checkbox_toggled(self, i_checked: bool):
        if self.updating_gui_bool:
            return
        wbd.wbd_global.active_state.filters.search_active_bool = i_checked
        self.filters_changed_signal.emit()

    def on_search_text_changed(self):
        if self.updating_gui_bool:
            return
        wbd.wbd_global.active_state.filters.search_term_str = self.search_qle.text().strip()
        # wbd.model.active_filters.search_active_bool = True
        # self.search_filter_qcb.setChecked(True)
        self.filters_changed_signal.emit()

    # Tag

    def on_tag_checkbox_toggled(self, i_checked: bool):
        if self.updating_gui_bool:
            return
        wbd.wbd_global.active_state.filters.tag_active_bool = i_checked
        if wbd.wbd_global.active_state.tag_id != wbd.wbd_global.NO_ACTIVE_TAG_INT:
            wbd.wbd_global.active_state.filters.tag_id_int = wbd.wbd_global.active_state.tag_id

            tag = wbd.model.TagM.get(wbd.wbd_global.active_state.filters.tag_id_int)
            self.tag_name_qll.setText(tag.title_str)
        else:
            self.tag_name_qll.setText("-")
        self.filters_changed_signal.emit()

    def on_set_tag_clicked(self):
        if self.updating_gui_bool:
            return
        self.set_tag(wbd.wbd_global.active_state.tag_id)

    def set_tag(self, i_new_tag_id: int):
        if wbd.wbd_global.active_state.tag_id != wbd.wbd_global.NO_ACTIVE_TAG_INT:
            logging.debug("on_set_tag_clicked - i_new_tag_id = " + str(i_new_tag_id))

            wbd.wbd_global.active_state.filters.tag_id_int = wbd.wbd_global.active_state.tag_id
            wbd.wbd_global.active_state.filters.tag_active_bool = True
            tag = wbd.model.TagM.get(wbd.wbd_global.active_state.filters.tag_id_int)
            self.tag_name_qll.setText(tag.title_str)
            self.filters_changed_signal.emit()
            self.update_gui()  # - so that the checkbox is updated

    # Rating

    def on_rating_checkbox_toggled(self, i_checked: bool):
        if self.updating_gui_bool:
            return
        wbd.wbd_global.active_state.filters.rating_active_bool = i_checked
        wbd.wbd_global.active_state.filters.rating_int = self.rating_filter_qsr.value()
        self.filters_changed_signal.emit()

    def on_rating_slider_changed(self):
        if self.updating_gui_bool:
            return
        wbd.wbd_global.active_state.filters.rating_int = self.rating_filter_qsr.value()
        wbd.wbd_global.active_state.filters.rating_active_bool = True
        self.rating_filter_qcb.setChecked(True)
        self.filters_changed_signal.emit()

    def update_gui(self):
        self.updating_gui_bool = True

        # TODO: Implementing this again
        """
        if wbd.wbd_global.active_view == wbd.wbd_global.ViewEnum.diary:
            new_font: QtGui.QFont = self.title_qll.font()
            new_font.setUnderline(True)
        else:
            new_font: QtGui.QFont = self.title_qll.font()
            new_font.setUnderline(False)
        self.title_qll.setFont(new_font)
        """

        # Filters
        # ..tags
        self.tag_filter_qcb.setChecked(wbd.wbd_global.active_state.filters.tag_active_bool)
        if wbd.wbd_global.active_state.filters.tag_id_int != wbd.wbd_global.NO_ACTIVE_TAG_INT:
            filter_tag = wbd.model.TagM.get(wbd.wbd_global.active_state.filters.tag_id_int)
            self.tag_name_qll.setText(filter_tag.title_str)
        # ..rating
        self.rating_filter_qcb.setChecked(wbd.wbd_global.active_state.filters.rating_active_bool)
        self.rating_filter_qsr.setValue(wbd.wbd_global.active_state.filters.rating_int)
        # ..search
        self.search_filter_qcb.setChecked(wbd.wbd_global.active_state.filters.search_active_bool)
        self.search_qle.setText(wbd.wbd_global.active_state.filters.search_term_str)
        # ..date
        self.date_filter_qcb.setChecked(wbd.wbd_global.active_state.filters.datetime_active_bool)
        start_qtdate = QtCore.QDate.fromString(
            wbd.wbd_global.active_state.filters.start_datetime_string,
            wbd.wbd_global.QT_DATE_ONLY_FORMAT_STR
        )
        self.start_date_qde.setDate(start_qtdate)
        end_qtdate = QtCore.QDate.fromString(
            wbd.wbd_global.active_state.filters.end_datetime_string,
            wbd.wbd_global.QT_DATE_ONLY_FORMAT_STR
        )
        self.start_date_qde.setDate(end_qtdate)
        """
        start_pydatetime = datetime.datetime.strptime(
            wbd.wbd_global.active_state.filters.start_datetime_string,
            wbd.wbd_global.PY_DATETIME_FORMAT_STR
        )
        """

        self.presets_qlw.update_gui()

        """        
        self.presets_qlw.clear()
        for filter_preset in wbd.model.FilterPresetM.get_all():
            self.presets_qlw.addItem(filter_preset.title_str)
        """

        self.updating_gui_bool = False


class HLine(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.show()

