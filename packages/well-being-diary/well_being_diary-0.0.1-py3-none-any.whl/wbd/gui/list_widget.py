import logging
import enum
import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui
import wbd.wbd_global
import wbd.model
import wbd.exception_handling

NO_POS_SET_INT = -1
NO_ITEM_ACTIVE_INT = -1


class MoveDirectionEnum(enum.Enum):
    up = enum.auto()
    down = enum.auto()


class ListWidget(QtWidgets.QListWidget):
    """
    Please note: Instead of updating the "active row/tag/question/_" we can send the id with the signal,
    and avoid updating the current widget in the main update_gui method

    Limitations:
    * Only a single item can be selected at a time

    Interface:
    .id_int
    .sort_order_int
    .title_str
    """
    # We might want this in the future for drag-n-drop between lists: drop_signal = QtCore.Signal()
    current_row_changed_signal = QtCore.Signal(int, bool, bool)  # -tag id, ctrl mod, alt mod

    def __init__(self, i_model_class, i_show_checkboxes: bool = False):
        super().__init__()

        self.updating_gui_bool = False

        assert issubclass(i_model_class, wbd.model.ListM)
        self.model_class = i_model_class
        self.show_checkboxes_bool = i_show_checkboxes

        """
        if self.model_class is wbd.model.FriendM:            
            check_state_bool = model_item.id_int in wbd.wbd_global.active_state.selected_friends_id_list
            row_qlwi.setCheckState(Qtcheck_state_bool)
        """

        self.currentRowChanged.connect(self.on_current_row_changed)

        self.update_gui()

    # Overridden
    def sizeHint(self) -> QtCore.QSize:
        """
        This function is overridden because the lower limit for the height is too large.
        Please note that updateGeometry has to be called for the sizehint to be updated.
        """
        qsize = QtCore.QSize()
        height_int = 2 * self.frameWidth()
        for row_nr_int in range(0, self.count()):
            height_int += self.sizeHintForRow(row_nr_int)
        qsize.setHeight(height_int)

        width_int = super().sizeHint().width()
        qsize.setWidth(width_int)

        return qsize

    def delete_item(self, i_id: int):
        self.clearSelection()
        self.model_class.remove(wbd.wbd_global.active_state.question_id)

        wbd.wbd_global.active_state.question_id = wbd.wbd_global.NO_ACTIVE_ROW_INT
        self.current_row_changed_signal.emit(wbd.wbd_global.active_state.question_id, False, False)
        # -TODO: Changing this to a separate signal for deleting?
        self.update_gui()

    def go_to_next_row(self) -> bool:
        current_row_int = self.currentRow()
        if current_row_int < self.count() - 1:
            self.setCurrentRow(current_row_int + 1)
            return True
        return False

    def on_current_row_changed(self):
        if self.updating_gui_bool:
            return
        current_row_int = self.currentRow()
        if current_row_int == wbd.wbd_global.QT_NO_ROW_SELECTED_INT:
            return
        current_item_qli = self.item(current_row_int)
        id_int = current_item_qli.data(QtCore.Qt.UserRole)

        if id_int is not None:
            ctrl_active_bool = False
            shift_active_bool = False
            if QtGui.QGuiApplication.keyboardModifiers() == QtCore.Qt.ControlModifier:
                ctrl_active_bool = True
            if QtGui.QGuiApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier:
                shift_active_bool = True
            self.current_row_changed_signal.emit(id_int, ctrl_active_bool, shift_active_bool)

            logging.debug("self.viewportSizeHint().height() = " + str(self.viewportSizeHint().height()))
            logging.debug("self.sizeHintForRow(current_item_qli) = " + str(self.sizeHintForRow(current_row_int)))
        else:
            logging.warning("on_current_row_changed: id_int is None")

    def update_gui(self,
        i_sort_type_enum: wbd.wbd_global.SortType = wbd.wbd_global.SortType.sort_by_time,
        i_checked_ids: [int] = None
    ):
        self.updating_gui_bool = True

        item_list = self.model_class.get_all(i_sort_type_enum)
        self.clear()

        """
        for model_item in item_list:
            row_qll = QtWidgets.QLabel(model_item.title_str)
            new_font = row_qll.font()
            new_font.setPointSize(14)
            row_qll.setFont(new_font)
            # Not needed: row_qll.updateGeometry()
            row_qlwi = QtWidgets.QListWidgetItem()
            row_qlwi.setData(QtCore.Qt.UserRole, model_item.id_int)
            row_qlwi.setSizeHint(row_qll.sizeHint())
            self.addItem(row_qlwi)
            self.setItemWidget(row_qlwi, row_qll)
        """
        for model_item in item_list:
            # Not needed: row_qll.updateGeometry()
            row_qlwi = QtWidgets.QListWidgetItem()
            row_qlwi.setText(model_item.title_str)
            new_font = row_qlwi.font()
            new_font.setPointSize(14)
            row_qlwi.setData(QtCore.Qt.UserRole, model_item.id_int)
            row_qlwi.setFont(new_font)
            if self.show_checkboxes_bool:
                # check_state_bool = model_item.id_int in wbd.wbd_global.active_state.selected_friends_id_list
                # Doesn't work, unknown why: row_qlwi.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
                if i_checked_ids is not None:
                    if model_item.id_int in i_checked_ids:
                        row_qlwi.setCheckState(QtCore.Qt.Checked)
                    else:
                        row_qlwi.setCheckState(QtCore.Qt.Unchecked)
                else:
                    row_qlwi.setCheckState(row_qlwi.checkState())
            self.addItem(row_qlwi)

        #self.qll
        # logging.debug("self.viewportSizeHint().height() = " + str(self.viewportSizeHint().height()))

        self.updating_gui_bool = False


