import os
import keyboard

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QMovie
from PyQt5 import QtTest
from PyQt5.QtCore import Qt


from UI import Ui_MainWindow
from scheduler import *

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        self.init_time_line()

        self.file_path = ""
        self.text_content = ""

        # init color 
        self.color = {
            "N": "rgb(160, 160, 160)",
            "P": "rgb(211, 82, 48)",
            "A": "rgb(0, 174, 0)",
            "S": "rgb(70, 165, 255)"
        }

    def setup_control(self):
        self.ui.select_file_btn.clicked.connect(self.select_file)
        self.ui.schedule_btn.clicked.connect(self.schedule)

    def select_file(self):
        self.file_path = QFileDialog.getOpenFileName(filter = "JSON Files (*.json)")[0]
        basename = self.file_path.split("/")[-1]
        self.print_msg(str(f"Selected file : {basename}\n"))

    def schedule(self):
        if os.path.exists(self.file_path) == False:
            self.print_msg("Please select a file first!\n")
            return
        self.schedule = Scheduler(self.file_path)
        self.schedule.schedule()

        for text in self.schedule.output_list:
            if text == "-1\n":
                self.print_msg("-1\n")
                QtTest.QTest.qWait(2000)
                for i in range(0, MAX_TIME):
                    color = self.color["N"]
                    self.time_line[i].setStyleSheet(f"background-color: {color};")
                    self.time_line[i].setText("")
                break
            if text == "FINISH":
                self.print_msg("Press Space to continue...\n")
                QtTest.QTest.qWait(200)
                while keyboard.is_pressed('space') == False:
                    continue
                for i in range(MAX_TIME):
                    color = self.color["N"]
                    self.time_line[i].setStyleSheet(f"background-color: {color};")
                    self.time_line[i].setText("")
                continue
            
            QtTest.QTest.qWait(500)
            self.print_msg(text)
            tokens = text.split(" ") 
            if len(tokens) < 5 or tokens[4] != "Complete\n":
                continue

            name = tokens[0]+tokens[1]
            start = int(tokens[2])
            end = int(tokens[3])
            if start != -1 and end != -1:
                for i in range(start, end):
                    color = self.color[tokens[0]]
                    self.time_line[i].setStyleSheet(f"background-color: {color};")
                    self.time_line[i].setText(name)
         

    def print_msg(self, text):
        self.text_content += text
        self.ui.textBrowser.setText(self.text_content)
        self.ui.textBrowser.moveCursor(self.ui.textBrowser.textCursor().End)


    def init_time_line(self):
        self.time_line = []
        self.time_line.append(self.ui.t00)
        self.time_line.append(self.ui.t01)
        self.time_line.append(self.ui.t02)
        self.time_line.append(self.ui.t03)
        self.time_line.append(self.ui.t04)
        self.time_line.append(self.ui.t05)
        self.time_line.append(self.ui.t06)
        self.time_line.append(self.ui.t07)
        self.time_line.append(self.ui.t08)
        self.time_line.append(self.ui.t09)
        self.time_line.append(self.ui.t10)
        self.time_line.append(self.ui.t11)
        self.time_line.append(self.ui.t12)
        self.time_line.append(self.ui.t13)
        self.time_line.append(self.ui.t14)
        self.time_line.append(self.ui.t15)
        self.time_line.append(self.ui.t16)
        self.time_line.append(self.ui.t17)
        self.time_line.append(self.ui.t18)
        self.time_line.append(self.ui.t19)
        self.time_line.append(self.ui.t20)
        self.time_line.append(self.ui.t21)
        self.time_line.append(self.ui.t22)
        self.time_line.append(self.ui.t23)
        self.time_line.append(self.ui.t24)
        self.time_line.append(self.ui.t25)
        self.time_line.append(self.ui.t26)
        self.time_line.append(self.ui.t27)
        self.time_line.append(self.ui.t28)
        self.time_line.append(self.ui.t29)
        self.time_line.append(self.ui.t30)
        self.time_line.append(self.ui.t31)
        self.time_line.append(self.ui.t32)
        self.time_line.append(self.ui.t33)
        self.time_line.append(self.ui.t34)
        self.time_line.append(self.ui.t35)
        self.time_line.append(self.ui.t36)
        self.time_line.append(self.ui.t37)
        self.time_line.append(self.ui.t38)
        self.time_line.append(self.ui.t39)
        self.time_line.append(self.ui.t40)
        self.time_line.append(self.ui.t41)
        self.time_line.append(self.ui.t42)
        self.time_line.append(self.ui.t43)
        self.time_line.append(self.ui.t44)
        self.time_line.append(self.ui.t45)
        self.time_line.append(self.ui.t46)
        self.time_line.append(self.ui.t47)
        self.time_line.append(self.ui.t48)
        self.time_line.append(self.ui.t49)
        self.time_line.append(self.ui.t50)
        self.time_line.append(self.ui.t51)
        self.time_line.append(self.ui.t52)
        self.time_line.append(self.ui.t53)
        self.time_line.append(self.ui.t54)
        self.time_line.append(self.ui.t55)
        self.time_line.append(self.ui.t56)
        self.time_line.append(self.ui.t57)
        self.time_line.append(self.ui.t58)
        self.time_line.append(self.ui.t59)
        self.time_line.append(self.ui.t60)
        self.time_line.append(self.ui.t61)
        self.time_line.append(self.ui.t62)
        self.time_line.append(self.ui.t63)
        self.time_line.append(self.ui.t64)
        self.time_line.append(self.ui.t65)
        self.time_line.append(self.ui.t66)
        self.time_line.append(self.ui.t67)
        self.time_line.append(self.ui.t68)
        self.time_line.append(self.ui.t69)
        self.time_line.append(self.ui.t70)
        self.time_line.append(self.ui.t71)
        self.time_line.append(self.ui.t72)
        self.time_line.append(self.ui.t73)
        self.time_line.append(self.ui.t74)
        self.time_line.append(self.ui.t75)
        self.time_line.append(self.ui.t76)
        self.time_line.append(self.ui.t77)
        self.time_line.append(self.ui.t78)
        self.time_line.append(self.ui.t79)
        self.time_line.append(self.ui.t80)
        self.time_line.append(self.ui.t81)
        self.time_line.append(self.ui.t82)
        self.time_line.append(self.ui.t83)
        self.time_line.append(self.ui.t84)
        self.time_line.append(self.ui.t85)
        self.time_line.append(self.ui.t86)
        self.time_line.append(self.ui.t87)
        self.time_line.append(self.ui.t88)
        self.time_line.append(self.ui.t89)
        self.time_line.append(self.ui.t90)
        self.time_line.append(self.ui.t91)
        self.time_line.append(self.ui.t92)
        self.time_line.append(self.ui.t93)
        self.time_line.append(self.ui.t94)
        self.time_line.append(self.ui.t95)
        self.time_line.append(self.ui.t96)
        self.time_line.append(self.ui.t97)
        self.time_line.append(self.ui.t98)
        self.time_line.append(self.ui.t99)