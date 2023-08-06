#!/usr/bin/env python3
import sqlite3
import sys
import os
import logging
import logging.handlers
import argparse
import configparser
import time
import PyQt5.Qt
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets
import wbd.wbd_global
import wbd.db
import wbd.gui.main_window
import hashlib
import PIL


if __name__ == "__main__":
    # Setting the current working directory
    base_dir_path_str = wbd.wbd_global.get_base_dir_path()
    os.chdir(base_dir_path_str)

    # Logging
    # Please also see the code in the wbd.__init__.py module for more info on how we do logging
    logger = logging.getLogger()
    # -if we set a name here for the logger the file handler will no longer work, unknown why
    logger.handlers = []  # -removing the default stream handler first
    # logger.propagate = False
    log_file_path_str = wbd.wbd_global.get_user_logs_path(wbd.wbd_global.LOG_FILE_NAME_STR)
    # ..to file
    rfile_handler = logging.handlers.RotatingFileHandler(log_file_path_str, maxBytes=8192, backupCount=2)
    rfile_handler.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    rfile_handler.setFormatter(formatter)
    logger.addHandler(rfile_handler)
    # ..to stdout
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # logging.getLogger().setLoggerClass(wbd.my_logger.MyLogger)
    # logger = logging.getLogger()
    # logger = wbd.my_logger.MyLogger("logger_name")

    # Checking if this is the first time that the application is started
    wbd.wbd_global.db_file_exists_at_application_startup_bl = os.path.isfile(wbd.wbd_global.get_database_filename())

    # Command line arguments
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--testing", "-t", help="Testing - data saved in memory only", action="store_true")
    # -for info about "store_true" please search here: https://docs.python.org/3/howto/argparse.html
    args = argument_parser.parse_args()
    wbd.wbd_global.testing_bool = False
    if args.testing:
        wbd.wbd_global.testing_bool = True

    # === Creating the application and main window ===
    app = QtWidgets.QApplication(sys.argv)
    # -"QWidget: Must construct a QApplication before a QWidget"
    logging.debug(f"app.applicationPid() = {app.applicationPid()}")
    main_window = wbd.gui.main_window.MainWindow()

    # Application information
    logging.getLogger().info("===== Starting " + wbd.wbd_global.WBD_APPLICATION_NAME_STR + " - "
        + wbd.wbd_global.WBD_APPLICATION_VERSION_STR + " =====")
    logging.info("Python version: " + str(sys.version))
    logging.info("SQLite version: " + str(sqlite3.sqlite_version))
    logging.info("PySQLite (Python module) version: " + str(sqlite3.version))
    logging.info("Qt version: " + str(QtCore.qVersion()))
    logging.info("PyQt (Python module) version: " + str(PyQt5.Qt.PYQT_VERSION_STR))
    logging.info("Pillow version: " + str(PIL.__version__))
    logging.info(wbd.wbd_global.WBD_APPLICATION_NAME_STR + " Application version: " + str(wbd.wbd_global.WBD_APPLICATION_VERSION_STR))
    db_conn = wbd.db.DbHelperM.get_db_connection()
    logging.info(wbd.wbd_global.WBD_APPLICATION_NAME_STR + " Database schema version: " + str(wbd.db.get_schema_version(db_conn)))
    time_offset_int = -1 * time.timezone // 3600
    if time_offset_int > 0:
        time_offset_str = "+" + str(time_offset_int)
    elif time_offset_int == 0:
        time_offset_str = "+/-" + str(time_offset_int)
    else:
        time_offset_str = "-" + str(time_offset_int)
    logging.info("Timezone: UTC" + time_offset_str)
    logging.info("=====")

    sys.exit(app.exec_())

