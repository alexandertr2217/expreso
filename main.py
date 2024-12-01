import io
import sqlite3
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyProgram(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.update()

    def update(self):
        cur = self.con.cursor()
        dun = cur.execute('select * from coffee').fetchall()
        self.tableWidget.setColumnCount(len(['ID', 'сорт', 'обжарка', 'молотый или в зернах', 'вкус', 'цена', 'объем']))
        self.tableWidget.setRowCount(len(dun))
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'сорт', 'обжарка', 'молотый или в зернах', 'вкус', 'цена', 'объем'])
        for i, elem in enumerate(dun):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyProgram()
    form.show()
    sys.exit(app.exec())
