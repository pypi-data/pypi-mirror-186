import datetime
import time
import logging
import re
import webbrowser
import smtplib
import email.message
# import envelopes
import os
import subprocess
import typing
import wbd.model
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets
from wbd import wbd_global
import wbd.gui.email_uname_and_pw_dlg

# -possible to use an svg file here instead?
NO_ENTRY_CLICKED_INT = -1


class DiaryEntriesCw(QtWidgets.QWidget):
    """
    Inspiration for this class:
    http://stackoverflow.com/questions/20041385/python-pyqt-setting-scroll-area
    """

    context_menu_delete_signal = QtCore.Signal()
    context_menu_email_share_signal = QtCore.Signal(int)
    diary_entry_edit_signal = QtCore.Signal(int)

    last_entry_clicked_id_int = NO_ENTRY_CLICKED_INT

    def __init__(self):
        super().__init__()

        """
        self.setSizePolicy(
            self.sizePolicy().horizontalPolicy(),
            QtWidgets.QSizePolicy.MinimumExpanding
        )
        """

        self.vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbox_l2)
        self.scroll_area_w3 = QtWidgets.QScrollArea()
        self.scroll_area_w3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_area_w3.setWidgetResizable(True)
        self.scroll_area_w3.verticalScrollBar().rangeChanged.connect(self.move_scrollbar_to_bottom)
        self.scroll_list_w4 = QtWidgets.QWidget()
        """
        BACKGROUND_IMAGE_PATH_STR = "Gerald-G-Yoga-Poses-stylized-1-300px-CC0.png"
        MY_WIDGET_NAME_STR = "test-name"
        self.scroll_list_w4.setObjectName(MY_WIDGET_NAME_STR)
        self.scroll_list_w4.setStyleSheet(
            "#" + MY_WIDGET_NAME_STR + "{" + "background-image:url(\"" + wbd.wbd_global.background_image_path
            + "\"); background-position:center; background-repeat:no-repeat" + "}")
        """
        self.scroll_list_vbox_l5 = QtWidgets.QVBoxLayout()

        self.scroll_list_w4.setLayout(self.scroll_list_vbox_l5)
        self.scroll_area_w3.setWidget(self.scroll_list_w4)
        self.vbox_l2.addWidget(self.scroll_area_w3)

        self.right_click_menu = None

    def move_scrollbar_to_bottom(self, i_min_unused: int, i_max: int):
        # -we must wait for rangeChange (the signal that this method is connected to) before calling setValue
        self.scroll_area_w3.verticalScrollBar().setValue(i_max)

    # The same function is used for all the "rows" and we send the id with the signal so we know which entry
    def on_custom_label_mouse_pressed(self, i_qmouseevent: QtGui.QMouseEvent, i_diary_id: int):
        logging.debug("button clicked: " + str(i_qmouseevent.button()))
        logging.debug("diary id: " + str(i_diary_id))
        self.last_entry_clicked_id_int = i_diary_id  # -used for the right click (context menu events)
        if i_qmouseevent.button() == QtCore.Qt.LeftButton:
            self.diary_entry_edit_signal.emit(i_diary_id)

    # Overridden - Docs: http://doc.qt.io/qt-5/qwidget.html#contextMenuEvent
    def contextMenuEvent(self, i_qcontextmenuevent):
        self.right_click_menu = QtWidgets.QMenu()

        email_share_action = QtGui.QAction("Share via email")
        email_share_action.triggered.connect(self.on_context_menu_email_share)
        self.right_click_menu.addAction(email_share_action)

        diaspora_share_action = QtGui.QAction("Share on Diaspora (experimental)")
        diaspora_share_action.triggered.connect(self.on_context_menu_diaspora_share)
        self.right_click_menu.addAction(diaspora_share_action)

        copy_action = QtGui.QAction("Copy diary text")
        copy_action.triggered.connect(self.on_context_menu_copy)
        self.right_click_menu.addAction(copy_action)

        edit_action = QtGui.QAction("Edit diary text")
        edit_action.triggered.connect(self.on_context_menu_edit)
        self.right_click_menu.addAction(edit_action)

        delete_action = QtGui.QAction("Delete")
        delete_action.triggered.connect(self.on_context_menu_delete)
        self.right_click_menu.addAction(delete_action)

        self.right_click_menu.exec_(QtGui.QCursor.pos())

    def on_context_menu_delete(self):
        message_box_reply = QtWidgets.QMessageBox.question(
            self, "Remove diary entry?", "Are you sure that you want to remove this diary entry?"
        )
        if message_box_reply == QtWidgets.QMessageBox.Yes:
            wbd.model.EntryM.remove(self.last_entry_clicked_id_int)
            self.context_menu_delete_signal.emit()
        else:
            pass  # -do nothing

    def on_context_menu_edit(self):
        self.diary_entry_edit_signal.emit(self.last_entry_clicked_id_int)

    def on_context_menu_copy(self):
        diary_entry = wbd.model.EntryM.get(self.last_entry_clicked_id_int)
        tag_list = wbd.model.get_all_tags_referenced_by_entry(self.last_entry_clicked_id_int)
        tag_title_list = [tag.title_str for tag in tag_list]
        tags_str = ", ".join(tag_title_list)

        qclipboard = QtGui.QGuiApplication.clipboard()
        qclipboard.setText(diary_entry.diary_text_str + "\n\n" + tags_str)

    def on_context_menu_email_share(self):
        self.context_menu_email_share_signal.emit(self.last_entry_clicked_id_int)

    def on_context_menu_diaspora_share(self):
        diary_entry = wbd.model.EntryM.get(self.last_entry_clicked_id_int)
        pydatetime = datetime.datetime.fromtimestamp(diary_entry.datetime_added_str)
        date_formatted_str = pydatetime.strftime("%Y-%m-%d")
        title_str = "Diary Entry for " + date_formatted_str
        diary_entry_str = diary_entry.diary_text_str
        tag_list: typing.List[wbd.model.TagM] = wbd.model.get_all_tags_referenced_by_entry(self.last_entry_clicked_id_int)
        tag_title_list = [tag.title_str for tag in tag_list]
        # "#" +
        tags_str = ", ".join(tag_title_list)
        share_url_str = "https://share.diasporafoundation.org/?title={title}&url={url}".format(
            title=title_str,
            url=diary_entry_str + " --- Tags: " + tags_str
        )
        logging.debug("share_url_str = " + str(share_url_str))
        webbrowser.open(share_url_str)

    def update_gui(self, i_diary_entry_list: typing.List[wbd.model.EntryM]):
        wbd.wbd_global.clear_widget_and_layout_children(self.scroll_list_vbox_l5)
        old_date_str = ""
        for diary_entry in i_diary_entry_list:
            entry_w6 = CustomEntryWidget(diary_entry.id)
            entry_w6.mouse_pressed_signal.connect(self.on_custom_label_mouse_pressed)
            self.scroll_list_vbox_l5.addWidget(entry_w6)

            if diary_entry.id == self.last_entry_clicked_id_int:
                entry_w6.setStyleSheet("background-color: yellow")

            entry_hbox_l7 = QtWidgets.QHBoxLayout()
            entry_w6.setLayout(entry_hbox_l7)

            # Left side (date and time)..

            if diary_entry.is_all_day():
                entry_datetime_pdt = datetime.datetime.strptime(
                    diary_entry.datetime_added_str,
                    wbd.wbd_global.PY_DATE_ONLY_FORMAT_STR
                )
            else:
                entry_datetime_pdt = datetime.datetime.strptime(
                    diary_entry.datetime_added_str,
                    wbd.wbd_global.PY_DATETIME_FORMAT_STR
                )

            # ..date
            left_w8 = QtWidgets.QWidget()
            entry_hbox_l7.addWidget(
                left_w8,
                alignment=QtCore.Qt.AlignTop,
                stretch=3
            )
            left_vbox_l9 = QtWidgets.QVBoxLayout()
            left_w8.setLayout(left_vbox_l9)

            date_string_format_str = "%A"  # -weekday
            if entry_datetime_pdt.year != datetime.datetime.now().year:
                date_string_format_str = "%-d %b %Y"  # - 12 jun 2018
            elif entry_datetime_pdt < datetime.datetime.now() - datetime.timedelta(weeks=1):
                date_string_format_str = "%-d %b"  # - 12 jun
            date_str = entry_datetime_pdt.strftime(date_string_format_str)

            if old_date_str == date_str:
                date_text_str = ""
            elif entry_datetime_pdt.date() == datetime.datetime.today().date():
                date_text_str = "Today"
            else:
                date_text_str = date_str
            old_date_str = date_str

            date_qlabel = QtWidgets.QLabel(date_text_str)
            new_font: QtGui.QFont = date_qlabel.font()
            new_font.setUnderline(True)
            date_qlabel.setFont(new_font)
            left_vbox_l9.addWidget(date_qlabel)

            # ..time
            if diary_entry.is_all_day():
                time_text_str = ""
            else:
                time_text_str = entry_datetime_pdt.strftime("%H:%M")

            # TODO: Removing newline at beginning - date_and_time_text_str.rstrip()

            time_qlabel = QtWidgets.QLabel(time_text_str)
            left_vbox_l9.addWidget(time_qlabel)

            entry_hbox_l7.addWidget(VLine())

            # Center..
            vbox_l8 = QtWidgets.QVBoxLayout()
            entry_hbox_l7.addLayout(vbox_l8, stretch=18)

            # ..image (top)

            if diary_entry.image_file_bytes is not None:
                image_qll = QtWidgets.QLabel()
                qpixmap = QtGui.QPixmap()
                qpixmap.loadFromData(diary_entry.image_file_bytes)
                # -documentation: http://doc.qt.io/qt-5/qpixmap.html#loadFromData-1
                image_qll.setPixmap(qpixmap)
                # image_qll.setScaledContents(True)
                # wbd.wbd_global.resize_image(image_qll, 200)
                vbox_l8.addWidget(image_qll)
                # image_qll.mouseReleaseEvent().mouse_pressed_signal.connect(self.on_custom_label_mouse_pressed)

            # ..text (vertical center)

            diary_text_str = diary_entry.diary_text_str.strip()

            # http://doc.qt.io/qt-5/richtext-html-subset.html
            if wbd.wbd_global.active_state.filters.search_active_bool:
                diary_text_str_possibly_with_bold = re.sub(
                    "(" + wbd.wbd_global.active_state.filters.search_term_str + ")",
                    r"<b>\1</b>",
                    diary_text_str,
                    flags=re.IGNORECASE
                )
            else:
                diary_text_str_possibly_with_bold = diary_text_str
            html_text_line_str = (
                '<p style="white-space: pre-wrap; font-size: ' + str(wbd_global.get_diary_font_size()) + 'pt;">'
                + diary_text_str_possibly_with_bold
                + '</p>'
            )
            diary_text_qll = QtWidgets.QLabel(html_text_line_str)
            diary_text_qll.setWordWrap(True)
            vbox_l8.addWidget(diary_text_qll)

            # ..tags (bottom)

            separator_str = ", "
            tags_qll = QtWidgets.QLabel()
            tags_for_entry_list = wbd.model.get_all_tags_referenced_by_entry(diary_entry.id)
            tag_string_str = ""
            count_int = 0
            for tag in tags_for_entry_list:
                tag_string_str += '<span style="background-color:white">' + tag.title_str
                if count_int < len(tags_for_entry_list) -1:
                    tag_string_str += separator_str
                tag_string_str += "</span>"
                count_int += 1
            # temporary = tag_string_str.rsplit(separator_str, 1)
            # tag_string_str = "".join(temporary)
            # -this is a trick inspired by this answer: https://stackoverflow.com/a/2556252/2525237
            tags_qll.setText(tag_string_str)
            vbox_l8.addWidget(tags_qll)

            # Right side (rating)

            rating_int = diary_entry.rating_int
            entry_hbox_l7.addWidget(
                QtWidgets.QLabel(str(rating_int)),
                alignment=QtCore.Qt.AlignTop,
                stretch=1
            )

            entry_w6.install_event_filter()

        self.scroll_list_vbox_l5.addStretch()


