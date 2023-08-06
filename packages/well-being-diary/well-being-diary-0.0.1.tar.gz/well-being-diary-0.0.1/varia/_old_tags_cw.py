from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6 import QtCore
import wbd.model
import wbd.wbd_global
import varia._old_details


class TagsCw(QtWidgets.QWidget):
    # search_text_changed_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()

        self.updating_gui_bool = False

        # self.setMaximumWidth(240)

        vbox1 = QtWidgets.QVBoxLayout()
        self.setLayout(vbox1)

        self.setMinimumWidth(150)

        self.tags_qlw = QtWidgets.QListWidget()
        for journal in wbd.model.TagM.get_all():
            self.tags_qlw.addItem(journal.title_str)
        self.tags_qlw.currentRowChanged.connect(self.tag_row_changed)
        vbox1.addWidget(self.tags_qlw)

        self.details_cw = varia._old_details.CompositeDetailsWidget()
        vbox1.addWidget(self.details_cw)

        self.update_gui()

    def tag_row_changed(self, i_current_row: int):
        tag_item = self.tags_qlw.item(i_current_row)
        journal_text_str = tag_item.text()
        journal_text_edited_str = wbd.wbd_global.format_to_hashtag(journal_text_str)

        wbd.wbd_global.active_tag_id_int = 1
        # TODO: wbd.wbd_global.active_tag_id_it =

        # TODO: Do we want to update the search view?
        # self.search_qle.setText(journal_text_edited_str)
        # self.search_view_qrb.setChecked(True)

    def on_tags_current_row_changed(self, i_search_text: str):
        self.search_qle.setText(i_search_text)

    def update_gui(self):
        self.updating_gui_bool = True

        self.updating_gui_bool = False


class CustomQLabel(QtWidgets.QLabel):
    NO_DIARY_ENTRY_SELECTED = -1
    tag_entry_id = NO_DIARY_ENTRY_SELECTED  # -"static"
    mouse_pressed_signal = QtCore.Signal(QtGui.QMouseEvent, int)

    def __init__(self, i_text_sg, i_diary_entry_id=NO_DIARY_ENTRY_SELECTED):
        super().__init__(i_text_sg)
        self.tag_entry_id = i_diary_entry_id

    # Overridden
    # Please note that this is the event handler (not an event!)
    def mousePressEvent(self, i_qmouseevent):
        super(CustomQLabel, self).mousePressEvent(i_qmouseevent)
        # -self is automatically sent as the 1st argument
        self.mouse_pressed_signal.emit(i_qmouseevent, self.tag_entry_id)