class ListWithOrderWidget(ListWidget):
    def __init__(self, i_model_class):
        super().__init__(i_model_class)

        self.model_class = i_model_class

        assert issubclass(i_model_class, wbd.model.ListWithCustomOrderM)
        # -this is not possible: https://stackoverflow.com/a/54241536/2525237

        #####if i_update_db_sort_order_func is not None:
        # self.list_qlw.setDragEnabled(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

    def __update_row_item(self, i_start_pos: int, i_end_pos: int):
        current_list_widget_item: QtWidgets.QListWidgetItem = self.item(i_start_pos)
        id_int = current_list_widget_item.data(QtCore.Qt.UserRole)
        ############item_widget_cql: CustomQLabel = self.itemWidget(current_list_widget_item)
        self.takeItem(i_start_pos)
        # -IMPORTANT: item is removed from list only after the item widget has been extracted.
        #  The reason for this is that if we take the item away from the list the associated
        #  widget (in our case a CustomLabel) will not come with us (which makes sense
        #  if the widget is stored in the list somehow)
        ######model_item = self.get_single_item_func(id_int)
        model_item = self.model_class.get(id_int)  # -duck typing
        item_label_qll = QtWidgets.QLabel(model_item.title_str)  # -duck typing
        row_item = QtWidgets.QListWidgetItem()
        self.insertItem(i_end_pos, row_item)
        self.setItemWidget(row_item, item_label_qll)
        self.setCurrentRow(i_end_pos)

    # overridden
    def dropEvent(self, i_QDropEvent):
        super().dropEvent(i_QDropEvent)
        self.update_db_sort_order_for_all_rows()

    def move_to_top(self):
        current_row_number_int = self.currentRow()
        self.__update_row_item(current_row_number_int, 0)
        self.update_db_sort_order_for_all_rows()

    def move_item_up(self):
        self.move_current_row_up_down(MoveDirectionEnum.up)

    def move_item_down(self):
        self.move_current_row_up_down(MoveDirectionEnum.down)

    def move_current_row_up_down(self, i_move_direction: MoveDirectionEnum) -> None:
        current_row_number_int = self.currentRow()
        position_int = NO_POS_SET_INT
        if i_move_direction == MoveDirectionEnum.up:
            if current_row_number_int >= 0:
                position_int = current_row_number_int - 1
        elif i_move_direction == MoveDirectionEnum.down:
            if current_row_number_int < self.count():
                position_int = current_row_number_int + 1
        if position_int != NO_POS_SET_INT:
            current_row_number_int = self.currentRow()
            self.__update_row_item(current_row_number_int, position_int)
            self.update_db_sort_order_for_all_rows()

    def update_db_sort_order_for_all_rows(self):
        logging.debug("update_db_sort_order_for_all_rows")
        i = 0
        while i < self.count():
            q_list_item_widget: QtWidgets.QListWidgetItem = self.item(i)
            id_int = q_list_item_widget.data(QtCore.Qt.UserRole)
            row_int = self.row(q_list_item_widget)
            self.model_class.update_sort_order(id_int, row_int)
            logging.debug("id_int = " + str(id_int) + ", row_int = " + str(row_int))
            i += 1


class ItemExperimental:
    def __init__(self, i_id: int, i_title: str, i_sort_order: int=0):
        self.id_int = i_id
        self.title_str = i_title
        self.sort_order_int = i_sort_order

list_of_items = [ItemExperimental(1, "First"), ItemExperimental(2, "2nd"), ItemExperimental(3, "3rd")]

def get_single_experimental(i_id: int):
    return list_of_items[0]

def get_all_experimental():
    return list_of_items

def update_sort_order_experimental(i_id: int, i_sort_order: int):
    pass


class TestListM(wbd.model.ListM):

    @staticmethod
    def get(i_id: int):
        pass

    @staticmethod
    def remove(i_id: int):
        pass

    @staticmethod
    def get_all(i_sort_type_enum: wbd.wbd_global.SortType = wbd.wbd_global.SortType.sort_by_default_db_order):
        row_one = TestListM()
        row_one.title_str = "one"
        row_one.id_int = 1
        return [row_one]


class TestMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()


        self.my_list_widget = ListWidget(TestListM)
        self.setCentralWidget(self.my_list_widget)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = TestMainWindow()
    main_window.show()
    app.exec_()

