import logging
import typing
from PySide6 import QtGui
from PySide6 import QtCore
from PySide6 import QtWidgets
import wbd.gui.entry_edit_cw
import wbd.model
import wbd.db
import wbd.gui.questions_cw
import wbd.wbd_global
import wbd.gui.tags_cw
import wbd.gui.filters_cw
import wbd.gui.export_dlg
import wbd.gui.image_selection_dlg
from wbd.wbd_global import EventSource
import wbd.exception_handling
import configparser


class MainWindow(QtWidgets.QMainWindow):
    """
    The main window of the application
    Suffix explanation:
    _w: widget
    _l: layout
    _# (number): The level in the layout stack
    """
    # noinspection PyArgumentList,PyUnresolvedReferences
    def __init__(self):
        super().__init__()

        # Initializing window
        self.setGeometry(40, 30, 1200, 700)
        self.showMaximized()
        if wbd.wbd_global.testing_bool:
            data_storage_str = "{data stored (temporarily) in memory}"
        else:
            data_storage_str = "{data stored on hard drive}"
        self.setWindowTitle(
            wbd.wbd_global.WBD_APPLICATION_NAME_STR
            + " [" + wbd.wbd_global.WBD_APPLICATION_VERSION_STR + "] "
            + data_storage_str
        )
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setStyleSheet("* {selection-background-color:#72ba5e;};")

        # Setup of widgets..
        layout_widget_l1 = QtWidgets.QWidget()
        self.setCentralWidget(layout_widget_l1)
        main_hbox_l2 = QtWidgets.QHBoxLayout()
        layout_widget_l1.setLayout(main_hbox_l2)

        # ..left side..
        left_vbox_l3 = QtWidgets.QVBoxLayout()
        main_hbox_l2.addLayout(left_vbox_l3, stretch=1)

        # ..pages
        self.pages_cw = PagesCw()
        self.pages_cw.page_changed_signal.connect(self.on_page_changed)
        left_vbox_l3.addWidget(self.pages_cw)

        # ..filters
        self.filters_cw3 = wbd.gui.filters_cw.FiltersCw()
        self.filters_cw3.filters_changed_signal.connect(self.on_filters_changed)
        self.filters_cw3.activated_signal.connect(self.on_diary_view_activated)
        left_vbox_l3.addWidget(self.filters_cw3, stretch=1)

        # ..questions
        self.questions_cw3 = wbd.gui.questions_cw.QuestionsCw()
        self.questions_cw3.current_row_changed_or_edited_signal.connect(self.on_question_item_row_changed)
        self.questions_cw3.write_entry_signal.connect(self.on_question_view_write_entry)
        left_vbox_l3.addWidget(self.questions_cw3, stretch=2)

        # ..central area..
        self.central_qsw = QtWidgets.QStackedWidget()
        main_hbox_l2.addWidget(self.central_qsw, stretch=3)

        # ..diary entries (inside a QStackedWidget)
        self.diary_widget = wbd.gui.diary_entries_cw.DiaryEntriesCw()
        self.diary_widget.diary_entry_edit_signal.connect(self.on_diary_entry_edit)
        self.diary_widget.context_menu_email_share_signal.connect(self.on_context_menu_share)
        self.diary_widget.context_menu_delete_signal.connect(self.on_context_menu_delete)
        self.diary_widget_nr_int = self.central_qsw.addWidget(self.diary_widget)

        # ..edit for entries (inside a QStackedWidget)
        self.edit_entry_cw = wbd.gui.entry_edit_cw.EntryEditCw()
        self.edit_entry_cw.close_signal.connect(self.on_entry_area_close)
        self.edit_entry_cw.close_and_next_signal.connect(self.on_entry_area_close_and_next)
        self.edit_entry_cw.selected_tag_changed_signal.connect(self.on_entry_selected_tag_changed)
        self.edit_entry_cw.suggested_tag_changed_signal.connect(self.on_entry_suggested_tag_changed)
        self.edit_entry_cw.tag_added_for_entry_signal.connect(self.on_tag_added_for_entry_changed)
        self.edit_entry_nr_int = self.central_qsw.addWidget(self.edit_entry_cw)

        self.central_qsw.setCurrentIndex(self.diary_widget_nr_int)

        # ..right side..
        # ..tags
        self.tags_cw3 = wbd.gui.tags_cw.TagsCw()
        self.tags_cw3.current_row_changed_signal.connect(self.on_tags_area_row_changed)
        self.tags_cw3.add_tag_for_entry_signal.connect(self.on_tags_add_tag_for_entry)
        main_hbox_l2.addWidget(self.tags_cw3, stretch=1)

        # Creating the menu bar..
        self.menu_bar = self.menuBar()
        # ..file menu
        file_menu = self.menu_bar.addMenu("&File")
        export_qaction = QtGui.QAction("Export to CSV", self)
        export_qaction.triggered.connect(self.on_export_action_triggered)
        file_menu.addAction(export_qaction)
        import_qaction = QtGui.QAction("Import from CSV", self)
        import_qaction.triggered.connect(self.on_import_action_triggered)
        file_menu.addAction(import_qaction)

        set_user_dir_qaction = QtGui.QAction("Set User Dir", self)
        set_user_dir_qaction.triggered.connect(self.on_set_user_dir_action_triggered)
        file_menu.addAction(set_user_dir_qaction)

        import_images_qaction = QtGui.QAction("Import Multiple Images", self)
        import_images_qaction.triggered.connect(self.on_import_images_action_triggered)
        file_menu.addAction(import_images_qaction)
        backup_qaction = QtGui.QAction("Backup db", self)
        backup_qaction.triggered.connect(self.on_backup_using_copyfile_triggered)
        file_menu.addAction(backup_qaction)
        exit_qaction = QtGui.QAction("Exit", self)
        exit_qaction.triggered.connect(self.close)
        # -we can't use sys.exit because then closeEvent is not triggered
        file_menu.addAction(exit_qaction)
        # ..debug menu
        debug_menu = self.menu_bar.addMenu("Debu&g")
        redraw_qaction = QtGui.QAction("Redraw", self)
        redraw_qaction.triggered.connect(self.on_redraw_action_triggered)
        debug_menu.addAction(redraw_qaction)
        take_iter_db_dump_qaction = QtGui.QAction("Take Iter DB dump", self)
        take_iter_db_dump_qaction.triggered.connect(wbd.db.take_iter_db_dump)
        debug_menu.addAction(take_iter_db_dump_qaction)
        backup_using_sqlite_qaction = QtGui.QAction("Backup using sqlite", self)
        backup_using_sqlite_qaction.triggered.connect(self.on_backup_using_sqlite_triggered)
        debug_menu.addAction(backup_using_sqlite_qaction)

        row_count_qaction = QtGui.QAction("Row Count", self)
        row_count_qaction.triggered.connect(wbd.db.get_row_count)
        debug_menu.addAction(row_count_qaction)

        # ..help menu
        help_menu = self.menu_bar.addMenu("&Help")
        about_qaction = QtGui.QAction("About", self)
        about_qaction.triggered.connect(self.show_about_box)
        help_menu.addAction(about_qaction)
        manual_qaction = QtGui.QAction("Manual", self)
        manual_qaction.triggered.connect(self.show_user_guide)
        help_menu.addAction(manual_qaction)

        self.updating_gui_bool = False
        self.update_gui(EventSource.application_start)

    # Menu actions
    def on_backup_using_copyfile_triggered(self):
        file_size_in_bytes_int = wbd.db.backup_db(wbd.db.DbBackupMethod.using_copyfile)
        if file_size_in_bytes_int == -1:
            pass
            # in-memory db
        elif file_size_in_bytes_int < 8192:
            wbd.exception_handling.error(
                "Problem with backup",
                "Something probably went wrong, the file size is just " + str(file_size_in_bytes_int) + " bytes"
            )

    def on_backup_using_sqlite_triggered(self):
        file_size_in_bytes_int = wbd.db.backup_db(wbd.db.DbBackupMethod.using_sqlite)
        if file_size_in_bytes_int < 8192:
            wbd.exception_handling.warning(
                "Problem with backup",
                "Something probably went wrong, the file size is just " + str(file_size_in_bytes_int) + " bytes"
            )

    def on_redraw_action_triggered(self):
        self.update_gui(EventSource.application_start)

    def on_export_action_triggered(self):
        result_bool = wbd.gui.export_dlg.ExportDlg.open_export_dialog()

    def on_import_images_action_triggered(self):
        file_paths_list: typing.List[str] = wbd.gui.image_selection_dlg.ImageFileDialog.open_dlg_and_get_image_paths()
        logging.debug("file_paths_list = " + str(file_paths_list))
        for file_path_str in file_paths_list:
            datetime_string = wbd.wbd_global.get_today_datetime_string()
            (image_file_bytes, image_taken_qdatetime) = wbd.wbd_global.process_image(file_path_str)
            if image_taken_qdatetime is not None:
                datetime_string = image_taken_qdatetime.toString(wbd.wbd_global.QT_DATETIME_FORMAT_STR)
            new_entry_id_int = wbd.model.EntryM.add(datetime_string, i_image_file=image_file_bytes)
            wbd.wbd_global.active_state.EntryM.add(new_entry_id_int)

        self.update_gui(EventSource.image_import)

    def on_import_action_triggered(self):
        import_file_path_str, _ = QtWidgets.QFileDialog.getOpenFileName(filter="CSV files (*.csv)")
        wbd.model.import_entries_from_csv(import_file_path_str)
        self.update_gui(EventSource.importing)
        #######self.tags_cw3.populate_all_tags_list()

    def on_set_user_dir_action_triggered(self):
        new_dir_str = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Choose dir", "/home", QtWidgets.QFileDialog.ShowDirsOnly
        )
        logging.debug("New user dir: " + new_dir_str)

        config = configparser.ConfigParser()
        config.add_section("general")
        config.set(
            wbd.wbd_global.SETTINGS_GENERAL_STR,
            wbd.wbd_global.SETTINGS_USER_DIR_STR,
            new_dir_str
        )
        with open(wbd.wbd_global.SETTINGS_FILE_STR, "w") as file:
            config.write(file)

        self.update_gui(EventSource.application_start)

    def show_user_guide(self):
        with open("web/user_guide.content.html", "r") as user_guide_file:
            QtWidgets.QMessageBox.information(self, "User Guide", user_guide_file.read())
        # TODO: We will need a custom box here with a scrollbar

    def show_about_box(self):
        QtWidgets.QMessageBox.about(
            self, "About " + wbd.wbd_global.WBD_APPLICATION_NAME_STR,
            (
                '<p>Concept and programming by Tord Dellsén (SunyataZero) and'
                '<a href="https://gitlab.com/SunyataZero/well-being-diary/graphs/master">other programming contributors</a></p>'
                '<p>Design help by: Tenzin</p>'
                '<p>Photography (for icons) by Torgny Dellsén - '
                '<a href="https://torgnydellsen.zenfolio.com/">torgnydellsen.zenfolio.com</a></p>'
                '<p>Software License: GPLv3</p>'
                '<p>Photo license: CC BY-SA 4.0</p>'
                "<p>Art license: CC PD</p>"
            )
        )

    # Widgets..

    # ..filters

    def on_diary_view_activated(self):
        self.check_and_delete_empty_active_entry()
        #wbd.wbd_global.active_view = wbd.wbd_global.ViewEnum.diary
        wbd.wbd_global.active_state.clear_entries()
        self.update_gui(EventSource.diary_view_activated)

    def on_page_changed(self):
        self.check_and_delete_empty_active_entry()
        wbd.wbd_global.active_state.question_id = wbd.wbd_global.NO_ACTIVE_QUESTION_INT
        #wbd.wbd_global.active_view = wbd.wbd_global.ViewEnum.diary
        wbd.wbd_global.active_state.clear_entries()
        self.update_gui(EventSource.page_changed)

    def on_filters_changed(self):
        self.check_and_delete_empty_active_entry()
        wbd.wbd_global.active_state.question_id = wbd.wbd_global.NO_ACTIVE_QUESTION_INT
        #wbd.wbd_global.active_view = wbd.wbd_global.ViewEnum.diary
        wbd.wbd_global.active_state.clear_entries()
        # wbd.wbd_global.active_state.current_page_number_int = 1  # -resetting
        self.update_gui(EventSource.filters_changed)

    # ..questions

    def on_question_view_write_entry(self):
        self.check_and_delete_empty_active_entry()
        wbd.wbd_global.active_state.question_id = wbd.wbd_global.NO_ACTIVE_QUESTION_INT
        time_as_iso_str = wbd.wbd_global.get_today_datetime_string()
        new_entry_id_int = wbd.model.EntryM.add(time_as_iso_str)
        # wbd.wbd_global.EntryM.add(new_entry_id_int)
        wbd.wbd_global.active_state.add_entry(new_entry_id_int)
        self.update_gui(EventSource.question_activated)

    def on_question_item_row_changed(self):
        self.check_and_delete_empty_active_entry()
        today_datetime_string = wbd.wbd_global.get_today_datetime_string()

        new_entry_id_int = wbd.model.EntryM.add(today_datetime_string)
        wbd.wbd_global.active_state.clear_entries()
        wbd.wbd_global.active_state.add_entry(new_entry_id_int)


        # TODO: Only if first time editing
        if wbd.wbd_global.active_state.question_id != wbd.wbd_global.NO_ACTIVE_QUESTION_INT:
            tags_suggested_list = wbd.model.TagsSuggestedForQuestionM.get_all()
            for tag_suggested in tags_suggested_list:
                if tag_suggested.tag_is_preselected_bool:
                    wbd.model.add_tag_entry_relation(tag_suggested.id_int, new_entry_id_int)

        self.update_gui(EventSource.question_activated)

    # ..diary

    def on_diary_entry_edit(self, i_diary_entry_id: int):
        if i_diary_entry_id is None:
            return

        wbd.wbd_global.active_state.add_entry(i_diary_entry_id)

        #wbd.wbd_global.active_view = wbd.wbd_global.ViewEnum.entry

        # self.edit_entry_cw.reinitiate()
        ####self.update_gui()  # -so that the button texts are updated

        self.update_gui(EventSource.entry_edit)

    # ..entry

    def on_entry_area_close(self):
        self.check_and_delete_empty_active_entry()
        wbd.wbd_global.active_state.remove_last_entry()
        wbd.wbd_global.active_state.filters.reset()
        self.update_gui(EventSource.entry_area_close)

    def on_entry_area_close_and_next(self):
        result_bool = self.questions_cw3.go_to_next_question()
        if not result_bool:
            wbd.wbd_global.active_state.question_id = wbd.wbd_global.NO_ACTIVE_QUESTION_INT
            self.on_entry_area_close()

    def on_context_menu_share(self, i_entry_id: int):
        wbd.gui.email_sharing_dlg.EmailSharingDlg.show_dlg_and_return_emails(i_entry_id)

    def on_context_menu_delete(self):
        self.update_gui(EventSource.entry_delete)

    def on_entry_selected_tag_changed(self, i_tag_id: int):
        wbd.wbd_global.active_state.tag_id = i_tag_id
        self.update_gui(wbd.wbd_global.EventSource.entry_selected_tag_changed)

    def on_entry_suggested_tag_changed(self, i_tag_id: int):
        wbd.wbd_global.active_state.tag_id = i_tag_id
        self.update_gui(wbd.wbd_global.EventSource.entry_suggested_tags_tag_changed)

    def on_tag_added_for_entry_changed(self, i_tag_id: int):
        wbd.wbd_global.active_state.tag_id = i_tag_id
        self.update_gui(wbd.wbd_global.EventSource.tag_added_for_entry)

    # ..tags

    def on_tags_area_row_changed(self, i_new_tag_id: int, i_ctrl_active: bool, i_shift_active: bool):
        wbd.wbd_global.active_state.tag_id = i_new_tag_id
        if i_ctrl_active:
            self.edit_entry_cw.add_active_tag(i_new_tag_id)
        if i_shift_active:
            self.filters_cw3.set_tag(i_new_tag_id)

        # Please note: The update_gui method is called in the Tags class

    def on_tags_add_tag_for_entry(self):
        self.edit_entry_cw.add_active_tag(wbd.wbd_global.active_state.tag_id)

    # overridden
    def closeEvent(self, i_QCloseEvent):
        logging.info("MainWindow - closeEvent")
        self.check_and_delete_empty_active_entry()

        wbd.model.export_to_csv(wbd.model.ExportTypeEnum.all)
        self.on_backup_using_sqlite_triggered()
        #####.on_backup_triggered()
        #######wbd.db.take_iter_db_dump()

        wbd.db.DbHelperM.close_db_connection()

        super().closeEvent(i_QCloseEvent)

    def check_and_delete_empty_active_entry(self):
        if len(wbd.wbd_global.active_state.edit_entry_id_list) == 0:
            logging.debug("check_and_delete_active_entry - no entries in edit list")
            return
        if not wbd.model.EntryM.does_entry_exist(wbd.wbd_global.active_state.last_entry()):
            logging.error("check_and_delete_active_entry - entry doesn't exist")
            return
        # Checking if the entry has been edited in a relevant way..
        diary_entry = wbd.model.EntryM.get(wbd.wbd_global.active_state.last_entry())
        if diary_entry.diary_text_str == "" and diary_entry.image_file_bytes is None:
            # ..if so we remove the entry
            wbd.model.EntryM.remove(wbd.wbd_global.active_state.last_entry())
            wbd.wbd_global.active_state.remove_last_entry()
            logging.debug("check_and_delete_active_entry - entry removed, id = " + str(wbd.wbd_global.active_state.last_entry()))
        else:
            logging.debug("diary_entry.diary_text_str = " + diary_entry.diary_text_str)

    def update_gui(self, i_event_source: EventSource):
        self.updating_gui_bool = True

        # Filters
        if i_event_source in [EventSource.application_start, EventSource.entry_area_close]:
            self.filters_cw3.update_gui()

        # Questions
        """
        if i_event_source == EventSource.undefined:
            self.questions_composite_w3.update_gui()
            # -it's important that we don't run this update when other widgets are selected, because
            # then we will loose the selection in the questions list
        """
        # if i_event_source != EventSource.question_activated
        if i_event_source in [EventSource.application_start]:
            # , EventSource.filters_changed
            self.questions_cw3.update_gui()

        # Central area..
        if wbd.wbd_global.active_state.is_entries_empty():
            # ..Diary
            self.central_qsw.setCurrentIndex(self.diary_widget_nr_int)
            self.pages_cw.setEnabled(True)
            if (i_event_source in [
                EventSource.application_start, EventSource.entry_area_close, EventSource.diary_view_activated,
                EventSource.filters_changed, EventSource.page_changed, EventSource.importing, EventSource.entry_delete
            ]):
                if i_event_source in [EventSource.page_changed, EventSource.entry_area_close]:
                    page_number_int = wbd.wbd_global.active_state.current_page_number_int
                else:
                    # i_event_source == EventSource.diary_view_activated
                    # image_import
                    # i_event_source == EventSource.filters_changed
                    # or i_event_source == EventSource.importing
                    # application_start
                    page_number_int = wbd.model.LAST_PAGE_INT

                diary_entry_list_and_max_pages = wbd.model.EntryM.get_entry_list_and_max_page_nr(
                    wbd.wbd_global.active_state.filters.tag_active_bool, wbd.wbd_global.active_state.filters.tag_id_int,
                    wbd.wbd_global.active_state.filters.search_active_bool, wbd.wbd_global.active_state.filters.search_term_str,
                    wbd.wbd_global.active_state.filters.rating_active_bool, wbd.wbd_global.active_state.filters.rating_int,
                    wbd.wbd_global.active_state.filters.datetime_active_bool,
                    wbd.wbd_global.active_state.filters.start_datetime_string,
                    wbd.wbd_global.active_state.filters.end_datetime_string,
                    page_number_int
                )
                diary_entry_list = diary_entry_list_and_max_pages[0]
                max_pages_int = diary_entry_list_and_max_pages[1]
                """
                # if i_event_source != EventSource.page_changed:
                if (i_event_source in [
                    EventSource.application_start, EventSource.entry_area_close, EventSource.diary_view_activated,
                    EventSource.filters_changed, EventSource.page_changed, EventSource.importing
                ]):
                """
                if i_event_source != EventSource.page_changed:
                    self.pages_cw.set_max_pages_and_go_to_first_page(max_pages_int)
                self.diary_widget.update_gui(diary_entry_list)
        else:
            # ..Entry area
            # if self.central_qsw.currentWidget()
            if i_event_source in [
            EventSource.application_start, EventSource.entry_area_close, EventSource.question_activated,
            EventSource.question_row_changed, EventSource.entry_edit,
            EventSource.tag_added_for_entry, EventSource.entry_selected_tag_changed,
            EventSource.entry_suggested_tags_tag_changed]:
                self.central_qsw.setCurrentIndex(self.edit_entry_nr_int)
                self.pages_cw.setEnabled(False)
                self.edit_entry_cw.update_gui()

        # Tags
        if i_event_source in [
        EventSource.application_start, EventSource.entry_area_close,
        EventSource.image_import, EventSource.importing,
        EventSource.tag_added_for_entry, EventSource.entry_selected_tag_changed,
        EventSource.entry_suggested_tags_tag_changed, EventSource.entry_delete
        ]:
            self.tags_cw3.update_gui(i_event_source)

        self.updating_gui_bool = False


