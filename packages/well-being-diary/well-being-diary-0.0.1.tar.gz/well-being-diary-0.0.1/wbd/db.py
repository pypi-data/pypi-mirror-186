import shutil
import sqlite3
import logging
import wbd.wbd_global
import wbd.model
# -TODO: This may be a risk of having problems with circular imports
#  We may want to move the function calls (which is only for setting up data) into another module
#  so that we can remove this import
import os
import enum
import datetime
import wbd.exception_handling

SQLITE_FALSE_INT = 0
SQLITE_TRUE_INT = 1
ALWAYS_AT_TOP_INT = -1


class DataSetupType(enum.Enum):
    test_data = enum.auto()
    first_start_data = enum.auto()


def get_schema_version(i_db_conn: sqlite3.Connection) -> int:
    t_cursor = i_db_conn.execute("PRAGMA user_version")
    ret_version_int = t_cursor.fetchone()[0]
    return ret_version_int


def set_schema_version(i_db_conn: sqlite3.Connection, i_version: int):
    i_db_conn.execute("PRAGMA user_version={:d}".format(i_version))


def db_exec(i_sql_string: str, i_values: tuple) -> sqlite3.Cursor:
    # i_sql_string is required to hold VALUES(,) or "?"
    db_connection = wbd.db.DbHelperM.get_db_connection()
    db_cursor = db_connection.cursor()
    """
    if len(i_values) > 0:
        i_first_value = i_values[0]
        if isinstance(i_first_value, bytes):
            logging.debug(f"db_exec: {i_sql_string=} {i_values=}")
    """
    try:
        db_cursor = db_cursor.execute(i_sql_string, i_values)
    except sqlite3.IntegrityError:
        wbd.exception_handling.error("sqlite3.IntegrityError")
    db_connection.commit()
    return db_cursor


######## NOT USED: WORK IN PROGRESS
# Please note: If this is going to work then we need to be sure that the text for an entry is only set
#  when entry_edit is opened for the entry (rather than in update_gui). This is because we can't
#  trust that the state of the text has been committed to the database (it probably hasn't)
def db_update_entry_text_without_commit(i_new_text: str, i_id: int) -> sqlite3.Cursor:
    # i_sql_string is required to hold VALUES(,) or "?"
    db_connection = wbd.db.DbHelperM.get_db_connection()
    sql_string = "UPDATE " + wbd.db.DbSchemaM.EntryTable.name\
        + " SET " + wbd.db.DbSchemaM.EntryTable.Cols.text + " = " + i_new_text\
        + " WHERE " + wbd.db.DbSchemaM.EntryTable.Cols.id + " = " + str(i_id)
    db_cursor = db_connection.cursor()
    try:
        db_cursor = db_cursor.execute(sql_string)
    except sqlite3.IntegrityError:
        wbd.exception_handling.error("sqlite3.IntegrityError")
    # db_connection.commit()
    return db_cursor


class DbSchemaM:
    # The reason that an integer is used as the key for the questions and tags rather than the title (which is unique)
    # is that we are storing the id in the relation tables, and we don't want to update these tables whenever the title
    # changes. Another reason for keeping the integer is that it's faster. The tables themselves doesn't have many
    # entries, but they are referenced in the relation tables, which can be large

    class FilterPresetTable:
        name = "filter_preset"

        class Cols:
            id = "id"  # key
            sort_order = "sort_order"
            title = "title"  # -UNIQUE
            tag_active = "tag_active"
            tag_id_ref = "tag_id_ref"
            search_active = "search_active"
            search_term = "search_term"
            rating_active = "rating_active"
            rating = "rating"
            datetime_active = "datetime_active"
            start_date = "start_date"
            end_date = "end_date"

    class QuestionTable:
        name = "question"

        class Cols:
            id = "id"  # key
            sort_order = "sort_order"
            title = "title"  # unique
            description = "description"

    class EntryTable:
        name = "entry"

        class Cols:
            id = "id"  # key
            datetime_added = "datetime_added"
            sort_order = "sort_order"  # unused
            rating = "rating"
            text = "diary_text"
            image_file = "image_file"

    class TagTable:
        name = "tag"

        class Cols:
            id = "id"  # key
            sort_order = "sort_order"
            title = "title"  # unique
            description = "description"
            friend_email = "friend_email"

    class FriendTable:
        name = "friend"

        class Cols:
            id = "id"  # key
            sort_order = "sort_order"
            friend_name = "friend_name"
            email = "email"  # unique

    class ViewTable:
        name = "view"

        class Cols:
            id = "id"  # key
            sort_order = "sort_order"
            title = "title"  # unique
            collection_type = "collection_type"

    class ViewTagRelationTable:
        name = "view_tag_relation"

        class Cols:
            view_id_ref = "view_id"
            tag_id_ref = "tag_id"
            # -these two above create the composite keys
            sort_order = "sort_order"

    class TagQuestionRelationTable:
        name = "tag_question_relation"

        class Cols:
            tag_id_ref = "tag_id"
            question_id_ref = "question_id"
            # -these two above create the composite keys
            sort_order = "sort_order"
            tag_is_preselected = "tag_is_preselected"

    class TagEntryRelationTable:
        name = "tag_entry_relation"

        class Cols:
            tag_id_ref = "tag_id"
            entry_id_ref = "entry_id"
            sort_order = "sort_order"
            # -these two above create the composite keys


