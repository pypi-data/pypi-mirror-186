import logging
import datetime
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui
import wbd.wbd_global
import wbd.model

ALL_DAY_STR = "[all day]"


class EntryDatetimeSelectionCw(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.updating_gui_bool = False

        self.vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbox_l2)

        now_today_yesterday_hbox_l3 = QtWidgets.QHBoxLayout()
        self.vbox_l2.addLayout(now_today_yesterday_hbox_l3)
        self.now_qpb = QtWidgets.QPushButton("Now")
        self.now_qpb.clicked.connect(self.on_now_clicked)
        now_today_yesterday_hbox_l3.addWidget(self.now_qpb)
        self.today_qpb = QtWidgets.QPushButton("Today")
        self.today_qpb.clicked.connect(self.on_today_clicked)
        now_today_yesterday_hbox_l3.addWidget(self.today_qpb)
        self.yesterday_qpb = QtWidgets.QPushButton("Yesterday")
        self.yesterday_qpb.clicked.connect(self.on_yesterday_clicked)
        now_today_yesterday_hbox_l3.addWidget(self.yesterday_qpb)

        self.date_qde = QtWidgets.QDateEdit()
        self.date_qde.setCalendarPopup(True)
        self.date_qde.dateChanged.connect(self.on_date_changed)
        self.vbox_l2.addWidget(self.date_qde)

        self.all_day_qcb = QtWidgets.QCheckBox("All Day")
        self.all_day_qcb.toggled.connect(self.on_all_day_toggled)
        self.all_day_qcb.setChecked(True)
        self.vbox_l2.addWidget(self.all_day_qcb)

        hbox_l3 = QtWidgets.QHBoxLayout()
        self.vbox_l2.addLayout(hbox_l3)

        vbox_l4 = QtWidgets.QVBoxLayout()
        hbox_l3.addLayout(vbox_l4)

        self.hour_of_day_qsr = QtWidgets.QSlider()
        self.hour_of_day_qsr.setOrientation(QtCore.Qt.Horizontal)
        self.hour_of_day_qsr.setMinimum(0)
        self.hour_of_day_qsr.setMaximum(23)
        self.hour_of_day_qsr.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.hour_of_day_qsr.setTickInterval(6)
        self.hour_of_day_qsr.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum
        )
        self.hour_of_day_qsr.valueChanged.connect(self.on_hour_slider_changed)
        vbox_l4.addWidget(self.hour_of_day_qsr)

        self.minute_qsr = QtWidgets.QSlider()
        self.minute_qsr.setOrientation(QtCore.Qt.Horizontal)
        self.minute_qsr.setMinimum(0)
        self.minute_qsr.setMaximum(11)
        self.minute_qsr.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.minute_qsr.setTickInterval(3)
        self.minute_qsr.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum
        )
        self.minute_qsr.valueChanged.connect(self.on_minute_slider_changed)
        vbox_l4.addWidget(self.minute_qsr)

        self.time_of_day_qll = QtWidgets.QLabel()
        hbox_l3.addWidget(self.time_of_day_qll)
        self.time_of_day_qll.setFixedWidth(80)

    def on_hour_slider_changed(self, i_value: int):
        if self.updating_gui_bool:
            return
        # qtime = QtCore.QTime(i_value, 0)

        self.all_day_qcb.setChecked(False)
        # self.time_of_day_qte.setTime(qtime)
        self.update_db_datetime()
        self.update_gui()

    def on_minute_slider_changed(self, i_value: int):
        if self.updating_gui_bool:
            return
        # qtime = QtCore.QTime(i_value, 0)

        self.all_day_qcb.setChecked(False)
        # self.time_of_day_qte.setTime(qtime)
        self.update_db_datetime()
        self.update_gui()

    def on_all_day_toggled(self):
        if self.updating_gui_bool or wbd.wbd_global.active_state.is_entries_empty():
            return
        self.update_db_datetime()
        self.update_gui()

    def get_minute_from_slider(self) -> int:
        return self.minute_qsr.value() * 5

    def on_date_changed(self):
        if self.updating_gui_bool:
            return
        self.update_db_datetime()

    def update_db_datetime(self):
        datetime_str = self.get_datetime_string_from_widgets()
        logging.debug("qdatetime = " + datetime_str)
        wbd.model.EntryM.update_datetime(
            wbd.wbd_global.active_state.last_entry(),
            datetime_str
        )

    def on_now_clicked(self):
        #pydatetime = datetime.datetime.today()
        pydatetime = datetime.datetime.now()
        wbd.model.EntryM.update_datetime(
            wbd.wbd_global.active_state.last_entry(),
            pydatetime.strftime(wbd.wbd_global.PY_DATETIME_FORMAT_STR)
        )
        self.update_gui()

    def on_today_clicked(self):
        pydatetime = datetime.datetime.today()
        wbd.model.EntryM.update_datetime(
            wbd.wbd_global.active_state.last_entry(),
            pydatetime.strftime(wbd.wbd_global.PY_DATE_ONLY_FORMAT_STR)
        )
        self.update_gui()

    def on_yesterday_clicked(self):
        pydatetime = datetime.datetime.today()
        pydatetime = pydatetime - datetime.timedelta(1)
        wbd.model.EntryM.update_datetime(
            wbd.wbd_global.active_state.last_entry(),
            pydatetime.strftime(wbd.wbd_global.PY_DATE_ONLY_FORMAT_STR)
        )
        self.update_gui()

    """
    def update_times(self, i_yesterday: bool=False):
        qdatetime = QtCore.QDateTime.currentDateTime()
        if i_yesterday:
            qdatetime = qdatetime.addDays(-1)
        active_qtime: QtCore.QTime = qdatetime.time()
        active_qdate: QtCore.QDate = qdatetime.date()
        # self.hour_of_day_qsr.setValue(active_qtime.hour())
        # -the label will be automatically updated when setValue is called
        self.date_qde.setDate(active_qdate)
    """

    def get_datetime_string_from_widgets(self) -> str:
        qdatetime = QtCore.QDateTime()
        qdatetime.setDate(self.date_qde.date())

        if self.all_day_qcb.isChecked():
            ret_string = qdatetime.toString(wbd.wbd_global.QT_DATE_ONLY_FORMAT_STR)
        else:
            qtime = QtCore.QTime()
            hour_int = self.hour_of_day_qsr.value()
            minute_int = self.get_minute_from_slider()
            qtime.setHMS(hour_int, minute_int, 0)
            qdatetime.setTime(qtime)
            ret_string = qdatetime.toString(wbd.wbd_global.QT_DATETIME_FORMAT_STR)

        return ret_string

    def update_gui(self):
        diary_entry = wbd.model.EntryM.get(wbd.wbd_global.active_state.last_entry())
        if diary_entry.is_all_day():
            qdate = QtCore.QDate.fromString(diary_entry.datetime_added_str, wbd.wbd_global.QT_DATE_ONLY_FORMAT_STR)
            self.date_qde.setDate(qdate)
            self.hour_of_day_qsr.setValue(0)
            self.minute_qsr.setValue(0)
            self.time_of_day_qll.setText(ALL_DAY_STR)
        else:
            qdatetime = QtCore.QDateTime.fromString(diary_entry.datetime_added_str,
                wbd.wbd_global.QT_DATETIME_FORMAT_STR)
            self.date_qde.setDate(qdatetime.date())

            hour_int = qdatetime.time().hour()
            self.hour_of_day_qsr.setValue(hour_int)

            minute_int = qdatetime.time().minute()
            self.minute_qsr.setValue(minute_int // 5)

            hour_formatted_str = str(hour_int).zfill(2) + ":" + str(minute_int).zfill(2)
            self.time_of_day_qll.setText(hour_formatted_str)
        self.all_day_qcb.setChecked(diary_entry.is_all_day())
        # self.time_of_day_qte.setTime(qdatetime.time())

