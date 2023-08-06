import logging
import subprocess
import webbrowser
import re
import wbd.gui.diary_entries_cw
import wbd.model
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui
import wbd.wbd_global
import wbd.gui.image_selection_dlg
import wbd.gui.list_widget
import wbd.gui.question_widgets
import wbd.gui.entry_datetime_selection_cw
import wbd.exception_handling

WIDTH_AND_HEIGHT_INT = 160
SEPARATOR_CHAR_INT_LIST = [
    QtCore.Qt.Key_Space,
    QtCore.Qt.Key_Comma, QtCore.Qt.Key_Colon, QtCore.Qt.Key_Semicolon, QtCore.Qt.Key_Period,
    QtCore.Qt.Key_ParenRight, QtCore.Qt.Key_BraceRight, QtCore.Qt.Key_BracketRight
]
# QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter


class EntryEditCw(QtWidgets.QWidget):
    close_signal = QtCore.Signal()
    close_and_next_signal = QtCore.Signal()
    close_and_share_signal = QtCore.Signal(int)
    tag_added_for_entry_signal = QtCore.Signal(int)
    selected_tag_changed_signal = QtCore.Signal(int)
    suggested_tag_changed_signal = QtCore.Signal(int)

    def __init__(self):
        super().__init__()

        self.selected_email_addresses_list = []

        self.updating_gui_bool = False

        self.vbox_l2 = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbox_l2)

        # Row 1 (question)
        hbox_l3 = QtWidgets.QHBoxLayout()
        self.vbox_l2.addLayout(hbox_l3)

        self.question_qll = QtWidgets.QLabel()
        self.question_qll.setWordWrap(True)
        new_font = self.question_qll.font()
        new_font.setPointSize(15)
        self.question_qll.setFont(new_font)
        hbox_l3.addWidget(self.question_qll, stretch=1)

        self.question_widgets_qlw = ShorterListWidget()  # QtWidgets.QListWidget()
        hbox_l3.addWidget(self.question_widgets_qlw)
        # self.question_widgets_qlw.setStyleSheet("QListWidget::item{border-bottom: 1px solid black;}")

        # Row 2 (text input area)
        hbox_l3 = QtWidgets.QHBoxLayout()
        self.vbox_l2.addLayout(hbox_l3)

        self.diary_entry_cpte = CustomPlainTextEdit()
        new_font = QtGui.QFont()
        new_font.setPointSize(wbd.wbd_global.get_entry_font_size())
        self.diary_entry_cpte.setFont(new_font)
        self.diary_entry_cpte.setStyleSheet("background-color:#d0e8c9")
        self.diary_entry_cpte.ctrl_plus_enter_signal.connect(self.on_entry_area_ctrl_plus_enter_pressed)
        self.diary_entry_cpte.space_signal.connect(self.on_space_pressed)
        self.diary_entry_cpte.textChanged.connect(self.on_diary_entry_text_changed)
        self.diary_entry_cpte.setSizePolicy(
            self.diary_entry_cpte.sizePolicy().horizontalPolicy(),
            QtWidgets.QSizePolicy.MinimumExpanding
        )
        self.vbox_l2.addWidget(self.diary_entry_cpte, stretch=1)
        # self.diary_entry_cpte.setPlainText("test")

        # Row 3 (varia)
        hbox_l3 = QtWidgets.QHBoxLayout()
        self.vbox_l2.addLayout(hbox_l3)

        # ..column 3 (add new buttons, time and date)..
        vbox_l4 = QtWidgets.QVBoxLayout()
        hbox_l3.addLayout(vbox_l4, stretch=3)

        # ..time
        self.datetime_selection_cw = wbd.gui.entry_datetime_selection_cw.EntryDatetimeSelectionCw()
        vbox_l4.addWidget(self.datetime_selection_cw)

        # ..(image)

        hbox_l5 = QtWidgets.QHBoxLayout()
        vbox_l4.addLayout(hbox_l5)
        self.set_image_qpb = QtWidgets.QPushButton("Add image")
        self.set_image_qpb.clicked.connect(self.on_set_image_clicked)
        hbox_l5.addWidget(self.set_image_qpb)

        self.remove_image_qpb = QtWidgets.QPushButton("Remove image")
        self.remove_image_qpb.clicked.connect(self.on_remove_image_clicked)
        hbox_l5.addWidget(self.remove_image_qpb)

        self.image_preview_qll = QtWidgets.QLabel()
        vbox_l4.addWidget(self.image_preview_qll)

        # Friends

        vbox_l4 = QtWidgets.QVBoxLayout()
        hbox_l3.addLayout(vbox_l4, stretch=3)

        self.friends_qlw = wbd.gui.list_widget.ListWidget(wbd.model.FriendM, True)
        # self.friends_qlw = QtWidgets.QListWidget()
        vbox_l4.addWidget(self.friends_qlw)
        # self.friends_qlw.current_row_changed_signal.connect(self.on_friends_checked_changed)
        self.friends_qlw.itemChanged.connect(self.on_friends_checked_changed)
        # self.friends_qlw.setSelectionMode()

        hbox_l2 = QtWidgets.QHBoxLayout()
        vbox_l4.addLayout(hbox_l2)
        vbox_l4.addLayout(hbox_l2)
        self.new_sharing_friend_name_qle = QtWidgets.QLineEdit()
        hbox_l2.addWidget(self.new_sharing_friend_name_qle)
        self.new_sharing_friend_email_qle = QtWidgets.QLineEdit()
        hbox_l2.addWidget(self.new_sharing_friend_email_qle)
        self.add_qpb = QtWidgets.QPushButton("Add")
        self.add_qpb.clicked.connect(self.on_add_new_sharing_friend_clicked)
        vbox_l4.addWidget(self.add_qpb)

        self.email_addresses_to_use_qll = QtWidgets.QLabel()
        vbox_l4.addWidget(self.email_addresses_to_use_qll)
        self.email_addresses_to_use_qll.setWordWrap(True)

        # ..rating
        self.rating_qbuttongroup = QtWidgets.QButtonGroup(self)
        # self.rating_qbuttongroup.buttonToggled.connect(self.on_rating_toggled)
        rating_hbox_l5 = QtWidgets.QHBoxLayout()
        vbox_l4.addLayout(rating_hbox_l5)
        self.rating_zero_qrb = QtWidgets.QRadioButton("0")
        self.rating_qbuttongroup.addButton(self.rating_zero_qrb, 0)
        rating_hbox_l5.addWidget(self.rating_zero_qrb)
        self.rating_one_qrb = QtWidgets.QRadioButton("1")
        self.rating_qbuttongroup.addButton(self.rating_one_qrb, 1)
        rating_hbox_l5.addWidget(self.rating_one_qrb)
        self.rating_two_qrb = QtWidgets.QRadioButton("2")
        self.rating_qbuttongroup.addButton(self.rating_two_qrb, 2)
        rating_hbox_l5.addWidget(self.rating_two_qrb)
        self.rating_three_qrb = QtWidgets.QRadioButton("3")
        self.rating_qbuttongroup.addButton(self.rating_three_qrb, 3)
        rating_hbox_l5.addWidget(self.rating_three_qrb)
        self.rating_one_qrb.setChecked(True)
        self.rating_qbuttongroup.buttonClicked.connect(self.on_rating_button_clicked)

        # ..sharing
        self.share_via_email_qpb = QtWidgets.QPushButton("Share via email")
        vbox_l4.addWidget(self.share_via_email_qpb)
        self.share_via_email_qpb.clicked.connect(self.on_share_via_email_button_clicked)

        self.share_to_diaspora_qpb = QtWidgets.QPushButton("Share to diaspora")
        vbox_l4.addWidget(self.share_to_diaspora_qpb)
        self.share_to_diaspora_qpb.clicked.connect(self.on_share_to_diaspora_clicked)

        self.translate_qpb = QtWidgets.QPushButton("Translate")
        vbox_l4.addWidget(self.translate_qpb)
        self.translate_qpb.clicked.connect(self.on_translate_clicked)

        # ..close
        close_hbox_l5 = QtWidgets.QHBoxLayout()
        vbox_l4.addLayout(close_hbox_l5)

        self.close_qpb = QtWidgets.QPushButton("Close")
        self.close_qpb.setFixedHeight(40)
        self.close_qpb.clicked.connect(self.on_close_clicked)
        close_hbox_l5.addWidget(self.close_qpb)

        self.close_and_go_to_next_question_qpb = QtWidgets.QPushButton("Close + go to next Q")
        vbox_l4.addWidget(self.close_and_go_to_next_question_qpb)
        self.close_and_go_to_next_question_qpb.clicked.connect(self.on_close_and_next_clicked)

        ######self.update_gui()

        # ..column [selected tags]
        vbox_l4 = QtWidgets.QVBoxLayout()
        hbox_l3.addLayout(vbox_l4, stretch=3)
        self.selected_tags_title_qll = QtWidgets.QLabel("Selected Tags")
        vbox_l4.addWidget(self.selected_tags_title_qll)

        self.selected_tags_qlw = wbd.gui.list_widget.ListWidget(wbd.model.TagsSelectedForEntryM)
        self.selected_tags_qlw.setSizePolicy(
            self.selected_tags_qlw.sizePolicy().horizontalPolicy(),
            QtWidgets.QSizePolicy.Maximum
        )
        self.selected_tags_qlw.current_row_changed_signal.connect(self.on_selected_tags_changed)
        vbox_l4.addWidget(self.selected_tags_qlw, stretch=2)

        # ..column [suggested tags]
        # vbox_l4 = QtWidgets.QVBoxLayout()
        # hbox_l3.addLayout(vbox_l4)
        self.suggested_tags_title_qll = QtWidgets.QLabel("Suggested Tags")
        vbox_l4.addWidget(self.suggested_tags_title_qll)
        self.suggested_tags_qlw = wbd.gui.list_widget.ListWidget(wbd.model.TagsSuggestedForQuestionM)
        # self.suggested_tags_qlw.setSizePolicy(self.suggested_tags_qlw.sizePolicy().horizontalPolicy(),QtWidgets.QSizePolicy.MinimumExpanding)
        self.suggested_tags_qlw.setSizePolicy(
            QtWidgets.QSizePolicy.Maximum,
            QtWidgets.QSizePolicy.Maximum)
        self.suggested_tags_qlw.current_row_changed_signal.connect(self.on_suggested_tags_changed)
        vbox_l4.addWidget(self.suggested_tags_qlw, stretch=2)
        """
        self.add_to_selected_tags_qpb = QtWidgets.QPushButton("Add to selected >")
        vbox_l4.addWidget(self.add_to_selected_tags_qpb)
        """

        # self.update_gui()

    def on_share_via_email_button_clicked(self):
        # Different options:
        # Nice overview! https://realpython.com/python-send-email/
        # 1. Using Python's webbrowser:
        # https://stackoverflow.com/questions/39267464/advanced-mailto-use-in-python
        # 2. another possibility is to use Qt:
        # https://forum.qt.io/topic/57662/qdesktopservices-openurl-qurl-mailto
        # https://doc.qt.io/qt-5/qdesktopservices.html#openUrl
        # 3. Using yagmail (Please note: Specifically for gmail):
        # https://github.com/kootenpv/yagmail
        # 4. Using smtp:
        # https://stackoverflow.com/a/6270987/2525237
        # https://docs.python.org/3/library/email.examples.html
        # 5. Using an email service like for example gunmail
        # 6. Calling the email client via the command line
        # For Thunderbird:
        # http://kb.mozillazine.org/Command_line_arguments_%28Thunderbird%29

        # Summary:
        # Something like 5 or 6 would be best in the sense that it gives the user the option to edit the text before sending

        """
        yag = yagmail.SMTP(from_email_address_str, from_password_str)
        subject_str = "subject test"
        contents_list = ["Email text body"]
        to_email_address_str = "tord.dellsen@gmail.com"
        yag.send(to_email_address_str, subject_str, contents_list)
        """

        """
        # Python's SMTP library

        email_msg = email.message.EmailMessage()
        email_msg.set_content("\nmessage body text")

        email_msg['Subject'] = "Test subject"
        email_msg['From'] = "tord@disroot.org"
        email_msg['To'] = "tord@disroot.org"

        # Please note that a local mailserver has to be started first:
        # python -m smtpd -n -c DebuggingServer localhost:1025
        smtp = smtplib.SMTP('localhost', 1025)
        smtp.send_message(email_msg)
        smtp.quit()
        Gives the following but no messsage recieved (maybe because there is no security?

        sunyata@sunyata-gratitude:~$ python -m smtpd -n -c DebuggingServer localhost:1025
        ---------- MESSAGE FOLLOWS ----------
        Content-Type: text/plain; charset="utf-8"
        Content-Transfer-Encoding: 7bit
        MIME-Version: 1.0
        Subject: Test subject
        From: tord@disroot.org
        To: tord.dellsen@gmail.com
        X-Peer: 127.0.0.1

        message body text
        ------------ END MESSAGE ------------
        """

        # https://realpython.com/python-send-email/#option-2-setting-up-a-local-smtp-server
        # Please remember security, it seems this is needed

        last_entry_id_int = wbd.wbd_global.active_state.last_entry()
        diary_entry = wbd.model.EntryM.get(last_entry_id_int)
        try:
            #subject_email_str = "Something that happened today [from WBD]"
            subject_email_str = "Diary entry for "
            subject_email_str += diary_entry.datetime_added_str
            ### subject_email_str += " [shared through WBD]"

            # Possible things to include:
            # WBD (or well-being diary)
            # time and date!
            # tags
            # snippet of text from the beginning

            message_composition_str = "to='"
            if not self.selected_email_addresses_list:
                QtWidgets.QMessageBox.warning(self, "Warning", "No contacts selected")
                return
            for friend_email_str in self.selected_email_addresses_list:
                message_composition_str += friend_email_str + ","
            message_composition_str += "',"

            """
            if len(self.selected_email_addresses_list) == 1:
                message_composition_str = "to='" + self.selected_email_addresses_list[0] + "',"
            else:
                # user_email_str = "tord.dellsen@gmail.com"
                # message_composition_str = "to='tord.dellsen@gmail.com,'" + "subject='Testing subject'," + "body='Text inside email body'"
                message_composition_str = "to='" + user_email_str + "',"
                message_composition_str += "bcc='"
                for friend_email_str in self.selected_email_addresses_list:
                    # message_composition_str += "bcc='"+friend_email_str+"',"
                    message_composition_str += friend_email_str + ","
            message_composition_str += "',"
            """

            body_email_str = self.diary_entry_cpte.toPlainText()

            body_footer_str = "\n\n---\n\nShared from Well-Being Diary - https://sunyatazero.gitlab.io/well-being-diary/"

            message_composition_str += (
                "subject='" + subject_email_str + "'," +
                "body='" + body_email_str + body_footer_str + "'"
            )
            # "\n\n" + tags_str +

            logging.debug(message_composition_str)

            # message_composition_str = "to='"+to_email_str+"',bcc='"+to_email_str+"',subject='"+subject_email_str+"'," + "body='"+body_email_str+"'"

            if diary_entry.image_file_bytes:
                # if photo_available: then transform from binary db data into file for attachment
                # smaller images are more popular because they put less strain on the inboxes of people,
                # and also it puts more focus on the text itself (rather than the image)
                # attachment=
                image_path_str = wbd.wbd_global.get_user_tmp_email_attachments_path("attached-image.png")
                with open(image_path_str, 'wb') as image_file:
                    # -the 'b' means that we are opening the file in binary mode
                    image_file.write(diary_entry.image_file_bytes)
                message_composition_str += ",attachment='" + image_path_str + "'"

            popen_id_int = subprocess.Popen(["thunderbird", "-compose", message_composition_str])
            # TODO: popen_id_int = subprocess.Popen(["trojita", "--compose", message_composition_str])
            # logging.info("popen_id_int = " + str(popen_id_int))
            # INFO: popen_id_int = <subprocess.Popen object at 0x7efee1d665c0>
            # thunderbird -compose "to='tord.dellsen@gmail.com',subject='Testing subject',body='Text inside email body',attachment='/home/sunyata/Nextcloud/Photos/DSC_0351.JPG'"

        except FileNotFoundError:
            wbd.exception_handling.error("Thunderbird not found")
            # TODO: If thunderbird is not available
            # then: using mailto and without attachment but instead the path to the file at the top of the email
            # (so that the user can insert the image file herself)
            """
            # Python's webbrowser:
            to_send_str = 'mailto:?to:email@email.123&subject=Test subject&body=test body text&attach=icon.png'
            # Please note: Different email clients can have different policies with this
            webbrowser.open(to_send_str.replace(' ', '%20'), new=1)
            """

    def on_translate_clicked(self):
        result = QtWidgets.QMessageBox.question(self, "are you sure?", "this will open google translate and share your private text with that web application, are you certain you want to do this?")
        if result == QtWidgets.QMessageBox.Yes:
            text_to_translate_str = self.diary_entry_cpte.toPlainText()
            g_translate_str = "https://translate.google.com/#view=home&op=translate&sl=auto&tl=en&text="
            webbrowser.open(g_translate_str + text_to_translate_str)

    def on_share_to_diaspora_clicked(self):
        last_entry_id_int = wbd.wbd_global.active_state.last_entry()
        diary_entry = wbd.model.EntryM.get(last_entry_id_int)
        title_str = "Diary entry for "
        title_str += diary_entry.datetime_added_str
        title_str += " [shared through WBD]"
        body_email_str = self.diary_entry_cpte.toPlainText()
        tag_list = wbd.model.get_all_tags_referenced_by_entry(last_entry_id_int)
        tag_title_list = [tag.title_str for tag in tag_list]
        # "#" +
        tags_str = ", ".join(tag_title_list)
        ###  + " --- Tags: " + tags_str
        share_url_str = "https://share.diasporafoundation.org/?title={title}&url={url}".format(
            title=title_str,
            url=body_email_str + " --- Tags: " + tags_str
        )
        logging.debug("share_url_str = " + str(share_url_str))
        webbrowser.open(share_url_str)

    def on_add_new_sharing_friend_clicked(self):
        name_str = self.new_sharing_friend_name_qle.text()
        email_address_str = self.new_sharing_friend_email_qle.text()
        wbd.model.FriendM.add(name_str, email_address_str)
        self.new_sharing_friend_name_qle.clear()
        self.new_sharing_friend_email_qle.clear()
        self.update_gui()

        # self.

    def on_friends_checked_changed(self, i_list_item: QtWidgets.QListWidgetItem):
        self.selected_email_addresses_list.clear()
        i = 0
        while i < self.friends_qlw.count():
            # https://stackoverflow.com/questions/12222594/how-can-i-iterate-through-qlistwidget-items-and-work-with-each-item
            list_item = self.friends_qlw.item(i)
            if list_item.checkState() == QtCore.Qt.Checked:
                friend_id_int = list_item.data(QtCore.Qt.UserRole)
                friend_obj = wbd.model.FriendM.get(int(friend_id_int))
                # friend_email_str = list_item.text().split("\n")[1]
                ######sel_friends_list = wbd.wbd_global.active_state.selected_friends_id_list
                self.selected_email_addresses_list.append(friend_obj.email_str)
            else:
                pass
            i += 1
        self.email_addresses_to_use_qll.setText(", ".join(self.selected_email_addresses_list))

    """
    def on_friends_checked_changed(self, i_list_item: QtWidgets.QListWidgetItem):
        self.selected_email_addresses_list = []
        sel_friends_id_list = wbd.wbd_global.active_state.selected_friends_id_list
        for friend_id_int in sel_friends_id_list:
            friend_obj = wbd.model.FriendM.get(friend_id_int)
            self.selected_email_addresses_list.append(friend_obj.email_str)
        self.email_addresses_to_use_qll.setText(", ".join(self.selected_email_addresses_list))
    """

    def on_selected_tags_changed(self, i_tag_id: int):
        self.selected_tag_changed_signal.emit(i_tag_id)

    def on_suggested_tags_changed(self, i_tag_id: int, i_ctrl_active: bool):
        ##### wbd.wbd_global.active_state.tag_id = i_tag_id
        self.update_gui(wbd.wbd_global.EventSource.entry_suggested_tags_tag_changed)
        if i_ctrl_active:
            self.add_active_tag(i_tag_id)
        self.suggested_tag_changed_signal.emit(i_tag_id)

    def on_entry_area_ctrl_plus_enter_pressed(self):
        self.close_signal.emit()

    def on_space_pressed(self, last_word_entered: str):
        tag_list = wbd.model.TagM.get_all() ######wbd.model.get_all_tags_referenced_by_entry(wbd.wbd_global.active_state.last_entry())
        one_or_more_tags_added_bool = False
        for tag in tag_list:
            tag_title_str = tag.title_str
            if tag_title_str.lower() == last_word_entered.lower():
                ############self.add_active_tag(tag.id_int)
                wbd.model.add_tag_entry_relation(
                    tag.id_int,
                    wbd.wbd_global.active_state.last_entry()
                )
                one_or_more_tags_added_bool = True
        if one_or_more_tags_added_bool:
            self.selected_tags_qlw.update_gui()

    def on_remove_image_clicked(self):
        if self.updating_gui_bool:
            return
        wbd.model.EntryM.update_image(wbd.wbd_global.active_state.last_entry(), None)
        self.update_gui()

    def on_set_image_clicked(self):
        if self.updating_gui_bool:
            return
        file_path_str = wbd.gui.image_selection_dlg.ImageFileDialog.open_dlg_and_get_image_path()
        if file_path_str:
            (image_file_bytes, image_taken_qdatetime) = wbd.wbd_global.process_image(file_path_str)
            wbd.model.EntryM.update_image(wbd.wbd_global.active_state.last_entry(), image_file_bytes)
            if image_taken_qdatetime is not None:
                wbd.model.EntryM.update_datetime(
                    wbd.wbd_global.active_state.last_entry(),
                    image_taken_qdatetime.toString(wbd.wbd_global.QT_DATETIME_FORMAT_STR)
                )
        self.update_gui()

    # "API"
    def add_active_tag(self, i_tag_id: int):
        # -TODO: This function may not be consistent with the approach taken in general
        if i_tag_id == wbd.wbd_global.NO_ACTIVE_TAG_INT:
            return

        wbd.model.add_tag_entry_relation(
            i_tag_id,
            wbd.wbd_global.active_state.last_entry()
        )
        ##############self.select_last_row()
        self.tag_added_for_entry_signal.emit(i_tag_id)

    def select_last_row(self):
        last_row_int = self.selected_tags_qlw.count() - 1
        list_item: QtWidgets.QListWidgetItem = self.selected_tags_qlw.item(last_row_int)
        list_item.setSelected(True)

    def on_close_and_next_clicked(self):
        self.close_and_next_signal.emit()

    def on_close_clicked(self):
        self.close_signal.emit()

    def on_close_and_share_clicked(self):
        last_entry_id_int = wbd.wbd_global.active_state.last_entry()
        self.close_and_share_signal.emit(last_entry_id_int)

    def on_diary_entry_text_changed(self):
        if self.updating_gui_bool:
            return
        notes_sg = self.diary_entry_cpte.toPlainText().strip()
        print("notes_sg = " + notes_sg)
        wbd.model.EntryM.update_text(wbd.wbd_global.active_state.last_entry(), notes_sg)
        # asdf
        # TODO: Considering waiting with commit, testing to see results
        #  https://stackoverflow.com/questions/1711631/improve-insert-per-second-performance-of-sqlite
        # TODO: Considering waiting with update until a word is written, or until the user closes the entry

    def on_rating_button_clicked(self):
        if self.updating_gui_bool:
            return
        selected_rating_int = self.rating_qbuttongroup.checkedId()
        wbd.model.EntryM.update_rating(wbd.wbd_global.active_state.last_entry(), selected_rating_int)

    def on_checkbox_question_widget_value_changed(self, i_new_value: str):
        # FInd start pos
        whole_text_str = self.diary_entry_cpte.toPlainText()
        start_pos_int = whole_text_str.find(wbd.gui.question_widgets.QuestionCheckboxCw.WIDGET_PREFIX_STR)
        logging.debug("start_pos_int "+str(start_pos_int))
        end_pos_int = whole_text_str.find(
            wbd.gui.question_widgets.QuestionCheckboxCw.WIDGET_SUFFIX_STR,
            start_pos_int
        ) + len(wbd.gui.question_widgets.QuestionCheckboxCw.WIDGET_SUFFIX_STR)

        logging.debug("end_pos_int "+str(end_pos_int))

        # Using cursors
        text_cursor=self.diary_entry_cpte.textCursor()
        text_cursor.setPosition(start_pos_int, QtGui.QTextCursor.MoveAnchor)
        text_cursor.setPosition(end_pos_int, QtGui.QTextCursor.KeepAnchor)
        text_cursor.setKeepPositionOnInsert(True)
        logging.debug("selected text:" + text_cursor.selectedText())
        #text_cursor.select(QtGui.QTextCursor.BlockUnderCursor)
        text_cursor.removeSelectedText()

        # text_cursor.movePosition(QtGui.QTextCursor.End)

        # text_cursor.clearSelection()
        self.diary_entry_cpte.setTextCursor(text_cursor)

        self.diary_entry_cpte.insertPlainText(i_new_value)
        text_cursor.setKeepPositionOnInsert(False)
        self.diary_entry_cpte.setTextCursor(text_cursor)
        #self.diary_entry_cpte.appendPlainText(i_new_value)

    def on_question_widget_value_changed(self, i_new_value: str):
        """
        string_one = "test"
        string_one.replace()
        self.diary_entry_cpte.appendPlainText(i_new_value)
        """

        # FInd start pos
        whole_text_str = self.diary_entry_cpte.toPlainText()
        start_pos_int = whole_text_str.find(wbd.gui.question_widgets.QuestionSliderCw.WIDGET_PREFIX_STR)
        logging.debug("start_pos_int "+str(start_pos_int))
        end_pos_int = whole_text_str.find(
            wbd.gui.question_widgets.QuestionSliderCw.WIDGET_SUFFIX_STR,
            start_pos_int
        ) + len(wbd.gui.question_widgets.QuestionSliderCw.WIDGET_SUFFIX_STR)
        # end_pos_int = whole_text_str.find(wbd.gui.question_widgets.QuestionSliderCw.WIDGET_SUFFIX_STR)+len(wbd.gui.question_widgets.QuestionSliderCw.WIDGET_SUFFIX_STR)
        logging.debug("end_pos_int "+str(end_pos_int))

        # Using cursors
        text_cursor=self.diary_entry_cpte.textCursor()
        text_cursor.setPosition(start_pos_int, QtGui.QTextCursor.MoveAnchor)
        text_cursor.setPosition(end_pos_int, QtGui.QTextCursor.KeepAnchor)
        text_cursor.setKeepPositionOnInsert(True)
        logging.debug("selected text:" + text_cursor.selectedText())
        #text_cursor.select(QtGui.QTextCursor.BlockUnderCursor)
        text_cursor.removeSelectedText()

        # text_cursor.movePosition(QtGui.QTextCursor.End)

        # text_cursor.clearSelection()
        self.diary_entry_cpte.setTextCursor(text_cursor)

        self.diary_entry_cpte.insertPlainText(i_new_value)
        text_cursor.setKeepPositionOnInsert(False)
        self.diary_entry_cpte.setTextCursor(text_cursor)
        #self.diary_entry_cpte.appendPlainText(i_new_value)

    def update_gui(self, i_space_pressed: bool=False):
        self.updating_gui_bool = True

        # Question widgets
        self.question_widgets_qlw.clear()

        #######################

        # for widget in model.question.widget_list
        qlwi = QtWidgets.QListWidgetItem()
        self.question_widgets_qlw.addItem(qlwi)
        # new_item_flags = qlwi.flags()
        # new_item_flags.set
        # new_item_flags.setFlag(QtCore.Qt.ItemIsSelectable, False)
        logging.debug("qlwi.flags = " +str(qlwi.flags()))
        qlwi.setFlags(QtCore.Qt.NoItemFlags)

        """
        partial_checkbox_func = functools.partial(
            self.on_checkbox_clicked, next_action.file_row_nr_int
        )
        # -this works, very nice! GOOD TO USE AGAIN IN THE FUTURE
        checkbox_qcb.clicked.connect(partial_checkbox_func)
        """

        question_widget_cw = wbd.gui.question_widgets.QuestionSliderCw("my title", 0, 42)
        # question_widget_cw = QtWidgets.QLabel("label")
        qlwi.setSizeHint(question_widget_cw.sizeHint())  # -important
        self.question_widgets_qlw.setItemWidget(qlwi, question_widget_cw)
        question_widget_cw.widget_update_signal.connect(self.on_question_widget_value_changed)

        #######################

        qlwi = QtWidgets.QListWidgetItem()
        self.question_widgets_qlw.addItem(qlwi)
        # new_item_flags = qlwi.flags()
        # new_item_flags.set
        # new_item_flags.setFlag(QtCore.Qt.ItemIsSelectable, False)
        logging.debug("qlwi.flags = " +str(qlwi.flags()))
        qlwi.setFlags(QtCore.Qt.NoItemFlags)

        checkbox_question_widget_cw = wbd.gui.question_widgets.QuestionCheckboxCw("cb title")
        # question_widget_cw = QtWidgets.QLabel("label")
        qlwi.setSizeHint(checkbox_question_widget_cw.sizeHint())  # -important
        logging.debug("checkbox_question_widget_cw.sizeHint().height = " + str(checkbox_question_widget_cw.sizeHint().height()))
        logging.debug("qlwi.sizeHint().height() = " + str(qlwi.sizeHint().height()))
        self.question_widgets_qlw.setItemWidget(qlwi, checkbox_question_widget_cw)
        checkbox_question_widget_cw.widget_update_signal.connect(self.on_checkbox_question_widget_value_changed)

        logging.debug("self.question_widgets_qlw.sizeHintForRow(0) = " + str(self.question_widgets_qlw.sizeHintForRow(0)))

        self.question_widgets_qlw.updateGeometry()  # <-Important!

        #self.question_widgets_qlw.

        #######################

        # Tags
        self.suggested_tags_qlw.update_gui()
        self.selected_tags_qlw.update_gui()
        """
        self.selected_tags_qlw.clear()
        if wbd.wbd_global.active_state.question_id != wbd.wbd_global.NO_ACTIVE_QUESTION_INT:
            tags_and_preselected_list = wbd.model.get_all_tags_referenced_by_question(wbd.wbd_global.active_state.question_id)
            for (tag, preselected_bool) in tags_and_preselected_list:
                self.selected_tags_qlw.addItem(tag.title_str)
                if preselected_bool:
                    self.select_last_row()
        else:
            tags_list = wbd.model.get_all_tags_referenced_by_entry(wbd.wbd_global.active_state.last_entry())
            for tag in tags_list:
                self.selected_tags_qlw.addItem(tag.title_str)
                self.select_last_row()  # -selecting all rows
        """

        if i_space_pressed == False:
            if wbd.wbd_global.active_state.is_entries_empty():
                logging.error("wbd.wbd_global.active_diary_entry_id is not set in update_gui function")

            diary_entry = wbd.model.EntryM.get(wbd.wbd_global.active_state.last_entry())

            # Question text
            if wbd.wbd_global.active_state.question_id == wbd.wbd_global.NO_ACTIVE_QUESTION_INT:
                self.question_qll.hide()
            else:
                self.question_qll.show()
                question = wbd.model.QuestionM.get(wbd.wbd_global.active_state.question_id)
                self.question_qll.setText(question.description_str)

            # Entry area
            self.diary_entry_cpte.setPlainText(diary_entry.diary_text_str)
            # TODO: Removing this and instead using a stacked widget for the entries

            # Image
            if diary_entry.image_file_bytes is not None:
                # self.image_file_name_qll.setText(diary_entry.image_file_bytes)
                qpixmap = QtGui.QPixmap()
                qpixmap.loadFromData(diary_entry.image_file_bytes)
                # -documentation: http://doc.qt.io/qt-5/qpixmap.html#loadFromData-1
                scaled_qpixmap = qpixmap.scaled(
                    WIDTH_AND_HEIGHT_INT,
                    WIDTH_AND_HEIGHT_INT,
                    QtCore.Qt.KeepAspectRatio,
                    QtCore.Qt.SmoothTransformation
                )
                self.image_preview_qll.setPixmap(scaled_qpixmap)
            else:
                self.image_preview_qll.setText("<preview area>")

            # if wbd.wbd_global.active_diary_entry_id == wbd.wbd_global.NO_DIARY_ENTRY_EDITING_INT:
            # else:

            # Date
            """
            date_part_int = diary_entry.date_added_it // 86400  # -will be rounded down
            time_part_int = diary_entry.date_added_it % 86400
            """

            # diary_entry.datetime_added_str

            self.datetime_selection_cw.update_gui()

            # Rating
            if diary_entry.rating_int == 0:
                self.rating_zero_qrb.click()
            elif diary_entry.rating_int == 1:
                self.rating_one_qrb.click()
            elif diary_entry.rating_int == 2:
                self.rating_two_qrb.click()
            elif diary_entry.rating_int == 3:
                self.rating_three_qrb.click()

        """
        # Sharing
        self.friends_qlw.clear()
        for friend_item in wbd.model.FriendM.get_all():
            list_item = QtWidgets.QListWidgetItem()
            list_item.setText(friend_item.title_str + "\n" + friend_item.email_str)
            list_item.setCheckState(QtCore.Qt.Unchecked)
            self.friends_qlw.addItem(list_item)
        """

        self.diary_entry_cpte.setFocus()

        self.updating_gui_bool = False


