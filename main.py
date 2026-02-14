from PySide6.QtWidgets import * 
from PySide6.QtGui import *
from PySide6.QtCore import *
import pymysql
import sys
from main_design import Ui_MainWindow
from dialog import Ui_Dialog

class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = DataBase()
        self.create_combobox()
    
    def create_combobox(self):
        sup = self.db.get_suppliers()
        for item in sup:
            self.ui.comboBox.addItem(item['name'])
        creators = self.db.get_creators()
        for item in creators:
            self.ui.comboBox_2.addItem(item['name'])
        self.ui.comboBox_3.addItem('Женская')
        self.ui.comboBox_3.addItem('Мужская')




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = DataBase()
        self.dialog = Dialog()

        self.load_data()

        self.ui.delete_btn.clicked.connect(self.delete)
        self.ui.add_btn.clicked.connect(self.add)


    def load_data(self):
        """
        Вывод данных

        """
        data = self.db.get_stuff()
        self.ui.tableWidget.setColumnCount(len(data[0]))
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setHorizontalHeaderLabels(data[0].keys())

        for row_id, row_data in enumerate(data):
            for col_id, value in enumerate(row_data.values()):
                if col_id == 1:
                    if value == 0: value = 'женская'
                    else: value = 'мужская'
                self.ui.tableWidget.setItem(row_id, col_id, QTableWidgetItem(str(value)))

    def get_selected_id(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row:
            return(self.ui.tableWidget.item(current_row, 0).text())
    
    def delete(self):
        id = self.get_selected_id()
        result = QMessageBox.question(self, 'Подтверждение', 'Вы уверены?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if result == QMessageBox.StandardButton.Yes:
            self.db.delete_kruto(id)
            self.load_data()

    def add(self):
        self.dialog.show()

        
    



class DataBase():
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='demo',
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_stuff(self):
        with self.conn.cursor() as cursor:
            cursor.execute("""
            SELECT s.id,
            s.category,
            s.name,
            s.discription,
            c.name as creator_name,
            sup.name as supplier_name,
            s.price,
            s.unit,
            s.quantity,
            s.photo
        from `stuff` as s
        join `creator` as c on s.creator_id = c.id
        join `supplier` as sup on s.supplier_id = sup.id
        """)
        
        return cursor.fetchall()
    
    def delete_kruto(self, id):
        with self.conn.cursor() as cursor:
            cursor.execute("""
            DELETE FROM stuff WHERE `stuff`.`id` = %s
            """, (id,))
            self.conn.commit()

    def get_suppliers(self):
        with self.conn.cursor() as cursor:
            cursor.execute("""
            SELECT name FROM `supplier` 
        """)
        return cursor.fetchall()
    
    def get_creators(self):
        with self.conn.cursor() as cursor:
            cursor.execute("""
            SELECT name FROM `creator` 
        """)
        return cursor.fetchall()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    db = DataBase()
    # print(db.get_stuff())

    app.exit(app.exec())

