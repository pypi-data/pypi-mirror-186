"""
Module comments:
Global vars are used for storing some of the global application states.
Please don't use global vars for storing other types of values
Also, please collect all global vars in this file
"""

import logging
import enum
import os
import datetime
import subprocess
import io
import typing
from PySide6 import QtCore
import PIL.Image
import PIL.ExifTags
import configparser


# Directory and file names
IMAGES_DIR_STR = "thumbnail_images"
ICONS_DIR_STR = "icons"
BACKUP_DIR_STR = "backups"
EXPORTED_DIR_STR = "exported"
LOGS_DIR_STR = "logs"
PUBLIC_DIR_STR = "public"
USER_IMAGES_DIR_STR = "images"
ITERDUMP_DIR_STR = "iterdump"
LOG_FILE_NAME_STR = "wbd.log"
DATABASE_FILE_STR = "wbd_database.sqlite"
DB_IN_MEMORY_STR = ":memory:"


db_file_exists_at_application_startup_bl = False
testing_bool = False
database_debugging_bool = False

WBD_APPLICATION_VERSION_STR = "prototype 5"
WBD_APPLICATION_NAME_STR = "Well-Being Diary"
DIARY_ENTRIES_PER_PAGE_INT = 10
TMP_EMAIL_ATTACHMENTS_DIR_STR = "tmp_email_attachments"

NO_ACTIVE_ROW_INT = -1
NO_ACTIVE_QUESTION_INT = -1
########NO_ACTIVE_FILTER_PRESET_INT = -1
NO_ACTIVE_TAG_INT = -1
NO_DIARY_ENTRY_EDITING_INT = -1
NO_VIEW_ACTIVE_INT = -1
NO_GROUP_ACTIVE_INT = -1
DATETIME_NOT_SET_STR = ""
QT_NO_ROW_SELECTED_INT = -1

# Image related constants
ORIENTATION_EXIF_TAG_NAME_STR = "Orientation"
DATETIME_ORIGINAL_EXIF_TAG_NAME_STR = "DateTimeOriginal"
SIZE_TE = (512, 512)
JPEG_FORMAT_STR = "JPEG"

# Datetime formats
# Python: https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat
# SQLite: https://www.sqlite.org/lang_datefunc.html
# Qt: http://doc.qt.io/qt-5/qdatetime.html#fromString-1
# Camera EXIF: https://www.awaresystems.be/imaging/tiff/tifftags/privateifd/exif/datetimeoriginal.html
PY_DATETIME_FORMAT_STR = "%Y-%m-%dT%H:%M:%S"
PY_DATE_ONLY_FORMAT_STR = "%Y-%m-%d"
PY_DATETIME_FILENAME_FORMAT_STR = "%Y-%m-%dT%H-%M-%S"
QT_EXIF_DATETIME_FORMAT_STR = "yyyy:MM:dd HH:mm:ss"
# -please note the colons instead of dashes in the date
QT_DATETIME_FORMAT_STR = "yyyy-MM-ddTHH:mm:ss"
QT_DATE_ONLY_FORMAT_STR = "yyyy-MM-dd"


class EventSource(enum.Enum):
    application_start = enum.auto()
    page_changed = enum.auto()
    filters_changed = enum.auto()
    question_activated = enum.auto()

    tags_changed = enum.auto()

    entry_edit = enum.auto()
    entry_delete = enum.auto()

    importing = enum.auto()

    diary_view_activated = enum.auto()
    entry_area_close = enum.auto()

    image_import = enum.auto()

    collection_changed = enum.auto()
    view_tags_tag_changed = enum.auto()
    all_tags_tag_changed = enum.auto()

    tag_deleted = enum.auto()
    tag_added = enum.auto()

    add_tag_to_view = enum.auto()
    remove_tag_from_view = enum.auto()
    tag_edited = enum.auto()
    all_tags_sort_type_changed = enum.auto()
    view_added = enum.auto()
    entry_selected_tag_changed = enum.auto()
    tag_added_for_entry = enum.auto()
    question_row_changed = enum.auto()
    entry_suggested_tags_tag_changed = enum.auto()
    # -please note that unlike the other _tag_changed enums this one is sent outside of the tags class


SETTINGS_FILE_STR = "settings.ini"
SETTINGS_GENERAL_STR = "general"
SETTINGS_USER_DIR_STR = "user_dir_str"
SETTINGS_DIARY_FONT_SIZE_STR = "diary_font_size"
DEFAULT_DIARY_FONT_SIZE_INT = 13
SETTINGS_ENTRY_FONT_SIZE_STR = "entry_font_size"
DEFAULT_ENTRY_FONT_SIZE_INT = 14
DEFAULT_USER_DIR_STR = "/home/sunyata/PycharmProjects/well-being-diary/user_files"