class CustomEntryWidget(QtWidgets.QWidget):
    diary_entry_id = wbd_global.NO_DIARY_ENTRY_EDITING_INT
    mouse_pressed_signal = QtCore.Signal(QtGui.QMouseEvent, int)

    def __init__(self, i_diary_entry_id: int):
        super().__init__()
        self.diary_entry_id = i_diary_entry_id

    """
    def mousePressEvent(self, i_qmouseevent):
        super().mousePressEvent(i_qmouseevent)
        logging.debug("======== CustomWidget - mousePressEvent ========")
        self.mouse_pressed_signal.emit(i_qmouseevent, self.diary_entry_id)
    """

    def eventFilter(self, QObject_watched, qevent: QtCore.QEvent):
        # logging.debug("======== CustomWidget - eventFilter ========")
        if qevent.type() == QtCore.QEvent.MouseButtonPress:
            logging.debug("======== CustomWidget - QtCore.QEvent.MouseButtonPress ========")
            self.mouse_pressed_signal.emit(qevent, self.diary_entry_id)
        return super().eventFilter(QObject_watched, qevent)

    def install_event_filter(self):
        for widget in self.findChildren(QtWidgets.QWidget) + [self]:
            widget.installEventFilter(self)


class VLine(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameShape(QtWidgets.QFrame.VLine)
        self.setLineWidth(4)
        self.setFixedWidth(12)
        self.setStyleSheet("color: #bbbbbb")
        self.setContentsMargins(0, 0, 8, 0)
        # cccccc
        # 000000
