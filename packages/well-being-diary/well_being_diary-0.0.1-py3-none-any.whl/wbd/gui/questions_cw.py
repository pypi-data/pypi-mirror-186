import logging
import wbd.model
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui
import wbd.wbd_global
import wbd.gui.safe_confirmation_dlg
import wbd.gui.list_widget

NO_POS_SET_INT = -1


class QuestionsCw(QtWidgets.QWidget):
    current_row_changed_or_edited_signal = QtCore.Signal()
    write_entry_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()

        self.new_entry_bool = False

        vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_l2)

        self.edit_dialog = None

        hbox_l3 = QtWidgets.QHBoxLayout()
        vbox_l2.addLayout(hbox_l3)
        self.title_qll = QtWidgets.QLabel("Questions/Entry_edit")
        hbox_l3.addWidget(self.title_qll)
        hbox_l3.addStretch(1)
        self.activate_qpb = QtWidgets.QPushButton("Write Entry - free writing")
        self.activate_qpb.clicked.connect(self.on_activate_clicked)
        self.activate_qpb.setToolTip("No question")
        hbox_l3.addWidget(self.activate_qpb)

        # Creating widgets
        # ..for list items (questions)
        self.list_clw = wbd.gui.list_widget.ListWithOrderWidget(wbd.model.QuestionM)
        #########CustomListWidget()
        # self.list_clw.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        # self.list_qlw.setDragEnabled(True)
        # self.list_clw.drop_signal.connect(self.update_db_sort_order_for_all_rows)
        self.list_clw.current_row_changed_signal.connect(self.on_current_row_changed)
        vbox_l2.addWidget(self.list_clw, stretch=1)
        # self.list_widget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        # self.list_widget.itemPressed.connect(self.on_item_selection_changed)
        # -itemClicked didn't work, unknown why (it worked on the first click but never when running in debug mode)
        # -currentItemChanged cannot be used here since it is activated before the list of selected items is updated

        # ..for adding a new list item
        hbox_l3 = QtWidgets.QHBoxLayout()
        vbox_l2.addLayout(hbox_l3)
        self.adding_new_item_qle = QtWidgets.QLineEdit()
        self.adding_new_item_qle.setPlaceholderText("New question")
        hbox_l3.addWidget(self.adding_new_item_qle)
        self.adding_new_item_qpb = QtWidgets.QPushButton("Add")
        self.adding_new_item_qpb.clicked.connect(self.on_add_new_item_button_pressed)
        hbox_l3.addWidget(self.adding_new_item_qpb)

        hbox_l3 = QtWidgets.QHBoxLayout()
        vbox_l2.addLayout(hbox_l3)
        self.edit_texts_qpb = QtWidgets.QPushButton()
        self.edit_texts_qpb.setIcon(QtGui.QIcon(wbd.wbd_global.get_icon_path("pencil-2x.png")))
        self.edit_texts_qpb.setToolTip("Edit")
        self.edit_texts_qpb.clicked.connect(self.on_edit_clicked)
        hbox_l3.addWidget(self.edit_texts_qpb)

        self.move_to_top_qpb = QtWidgets.QPushButton()
        self.move_to_top_qpb.setIcon(QtGui.QIcon(wbd.wbd_global.get_icon_path("data-transfer-upload-2x.png")))
        self.move_to_top_qpb.setToolTip(self.tr("Move to top"))
        self.move_to_top_qpb.clicked.connect(self.list_clw.move_to_top)
        hbox_l3.addWidget(self.move_to_top_qpb)
        self.move_up_qpb = QtWidgets.QPushButton()
        self.move_up_qpb.setIcon(QtGui.QIcon(wbd.wbd_global.get_icon_path("arrow-top-2x.png")))
        self.move_up_qpb.setToolTip(self.tr("Move up"))
        self.move_up_qpb.clicked.connect(self.list_clw.move_item_up)
        hbox_l3.addWidget(self.move_up_qpb)
        self.move_down_qpb = QtWidgets.QPushButton()
        self.move_down_qpb.setIcon(QtGui.QIcon(wbd.wbd_global.get_icon_path("arrow-bottom-2x.png")))
        self.move_down_qpb.setToolTip(self.tr("Move down"))
        self.move_down_qpb.clicked.connect(self.list_clw.move_item_down)
        hbox_l3.addWidget(self.move_down_qpb)

        hbox_l3.addStretch(1)

        self.delete_phrase_qpb = QtWidgets.QPushButton()
        self.delete_phrase_qpb.setIcon(QtGui.QIcon(wbd.wbd_global.get_icon_path("trash-2x.png")))
        self.delete_phrase_qpb.setToolTip(self.tr("Delete"))
        self.delete_phrase_qpb.clicked.connect(self.delete_item)
        hbox_l3.addWidget(self.delete_phrase_qpb)

        self.update_gui()

    def on_activate_clicked(self):
        self.write_entry_signal.emit()

    def delete_item(self):
        if wbd.wbd_global.active_state.question_id != wbd.wbd_global.NO_ACTIVE_QUESTION_INT:
            active_question = wbd.model.QuestionM.get(wbd.wbd_global.active_state.question_id)
            conf_result_bool = wbd.gui.safe_confirmation_dlg.SafeConfirmationDlg.get_safe_confirmation_dialog(
                "Are you sure that you want to remove this question?<br><i>Please type the name to confirm</i>",
                active_question.title_str
            )
            if conf_result_bool:
                self.list_clw.delete_item(wbd.wbd_global.active_state.question_id)
        else:
            raise Exception("Should not be possible to get here")

    def go_to_next_question(self) -> bool:
        result_bool = self.list_clw.go_to_next_row()
        return result_bool

    # Question item buttons

    def on_current_row_changed(self, i_new_question_id: int):
        wbd.wbd_global.active_state.question_id = i_new_question_id
        self.current_row_changed_or_edited_signal.emit()

    # Edit dialog

    def on_edit_clicked(self):
        self.new_entry_bool = False
        self.show_edit_dialog()

    def show_edit_dialog(self):
        self.edit_dialog = EditDialog()
        self.edit_dialog.finished.connect(self.on_edit_dialog_finished)
        #self.edit_dialog.populate_lists()
        self.edit_dialog.update_gui()
        self.edit_dialog.show()

    def on_edit_dialog_finished(self, i_result: int):

        # self.populate_list()

        if self.new_entry_bool:
            last_row_int = self.list_clw.count() - 1
            self.list_clw.setCurrentRow(last_row_int)
            self.new_entry_bool = False
        else:
            self.current_row_changed_or_edited_signal.emit()

        self.update_gui()

    def on_add_new_item_button_pressed(self):
        text_sg = self.adding_new_item_qle.text().strip()  # strip is needed to remove a newline at the end (why?)
        if not text_sg.strip():
            return
        wbd.wbd_global.active_state.question_id = wbd.model.QuestionM.add(text_sg, "")

        self.adding_new_item_qle.clear()
        self.update_gui()

        self.new_entry_bool = True
        self.show_edit_dialog()

    # Updating

    """
    def populate_list(self):
        self.list_clw.clear()
        for question in wbd.model.QuestionM.get_all():
            question_qll = CustomQLabel(question.title_str, question.id_int)
            row_item = QtWidgets.QListWidgetItem()
            self.list_clw.addItem(row_item)
            self.list_clw.setItemWidget(row_item, question_qll)
    """

    def update_gui(self):
        #### , i_reset_current_row: bool=False
        self.updating_gui_bool = True
        logging.debug("questions - update_gui() entered")

        self.list_clw.update_gui()

        # TODO: Implementing this again
        """
        if wbd.wbd_global.active_view == wbd.wbd_global.ViewEnum.entry:
            new_font: QtGui.QFont = self.title_qll.font()
            new_font.setUnderline(True)
        else:
            new_font: QtGui.QFont = self.title_qll.font()
            new_font.setUnderline(False)
        self.title_qll.setFont(new_font)
        """

        self.updating_gui_bool = False