class MoveDirectionEnum(enum.Enum):
    up = 1
    down = 2


class SortType(enum.Enum):
    sort_by_default_db_order = -2
    sort_by_custom_order = -1
    sort_by_name = 0
    sort_by_frequency = 1
    sort_by_time = 2


class Filters:
    def __init__(self):
        self.reset()

    def reset(self):
        self.tag_active_bool = False
        self.tag_id_int = NO_ACTIVE_TAG_INT
        self.search_active_bool = False
        self.search_term_str = ""
        self.rating_active_bool = False
        self.rating_int = 0
        self.datetime_active_bool = False
        self.start_datetime_string = DATETIME_NOT_SET_STR
        self.end_datetime_string = DATETIME_NOT_SET_STR


class ApplicationState:
    def __init__(self):
        self.current_page_number_int = 1
        self.filters = Filters()
        self.question_id: int = NO_ACTIVE_QUESTION_INT
        self.edit_entry_id_list: list = []
        self.collection_id: int = NO_VIEW_ACTIVE_INT
        self.tag_id: int = NO_ACTIVE_TAG_INT

    #Please note that we can use the view_id to see if the focus is on the left or right tags list

    """
    self.selected_friends_id_list = []

    def add_selected_friend(self, i_new_friend_id: int) -> None:
        self.selected_friends_id_list.append(i_new_friend_id)

    def remove_selected_friend(self, i_new_friend_id: int) -> None:
        self.selected_friends_id_list.remove(i_new_friend_id)

    def clear_selected_friends_list(self) -> None:
        self.selected_friends_id_list.clear()
    """

    def add_entry(self, new_entry_id: int) -> None:
        if new_entry_id not in self.edit_entry_id_list:
            self.edit_entry_id_list.append(new_entry_id)

    def last_entry(self):
        if len(self.edit_entry_id_list) > 0:
            return self.edit_entry_id_list[-1]
        else:
            return False

    def is_entries_empty(self) -> bool:
        if len(self.edit_entry_id_list) > 0:
            return False
        else:
            return True

    def clear_entries(self):
        self.edit_entry_id_list.clear()

    def remove_last_entry(self) -> bool:
        # -bool is unused at the time of writing
        if len(self.edit_entry_id_list) > 0:
            del self.edit_entry_id_list[-1]
            return True
        else:
            return False


active_state = ApplicationState()


def get_base_dir_path(*args, i_file_name: str="") -> str:
    first_str = os.path.abspath(__file__)
    # -__file__ is the file that started the application, in other words mindfulness-at-the-computer.py
    second_str = os.path.dirname(first_str)
    base_dir_str = os.path.dirname(second_str)
    ret_path = base_dir_str
    for arg in args:
        ret_path = os.path.join(ret_path, arg)
    os.makedirs(ret_path, exist_ok=True)
    if i_file_name:
        ret_path = os.path.join(ret_path, i_file_name)
    return ret_path


def get_diary_font_size() -> int:
    config = configparser.ConfigParser()
    config.read(SETTINGS_FILE_STR)
    ret_font_size_int = 0
    ret_font_size_int = config.getint(
        SETTINGS_GENERAL_STR,
        SETTINGS_DIARY_FONT_SIZE_STR,
        fallback=DEFAULT_DIARY_FONT_SIZE_INT
    )
    return ret_font_size_int


def get_entry_font_size() -> int:
    config = configparser.ConfigParser()
    config.read(SETTINGS_FILE_STR)
    ret_font_size_int = 0
    try:
        ret_font_size_int = config.getint(SETTINGS_GENERAL_STR, SETTINGS_ENTRY_FONT_SIZE_STR)
    except configparser.NoOptionError:
        ret_font_size_int = DEFAULT_ENTRY_FONT_SIZE_INT
    return ret_font_size_int


def get_user_dir_path(*args, i_file_name: str="") -> str:
    ret_path = ""
    if testing_bool:
        # ret_path = "/home/sunyata/PycharmProjects/my-gtd/example"
        ret_path = DEFAULT_USER_DIR_STR
    else:
        config = configparser.ConfigParser()
        config.read(SETTINGS_FILE_STR)
        # TODO: Absolute path for settings file

        try:
            ret_path = config[SETTINGS_GENERAL_STR][SETTINGS_USER_DIR_STR]
        except KeyError:
            ret_path = DEFAULT_USER_DIR_STR
            # -using the application dir if the settings can't be read
        """
        if not ret_path:
            raise Exception("No path has been set as the base dir")
        """
    for arg in args:
        ret_path = os.path.join(ret_path, arg)
    os.makedirs(ret_path, exist_ok=True)
    if i_file_name:
        ret_path = os.path.join(ret_path, i_file_name)
    return ret_path


