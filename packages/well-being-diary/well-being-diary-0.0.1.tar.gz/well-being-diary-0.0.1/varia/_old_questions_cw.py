import logging

import wbd.model
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui

import wbd.wbd_global
import wbd.gui.safe_confirmation_dlg


class QuestionsCw(QtWidgets.QWidget):
    # item_selection_changed_signal = QtCore.Signal()
    current_row_changed_signal = QtCore.Signal()
    write_entry_signal = QtCore.Signal()
    # new_practice_button_pressed_signal = QtCore.Signal(str)

    def __init__(self):
        super().__init__()

        self.updating_gui_bool = False

        self.show_archived_questions_bool = False
        self.last_entry_clicked_id_int = wbd.wbd_global.NO_ACTIVE_QUESTION_INT
        vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_l2)

        self.setMaximumWidth(500)

        hbox_l3 = QtWidgets.QHBoxLayout()
        vbox_l2.addLayout(hbox_l3)
        self.title_qll = QtWidgets.QLabel("Questions")
        hbox_l3.addWidget(self.title_qll)
        hbox_l3.addStretch(1)
        self.activate_qpb = QtWidgets.QPushButton("Write Entry")
        self.activate_qpb.clicked.connect(self.on_activate_clicked)
        hbox_l3.addWidget(self.activate_qpb)

        question_lists_hbox_l3 = QtWidgets.QHBoxLayout()
        vbox_l2.addLayout(question_lists_hbox_l3, stretch=7)

        # Creating widgets
        # ..for questions
        self.questions_qlw = QtWidgets.QListWidget()
        # self.questions_qlw.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        # self.questions_qlw.setDragEnabled(True)
        self.questions_qlw.currentRowChanged.connect(self.on_current_row_changed)
        new_font = self.questions_qlw.font()
        new_font.setPointSize(12)
        self.questions_qlw.setFont(new_font)
        question_lists_hbox_l3.addWidget(self.questions_qlw)
        ###self.list_widget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        ###self.list_widget.itemPressed.connect(self.on_item_selection_changed)
        # -itemClicked didn't work, unknown why (it worked on the first click but never when running in debug mode)
        # -currentItemChanged cannot be used here since it is activated before the list of selected items is updated

        # ..for adding a new question
        hbox_l3 = QtWidgets.QHBoxLayout()
        vbox_l2.addLayout(hbox_l3)
        self.adding_new_practice_qle = QtWidgets.QLineEdit()
        self.adding_new_practice_qle.setPlaceholderText("New question")
        hbox_l3.addWidget(self.adding_new_practice_qle)
        self.adding_new_practice_bn = QtWidgets.QPushButton("Add")
        hbox_l3.addWidget(self.adding_new_practice_bn)
        self.adding_new_practice_bn.clicked.connect(self.on_add_new_practice_button_pressed)

        hbox_l3 = QtWidgets.QHBoxLayout()
        vbox_l2.addLayout(hbox_l3)
        self.edit_texts_qpb = QtWidgets.QPushButton()
        self.edit_texts_qpb.setIcon(QtGui.QIcon(wbd.wbd_global.get_icon_path("pencil-2x.png")))
        self.edit_texts_qpb.setToolTip(self.tr("Edit the selected question"))
        self.edit_texts_qpb.clicked.connect(self.on_edit_clicked)
        hbox_l3.addWidget(self.edit_texts_qpb)

        self.move_to_top_qpb = QtWidgets.QPushButton()
        self.move_to_top_qpb.setIcon(QtGui.QIcon(wbd.wbd_global.get_icon_path("data-transfer-upload-2x.png")))
        self.move_to_top_qpb.setToolTip(self.tr("Move the selected breathing phrase to top"))
        #####self.move_to_top_qpb.clicked.connect(self.on_move_to_top_clicked)
        hbox_l3.addWidget(self.move_to_top_qpb)

        self.move_up_qpb = QtWidgets.QPushButton()
        self.move_up_qpb.setIcon(QtGui.QIcon(wbd.wbd_global.get_icon_path("arrow-top-2x.png")))
        self.move_up_qpb.setToolTip(self.tr("Move the selected breathing phrase up"))
        self.move_up_qpb.clicked.connect(self.move_item_up)
        hbox_l3.addWidget(self.move_up_qpb)
        self.move_down_qpb = QtWidgets.QPushButton()
        self.move_down_qpb.setIcon(QtGui.QIcon(wbd.wbd_global.get_icon_path("arrow-bottom-2x.png")))
        self.move_down_qpb.setToolTip(self.tr("Move the selected breathing phrase down"))
        self.move_down_qpb.clicked.connect(self.move_item_down)
        hbox_l3.addWidget(self.move_down_qpb)
        hbox_l3.addStretch(1)

        self.delete_phrase_qpb = QtWidgets.QPushButton()
        self.delete_phrase_qpb.setIcon(QtGui.QIcon(wbd.wbd_global.get_icon_path("trash-2x.png")))
        self.delete_phrase_qpb.setToolTip(self.tr("Delete the selected breathing phrase"))
        self.delete_phrase_qpb.clicked.connect(self.delete_item)
        hbox_l3.addWidget(self.delete_phrase_qpb)

    def on_activate_clicked(self):
        self.write_entry_signal.emit()

    def delete_item(self):
        if self.last_entry_clicked_id_int != wbd.wbd_global.NO_ACTIVE_QUESTION_INT:
            active_question = wbd.model.QuestionM.get(wbd.wbd_global.active_question_id_int)
            conf_result_bool = wbd.gui.safe_confirmation_dlg.SafeConfirmationDlg.get_safe_confirmation_dialog(
                "Are you sure that you want to remove this entry?<br><i>Please type the name to confirm</i>",
                active_question.title_str
            )

            if conf_result_bool:
                self.questions_qlw.clearSelection()
                wbd.wbd_global.active_question_id_int = wbd.wbd_global.NO_ACTIVE_QUESTION_INT
                self.current_row_changed_signal.emit()

                wbd.model.QuestionM.remove(self.last_entry_clicked_id_int)
                self.update_gui()
                ### self.context_menu_delete_signal.emit()
        else:
            raise Exception("Should not be possible to get here")

    def move_item_up(self):
        """
        wbd.model.QuestionM.update_active_sort_order_move_up_down(
            self.last_entry_clicked_id_int, wbd.model.MoveDirectionEnum.up)
        """
        self.move_current_row_up_down(wbd.wbd_global.MoveDirectionEnum.up)
        self.update_gui()

    def move_item_down(self):
        """
        wbd.model.QuestionM.update_active_sort_order_move_up_down(
            self.last_entry_clicked_id_int, wbd.model.MoveDirectionEnum.down)
        """
        self.move_current_row_up_down(wbd.wbd_global.MoveDirectionEnum.down)
        self.update_gui()

    def on_current_row_changed(self):
        if self.updating_gui_bool:
            return
        current_row_int = self.questions_qlw.currentRow()
        # if current_row_int != NO_QUESTION_INT:
        current_question_qli = self.questions_qlw.item(current_row_int)
        customqlabel_widget = self.questions_qlw.itemWidget(current_question_qli)
        if customqlabel_widget is not None:
            wbd.wbd_global.active_question_id_int = customqlabel_widget.question_entry_id
            self.current_row_changed_signal.emit()
        # self.details_cw.update_gui()

        # self.current_row_changed_signal.

    def on_edit_clicked(self):
        self.show_edit_dialog()

    def show_edit_dialog(self):
        id_int = wbd.wbd_global.active_question_id_int
        # if id_int != wbd.wbd_global.NO_ACTIVE_QUESTION_INT:
        self.edit_dialog = EditDialog()
        self.edit_dialog.finished.connect(self.on_edit_dialog_finished)
        self.edit_dialog.show()

    def on_edit_dialog_finished(self, i_result: int):
        if i_result == QtWidgets.QDialog.Accepted:
            # assert mc.mc_global.active_phrase_id_it != wbd.wbd_global.NO_PHRASE_SELECTED_INT
            # question = wbd.model.QuestionM.get(wbd.wbd_global.active_question_id_it)
            wbd.model.QuestionM.update_title(
                wbd.wbd_global.active_question_id_int,
                self.edit_dialog.question_title_qle.text()
            )
            plain_text_str = self.edit_dialog.description_qpte.toPlainText()
            wbd.model.QuestionM.update_description(
                wbd.wbd_global.active_question_id_int,
                plain_text_str
            )

            # Tags
            tag_id_list = []
            for selected_item in self.edit_dialog.tags_qlw.selectedItems():
                tag_name_str = selected_item.text()
                tag = wbd.model.TagM.get_by_title(tag_name_str)
                tag_id_int = tag.id_int
                logging.debug("tag.id_int = " + str(tag.id_int))
                logging.debug("wbd.wbd_global.active_question_id_it = " + str(wbd.wbd_global.active_question_id_int))
                wbd.model.add_tag_question_relation(
                    tag_id_int,
                    wbd.wbd_global.active_question_id_int
                )
                logging.debug("Relation between tag " + str(tag_id_int) + " and question " + str(wbd.wbd_global.active_question_id_int) + " added")
        else:
            pass
        ### self.phrase_changed_signal.emit(True)
        self.update_gui(True)

    def update_db_sort_order_for_all_rows(self):
        logging.debug("update_db_sort_order_for_all_rows")
        i = 0
        while i < self.questions_qlw.count():
            q_list_item_widget = self.questions_qlw.item(i)
            custom_label = self.questions_qlw.itemWidget(q_list_item_widget)
            id_int = custom_label.question_entry_id
            row_int = self.questions_qlw.row(q_list_item_widget)
            wbd.model.QuestionM.update_sort_order(
                id_int,
                row_int
            )
            logging.debug("id_int = " + str(id_int) + ", row_int = " + str(row_int))
            i += 1

    def move_current_row_up_down(self, i_move_direction: wbd.wbd_global.MoveDirectionEnum) -> None:
        current_row_int = self.questions_qlw.currentRow()
        current_list_widget_item = self.questions_qlw.item(current_row_int)
        item_widget = self.questions_qlw.itemWidget(current_list_widget_item)
        self.questions_qlw.takeItem(current_row_int)
        # -IMPORTANT: item is removed from list only after the item widget has been extracted.
        #  The reason for this is that if we take the item away from the list the associated
        #  widget (in our case a CustomLabel) will not come with us (which makes sense
        #  if the widget is stored in the list somehow)
        if i_move_direction == wbd.wbd_global.MoveDirectionEnum.up:
            # if main_sort_order_int == 0 or main_sort_order_int > len(QuestionM.get_all()):
            if current_row_int >= 0:
                self.questions_qlw.insertItem(current_row_int - 1, current_list_widget_item)
                self.questions_qlw.setItemWidget(current_list_widget_item, item_widget)
                self.questions_qlw.setCurrentRow(current_row_int - 1)
        elif i_move_direction == wbd.wbd_global.MoveDirectionEnum.down:
            # if main_sort_order_int < 0 or main_sort_order_int >= len(QuestionM.get_all()):
            if current_row_int < self.questions_qlw.count():
                self.questions_qlw.insertItem(current_row_int + 1, current_list_widget_item)
                self.questions_qlw.setItemWidget(current_list_widget_item, item_widget)
                self.questions_qlw.setCurrentRow(current_row_int + 1)

        self.update_db_sort_order_for_all_rows()
        # TODO: Adding drag and drop, and perhaps removing the up and down buttons

    def on_add_new_practice_button_pressed(self):
        text_sg = self.adding_new_practice_qle.text().strip()  # strip is needed to remove a newline at the end (why?)
        if not (text_sg and text_sg.strip()):
            return
        wbd.wbd_global.active_question_id_int = wbd.model.QuestionM.add(text_sg, "")

        self.adding_new_practice_qle.clear()
        self.update_gui()

        self.show_edit_dialog()

    # The same function is used for all the "rows"
    def on_list_row_label_mouse_pressed(self, i_qmouseevent, i_diary_id_it):
        logging.debug("button clicked: " + str(i_qmouseevent.button()))
        logging.debug("diary id: " + str(i_diary_id_it))
        self.last_entry_clicked_id_int = i_diary_id_it

    def update_gui(self, i_reset_current_row: bool=False):
        self.updating_gui_bool = True
        logging.debug("questions - update_gui() entered")

        if wbd.wbd_global.active_view == wbd.wbd_global.ViewEnum.entry:
            new_font: QtGui.QFont = self.title_qll.font()
            new_font.setUnderline(True)
        else:
            new_font: QtGui.QFont = self.title_qll.font()
            new_font.setUnderline(False)
        self.title_qll.setFont(new_font)

        # self.setPalette()

        self.questions_qlw.clear()
        self.questions_qlw.clearSelection()

        for question in wbd.model.QuestionM.get_all():
            row_item = QtWidgets.QListWidgetItem()

            """
            all_for_active_day_list = wbd.model.EntryM.get_for_question_and_active_day(question.id_int)
            if len(all_for_active_day_list) > 0:
                question_title_str = "<b>" + question_title_str + "</b>"
            """
            # TODO: Use the relation table above for setting text in bold

            question_title_qll = CustomQLabel(question.title_str, question.id_int)
            question_title_qll.mouse_pressed_signal.connect(
                self.on_list_row_label_mouse_pressed
            )

            self.questions_qlw.addItem(row_item)
            self.questions_qlw.setItemWidget(row_item, question_title_qll)

            if i_reset_current_row and wbd.wbd_global.active_question_id_int == question.id_int:
                self.questions_qlw.setCurrentItem(row_item)

        # self.details_cw.update_gui()
        # TODO: If NO_ACTIVE_QUESTION then using a stacked widget to just show a label (instead of the details widget)
        self.updating_gui_bool = False


