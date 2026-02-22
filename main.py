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

        self.ui.lineEdit_3.setValidator(QIntValidator(0, 10000, self))
        self.ui.lineEdit_5.setValidator(QIntValidator(0, 100, self))
        self.ui.lineEdit_6.setValidator(QIntValidator(0, 10000, self))

        validator = QDoubleValidator(0.00, 9999999.99, 2)
        validator.setLocale(QLocale(QLocale.English))
        self.ui.lineEdit_4.setValidator(validator)


        self.create_combobox()
        self.ui.buttonBox.accepted.connect(self.add_staff)
    
    def create_combobox(self):
        sup = self.db.get_suppliers()
        for item in sup:
            self.ui.comboBox.addItem(item['name'], item['id'])
        creators = self.db.get_creators()
        for item in creators:
            self.ui.comboBox_2.addItem(item['name'], item['id'])
        self.ui.comboBox_3.addItem('Женская', 0)
        self.ui.comboBox_3.addItem('Мужская', 1)

    def add_staff(self):
        new_data = {
            'id': self.ui.lineEdit.text(),
            'name': self.ui.lineEdit_2.text(),
            'unit': self.ui.lineEdit_3.text(),
            'price': self.ui.lineEdit_4.text(),
            'supplier': self.ui.comboBox.currentData(),
            'creator': self.ui.comboBox_2.currentData(),
            'category': self.ui.comboBox_3.currentData(),
            'sale': self.ui.lineEdit_5.text(),
            'quantity': self.ui.lineEdit_6.text(),
            'discription': self.ui.textEdit.toPlainText(),
            'photo': self.ui.lineEdit_7.text()
        }
        try:
            db.add_staff(new_data)
        except Exception as e:
            print(e)


class DialogEdit(QDialog):
    def __init__(self, item_id=None):
        super(DialogEdit, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = DataBase()
        self.create_combobox()
        self.item_id = item_id

        self.ui.lineEdit_3.setValidator(QIntValidator(0, 10000, self))
        self.ui.lineEdit_5.setValidator(QIntValidator(0, 100, self))
        self.ui.lineEdit_6.setValidator(QIntValidator(0, 10000, self))

        validator = QDoubleValidator(0.00, 9999999.99, 2)
        validator.setLocale(QLocale(QLocale.English))
        self.ui.lineEdit_4.setValidator(validator)


        # self.ui.buttonBox.accepted.connect(self.add_staff)

        if self.item_id:
            self.load_data()


    def load_data(self):
        data = self.db.get_one_stuff(self.item_id)
        print(data)
        self.ui.lineEdit.setText(data['id']),
        self.ui.lineEdit_2.setText(data['name']),
        self.ui.lineEdit_3.setText(str(data['unit'])),
        self.ui.lineEdit_4.setText(str(data['price'])),
        self.ui.comboBox.setCurrentIndex(self.ui.comboBox.findData(data['supplier_id'])),
        self.ui.comboBox_2.setCurrentIndex(self.ui.comboBox_2.findData(data['creator_id'])),
        self.ui.comboBox_3.setCurrentIndex(self.ui.comboBox_3.findData(data['category'])),
        self.ui.lineEdit_5.setText(str(data['sale'])),
        self.ui.lineEdit_6.setText(str(data['quantity'])),
        self.ui.textEdit.setText(data['discription']),
        self.ui.lineEdit_7.setText(data['photo'])

    
    def create_combobox(self):
        sup = self.db.get_suppliers()
        for item in sup:
            self.ui.comboBox.addItem(item['name'], item['id'])
        creators = self.db.get_creators()
        for item in creators:
            self.ui.comboBox_2.addItem(item['name'], item['id'])
        self.ui.comboBox_3.addItem('Женская', 0)
        self.ui.comboBox_3.addItem('Мужская', 1)

    # def edit_staff(self):
    #     new_data = {
    #         'id': self.ui.lineEdit.text(),
    #         'name': self.ui.lineEdit_2.text(),
    #         'unit': self.ui.lineEdit_3.text(),
    #         'price': self.ui.lineEdit_4.text(),
    #         'supplier': self.ui.comboBox.currentData(),
    #         'creator': self.ui.comboBox_2.currentData(),
    #         'category': self.ui.comboBox_3.currentData(),
    #         'sale': self.ui.lineEdit_5.text(),
    #         'quantity': self.ui.lineEdit_6.text(),
    #         'discription': self.ui.textEdit.toPlainText(),
    #         'photo': self.ui.lineEdit_7.text()
    #     }
    #     try:
    #         db.add_staff(new_data)
    #     except Exception as e:
    #         print(e)
        




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = DataBase()
        self.dialog = Dialog()
        self.dialog_edit = DialogEdit()

        self.load_data()

        self.ui.delete_btn.clicked.connect(self.delete)
        self.ui.add_btn.clicked.connect(self.add)
        self.ui.edit_btn.clicked.connect(self.edit)


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

    def edit(self):
        id = self.get_selected_id()
        self.dialog_edit = DialogEdit(id)
        self.dialog_edit.show()


        
    



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
    
    def get_one_stuff(self, id):
        with self.conn.cursor() as cursor:
            cursor.execute("""
            SELECT * FROM `stuff` WHERE id = %s; 
        """, (id,))
        
        return cursor.fetchone()
    

    def get_one_stuff_noid(self, id):
        with self.conn.cursor() as cursor:
            cursor.execute("""
            SELECT s.id, s.category, s.name, s.discription, c.name as creator_name, sup.name as supplier_name, s.price, s.unit, s.quantity, s.photo from `stuff` as s join `creator` as c on s.creator_id = c.id join `supplier` as sup on s.supplier_id = sup.id where s.id = %s; 
        """, (id,))
        
        return cursor.fetchone()
    
    def delete_kruto(self, id):
        with self.conn.cursor() as cursor:
            cursor.execute("""
            DELETE FROM stuff WHERE `stuff`.`id` = %s
            """, (id,))
            self.conn.commit()

    def get_suppliers(self):
        with self.conn.cursor() as cursor:
            cursor.execute("""
            SELECT id, name FROM `supplier` 
        """)
        return cursor.fetchall()
    
    def get_creators(self):
        with self.conn.cursor() as cursor:
            cursor.execute("""
            SELECT id, name FROM `creator` 
        """)
        return cursor.fetchall()
    
    def add_staff(self, data):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO `stuff` (`id`, `name`, `unit`, `price`, `supplier_id`, `creator_id`, `category`, `sale`, `quantity`, `discription`, `photo`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (data['id'], data['name'], data['unit'], data['price'], data['supplier'], data['creator'], data['category'], data['sale'], data['quantity'], data['discription'], data['photo'], ))
                self.conn.commit()
        except Exception as e:
            print(e)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    db = DataBase()
    # print(db.get_stuff())

    app.exit(app.exec())