class CustomPlainTextEdit(QtWidgets.QPlainTextEdit):
    ctrl_plus_enter_signal = QtCore.Signal()
    space_signal = QtCore.Signal(str)  # -str contains the last word entered

    def __init__(self):
        super().__init__()

    # Overridden
    def keyPressEvent(self, i_qkeyevent):
        if QtWidgets.QApplication.keyboardModifiers() == QtCore.Qt.ControlModifier:
            if i_qkeyevent.key() == QtCore.Qt.Key_Enter or i_qkeyevent.key() == QtCore.Qt.Key_Return:
                logging.debug("CtrlModifier + Enter/Return")
                self.ctrl_plus_enter_signal.emit()
                return
        else:  # -no keyboard modifier
            if i_qkeyevent.key() == QtCore.Qt.Key_Enter or i_qkeyevent.key() == QtCore.Qt.Key_Return:
                # -http://doc.qt.io/qt-5/qguiapplication.html#keyboardModifiers
                # -Please note that the modifiers are placed directly in the QtCore.Qt namespace
                # Alternatively:
                # if QtWidgets.QApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier:
                # -using bitwise and to find out if the shift key is pressed
                logging.debug("enter or return key pressed in textedit area")
                # self.ref_central.save_entry()
                # return
            elif i_qkeyevent.key() in SEPARATOR_CHAR_INT_LIST:
                # == QtCore.Qt.Key_Space

                QtWidgets.QPlainTextEdit.keyPressEvent(self, i_qkeyevent)
                # -this doesn't cover the case when we are pasting text, but maybe we don't want an analysis in
                #  those cases

                logging.debug("space bar key pressed in textedit area")

                whole_text_str = self.toPlainText()
                # last_word_str = whole_text_str.strip().split(" ")[-1]

                """
                regex_split_str = "["
                for char_int in SEPARATOR_CHAR_INT_LIST:
                    backslash_str = "\\u"
                    print("len"+str(len(backslash_str)))
                    hex_str = backslash_str + format(char_int, "08x")
                    regex_split_str += hex_str
                regex_split_str += "]+"
                word_strlist = re.split(regex_split_str, whole_text_str)
                """

                word_strlist = re.split("[ ;:.,]+", whole_text_str)
                # -TODO: This needs to match the SEPARATOR_CHAR_INT_LIST list for the code to be reliable

                if len(word_strlist) >= 2:
                    last_word_str = word_strlist[-2]
                    # TODO: Rather than the last word we want to take the word to the left of the cursor
                    self.space_signal.emit(last_word_str)
                    #####self.
                return

        # QtWidgets.QPlainTextEdit.keyPressEvent(self, i_qkeyevent)
        super().keyPressEvent(i_qkeyevent)
        # -if we get here it means that the key has not been captured elsewhere (or possibly
        # (that the key has been captured but that we want "double handling" of the key event)


class ShorterListWidget(QtWidgets.QListWidget):
    # Overridden
    def sizeHint(self) -> QtCore.QSize:
        """
        This function is overridden because the lower limit for the height is too large.
        Please note that updateGeometry has to be called for the sizehint to be updated.
        """
        qsize = QtCore.QSize()
        # height_int = 100
        # self.sizeHintForRow()

        # height_int = super().sizeHint().height()
        # height_int = self.sizeHintForRow(0) * self.count() + 2 * self.frameWidth()
        height_int = 2 * self.frameWidth()
        for row_nr_int in range(0, self.count()):
            height_int += self.sizeHintForRow(row_nr_int)
        qsize.setHeight(height_int)

        width_int = super().sizeHint().width()
        qsize.setWidth(width_int)

        return qsize

