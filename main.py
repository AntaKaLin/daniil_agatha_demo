from PySide6.QtWidgets import *
from PySide6.QtCore import *
import pymysql
import sys
from main_design import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


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
            s.quantity
        from `stuff` as s
        join `creator` as c on s.creator_id = c.id
        join `supplier` as sup on s.supplier_id = sup.id
        """)
        
        return cursor.fetchall()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    db = DataBase()
    print(db.get_stuff())

    app.exit(app.exec())