class CustomQLabel(QtWidgets.QLabel):
    NO_DIARY_ENTRY_SELECTED = -1
    question_entry_id = NO_DIARY_ENTRY_SELECTED  # -"static"
    mouse_pressed_signal = QtCore.Signal(QtGui.QMouseEvent, int)

    def __init__(self, i_text_sg, i_diary_entry_id=NO_DIARY_ENTRY_SELECTED):
        super().__init__(i_text_sg)
        self.question_entry_id = i_diary_entry_id

    # Overridden
    # Please note that this is the event handler (not an event!)
    def mousePressEvent(self, i_qmouseevent):
        super(CustomQLabel, self).mousePressEvent(i_qmouseevent)
        # -self is automatically sent as the 1st argument
        self.mouse_pressed_signal.emit(i_qmouseevent, self.question_entry_id)


class EditDialog(QtWidgets.QDialog):
    """
    Inspiration: Answer by lou here:
    https://stackoverflow.com/questions/18196799/how-can-i-show-a-pyqt-modal-dialog-and-get-data-out-of-its-controls-once-its-clo
    """
    def __init__(self, i_parent=None):
        super(EditDialog, self).__init__(i_parent)

        self.setModal(True)

        self.setMinimumWidth(400)
        self.setMinimumHeight(600)

        self.updating_gui_bool = False

        # question = wbd.model.QuestionM.get_question(wbd.wbd_global.active_question_id_it)

        hbox_l2 = QtWidgets.QHBoxLayout(self)
        self.setLayout(hbox_l2)

        vbox_l3 = QtWidgets.QVBoxLayout(self)
        hbox_l2.addLayout(vbox_l3, stretch=2)
        spacing_int = 20

        vbox_l3.addWidget(QtWidgets.QLabel(self.tr("Title")))
        self.question_title_qle = QtWidgets.QLineEdit()
        vbox_l3.addWidget(self.question_title_qle)
        vbox_l3.addSpacing(spacing_int)

        vbox_l3.addWidget(QtWidgets.QLabel(self.tr("Description")))
        self.description_qpte = QtWidgets.QPlainTextEdit()
        self.description_qpte.setPlaceholderText("Please enter a description")
        vbox_l3.addWidget(self.description_qpte)

        # descr_help_str = """You can enclose text inside < and > to make it clickable """
        """so that it is added to the edit area when clicking it"""
        # self.description_help_qll = QtWidgets.QLabel(descr_help_str)
        # self.description_help_qll.setWordWrap(True)
        # vbox_l3.addWidget(self.description_help_qll)

        vbox_l3.addSpacing(spacing_int)

        self.button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal,
            self
        )
        vbox_l3.addWidget(self.button_box)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        # -accept and reject are "slots" built into Qt

        tags_vbox_l3 = QtWidgets.QVBoxLayout()
        hbox_l2.addLayout(tags_vbox_l3, stretch=1)

        tags_vbox_l3.addWidget(QtWidgets.QLabel("Default tags"))
        self.tags_qlw = QtWidgets.QListWidget()
        self.tags_qlw.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        # self.tags_qlw.itemSelectionChanged.connect(self.on_tags_selection_changed)
        tags_vbox_l3.addWidget(self.tags_qlw)
        for tag in wbd.model.TagM.get_all():
            self.tags_qlw.addItem(tag.title_str)

        question = wbd.model.QuestionM.get(wbd.wbd_global.active_question_id_int)
        self.question_title_qle.setText(question.title_str)
        if wbd.wbd_global.active_question_id_int == wbd.wbd_global.NO_ACTIVE_QUESTION_INT:
            self.question_title_qle.setEnabled(False)
            self.description_qpte.setEnabled(False)
            self.description_qpte.setPlaceholderText("<i>No description for this entry</i>")
        else:
            self.description_qpte.setPlainText(question.description_str)
        # self.is_scheduled_qcb.setChecked(self.is_sheduled_bool)

        self.update_gui()

    def update_gui(self):
        # self.is_scheduled_qcb.setChecked(self.is_sheduled_bool)
        self.adjustSize()