"""



Views:
* Standard (as now)
* Hourly (one day per page), including empty hours
* Weekly, including empty days and hours


unsure of date, what to do?


nr of steps: slider + spinner
metta phrases: combobox

User customization:
* button names and (text) output when clicking buttons
* Range for sliders and spinners

Output:
* [Title: Value]


Well-being of everyone
Interbeing of my wb and wb of everyone else (esp. those close to me)


TODO: show contents of external file, e.g. checklist file från kammanta


https://stackoverflow.com/questions/17106315/failed-to-load-platform-plugin-xcb-while-launching-qt5-app-on-linux-without


clearing friends checked after email sharing

email signature where the user can (for example) add a translation link
maybe the translation link can be included for all non-native speakers?
still there is the privacy issue though




### Programming

#### Tasks

#### Ideas


### Design

Creating a collection of kind actions that the user has seen, so she can return to this list. (Idea from end of Hunger Games series')

#### Tasks

Frågor med widgetar, hur ser detta ut och funkar det?

WBD Figuring out ways to review old entries


#### Ideas

Energy/depression and Anxiety for each hour


WBD: Same question for self and others? (inter-being)

Questions:
* **Buddhist practice**
* **Most difficult (suffering) today** (research support for this being a good question!)
* Suffering in the world
  * Sila, how i have helped
* **Gratitudes**
* **Sleep!**
* Social
  * writing about the experiences of others?
  * meeting with friends
  * inter-being
* Nature

Design:
Mindfulness diary, what have we been aware of during the day?
* insights
* inter-being
* impermanence
* giving
* gratitude
Morning ritual and evening ritual

interbeing is a priority, considering different ways that this can be added

everything i do is an offering
gratitude for other people, and for the earth and universe

för impermanence: https://en.wikipedia.org/wiki/List_of_sundial_mottos



**************
**************
**************


Programming TODO: Auto-selecting newly added friends
Programming TODO: Bug: Update-GUI in the Sharing Dialog is not removing checked states
Programming TODO: Search for (filter) tags. Design: If only one remaining, making it easy to select

Programming TODO: Checkboxes for the tags? Or another easy way to add tags for entries
Design idea: Images of people that expect happiness and progress, displayed in the entry area

Tech research TODO: Looking into PyDoc: https://docs.python.org/3/library/pydoc.html
Can saved to html files (for example)

Reducing page size?
https://stackoverflow.com/questions/4657648/what-is-a-page-in-sql-server-and-do-i-need-to-worry
> The minimum size of an SQLite database is one page for each table and each index. With a larger page size, the size of an empty database for a given schema will grow by a factor of four, therefore. However, once the database begins to fill with content the size of the older 1024-byte page databases and the newer 4096-byte page databases will quickly converge. Due to relaxed bin-packing constraints, the 4096-byte page size might actually result in a smaller file, once substantial content is added.
> on modern hardware, a 4096 byte page is a faster and better choice.
https://sqlite.org/pgszchng2016.html

researching:
https://www.sqlite.org/appfileformat.html

researching sharing to diaspora
hank: api status?
alyson, fediverse?

Design TODO: Adding an hour view for a day, and maybe yesterday also. This makes it easier for the user to track
what she is doing
-Possibly end time (or length which is the same)
-VIsa tomma rader är en enkel lösning
Design TODO: Reviewing diary entries, focus view?
design todo: showing yesterday and today?

"Well being for ourselves, our family+friends, and for the world"

Redesign of model.py:
get, set
Object (ORM), direct access
https://softwareengineering.stackexchange.com/questions/ask

Bug 1:
2019-11-18 22:51:37,663 - ERROR - sqlite3.IntegrityError - sqlite3.IntegrityError
  File "/home/sunyata/PycharmProjects/well-being-diary/well-being-diary.py", line 87, in <module>
    sys.exit(app.exec_())
  File "/home/sunyata/PycharmProjects/well-being-diary/wbd/gui/list_widget.py", line 121, in on_current_row_changed
    self.current_row_changed_signal.emit(id_int, ctrl_active_bool, shift_active_bool)
  File "/home/sunyata/PycharmProjects/well-being-diary/wbd/gui/tags_cw.py", line 260, in on_collection_row_changed
    self.update_gui(wbd.wbd_global.EventSource.collection_changed)
  File "/home/sunyata/PycharmProjects/well-being-diary/wbd/gui/tags_cw.py", line 385, in update_gui
    self.collection_tags_clw.update_gui()
  File "/home/sunyata/PycharmProjects/well-being-diary/wbd/gui/list_widget.py", line 159, in update_gui
    item_list = self.model_class.get_all()  # -duck typing
  File "/home/sunyata/PycharmProjects/well-being-diary/wbd/model.py", line 1035, in get_all
    (wbd.wbd_global.active_state.collection_id,)
  File "/home/sunyata/PycharmProjects/well-being-diary/wbd/db.py", line 30, in db_exec
    db_connection = wbd.db.DbHelperM.get_db_connection()
  File "/home/sunyata/PycharmProjects/well-being-diary/wbd/db.py", line 338, in get_db_connection
    wbd.model.populate_db(False)
  File "/home/sunyata/PycharmProjects/well-being-diary/wbd/model.py", line 1518, in populate_db
    contribution_tag_id_int = TagM.add("Contribution", "Contribution and generosity")
  File "/home/sunyata/PycharmProjects/well-being-diary/wbd/model.py", line 544, in add
    (sort_order, i_title, i_description)
  File "/home/sunyata/PycharmProjects/well-being-diary/wbd/db.py", line 40, in db_exec
    wbd.exception_handling.error("sqlite3.IntegrityError", "sqlite3.IntegrityError")
  File "/home/sunyata/PycharmProjects/well-being-diary/wbd/exception_handling.py", line 89, in error
    stack_str = ''.join(traceback.format_stack())


https://docs.python.org/3/howto/logging-cookbook.html#a-qt-gui-for-logging

"""