class CustomListWidget(QtWidgets.QListWidget):
    drop_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        # CustomListWidget, self

    # overridden
    def dropEvent(self, QDropEvent):
        super().dropEvent(QDropEvent)
        self.drop_signal.emit()


class EditDialog(QtWidgets.QDialog):
    """
    Inspiration: Answer by lou here:
    https://stackoverflow.com/questions/18196799/how-can-i-show-a-pyqt-modal-dialog-and-get-data-out-of-its-controls-once-its-clo
    """
    def __init__(self, i_parent=None):
        super().__init__(i_parent)

        self.setModal(True)

        self.setMinimumWidth(400)
        self.setMinimumHeight(500)

        self.updating_gui_bool = True

        # question = wbd.model.QuestionM.get_question(wbd.wbd_global.active_question_id_it)

        vbox_l1 = QtWidgets.QVBoxLayout(self)
        self.setLayout(vbox_l1)

        hbox_l2 = QtWidgets.QHBoxLayout()
        vbox_l1.addLayout(hbox_l2)

        left_vbox_l3 = QtWidgets.QVBoxLayout(self)
        hbox_l2.addLayout(left_vbox_l3, stretch=2)
        spacing_int = 20

        left_vbox_l3.addWidget(QtWidgets.QLabel(self.tr("Title")))
        self.title_qle = QtWidgets.QLineEdit()
        self.title_qle.textChanged.connect(self.on_title_text_changed)
        left_vbox_l3.addWidget(self.title_qle)

        left_vbox_l3.addSpacing(spacing_int)

        left_vbox_l3.addWidget(QtWidgets.QLabel(self.tr("Description")))
        self.description_qpte = QtWidgets.QPlainTextEdit()
        self.description_qpte.setPlaceholderText("Please enter a description")
        self.description_qpte.textChanged.connect(self.on_description_text_changed)
        left_vbox_l3.addWidget(self.description_qpte)

        # descr_help_str = """You can enclose text inside < and > to make it clickable """
        """so that it is added to the edit area when clicking it"""
        # self.description_help_qll = QtWidgets.QLabel(descr_help_str)
        # self.description_help_qll.setWordWrap(True)
        # left_vbox_l3.addWidget(self.description_help_qll)

        # left_vbox_l3.addSpacing(spacing_int)

        self.button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Close,
            QtCore.Qt.Horizontal,
            self
        )
        vbox_l1.addWidget(self.button_box)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        # -accept and reject are "slots" built into Qt

        # Tags

        right_vbox_l3 = QtWidgets.QVBoxLayout()
        hbox_l2.addLayout(right_vbox_l3, stretch=1)

        right_vbox_l3.addWidget(QtWidgets.QLabel("Please choose tags suggested to the user"))
        self.all_tags_qlw = wbd.gui.list_widget.ListWidget(wbd.model.TagM, True)
        self.all_tags_qlw.itemChanged.connect(self.on_tag_checked_changed)
        # self.source_tags_qlw.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        # self.tags_qlw.itemSelectionChanged.connect(self.on_tags_selection_changed)
        right_vbox_l3.addWidget(self.all_tags_qlw)

        self.updating_gui_bool = False

        #self.populate_lists()
        self.update_gui()

    def on_title_text_changed(self):
        title_text_str = self.title_qle.text()
        wbd.model.QuestionM.update_title(wbd.wbd_global.active_state.question_id, title_text_str)

    def on_description_text_changed(self):
        description_plain_text_str = self.description_qpte.toPlainText()
        wbd.model.QuestionM.update_description(wbd.wbd_global.active_state.question_id, description_plain_text_str)

    def on_add_clicked(self):
        selected_items = self.all_tags_qlw.selectedItems()
        selected_item = selected_items[0]
        label_cll: CustomQLabel = self.all_tags_qlw.itemWidget(selected_item)
        tag = wbd.model.TagM.get(label_cll.id_int)

        success_bool = wbd.model.add_tag_question_relation(
            label_cll.id_int,
            wbd.wbd_global.active_state.question_id,
            False
        )
        if success_bool:
            tag_qll = CustomQLabel(tag.title_str, tag.id_int)
            row_item = QtWidgets.QListWidgetItem()
            self.dest_tags_qlw.addItem(row_item)
            self.dest_tags_qlw.setItemWidget(row_item, tag_qll)

        """
        tag_list = self.edit_dialog.dest_tags_qlw.items
        wbd.model.remove_all_tag_relations_for_question()
        for tag_id in self.edit_dialog.get_ids_for_selected_tags():
            wbd.model.add_tag_question_relation(tag_id, wbd.wbd_global.active_question_id_int)
        """

    def on_remove_clicked(self):
        selected_dest_item_list = self.dest_tags_qlw.selectedItems()
        selected_dest_item = selected_dest_item_list[0]
        label_cll: CustomQLabel = self.dest_tags_qlw.itemWidget(selected_dest_item)
        tag = wbd.model.TagM.get(label_cll.id_int)

        wbd.model.remove_tag_question_relation(
            label_cll.id_int,
            wbd.wbd_global.active_state.question_id
        )

        row_for_dest_selected_item_int = self.dest_tags_qlw.row(selected_dest_item)
        self.dest_tags_qlw.removeItemWidget(selected_dest_item)
        self.dest_tags_qlw.takeItem(row_for_dest_selected_item_int)

    def on_tag_checked_changed(self, i_list_item: QtWidgets.QListWidgetItem):
        self.selected_email_addresses_list = []
        i = 0
        while i < self.all_tags_qlw.count():
            # https://stackoverflow.com/questions/12222594/how-can-i-iterate-through-qlistwidget-items-and-work-with-each-item
            list_item = self.all_tags_qlw.item(i)
            tag_id_int = list_item.data(QtCore.Qt.UserRole)
            if list_item.checkState() == QtCore.Qt.Checked:
                #tag_obj = wbd.model.FriendM.get(int(tag_id_int))
                ############self.selected_email_addresses_list.append(tag_obj.email_str)
                success_bool = wbd.model.add_tag_question_relation(
                    tag_id_int,
                    wbd.wbd_global.active_state.question_id,
                    False
                )
            else:
                wbd.model.remove_tag_question_relation(
                    tag_id_int,
                    wbd.wbd_global.active_state.question_id
                )
            i += 1

    def update_gui(self):
        self.updating_gui_bool = True

        question = wbd.model.QuestionM.get(wbd.wbd_global.active_state.question_id)
        self.title_qle.setText(question.title_str)
        if wbd.wbd_global.active_state.question_id == wbd.wbd_global.NO_ACTIVE_QUESTION_INT:
            self.title_qle.setEnabled(False)
            self.description_qpte.setEnabled(False)
            # self.description_qpte.setPlaceholderText("<i>No description for this entry</i>")
        else:
            self.title_qle.setEnabled(True)
            self.description_qpte.setEnabled(True)
            self.description_qpte.setPlainText(question.description_str)
        # self.is_scheduled_qcb.setChecked(self.is_sheduled_bool)

        # Tags
        checked_ids_list = [
            tag.id_int for tag in wbd.model.get_all_tags_referenced_by_question(wbd.wbd_global.active_state.question_id)
        ]
        self.all_tags_qlw.update_gui(i_checked_ids=checked_ids_list)

        # self.is_scheduled_qcb.setChecked(self.is_sheduled_bool)
        self.adjustSize()

        self.updating_gui_bool = False


"""
class CustomQLabel(QtWidgets.QLabel):
    def __init__(self, i_text: str, i_id: int):
        super().__init__(i_text)
        self.id_int = i_id
        # logging.debug("CustomQLabel i_text = " + i_text + " i_id = " + str(i_id))
"""
