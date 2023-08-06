import logging
import wbd.model
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui
import wbd.wbd_global
import wbd.gui.safe_confirmation_dlg
import wbd.gui.list_widget
from wbd.wbd_global import EventSource

NO_POS_SET_INT = -1


class TagsCw(QtWidgets.QWidget):
    current_row_changed_signal = QtCore.Signal(int, bool, bool)
    add_tag_for_entry_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()

        vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_l2)

        self.edit_dialog = None

        # Creating widgets

        hbox_l3 = QtWidgets.QHBoxLayout()
        vbox_l2.addLayout(hbox_l3)

        # ..for views and groups
        vbox_l4 = QtWidgets.QVBoxLayout()
        hbox_l3.addLayout(vbox_l4)

        self.views_qll = QtWidgets.QLabel("Views")
        vbox_l4.addWidget(self.views_qll)
        self.views_clw = wbd.gui.list_widget.ListWidget(wbd.model.ViewM)
        self.views_clw.current_row_changed_signal.connect(self.on_collection_row_changed)
        new_font = self.views_clw.font()
        new_font.setPointSize(12)
        self.views_clw.setFont(new_font)
        vbox_l4.addWidget(self.views_clw)

        """
        self.groups_qll = QtWidgets.QLabel("Groups")
        vbox_l4.addWidget(self.groups_qll)
        self.groups_clw = wbd.gui.list_widget.ListWidget(wbd.model.GroupM)
        # -TODO: Updating this
        self.groups_clw.current_row_changed_signal.connect(self.on_collection_row_changed)
        new_font = self.groups_clw.font()
        new_font.setPointSize(12)
        self.groups_clw.setFont(new_font)
        vbox_l4.addWidget(self.groups_clw)
        """

        hbox_l5 = QtWidgets.QHBoxLayout()
        vbox_l4.addLayout(hbox_l5)
        self.adding_new_view_qle = QtWidgets.QLineEdit()
        self.adding_new_view_qle.setPlaceholderText("New view")
        hbox_l5.addWidget(self.adding_new_view_qle)
        self.adding_new_view_qpb = QtWidgets.QPushButton("Add")
        self.adding_new_view_qpb.clicked.connect(self.on_add_new_view_button_pressed)
        hbox_l5.addWidget(self.adding_new_view_qpb)

        self.collection_tags_clw = wbd.gui.list_widget.ListWidget(wbd.model.TagInsideViewM)
        # functools.partial(wbd.model.get_all_tags_for_view, )
        self.collection_tags_clw.current_row_changed_signal.connect(self.on_collection_tags_current_row_changed)
        # self.tag_view_clw.addItems(["Connection", "Peace", "Safety", "To be seen", "Kindness", "Caring"])
        vbox_l4.addWidget(self.collection_tags_clw)

        # ..for list items (tags)
        vbox_l4 = QtWidgets.QVBoxLayout()
        hbox_l3.addLayout(vbox_l4)

        self.sort_qcb = QtWidgets.QComboBox()
        self.sort_qcb.addItems([
            wbd.wbd_global.SortType.sort_by_name.name,
            wbd.wbd_global.SortType.sort_by_frequency.name,
            wbd.wbd_global.SortType.sort_by_time.name
        ])
        self.sort_qcb.activated.connect(self.on_sort_activated)
        vbox_l4.addWidget(self.sort_qcb)

        """
        OLD:
        self.all_tags_clw = CustomListWidget()
        self.all_tags_clw.currentRowChanged.connect(self.on_all_tags_current_row_changed)
        vbox_l4.addWidget(self.all_tags_clw)
        """

        self.all_tags_clw = wbd.gui.list_widget.ListWithOrderWidget(wbd.model.TagM)  #### CustomListWidget()
        self.all_tags_clw.current_row_changed_signal.connect(self.on_all_tags_current_row_changed)
        vbox_l4.addWidget(self.all_tags_clw)

        # self.all_tags_clw.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        # self.list_qlw.setDragEnabled(True)
        # self.all_tags_clw.drop_signal.connect(self.update_db_sort_order_for_all_rows)
        # vbox_l2.addWidget(self.all_tags_clw, stretch=7)
        # self.list_widget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        # self.list_widget.itemPressed.connect(self.on_item_selection_changed)
        # -itemClicked didn't work, unknown why (it worked on the first click but never when running in debug mode)
        # -currentItemChanged cannot be used here since it is activated before the list of selected items is updated

        # ..for adding a new list item
        hbox_l3 = QtWidgets.QHBoxLayout()
        vbox_l2.addLayout(hbox_l3)
        self.adding_new_item_qle = QtWidgets.QLineEdit()
        self.adding_new_item_qle.setPlaceholderText("New tag")
        hbox_l3.addWidget(self.adding_new_item_qle)
        self.adding_new_item_qpb = QtWidgets.QPushButton("Add")
        self.adding_new_item_qpb.clicked.connect(self.on_add_new_tag_button_pressed)
        hbox_l3.addWidget(self.adding_new_item_qpb)

        hbox_l3 = QtWidgets.QHBoxLayout()
        vbox_l2.addLayout(hbox_l3)
        self.edit_texts_qpb = QtWidgets.QPushButton()
        self.edit_texts_qpb.setIcon(QtGui.QIcon(wbd.wbd_global.get_icon_path("pencil-2x.png")))
        self.edit_texts_qpb.setToolTip("Edit")
        self.edit_texts_qpb.clicked.connect(self.show_edit_dialog)
        hbox_l3.addWidget(self.edit_texts_qpb)

        hbox_l3.addStretch(1)

        self.delete_phrase_qpb = QtWidgets.QPushButton()
        self.delete_phrase_qpb.setIcon(QtGui.QIcon(wbd.wbd_global.get_icon_path("trash-2x.png")))
        self.delete_phrase_qpb.setToolTip(self.tr("Delete"))
        self.delete_phrase_qpb.clicked.connect(self.delete_item)
        hbox_l3.addWidget(self.delete_phrase_qpb)

        hbox_l3 = QtWidgets.QHBoxLayout()
        vbox_l2.addLayout(hbox_l3)
        self.add_for_entry_qpb = QtWidgets.QPushButton("Add for entry")
        self.add_for_entry_qpb.clicked.connect(self.on_add_for_entry_clicked)
        hbox_l3.addWidget(self.add_for_entry_qpb)
        self.add_tag_to_view_qpb = QtWidgets.QPushButton("Add to view")
        self.add_tag_to_view_qpb.clicked.connect(self.on_add_tag_to_view_clicked)
        hbox_l3.addWidget(self.add_tag_to_view_qpb)
        self.remove_tag_from_view_qpb = QtWidgets.QPushButton("Remove from view")
        self.remove_tag_from_view_qpb.clicked.connect(self.on_remove_tag_from_view_clicked)
        hbox_l3.addWidget(self.remove_tag_from_view_qpb)

        self.details_or_empty_sw = QtWidgets.QStackedWidget()
        self.details_or_empty_sw.setFixedHeight(210)
        vbox_l2.addWidget(self.details_or_empty_sw)
        # , stretch=5

        self.details_cw = CompositeDetailsWidget()
        # vbox_l2.addWidget(self.details_cw, stretch=5)
        self.details_cw_int = self.details_or_empty_sw.addWidget(self.details_cw)
        self.empty_details_qll = QtWidgets.QLabel("No tag selected")
        self.empty_details_int = self.details_or_empty_sw.addWidget(self.empty_details_qll)

        self.all_tags_clw.update_gui()

    def on_sort_activated(self, i_index: int):
        logging.debug("i_index = " + str(i_index))
        self.update_gui(EventSource.all_tags_sort_type_changed)

    # Tag item buttons

    def on_search_box_text_changed(self):
        logging.debug("on_search_box_text_changed")
        # self.all_tags_clw.

    def on_add_tag_to_view_clicked(self):
        if (wbd.wbd_global.active_state.collection_id != wbd.wbd_global.NO_VIEW_ACTIVE_INT
        and wbd.wbd_global.active_state.tag_id != wbd.wbd_global.NO_ACTIVE_TAG_INT):
            wbd.model.add_view_tag_relation(wbd.wbd_global.active_state.collection_id, wbd.wbd_global.active_state.tag_id)
        self.update_gui(EventSource.add_tag_to_view)

    def on_remove_tag_from_view_clicked(self):
        if (wbd.wbd_global.active_state.collection_id != wbd.wbd_global.NO_VIEW_ACTIVE_INT
        and wbd.wbd_global.active_state.tag_id != wbd.wbd_global.NO_ACTIVE_TAG_INT):
            wbd.model.remove_view_tag_relation(wbd.wbd_global.active_state.collection_id, wbd.wbd_global.active_state.tag_id)
        self.update_gui(EventSource.remove_tag_from_view)

    def on_add_for_entry_clicked(self):
        self.add_tag_for_entry_signal.emit()

    def delete_item(self):
        if wbd.wbd_global.active_state.tag_id != wbd.wbd_global.NO_ACTIVE_TAG_INT:
            active_tag = wbd.model.TagM.get(wbd.wbd_global.active_state.tag_id)
            conf_result_bool = wbd.gui.safe_confirmation_dlg.SafeConfirmationDlg.get_safe_confirmation_dialog(
                "Are you sure that you want to remove this entry?<br><i>Please type the name to confirm</i>",
                active_tag.title_str
            )
            if conf_result_bool:
                self.all_tags_clw.clearSelection()
                wbd.model.TagM.remove(wbd.wbd_global.active_state.tag_id)
                wbd.wbd_global.active_state.tag_id = wbd.wbd_global.NO_ACTIVE_TAG_INT
                self.current_row_changed_signal.emit(wbd.wbd_global.NO_ACTIVE_QUESTION_INT, False, False)
                self.update_gui(EventSource.tag_deleted)
        else:
            raise Exception("Should not be possible to get here")

    def on_collection_row_changed(self, i_view_id: int):
        wbd.wbd_global.active_state.collection_id = i_view_id
        # Updating the tag view list
        self.collection_tags_clw.clear()

        self.update_gui(wbd.wbd_global.EventSource.collection_changed)

    def on_collection_tags_current_row_changed(self, i_new_tag_id: int, i_ctrl_active: bool, i_shift_active: bool):
        #######wbd.wbd_global.active_state.tag_id = i_new_tag_id
        """
        current_row_int = self.view_tags_clw.currentRow()
        current_item_qli: QtWidgets.QListWidgetItem = self.view_tags_clw.item(current_row_int)
        if current_item_qli is not None:
            wbd.wbd_global.active_tag_id_int = int(current_item_qli.data(QtCore.Qt.UserRole))
            self.current_row_changed_signal.emit()
        """
        self.current_row_changed_signal.emit(i_new_tag_id, i_ctrl_active, i_shift_active)
        self.update_gui(EventSource.view_tags_tag_changed)

    def on_all_tags_current_row_changed(self, i_tag_id: int, i_ctrl_active: bool, i_shift_active: bool):
        # if current_row_int != NO_QUESTION_INT:
        # wbd.wbd_global.active_state.question_id = wbd.wbd_global.NO_ACTIVE_QUESTION_INT
        #######wbd.wbd_global.active_state.tag_id = i_tag_id

        current_row_int = self.all_tags_clw.currentRow()
        self.current_row_changed_signal.emit(i_tag_id, i_ctrl_active, i_shift_active)
        self.update_gui(wbd.wbd_global.EventSource.all_tags_tag_changed)

    def show_edit_dialog(self):
        if wbd.wbd_global.active_state.tag_id != wbd.wbd_global.NO_ACTIVE_TAG_INT:
            self.edit_dialog = EditDialog()
            self.edit_dialog.finished.connect(self.on_edit_dialog_finished)
            self.edit_dialog.show()

    def on_edit_dialog_finished(self, i_result: int):
        if i_result == QtWidgets.QDialog.Accepted:
            # assert mc.mc_global.active_phrase_id_it != wbd.wbd_global.NO_PHRASE_SELECTED_INT
            # question = wbd.model.QuestionM.get(wbd.wbd_global.active_question_id_it)
            title_text_str = self.edit_dialog.title_qle.text()
            wbd.model.TagM.update_title(wbd.wbd_global.active_state.tag_id, title_text_str)
            description_plain_text_str = self.edit_dialog.description_qpte.toPlainText()
            wbd.model.TagM.update_description(wbd.wbd_global.active_state.tag_id, description_plain_text_str)

        # Changing the title in the list
        # current_row_number_int = self.list_clw.currentRow()
        # self.update_row_item(current_row_number_int, current_row_number_int)

        self.all_tags_clw.update_gui()

        last_row_int = self.all_tags_clw.count() - 1
        self.all_tags_clw.setCurrentRow(last_row_int)

        self.update_gui(EventSource.tag_edited)

    def on_add_new_view_button_pressed(self):
        text_sg = self.adding_new_view_qle.text().strip()  # strip is needed to remove a newline at the end (why?)
        if not (text_sg and text_sg.strip()):
            return
        wbd.wbd_global.active_state.collection_id = wbd.model.ViewM.add(text_sg)

        self.adding_new_view_qle.clear()
        self.update_gui(EventSource.view_added)

    def on_add_new_tag_button_pressed(self):
        text_sg = self.adding_new_item_qle.text().strip()  # strip is needed to remove a newline at the end (why?)
        if not (text_sg and text_sg.strip()):
            return
        wbd.wbd_global.active_state.tag_id = wbd.model.TagM.add(text_sg, "")

        self.adding_new_item_qle.clear()
        self.update_gui(EventSource.tag_added)

        self.show_edit_dialog()

    def update_gui(self, i_event_source: wbd.wbd_global.EventSource):
        outside_event_sources_list = [
            EventSource.application_start, EventSource.entry_area_close, EventSource.image_import,
            EventSource.importing, EventSource.entry_suggested_tags_tag_changed
        ]

        # Views
        if i_event_source in outside_event_sources_list + [EventSource.view_added]:
            #####view_list: typing.List[wbd.model.ViewM] = wbd.model.ViewM.get_all()
            self.views_clw.update_gui()

        # View tags
        if i_event_source in outside_event_sources_list + [EventSource.collection_changed,
            EventSource.tag_deleted, EventSource.tag_added, EventSource.add_tag_to_view,
            EventSource.remove_tag_from_view, EventSource.tag_edited, EventSource.view_added]:

            self.collection_tags_clw.update_gui()

            """
            view_tag_and_sort_order_list: typing.List[typing.Tuple[wbd.model.TagM, int]] = (
                wbd.model.get_all_tags_in_collection(wbd.wbd_global.active_state.collection_id)
            )
            self.view_tags_clw.clear()
            for (view_tag, sort_order_int) in view_tag_and_sort_order_list:
                new_item = QtWidgets.QListWidgetItem(view_tag.title_str)
                new_item.setData(QtCore.Qt.UserRole, view_tag.id_int)
                self.view_tags_clw.addItem(new_item)
            """

        # All tags
        if i_event_source in outside_event_sources_list + [
        EventSource.tag_deleted, EventSource.tag_added,
        EventSource.tag_edited, EventSource.all_tags_sort_type_changed]:
            current_index_int = self.sort_qcb.currentIndex()
            sort_type_enum = wbd.wbd_global.SortType(current_index_int)
            self.all_tags_clw.update_gui(sort_type_enum)

        # Details
        if i_event_source in outside_event_sources_list + [
            EventSource.all_tags_tag_changed,
            EventSource.view_tags_tag_changed, EventSource.tag_deleted, EventSource.tag_added,
            EventSource.add_tag_to_view, EventSource.remove_tag_from_view, EventSource.tag_edited,
            EventSource.tag_added_for_entry, EventSource.entry_selected_tag_changed]:
            if wbd.wbd_global.active_state.tag_id == wbd.wbd_global.NO_ACTIVE_TAG_INT:
                self.details_or_empty_sw.setCurrentIndex(self.empty_details_int)
            else:
                self.details_or_empty_sw.setCurrentIndex(self.details_cw_int)
                self.details_cw.update_gui()