def initial_schema_and_setup(i_db_conn):
    # Auto-increment is not needed for the primary key in our case:
    # https://www.sqlite.org/autoinc.html

    i_db_conn.execute(
        "CREATE TABLE " + DbSchemaM.FilterPresetTable.name
        + "(" + DbSchemaM.FilterPresetTable.Cols.id + " INTEGER PRIMARY KEY"
        + ", " + DbSchemaM.FilterPresetTable.Cols.sort_order + " INTEGER NOT NULL"
        + ", " + DbSchemaM.FilterPresetTable.Cols.title + " TEXT NOT NULL UNIQUE"
        + ", " + DbSchemaM.FilterPresetTable.Cols.tag_active + " INTEGER NOT NULL DEFAULT " + str(SQLITE_FALSE_INT)
        + ", " + DbSchemaM.FilterPresetTable.Cols.tag_id_ref + " INTEGER NOT NULL DEFAULT "
        + str(wbd.wbd_global.NO_ACTIVE_TAG_INT)
        + ", " + DbSchemaM.FilterPresetTable.Cols.search_active + " INTEGER NOT NULL DEFAULT " + str(SQLITE_FALSE_INT)
        + ", " + DbSchemaM.FilterPresetTable.Cols.search_term + " TEXT NOT NULL DEFAULT ''"
        + ", " + DbSchemaM.FilterPresetTable.Cols.rating_active + " INTEGER NOT NULL DEFAULT " + str(SQLITE_FALSE_INT)
        + ", " + DbSchemaM.FilterPresetTable.Cols.rating + " INTEGER NOT NULL DEFAULT " + str(0)
        + ", " + DbSchemaM.FilterPresetTable.Cols.datetime_active + " INTEGER NOT NULL DEFAULT " + str(SQLITE_FALSE_INT)
        + ", " + DbSchemaM.FilterPresetTable.Cols.start_date + " TEXT NOT NULL DEFAULT "
        + "'" + str(wbd.wbd_global.DATETIME_NOT_SET_STR) + "'"
        + ", " + DbSchemaM.FilterPresetTable.Cols.end_date + " TEXT NOT NULL DEFAULT "
        + "'" + str(wbd.wbd_global.DATETIME_NOT_SET_STR) + "'"
        + ")"
    )

    """
    i_db_conn.execute(
        "INSERT INTO " + DbSchemaM.FilterPresetTable.name
        + "(" + DbSchemaM.FilterPresetTable.Cols.id
        + ", " + DbSchemaM.FilterPresetTable.Cols.sort_order
        + ", " + DbSchemaM.FilterPresetTable.Cols.title
        + ") VALUES (?, ?, ?)",
        (wbd.wbd_global.NO_ACTIVE_FILTER_PRESET_INT, ALWAYS_AT_TOP_INT, "<i>no filter</i>")
    )
    """

    i_db_conn.execute(
        "CREATE TABLE " + DbSchemaM.QuestionTable.name
        + "(" + DbSchemaM.QuestionTable.Cols.id + " INTEGER PRIMARY KEY"
        + ", " + DbSchemaM.QuestionTable.Cols.sort_order + " INTEGER NOT NULL"
        + ", " + DbSchemaM.QuestionTable.Cols.title + " TEXT NOT NULL UNIQUE"
        + ", " + DbSchemaM.QuestionTable.Cols.description + " TEXT NOT NULL DEFAULT ''"
        + ")"
    )

    """
    i_db_conn.execute(
        "INSERT INTO " + DbSchemaM.QuestionTable.name
        + "(" + DbSchemaM.QuestionTable.Cols.id
        + ", " + DbSchemaM.QuestionTable.Cols.sort_order
        + ", " + DbSchemaM.QuestionTable.Cols.title
        + ", " + DbSchemaM.QuestionTable.Cols.description
        + ") VALUES (?, ?, ?, ?)",
        (wbd.wbd_global.NO_ACTIVE_QUESTION_INT, ALWAYS_AT_TOP_INT, "<i>No question (free writing)</i>", "")
    )
    """

    i_db_conn.execute(
        "CREATE TABLE " + DbSchemaM.EntryTable.name
        + "(" + DbSchemaM.EntryTable.Cols.id + " INTEGER PRIMARY KEY"
        + ", " + DbSchemaM.EntryTable.Cols.datetime_added + " TEXT"
        + ", " + DbSchemaM.EntryTable.Cols.sort_order + " INTEGER"
        + ", " + DbSchemaM.EntryTable.Cols.rating + " INTEGER NOT NULL DEFAULT '" + str(1) + "'"
        + ", " + DbSchemaM.EntryTable.Cols.text + " TEXT"
        + ", " + DbSchemaM.EntryTable.Cols.image_file + " BLOB DEFAULT NULL"
        + ")"
    )
    i_db_conn.execute(
        "CREATE TABLE " + DbSchemaM.TagTable.name
        + "(" + DbSchemaM.TagTable.Cols.id + " INTEGER PRIMARY KEY"
        + ", " + DbSchemaM.TagTable.Cols.sort_order + " INTEGER NOT NULL"
        + ", " + DbSchemaM.TagTable.Cols.title + " TEXT NOT NULL UNIQUE"
        + ", " + DbSchemaM.TagTable.Cols.description + " TEXT NOT NULL DEFAULT ''"
        + ")"
    )
    i_db_conn.execute(
        "CREATE TABLE " + DbSchemaM.ViewTable.name
        + "(" + DbSchemaM.ViewTable.Cols.id + " INTEGER PRIMARY KEY"
        + ", " + DbSchemaM.ViewTable.Cols.sort_order + " INTEGER NOT NULL"
        + ", " + DbSchemaM.ViewTable.Cols.title + " TEXT NOT NULL UNIQUE"
        + ")"
    )

    i_db_conn.execute(
        "CREATE TABLE " + DbSchemaM.TagEntryRelationTable.name
        + "(" + DbSchemaM.TagEntryRelationTable.Cols.tag_id_ref + " INTEGER REFERENCES "
        + DbSchemaM.TagTable.name + "(" + DbSchemaM.TagTable.Cols.id + ")"
        + ", " + DbSchemaM.TagEntryRelationTable.Cols.entry_id_ref + " INTEGER REFERENCES "
        + DbSchemaM.EntryTable.name + "(" + DbSchemaM.EntryTable.Cols.id + ")"
        + ", " + DbSchemaM.TagEntryRelationTable.Cols.sort_order + " INTEGER NOT NULL"
        + ", PRIMARY KEY (" + DbSchemaM.TagEntryRelationTable.Cols.tag_id_ref + ", " + DbSchemaM.TagEntryRelationTable.Cols.entry_id_ref + ")"
        + ") WITHOUT ROWID"
    )

    index_name_str = "idx_tagentryrelation_tagid"
    i_db_conn.execute(
        "CREATE INDEX " + index_name_str + " ON " + DbSchemaM.TagEntryRelationTable.name
        + " (" + DbSchemaM.TagEntryRelationTable.Cols.tag_id_ref + ")"
    )
    index_name_str = "idx_tagentryrelation_entryid"
    i_db_conn.execute(
        "CREATE INDEX " + index_name_str + " ON " + DbSchemaM.TagEntryRelationTable.name
        + " (" + DbSchemaM.TagEntryRelationTable.Cols.entry_id_ref + ")"
    )
    # About indexes in SQLite: https://www.sqlitetutorial.net/sqlite-index/
    # TODO: Add index for entry_id?


    i_db_conn.execute(
        "CREATE TABLE " + DbSchemaM.TagQuestionRelationTable.name
        + "(" + DbSchemaM.TagQuestionRelationTable.Cols.tag_id_ref + " INTEGER REFERENCES "
        + DbSchemaM.TagTable.name + "(" + DbSchemaM.TagTable.Cols.id + ")"
        + ", " + DbSchemaM.TagQuestionRelationTable.Cols.question_id_ref + " INTEGER REFERENCES "
        + DbSchemaM.QuestionTable.name + "(" + DbSchemaM.QuestionTable.Cols.id + ")"
        + ", " + DbSchemaM.TagQuestionRelationTable.Cols.sort_order + " INTEGER NOT NULL DEFAULT " + str(SQLITE_FALSE_INT)
        + ", " + DbSchemaM.TagQuestionRelationTable.Cols.tag_is_preselected + " INTEGER NOT NULL DEFAULT " + str(SQLITE_FALSE_INT)
        + ", PRIMARY KEY (" + DbSchemaM.TagQuestionRelationTable.Cols.tag_id_ref + ", " + DbSchemaM.TagQuestionRelationTable.Cols.question_id_ref + ")"
        + ") WITHOUT ROWID"
    )

    i_db_conn.execute(
        "CREATE TABLE " + DbSchemaM.ViewTagRelationTable.name
        + "(" + DbSchemaM.ViewTagRelationTable.Cols.view_id_ref + " INTEGER REFERENCES "
        + DbSchemaM.ViewTable.name + "(" + DbSchemaM.ViewTable.Cols.id + ")"
        + ", " + DbSchemaM.ViewTagRelationTable.Cols.tag_id_ref + " INTEGER REFERENCES "
        + DbSchemaM.TagTable.name + "(" + DbSchemaM.TagTable.Cols.id + ")"
        + ", " + DbSchemaM.ViewTagRelationTable.Cols.sort_order + " INTEGER NOT NULL DEFAULT " + str(SQLITE_FALSE_INT)
        + ", PRIMARY KEY (" + DbSchemaM.ViewTagRelationTable.Cols.view_id_ref + ", " + DbSchemaM.ViewTagRelationTable.Cols.tag_id_ref + ")"
        + ") WITHOUT ROWID"
    )