def get_icon_path(i_file_name: str) -> str:
    ret_icon_path_str = get_base_dir_path(ICONS_DIR_STR, i_file_name=i_file_name)
    return ret_icon_path_str


def get_database_filename() -> str:
    # i_backup_timestamp: str = ""
    # if i_backup_timestamp:
    #     database_filename_str = i_backup_timestamp + "_" + DATABASE_FILE_STR
    if testing_bool:
        return DB_IN_MEMORY_STR
    else:
        # ret_path_str = os.path.join(get_base_dir(), DEFAULT_USER_DIR_STR, DATABASE_FILE_STR)
        ret_path_str = get_user_dir_path(i_file_name=DATABASE_FILE_STR)
        return ret_path_str


def get_user_logs_path(i_file_name: str = "") -> str:
    log_files_path_str = get_base_dir_path(LOGS_DIR_STR)
    if i_file_name:
        log_files_path_str = os.path.join(log_files_path_str, i_file_name)
    return log_files_path_str


def get_public_path(i_file_name: str = "") -> str:
    public_files_path_str = get_base_dir_path(PUBLIC_DIR_STR)
    if i_file_name:
        public_files_path_str = os.path.join(public_files_path_str, i_file_name)
    return public_files_path_str


def get_user_backup_path(i_file_name: str = "") -> str:
    # file_or_dir_path_str = os.path.join(get_base_dir(), DEFAULT_USER_DIR_STR, BACKUP_DIR_STR)
    file_or_dir_path_str = get_user_dir_path(BACKUP_DIR_STR, i_file_name=i_file_name)
    return file_or_dir_path_str


def get_user_tmp_email_attachments_path(i_file_name: str = "") -> str:
    user_files_path_str = get_user_dir_path(TMP_EMAIL_ATTACHMENTS_DIR_STR, i_file_name=i_file_name)
    return user_files_path_str


def get_user_iterdump_path(i_file_name: str = "") -> str:
    user_files_path_str = get_user_dir_path(ITERDUMP_DIR_STR, i_file_name=i_file_name)
    return user_files_path_str


def get_user_exported_path(i_file_name: str = "") -> str:
    file_path_str = get_user_dir_path(EXPORTED_DIR_STR, i_file_name=i_file_name)
    return file_path_str


def get_user_exported_images_path(i_file_name: str = "") -> str:
    path_str = get_user_dir_path(EXPORTED_DIR_STR, USER_IMAGES_DIR_STR, i_file_name=i_file_name)
    return path_str


def get_testing_images_path(i_file_name: str="") -> str:
    testing_images_path_str = get_base_dir_path("varia", "unprocessed_image_files_for_testing", i_file_name=i_file_name)
    return testing_images_path_str


RGB_STR = 'RGB'
BW_STR = 'L'


def process_image(i_file_path: str) -> (bytes, QtCore.QDateTime):
    image_pi: PIL.Image = PIL.Image.open(i_file_path)

    # Time when the photo was taken
    time_photo_taken_qdatetime = get_datetime_image_taken(image_pi)
    # -important that this is done before rotating since rotating removes exif data

    # Rotating
    rotation_degrees_int = get_rotation_degrees(image_pi)
    if rotation_degrees_int != 0:
        image_pi = image_pi.rotate(rotation_degrees_int, expand=True)
        # -Warning: Rotating removes exif data (unknown why)

    if image_pi.mode != RGB_STR:
        image_pi = image_pi.convert(RGB_STR)
    # -How to check is described in this answer: https://stackoverflow.com/a/43259180/2525237
    image_pi.thumbnail(SIZE_TE, PIL.Image.ANTIALIAS)
    # -Please note that exif metadata is removed. If we want to
    #  keep exif metadata: https://stackoverflow.com/q/17042602/2525237

    image_byte_stream = io.BytesIO()
    image_pi.save(image_byte_stream, format=JPEG_FORMAT_STR)
    image_bytes = image_byte_stream.getvalue()

    return (image_bytes, time_photo_taken_qdatetime)


def jpg_image_file_to_bytes(i_file_path: str) -> bytes:
    image_pi: PIL.Image = PIL.Image.open(i_file_path)
    image_byte_stream = io.BytesIO()
    image_pi.save(image_byte_stream, format=JPEG_FORMAT_STR)
    image_bytes = image_byte_stream.getvalue()
    return image_bytes


