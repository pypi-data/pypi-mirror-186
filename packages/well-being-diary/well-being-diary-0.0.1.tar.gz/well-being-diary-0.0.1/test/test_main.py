import sys
import unittest
from PySide6 import QtTest
from PySide6 import QtCore
from PySide6 import QtWidgets
import wbd.wbd_global
import wbd.gui.main_window

test_app = QtWidgets.QApplication(sys.argv)
# -has to be set here (rather than in __main__) to avoid an error


class MainTest(unittest.TestCase):
    """
    "@unittest.skip" can be used to skip a test
    """

    @classmethod
    def setUpClass(cls):
        wbd.wbd_global.testing_bool = True

    def setUp(self):
        pass

    def test_main_window(self):
        main_window = wbd.gui.main_window.MainWindow()



# Database testing!