"""
Example of db upgrade code:
def upgrade_2_3(i_db_conn):
    backup_db_file()
    i_db_conn.execute(
        "ALTER TABLE " + DbSchemaM.QuestionTable.name + " ADD COLUMN "
        + DbSchemaM.QuestionTable.Cols.labels + " TEXT DEFAULT ''"
    )
"""

"""
def upgrade_1_2(i_db_conn):
    backup_db_file()
    i_db_conn.execute(
        "ALTER TABLE " + DbSchemaM.TagTable.name + " ADD COLUMN "
        + DbSchemaM.TagTable.Cols.friend_email + " TEXT NOT NULL DEFAULT ''"
    )
    i_db_conn.execute(
        "ALTER TABLE " + DbSchemaM.ViewTable.name + " ADD COLUMN "
        + DbSchemaM.ViewTable.Cols.collection_type + " INTEGER NOT NULL DEFAULT " + str(wbd.wbd_global.CollectionType.views.value)
    )
"""


def upgrade_1_2(i_db_conn):
    backup_db(DbBackupMethod.using_copyfile)
    i_db_conn.execute(
        "CREATE TABLE " + DbSchemaM.FriendTable.name
        + "(" + DbSchemaM.FriendTable.Cols.id + " INTEGER PRIMARY KEY"
        + ", " + DbSchemaM.FriendTable.Cols.sort_order + " INTEGER NOT NULL"
        + ", " + DbSchemaM.FriendTable.Cols.friend_name + " TEXT NOT NULL"
        + ", " + DbSchemaM.FriendTable.Cols.email + " TEXT NOT NULL UNIQUE"
        + ")"
    )