def get_rotation_degrees(i_image_pi: PIL.Image, i_switch_direction: bool=False) -> int:
    # Inspiration for this function:
    # https://stackoverflow.com/questions/4228530/pil-thumbnail-is-rotating-my-image
    # https://coderwall.com/p/nax6gg/fix-jpeg-s-unexpectedly-rotating-when-saved-with-pil
    ret_degrees_int = 0

    orientation_tag_key_str = ""
    for tag_key_str in PIL.ExifTags.TAGS.keys():
        if PIL.ExifTags.TAGS[tag_key_str] == ORIENTATION_EXIF_TAG_NAME_STR:
            orientation_tag_key_str = tag_key_str
            break
    if orientation_tag_key_str == "":
        logging.warning("get_rotation_degrees - exif tag not found")

    ret_degrees_int = 0
    try:
        exif_data_dict = dict(i_image_pi._getexif().items())
        if exif_data_dict[orientation_tag_key_str] == 3:
            ret_degrees_int = 180
        elif exif_data_dict[orientation_tag_key_str] == 6:
            ret_degrees_int = 270
        elif exif_data_dict[orientation_tag_key_str] == 8:
            ret_degrees_int = 90
        if i_switch_direction:
            ret_degrees_int = -ret_degrees_int
    except AttributeError:
        # -A strange problem: If we use hasattr(i_image_pi, "_getexif") this will return True,
        #  so instead we use this exception handling
        logging.warning(
            "get_rotation_degrees - Image doesn't have exif data. This may be because it has already been processed by an application"
        )

    return ret_degrees_int


def get_datetime_image_taken(i_image_pi: PIL.Image) -> QtCore.QDateTime:
    # Please note that usually (always?) the time we get from the camera is in the UTC time zone:
    # https://photo.stackexchange.com/questions/82166/is-it-possible-to-get-the-time-a-photo-was-taken-timezone-aware
    # So we need to convert the time that we get
    ret_datetime_qdt = None
    datetime_original_tag_key_str = ""
    for tag_key_str in PIL.ExifTags.TAGS.keys():
        if PIL.ExifTags.TAGS[tag_key_str] == DATETIME_ORIGINAL_EXIF_TAG_NAME_STR:
            datetime_original_tag_key_str = tag_key_str
            break
    if datetime_original_tag_key_str == "":
        logging.warning("get_datetime_image_taken - exif tag not found")
    try:
        exif_data_dict = dict(i_image_pi._getexif().items())
        # -Good to be aware that _getexif() is an experimental function:
        #  https://stackoverflow.com/a/48428533/2525237
        datetime_exif_string = exif_data_dict[datetime_original_tag_key_str]
        logging.debug("datetime_exif_string = " + datetime_exif_string)
        from_camera_qdt = QtCore.QDateTime.fromString(datetime_exif_string, QT_EXIF_DATETIME_FORMAT_STR)
        from_camera_qdt.setTimeSpec(QtCore.Qt.UTC)
        ret_datetime_qdt = from_camera_qdt.toLocalTime()
        logging.debug("from_camera_qdt.toString = " + ret_datetime_qdt.toString(QT_DATETIME_FORMAT_STR))
    except AttributeError:
        # -A strange problem: If we use hasattr(i_image_pi, "_getexif") this will return True,
        #  so instead we use this exception handling
        logging.warning("get_datetime_image_taken - Image doesn't have exif data. This may be because it has already been processed by an application")

    return ret_datetime_qdt


def get_today_datetime_string() -> str:
    now_pdt = datetime.datetime.now()
    time_as_iso_str = now_pdt.strftime(PY_DATE_ONLY_FORMAT_STR)
    return time_as_iso_str


def get_now_datetime_string() -> str:
    now_pdt = datetime.datetime.now()
    time_as_iso_str = now_pdt.strftime(PY_DATETIME_FORMAT_STR)
    return time_as_iso_str


def clear_widget_and_layout_children(qlayout_or_qwidget):
    if qlayout_or_qwidget.widget():
        qlayout_or_qwidget.widget().deleteLater()
    elif qlayout_or_qwidget.layout():
        while qlayout_or_qwidget.layout().count():
            child_qlayoutitem = qlayout_or_qwidget.takeAt(0)
            clear_widget_and_layout_children(child_qlayoutitem)  # Recursive call


def removing_oldest_files(directory_path: str, i_suffix: str, i_nr_of_files_to_keep: int):
    # Removing the oldest files
    filtered_files_list = [
        fn for fn in os.listdir(directory_path) if fn.endswith(i_suffix)
    ]
    sorted_and_filtered_files_list = sorted(filtered_files_list)
    # logging.debug("sorted_and_filtered_files_list = " + str(sorted_and_filtered_files_list))
    for file_name_str in sorted_and_filtered_files_list[:-i_nr_of_files_to_keep]:
        file_path_str = os.path.join(directory_path, file_name_str)
        os.remove(file_path_str)
        logging.debug("Old backup file " + file_name_str + " was removed")


def open_directory(i_directory_path: str):
    try:
        # noinspection PyUnresolvedReferences
        os.startfile(i_directory_path)
        # -only available on windows
    except:
        subprocess.Popen(["xdg-open", i_directory_path])

