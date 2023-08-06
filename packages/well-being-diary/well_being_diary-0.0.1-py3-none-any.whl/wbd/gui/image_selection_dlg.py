import typing
from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6 import QtCore
import PIL.Image
import wbd.wbd_global

WIDTH_AND_HEIGHT_INT = 250


class ImageFileDialog(QtWidgets.QFileDialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QFileDialog.__init__(self, *args, **kwargs)

        self.setOption(QtWidgets.QFileDialog.DontUseNativeDialog)

        self.setFixedSize(self.width() + WIDTH_AND_HEIGHT_INT, self.height())

        vbox_l2 = QtWidgets.QVBoxLayout()

        self.preview_qll = QtWidgets.QLabel()
        self.preview_qll.setFixedSize(WIDTH_AND_HEIGHT_INT, WIDTH_AND_HEIGHT_INT)
        self.preview_qll.setAlignment(QtCore.Qt.AlignCenter)
        self.preview_qll.setObjectName("preview_qll")

        vbox_l2.addWidget(self.preview_qll)

        self.layout().addLayout(vbox_l2, 1, 3, 1, 1)

        self.currentChanged.connect(self.on_current_changed)
        self.fileSelected.connect(self.on_file_selected)
        self.filesSelected.connect(self.on_files_selected)

        self._file_selected_str = None
        self._files_selected_str_list = []

        sidebar_qurllist = []
        sidebar_qurllist.append(QtCore.QUrl.fromLocalFile(QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.HomeLocation)[0]))
        sidebar_qurllist.append(QtCore.QUrl.fromLocalFile(QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.PicturesLocation)[0]))
        sidebar_qurllist.append(QtCore.QUrl.fromLocalFile(QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.DownloadLocation)[0]))
        self.setSidebarUrls(sidebar_qurllist)

        # self.setDirectory()

    def on_current_changed(self, i_new_file_path: str):
        pixmap = QtGui.QPixmap(i_new_file_path)
        if pixmap.isNull():
            self.preview_qll.setText("Preview")
        else:
            pixmap = pixmap.scaled(
                WIDTH_AND_HEIGHT_INT,
                WIDTH_AND_HEIGHT_INT,
                QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation
            )

            image_pi: PIL.Image = PIL.Image.open(i_new_file_path)
            rotation_degrees_int = wbd.wbd_global.get_rotation_degrees(image_pi, True)
            # -rotation is done in the other direction than when using Pillow
            if rotation_degrees_int != 0:
                rotation_qtransform = QtGui.QTransform()
                rotation_qtransform.rotate(rotation_degrees_int)
                pixmap = pixmap.transformed(rotation_qtransform)

            self.preview_qll.setPixmap(pixmap)

    def on_file_selected(self, i_file: str):
        self._file_selected_str = i_file

    def on_files_selected(self, i_file: str):
        self._files_selected_str_list = i_file

    def get_file_selected(self) -> str:
        return self._file_selected_str

    def get_files_selected(self) -> typing.List[str]:
        return self._files_selected_str_list

    @staticmethod
    def open_dlg_and_get_image_path() -> str:
        image_dlg = ImageFileDialog(filter="Images (*.png *.jpg)")
        image_dlg.exec_()
        image_path_str = image_dlg.get_file_selected()
        return image_path_str

    @staticmethod
    def open_dlg_and_get_image_paths() -> typing.List[str]:
        image_dlg = ImageFileDialog(filter="Images (*.png *.jpg)")
        image_dlg.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        image_dlg.exec_()
        image_path_str_list = image_dlg.get_files_selected()
        return image_path_str_list

        # image_path_str_list = ImageFileDialog.getOpenFileNames(filter="Images (*.png *.jpg)")
        # return image_path_str_list