upgrade_steps = {
    1: initial_schema_and_setup,
    2: upgrade_1_2
}


class DbHelperM():
    """
    Like a singleton
    """
    __db_connection = None  # -"static"

    # noinspection PyTypeChecker
    @staticmethod
    def get_db_connection() -> sqlite3.Connection:
        if DbHelperM.__db_connection is None:
            DbHelperM.__db_connection = sqlite3.connect(wbd.wbd_global.get_database_filename())

            # Upgrading the database
            # Very good upgrade explanation:
            # http://stackoverflow.com/questions/19331550/database-change-with-software-update
            # More info here: https://www.sqlite.org/pragma.html#pragma_schema_version
            current_db_ver_it = get_schema_version(DbHelperM.__db_connection)
            target_db_ver_it = max(upgrade_steps)
            for upgrade_step_it in range(current_db_ver_it + 1, target_db_ver_it + 1):
                if upgrade_step_it in upgrade_steps:
                    upgrade_steps[upgrade_step_it](DbHelperM.__db_connection)
                    set_schema_version(DbHelperM.__db_connection, upgrade_step_it)
            DbHelperM.__db_connection.commit()

            if wbd.wbd_global.testing_bool:
                wbd.model.populate_db(DataSetupType.test_data)
            elif not wbd.wbd_global.db_file_exists_at_application_startup_bl:
                wbd.model.populate_db(DataSetupType.first_start_data)
            if wbd.wbd_global.database_debugging_bool:
                sqlite3.enable_callback_tracebacks(True)
                DbHelperM.__db_connection.set_trace_callback(logging.debug)
                logging.info("Db debugging activated")
                # DbHelperM.__db_connection.set_trace_callback(print)
        return DbHelperM.__db_connection

    @staticmethod
    def close_db_connection():
        connection = DbHelperM.get_db_connection()
        connection.commit()
        connection.close()
        # -Do we need to close the db connection? Reference:
        #  http://stackoverflow.com/questions/3850261/doing-something-before-program-exit
        DbHelperM.__db_connection = None