class PagesCw(QtWidgets.QWidget):
    page_changed_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()

        vbox1 = QtWidgets.QVBoxLayout()
        self.setLayout(vbox1)

        pages_hbox_l2 = QtWidgets.QHBoxLayout()
        vbox1.addLayout(pages_hbox_l2)

        self.title_qll = QtWidgets.QLabel("Pages:")
        pages_hbox_l2.addWidget(self.title_qll)

        pages_hbox_l2.addStretch(1)
        self.first_page_qpb = QtWidgets.QPushButton("[Now] |<")
        # self.first_page_qpb.setFixedWidth(30)
        self.first_page_qpb.clicked.connect(self.on_first_page_button_clicked)
        pages_hbox_l2.addWidget(self.first_page_qpb)
        self.prev_page_qpb = QtWidgets.QPushButton("<")
        self.prev_page_qpb.setFixedWidth(30)
        self.prev_page_qpb.clicked.connect(self.on_prev_page_button_clicked)
        pages_hbox_l2.addWidget(self.prev_page_qpb)
        self.page_number_qll = QtWidgets.QLabel("-")
        pages_hbox_l2.addWidget(self.page_number_qll)
        self.next_page_qpb = QtWidgets.QPushButton(">")
        self.next_page_qpb.setFixedWidth(30)
        self.next_page_qpb.clicked.connect(self.on_next_page_button_clicked)
        pages_hbox_l2.addWidget(self.next_page_qpb)
        self.last_page_qpb = QtWidgets.QPushButton(">|")
        self.last_page_qpb.setFixedWidth(30)
        self.last_page_qpb.clicked.connect(self.on_last_page_button_clicked)
        pages_hbox_l2.addWidget(self.last_page_qpb)

    def on_first_page_button_clicked(self):
        wbd.wbd_global.active_state.current_page_number_int = 1
        self.page_changed_signal.emit()
        self.update_gui()

    def on_prev_page_button_clicked(self):
        if wbd.wbd_global.active_state.current_page_number_int > 1:
            wbd.wbd_global.active_state.current_page_number_int -= 1
        self.page_changed_signal.emit()
        self.update_gui()

    def on_next_page_button_clicked(self):
        wbd.wbd_global.active_state.current_page_number_int += 1
        if wbd.wbd_global.active_state.current_page_number_int > self.max_pages_int:
            wbd.wbd_global.active_state.current_page_number_int = self.max_pages_int
        self.page_changed_signal.emit()
        self.update_gui()

    def on_last_page_button_clicked(self):
        wbd.wbd_global.active_state.current_page_number_int = self.max_pages_int
        self.page_changed_signal.emit()
        self.update_gui()

    def set_max_pages_and_go_to_first_page(self, i_max_pages: int):
        self.max_pages_int = i_max_pages
        if self.max_pages_int < 1:
            self.max_pages_int = 1
        wbd.wbd_global.active_state.current_page_number_int = 1
        self.update_gui()

    def update_gui(self):
        current_page_str = str(wbd.wbd_global.active_state.current_page_number_int)
        max_page_str = str(self.max_pages_int)
        self.page_number_qll.setText(current_page_str + " / " + max_page_str)