class EditDialog(QtWidgets.QDialog):
    """
    Inspiration: Answer by lou here:
    https://stackoverflow.com/questions/18196799/how-can-i-show-a-pyqt-modal-dialog-and-get-data-out-of-its-controls-once-its-clo
    """
    SPACING_INT = 20

    def __init__(self, i_parent=None):
        super().__init__(i_parent)

        self.setModal(True)

        self.setMinimumWidth(400)
        self.setMinimumHeight(600)

        vbox_l1 = QtWidgets.QVBoxLayout(self)
        self.setLayout(vbox_l1)

        vbox_l1.addWidget(QtWidgets.QLabel(self.tr("Title")))
        self.title_qle = QtWidgets.QLineEdit()
        vbox_l1.addWidget(self.title_qle)
        vbox_l1.addSpacing(SPACING_INT)

        hbox_l2 = QtWidgets.QHBoxLayout()
        vbox_l1.addLayout(hbox_l2)
        self.friend_qcb = QtWidgets.QCheckBox("Friend?")
        self.friend_qcb.toggled.connect(self.on_friend_email_toggled)
        hbox_l2.addWidget(self.friend_qcb)
        self.friend_email_qle = QtWidgets.QLineEdit()
        self.friend_email_qle.textChanged.connect(self.on_friend_email_text_changed)
        hbox_l2.addWidget(self.friend_email_qle)

        vbox_l1.addWidget(QtWidgets.QLabel(self.tr("Description")))
        self.description_qpte = QtWidgets.QPlainTextEdit()
        self.description_qpte.setPlaceholderText("Please enter a description")
        vbox_l1.addWidget(self.description_qpte)

        vbox_l1.addSpacing(SPACING_INT)

        self.button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal,
            self
        )
        vbox_l1.addWidget(self.button_box)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        # -accept and reject are "slots" built into Qt

        self.update_gui()

    def on_friend_email_text_changed(self):
        if self.updating_gui_bool:
            return
        new_text_str = self.friend_email_qle.text()
        wbd.model.TagM.update_friend_email(wbd.wbd_global.active_state.tag_id, new_text_str)

    def on_friend_email_toggled(self, i_checked: bool):
        if self.updating_gui_bool:
            return
        if i_checked:
            self.friend_email_qle.setText("no-email")
        else:
            self.friend_email_qle.setText("")

    def update_gui(self):
        self.updating_gui_bool = True

        tag: wbd.model.TagM = wbd.model.TagM.get(wbd.wbd_global.active_state.tag_id)
        self.title_qle.setText(tag.title_str)
        # self.friend_qcb.setChecked(bool(tag.friend_email_str))  # -the empty string ("") is falsy
        # self.friend_email_qle.setText(tag.friend_email_str)
        self.description_qpte.setPlainText(tag.description_str)

        self.adjustSize()

        self.updating_gui_bool = False


class CompositeDetailsWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        vbox_l1 = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_l1)

        self.title_qll = QtWidgets.QLabel()
        vbox_l1.addWidget(self.title_qll)

        self.description_qpte = QtWidgets.QPlainTextEdit()
        self.description_qpte.setReadOnly(True)
        vbox_l1.addWidget(self.description_qpte)

    def update_gui(self):
        if wbd.wbd_global.active_state.tag_id == wbd.wbd_global.NO_ACTIVE_TAG_INT:
            return
        tag = wbd.model.TagM.get(wbd.wbd_global.active_state.tag_id)
        self.title_qll.setText('<span style="font-size: 14pt">' + tag.title_str + '</span>')
        self.description_qpte.setPlainText(tag.description_str)


"""
class CustomPushButton(QtWidgets.QPushButton):
    def __init__(self, i_id: int, i_title: str):
        super().__init__(i_title)

        self.id_int = i_id

    # overridden
    def clicked(self, checked=False):
        super().clicked(checked)
"""