class DbBackupMethod(enum.Enum):
    using_sqlite = enum.auto()
    using_copyfile = enum.auto()


def backup_db(i_method: DbBackupMethod) -> int:
    if wbd.wbd_global.testing_bool and i_method == DbBackupMethod.using_copyfile:
        logging.info("Since we are testing and therefore storing the db in :memory: we cannot copy it to a new file")
        return -1
    backup_suffix_str = "_db_backup_" + i_method.name + ".sqlite"
    date_sg = datetime.datetime.now().strftime(wbd.wbd_global.PY_DATETIME_FILENAME_FORMAT_STR)
    backup_dir_str = wbd.wbd_global.get_user_backup_path()  # -alt: os.path.abspath(new_file_path_str)
    wbd.wbd_global.removing_oldest_files(backup_dir_str, backup_suffix_str, 3)
    backup_file_path_str = wbd.wbd_global.get_user_backup_path(date_sg + backup_suffix_str)
    if i_method == DbBackupMethod.using_sqlite:
        source_connection = DbHelperM.get_db_connection()
        with sqlite3.connect(backup_file_path_str) as dest_connection:
            source_connection.backup(dest_connection)
            # -Please note: This .backup() function is new in Python version 3.7
    elif i_method == DbBackupMethod.using_copyfile:
        shutil.copyfile(wbd.wbd_global.get_database_filename(), backup_file_path_str)
    else:
        pass
    file_size_in_bytes_int = os.path.getsize(backup_file_path_str)
    return file_size_in_bytes_int


ITER_DUMP_SUFFIX_STR = "_db_iter_dump.sql"


def take_iter_db_dump():
    connection = DbHelperM.get_db_connection()
    date_sg = datetime.datetime.now().strftime(wbd.wbd_global.PY_DATETIME_FILENAME_FORMAT_STR)
    file_path_str = wbd.wbd_global.get_user_iterdump_path(date_sg + ITER_DUMP_SUFFIX_STR)

    backup_dir_str = wbd.wbd_global.get_user_iterdump_path()
    wbd.wbd_global.removing_oldest_files(backup_dir_str, ITER_DUMP_SUFFIX_STR, 3)

    with open(file_path_str, 'w') as file:
        # noinspection PyTypeChecker
        for sql_line_str in connection.iterdump():
            file.write(sql_line_str + '\n')
        # file.writelines(connection.iterdump())


def get_row_count() -> int:
    """
    Three ways to get the number of rows:
    1. using cursor.rowcount - https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.rowcount
    There are some things to be aware of here however: https://stackoverflow.com/q/839069/2525237
    2. using len(db_cursor.fetchall()) as described here: https://stackoverflow.com/a/21838197/2525237
    3. using SELECT COUNT(*)
    Please note that in all cases we need to have selected some table (it doesn't seem to be possible to count
    all the rows)
    :return:
    """
    db_connection = DbHelperM.get_db_connection()

    db_cursor = db_connection.cursor()
    db_cursor = db_cursor.execute(
        "SELECT * FROM " + wbd.db.DbSchemaM.EntryTable.name
    )
    db_connection.commit()

    ret_row_count_int = db_cursor.rowcount
    logging.debug("ret_row_count_int = " + str(ret_row_count_int))
    fetch_all_row_count_int = len(db_cursor.fetchall())
    logging.debug("fetch_all_row_count_int = " + str(fetch_all_row_count_int))

    sqlite_select_count_string_str = (
        "SELECT COUNT(*)"
        + " FROM " + wbd.db.DbSchemaM.EntryTable.name
    )

    return ret_row_count_int

    # Please note that it can be good to compare with len(cursor.fetchall), see this answer:
    # https://stackoverflow.com/a/21838197/2525237

