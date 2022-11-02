from PyQt5 import QtCore, QtGui, QtWidgets
from login_fillin import RegisterCheck, PasswordCheck, ChangeButtonColor
from item_price import Meal, Drink
from receipt import ReceiptPrint
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1241, 863)
        MainWindow.setStyleSheet("background-color: rgb(36, 49, 60);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(36, 49, 60);")
        self.centralwidget.setObjectName("centralwidget")
        self.switch_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.switch_tabs.setGeometry(QtCore.QRect(-10, -30, 1391, 941))
        self.switch_tabs.setStyleSheet("background-color: rgb(36, 49, 60);")
        self.switch_tabs.setObjectName("switch_tabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.login_button1 = QtWidgets.QPushButton(self.tab)
        self.login_button1.setGeometry(QtCore.QRect(620, 140, 191, 51))
        self.login_button1.setStyleSheet("background-color: rgb(67, 82, 89);\n"
                                         "color: rgb(198, 198, 198);\n"
                                         "font: 14pt \"MS Shell Dlg 2\";\n"
                                         "gridline-color: rgb(24, 160, 123);")
        self.login_button1.setDefault(False)
        self.login_button1.setFlat(False)
        self.login_button1.setObjectName("login_button1")
        self.signup_button1 = QtWidgets.QPushButton(self.tab)
        self.signup_button1.setGeometry(QtCore.QRect(440, 140, 181, 51))
        self.signup_button1.setStyleSheet("background-color: rgb(24, 160, 123);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 14pt \"MS Shell Dlg 2\";\n"
                                          "gridline-color: rgb(24, 160, 123);")
        self.signup_button1.setObjectName("signup_button1")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(400, 70, 451, 591))
        self.label.setStyleSheet("background-color: rgb(36, 49, 60);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(440, 210, 371, 71))
        self.label_3.setStyleSheet("background-color: rgb(36, 49, 60);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "font: 20pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.name1 = QtWidgets.QLineEdit(self.tab)
        self.name1.setGeometry(QtCore.QRect(480, 300, 301, 41))
        self.name1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 13pt \"MS Shell Dlg 2\";")
        self.name1.setObjectName("name1")
        self.email1 = QtWidgets.QLineEdit(self.tab)
        self.email1.setGeometry(QtCore.QRect(480, 370, 301, 41))
        self.email1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "font: 13pt \"MS Shell Dlg 2\";")
        self.email1.setObjectName("email1")
        self.password1 = QtWidgets.QLineEdit(self.tab)
        self.password1.setGeometry(QtCore.QRect(480, 440, 301, 41))
        self.password1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 13pt \"MS Shell Dlg 2\";")
        self.password1.setObjectName("password1")
        self.sign_up_buttonstarted = QtWidgets.QPushButton(self.tab)
        self.sign_up_buttonstarted.setGeometry(QtCore.QRect(480, 530, 301, 51))
        self.sign_up_buttonstarted.setStyleSheet("background-color: rgb(24, 160, 123);\n"
                                                 "color: rgb(255, 255, 255);\n"
                                                 "font: 14pt \"MS Shell Dlg 2\";\n"
                                                 "gridline-color: rgb(24, 160, 123);")
        self.sign_up_buttonstarted.setObjectName("sign_up_buttonstarted")
        self.error_label = QtWidgets.QLabel(self.tab)
        self.error_label.setGeometry(QtCore.QRect(480, 490, 301, 16))
        self.error_label.setStyleSheet("color: rgb(255, 48, 48);\n"
                                       "font: 10pt \"MS Shell Dlg 2\";")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.label.raise_()
        self.login_button1.raise_()
        self.signup_button1.raise_()
        self.label_3.raise_()
        self.name1.raise_()
        self.email1.raise_()
        self.password1.raise_()
        self.sign_up_buttonstarted.raise_()
        self.error_label.raise_()
        self.switch_tabs.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(400, 70, 451, 591))
        self.label_2.setStyleSheet("background-color: rgb(36, 49, 60);")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.signup_button2 = QtWidgets.QPushButton(self.tab_2)
        self.signup_button2.setGeometry(QtCore.QRect(440, 140, 181, 51))
        self.signup_button2.setStyleSheet("background-color: rgb(24, 160, 123);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 14pt \"MS Shell Dlg 2\";\n"
                                          "")
        self.signup_button2.setObjectName("signup_button2")
        self.login_button2 = QtWidgets.QPushButton(self.tab_2)
        self.login_button2.setGeometry(QtCore.QRect(620, 140, 191, 51))
        self.login_button2.setStyleSheet("background-color: rgb(67, 82, 89);\n"
                                         "color: rgb(198, 198, 198);\n"
                                         "font: 14pt \"MS Shell Dlg 2\";\n"
                                         "gridline-color: rgb(24, 160, 123);")
        self.login_button2.setDefault(False)
        self.login_button2.setFlat(False)
        self.login_button2.setObjectName("login_button2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(440, 210, 371, 71))
        self.label_4.setStyleSheet("background-color: rgb(36, 49, 60);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "font: 20pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.name2 = QtWidgets.QLineEdit(self.tab_2)
        self.name2.setGeometry(QtCore.QRect(480, 300, 301, 41))
        self.name2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 13pt \"MS Shell Dlg 2\";")
        self.name2.setObjectName("name2")
        self.password2 = QtWidgets.QLineEdit(self.tab_2)
        self.password2.setGeometry(QtCore.QRect(480, 370, 301, 41))
        self.password2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 13pt \"MS Shell Dlg 2\";")
        self.password2.setObjectName("password2")
        self.password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_buttonstarted = QtWidgets.QPushButton(self.tab_2)
        self.login_buttonstarted.setGeometry(QtCore.QRect(480, 450, 301, 51))
        self.login_buttonstarted.setStyleSheet("background-color: rgb(24, 160, 123);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "font: 14pt \"MS Shell Dlg 2\";\n"
                                               "gridline-color: rgb(24, 160, 123);")
        self.login_buttonstarted.setObjectName("login_buttonstarted")
        self.error_label_2 = QtWidgets.QLabel(self.tab_2)
        self.error_label_2.setGeometry(QtCore.QRect(480, 420, 301, 16))
        self.error_label_2.setStyleSheet("color: rgb(255, 48, 48);\n"
                                         "font: 10pt \"MS Shell Dlg 2\";")
        self.error_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label_2.setObjectName("error_label_2")
        self.switch_tabs.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(0, -20, 1251, 111))
        self.label_5.setStyleSheet("background-color: rgb(36, 49, 60);")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.datelabel = QtWidgets.QLabel(self.tab_3)
        self.datelabel.setGeometry(QtCore.QRect(880, 40, 531, 41))
        self.datelabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 15pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(36, 49, 60);")
        self.datelabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.datelabel.setObjectName("datelabel")
        self.operator_name = QtWidgets.QLabel(self.tab_3)
        self.operator_name.setGeometry(QtCore.QRect(620, 40, 231, 31))
        self.operator_name.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "font: 15pt \"MS Shell Dlg 2\";\n"
                                         "background-color: rgb(36, 49, 60);")
        self.operator_name.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.operator_name.setObjectName("operator_name")
        self.operatorlabel = QtWidgets.QLabel(self.tab_3)
        self.operatorlabel.setGeometry(QtCore.QRect(490, 40, 121, 31))
        self.operatorlabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "font: 15pt \"MS Shell Dlg 2\";\n"
                                         "background-color: rgb(36, 49, 60);")
        self.operatorlabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.operatorlabel.setObjectName("operatorlabel")
        self.operatorlabel_2 = QtWidgets.QLabel(self.tab_3)
        self.operatorlabel_2.setGeometry(QtCore.QRect(20, 40, 341, 31))
        self.operatorlabel_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "font: 15pt \"MS Shell Dlg 2\";\n"
                                           "background-color: rgb(36, 49, 60);")
        self.operatorlabel_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.operatorlabel_2.setObjectName("operatorlabel_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 180, 291, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.item2_spinbox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.item2_spinbox.setStyleSheet("background-color: rgb(83, 113, 138);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font: 15pt \"MS Shell Dlg 2\";")
        self.item2_spinbox.setObjectName("item2_spinbox")
        self.gridLayout.addWidget(self.item2_spinbox, 1, 1, 1, 1)
        self.item2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.item2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 15pt \"MS Shell Dlg 2\";")
        self.item2.setObjectName("item2")
        self.gridLayout.addWidget(self.item2, 1, 0, 1, 1)
        self.item1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.item1.setFont(font)
        self.item1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 15pt \"MS Shell Dlg 2\";")
        self.item1.setObjectName("item1")
        self.gridLayout.addWidget(self.item1, 0, 0, 1, 1)
        self.item1_spinbox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.item1_spinbox.setFont(font)
        self.item1_spinbox.setStyleSheet("background-color: rgb(83, 113, 138);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font: 15pt \"MS Shell Dlg 2\";")
        self.item1_spinbox.setObjectName("item1_spinbox")
        self.gridLayout.addWidget(self.item1_spinbox, 0, 1, 1, 1)
        self.item3_spinbox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.item3_spinbox.setStyleSheet("background-color: rgb(83, 113, 138);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font: 15pt \"MS Shell Dlg 2\";")
        self.item3_spinbox.setObjectName("item3_spinbox")
        self.gridLayout.addWidget(self.item3_spinbox, 2, 1, 1, 1)
        self.item4_spinbox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.item4_spinbox.setStyleSheet("background-color: rgb(83, 113, 138);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font: 15pt \"MS Shell Dlg 2\";")
        self.item4_spinbox.setObjectName("item4_spinbox")
        self.gridLayout.addWidget(self.item4_spinbox, 3, 1, 1, 1)
        self.item3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.item3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 15pt \"MS Shell Dlg 2\";")
        self.item3.setObjectName("item3")
        self.gridLayout.addWidget(self.item3, 2, 0, 1, 1)
        self.item4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.item4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 15pt \"MS Shell Dlg 2\";")
        self.item4.setObjectName("item4")
        self.gridLayout.addWidget(self.item4, 3, 0, 1, 1)
        self.item5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.item5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 15pt \"MS Shell Dlg 2\";")
        self.item5.setObjectName("item5")
        self.gridLayout.addWidget(self.item5, 4, 0, 1, 1)
        self.item5_spinbox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.item5_spinbox.setStyleSheet("background-color: rgb(83, 113, 138);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font: 15pt \"MS Shell Dlg 2\";")
        self.item5_spinbox.setObjectName("item5_spinbox")
        self.gridLayout.addWidget(self.item5_spinbox, 4, 1, 1, 1)
        self.mealtitle = QtWidgets.QLabel(self.tab_3)
        self.mealtitle.setGeometry(QtCore.QRect(80, 140, 271, 31))
        self.mealtitle.setStyleSheet("background-color: rgb(83, 113, 138);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "font: 75 20pt \"MS Shell Dlg 2\";")
        self.mealtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.mealtitle.setObjectName("mealtitle")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(30, 120, 371, 371))
        self.label_6.setStyleSheet("background-color: rgb(83, 113, 138);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(430, 120, 371, 371))
        self.label_7.setStyleSheet("background-color: rgb(83, 113, 138);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.drinktitle = QtWidgets.QLabel(self.tab_3)
        self.drinktitle.setGeometry(QtCore.QRect(480, 140, 271, 31))
        self.drinktitle.setStyleSheet("background-color: rgb(83, 113, 138);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 75 20pt \"MS Shell Dlg 2\";")
        self.drinktitle.setAlignment(QtCore.Qt.AlignCenter)
        self.drinktitle.setObjectName("drinktitle")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(470, 180, 291, 271))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.drink2_spinbox = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.drink2_spinbox.setStyleSheet("background-color: rgb(83, 113, 138);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 15pt \"MS Shell Dlg 2\";")
        self.drink2_spinbox.setObjectName("drink2_spinbox")
        self.gridLayout_2.addWidget(self.drink2_spinbox, 1, 1, 1, 1)
        self.drink2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.drink2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "font: 15pt \"MS Shell Dlg 2\";")
        self.drink2.setObjectName("drink2")
        self.gridLayout_2.addWidget(self.drink2, 1, 0, 1, 1)
        self.drink1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.drink1.setFont(font)
        self.drink1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "font: 15pt \"MS Shell Dlg 2\";")
        self.drink1.setObjectName("drink1")
        self.gridLayout_2.addWidget(self.drink1, 0, 0, 1, 1)
        self.drink1_spinbox = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.drink1_spinbox.setFont(font)
        self.drink1_spinbox.setStyleSheet("background-color: rgb(83, 113, 138);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 15pt \"MS Shell Dlg 2\";")
        self.drink1_spinbox.setObjectName("drink1_spinbox")
        self.gridLayout_2.addWidget(self.drink1_spinbox, 0, 1, 1, 1)
        self.drink3_spinbox = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.drink3_spinbox.setStyleSheet("background-color: rgb(83, 113, 138);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 15pt \"MS Shell Dlg 2\";")
        self.drink3_spinbox.setObjectName("drink3_spinbox")
        self.gridLayout_2.addWidget(self.drink3_spinbox, 2, 1, 1, 1)
        self.drink4_spinbox = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.drink4_spinbox.setStyleSheet("background-color: rgb(83, 113, 138);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 15pt \"MS Shell Dlg 2\";")
        self.drink4_spinbox.setObjectName("drink4_spinbox")
        self.gridLayout_2.addWidget(self.drink4_spinbox, 3, 1, 1, 1)
        self.drink3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.drink3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "font: 15pt \"MS Shell Dlg 2\";")
        self.drink3.setObjectName("drink3")
        self.gridLayout_2.addWidget(self.drink3, 2, 0, 1, 1)
        self.drink4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.drink4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "font: 15pt \"MS Shell Dlg 2\";")
        self.drink4.setObjectName("drink4")
        self.gridLayout_2.addWidget(self.drink4, 3, 0, 1, 1)
        self.drink5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.drink5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "font: 15pt \"MS Shell Dlg 2\";")
        self.drink5.setObjectName("drink5")
        self.gridLayout_2.addWidget(self.drink5, 4, 0, 1, 1)
        self.drink5_spinbox = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.drink5_spinbox.setStyleSheet("background-color: rgb(83, 113, 138);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 15pt \"MS Shell Dlg 2\";")
        self.drink5_spinbox.setObjectName("drink5_spinbox")
        self.gridLayout_2.addWidget(self.drink5_spinbox, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(30, 510, 371, 171))
        self.label_8.setStyleSheet("background-color: rgb(83, 113, 138);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(430, 510, 371, 171))
        self.label_9.setStyleSheet("background-color: rgb(83, 113, 138);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(50, 520, 331, 151))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.total_cost = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.total_cost.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 15pt \"MS Shell Dlg 2\";")
        self.total_cost.setObjectName("total_cost")
        self.gridLayout_4.addWidget(self.total_cost, 2, 0, 1, 1)
        self.meal_cost = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.meal_cost.setFont(font)
        self.meal_cost.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 15pt \"MS Shell Dlg 2\";")
        self.meal_cost.setObjectName("meal_cost")
        self.gridLayout_4.addWidget(self.meal_cost, 0, 0, 1, 1)
        self.drink_cost = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.drink_cost.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 15pt \"MS Shell Dlg 2\";")
        self.drink_cost.setObjectName("drink_cost")
        self.gridLayout_4.addWidget(self.drink_cost, 1, 0, 1, 1)
        self.meal_cost_price = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.meal_cost_price.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "font: 15pt \"MS Shell Dlg 2\";")
        self.meal_cost_price.setAlignment(QtCore.Qt.AlignCenter)
        self.meal_cost_price.setObjectName("meal_cost_price")
        self.gridLayout_4.addWidget(self.meal_cost_price, 0, 1, 1, 1)
        self.drink_cost_price = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.drink_cost_price.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "font: 15pt \"MS Shell Dlg 2\";")
        self.drink_cost_price.setAlignment(QtCore.Qt.AlignCenter)
        self.drink_cost_price.setObjectName("drink_cost_price")
        self.gridLayout_4.addWidget(self.drink_cost_price, 1, 1, 1, 1)
        self.total_cost_price = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.total_cost_price.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "font: 15pt \"MS Shell Dlg 2\";")
        self.total_cost_price.setAlignment(QtCore.Qt.AlignCenter)
        self.total_cost_price.setObjectName("total_cost_price")
        self.gridLayout_4.addWidget(self.total_cost_price, 2, 1, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(450, 520, 331, 151))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.final_total = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.final_total.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "font: 15pt \"MS Shell Dlg 2\";")
        self.final_total.setObjectName("final_total")
        self.gridLayout_5.addWidget(self.final_total, 2, 0, 1, 1)
        self.tax = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tax.setFont(font)
        self.tax.setStyleSheet("color: rgb(255, 255, 255);\n"
                               "font: 15pt \"MS Shell Dlg 2\";")
        self.tax.setObjectName("tax")
        self.gridLayout_5.addWidget(self.tax, 0, 0, 1, 1)
        self.subtotal = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.subtotal.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 15pt \"MS Shell Dlg 2\";")
        self.subtotal.setObjectName("subtotal")
        self.gridLayout_5.addWidget(self.subtotal, 1, 0, 1, 1)
        self.tax_box = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.tax_box.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 15pt \"MS Shell Dlg 2\";")
        self.tax_box.setAlignment(QtCore.Qt.AlignCenter)
        self.tax_box.setObjectName("tax_box")
        self.gridLayout_5.addWidget(self.tax_box, 0, 1, 1, 1)
        self.subtotal_box = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.subtotal_box.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 15pt \"MS Shell Dlg 2\";")
        self.subtotal_box.setAlignment(QtCore.Qt.AlignCenter)
        self.subtotal_box.setObjectName("subtotal_box")
        self.gridLayout_5.addWidget(self.subtotal_box, 1, 1, 1, 1)
        self.final_total_box = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.final_total_box.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "font: 15pt \"MS Shell Dlg 2\";")
        self.final_total_box.setAlignment(QtCore.Qt.AlignCenter)
        self.final_total_box.setObjectName("final_total_box")
        self.gridLayout_5.addWidget(self.final_total_box, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(30, 710, 771, 61))
        self.label_10.setStyleSheet("background-color: rgb(83, 113, 138);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.total_button = QtWidgets.QPushButton(self.tab_3)
        self.total_button.setGeometry(QtCore.QRect(60, 720, 151, 41))
        self.total_button.setStyleSheet("background-color: rgb(24, 160, 123);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 14pt \"MS Shell Dlg 2\";\n"
                                        "gridline-color: rgb(24, 160, 123);")
        self.total_button.setObjectName("total_button")
        self.receipt_button = QtWidgets.QPushButton(self.tab_3)
        self.receipt_button.setGeometry(QtCore.QRect(240, 720, 151, 41))
        self.receipt_button.setStyleSheet("background-color: rgb(24, 160, 123);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 14pt \"MS Shell Dlg 2\";\n"
                                          "gridline-color: rgb(24, 160, 123);")
        self.receipt_button.setObjectName("receipt_button")
        self.reset_button = QtWidgets.QPushButton(self.tab_3)
        self.reset_button.setGeometry(QtCore.QRect(430, 720, 151, 41))
        self.reset_button.setStyleSheet("background-color: rgb(24, 160, 123);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 14pt \"MS Shell Dlg 2\";\n"
                                        "gridline-color: rgb(24, 160, 123);")
        self.reset_button.setObjectName("reset_button")
        self.exit_button = QtWidgets.QPushButton(self.tab_3)
        self.exit_button.setGeometry(QtCore.QRect(620, 720, 151, 41))
        self.exit_button.setStyleSheet("background-color: rgb(24, 160, 123);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font: 14pt \"MS Shell Dlg 2\";\n"
                                       "gridline-color: rgb(24, 160, 123);")
        self.exit_button.setObjectName("exit_button")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(820, 120, 401, 651))
        self.label_11.setStyleSheet("background-color: rgb(83, 113, 138);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.receipt_label = QtWidgets.QPlainTextEdit(self.tab_3)
        self.receipt_label.setGeometry(QtCore.QRect(830, 130, 381, 631))
        self.receipt_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "font: 10pt \"MS Shell Dlg 2\";")
        self.receipt_label.setObjectName("receipt_label")
        self.receipt_label.setReadOnly(True)
        self.label_6.raise_()
        self.label_5.raise_()
        self.datelabel.raise_()
        self.operator_name.raise_()
        self.operatorlabel.raise_()
        self.operatorlabel_2.raise_()
        self.gridLayoutWidget.raise_()
        self.mealtitle.raise_()
        self.label_7.raise_()
        self.drinktitle.raise_()
        self.gridLayoutWidget_2.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.gridLayoutWidget_3.raise_()
        self.gridLayoutWidget_4.raise_()
        self.label_10.raise_()
        self.total_button.raise_()
        self.receipt_button.raise_()
        self.reset_button.raise_()
        self.exit_button.raise_()
        self.label_11.raise_()
        self.receipt_label.raise_()
        self.switch_tabs.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1241, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.switch_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Switch Tab Call Function ------------------------------------------------------------
        self.login_button1.clicked.connect(self.next_tab)
        self.signup_button2.clicked.connect(self.prev_tab)

    # ---------------------------------------------------------------
      # Start Program
        self.sign_up_buttonstarted.clicked.connect(self.sign_up)
        self.login_buttonstarted.clicked.connect(self.log_in)

    # ----------------------------------------------------------------------------
        self.total_button.clicked.connect(self.totalitem_price)
        self.receipt_button.clicked.connect(self.receipt_print)

    # -------------------------------------------------------------------------

        self.exit_button.clicked.connect(self.sysexit)
        self.reset_button.clicked.connect(self.reset)

    # -------------------------------------------------------------------------
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_button1.setText(_translate("MainWindow", "Log in"))
        self.signup_button1.setText(_translate("MainWindow", "Sign Up"))
        self.label_3.setText(_translate("MainWindow", "Create an Account"))
        self.name1.setPlaceholderText(_translate("MainWindow", "   Name"))
        self.email1.setPlaceholderText(_translate("MainWindow", "   Email"))
        self.password1.setPlaceholderText(_translate("MainWindow", "  Password"))
        self.sign_up_buttonstarted.setText(_translate("MainWindow", "LOGIN"))
        self.error_label.setText(_translate("MainWindow", ""))
        self.switch_tabs.setTabText(self.switch_tabs.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.signup_button2.setText(_translate("MainWindow", "Sign Up"))
        self.login_button2.setText(_translate("MainWindow", "Log in"))
        self.label_4.setText(_translate("MainWindow", "Log in"))
        self.name2.setPlaceholderText(_translate("MainWindow", "   Name"))
        self.password2.setPlaceholderText(_translate("MainWindow", "   Password"))
        self.login_buttonstarted.setText(_translate("MainWindow", "LOGIN"))
        self.error_label_2.setText(_translate("MainWindow", ""))
        self.switch_tabs.setTabText(self.switch_tabs.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.datelabel.setText(_translate("MainWindow", f"Today Date: {str(datetime.datetime.now().date())}\n"
                                                        ""))
        self.operator_name.setText(_translate("MainWindow", "Admin"))
        self.operatorlabel.setText(_translate("MainWindow", "Operator ID: "))
        self.operatorlabel_2.setText(_translate("MainWindow", "Order Management System"))
        self.item2.setText(_translate("MainWindow", "Bacon Egg and Cheese"))
        self.item1.setText(_translate("MainWindow", "Chicken Burger"))
        self.item3.setText(_translate("MainWindow", "Fried Chicken"))
        self.item4.setText(_translate("MainWindow", "Pancake"))
        self.item5.setText(_translate("MainWindow", "Wings"))
        self.mealtitle.setText(_translate("MainWindow", "Meals"))
        self.drinktitle.setText(_translate("MainWindow", "Drinks"))
        self.drink2.setText(_translate("MainWindow", "Vanilla Milk Shake"))
        self.drink1.setText(_translate("MainWindow", "Milk Share"))
        self.drink3.setText(_translate("MainWindow", "Coke"))
        self.drink4.setText(_translate("MainWindow", "Sprite"))
        self.drink5.setText(_translate("MainWindow", "Water"))
        self.total_cost.setText(_translate("MainWindow", "Total Cost of Meal"))
        self.meal_cost.setText(_translate("MainWindow", "Cost of Meals"))
        self.drink_cost.setText(_translate("MainWindow", "Cost of Drinks"))
        self.final_total.setText(_translate("MainWindow", "Total"))
        self.tax.setText(_translate("MainWindow", "Tax"))
        self.subtotal.setText(_translate("MainWindow", "SubTotal"))
        self.total_button.setText(_translate("MainWindow", "Total"))
        self.receipt_button.setText(_translate("MainWindow", "Receipt"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.switch_tabs.setTabText(self.switch_tabs.indexOf(self.tab_3), _translate("MainWindow", "Page"))

    def next_tab(self):
        change_button_color = ChangeButtonColor()

        change_button_color.log_in_click(self.login_button2)
        change_button_color.sign_up_click(self.signup_button2)

        self.switch_tabs.setCurrentIndex(self.switch_tabs.currentIndex() + 1)


    def prev_tab(self):
        self.switch_tabs.setCurrentIndex(self.switch_tabs.currentIndex() - 1)


    def sign_up(self):
        check = RegisterCheck()
        info_writeup = PasswordCheck()

        check.signup_checking(self.name1,self.email1, self.password1, self.error_label, self.switch_tabs)
        info_writeup.sign_up_info(self.name1.text(), self.password1.text())

    def log_in(self):
        check = RegisterCheck()
        info_read = PasswordCheck()

        if info_read.login_check(self.name2.text(), self.password2.text(), self.error_label_2):
            check.login_checking(self.name2, self.password2, self.error_label_2, self.switch_tabs)
            self.operator_id()

    def operator_id(self):
        self.operator_name.setText(self.name2.text().capitalize())

    def totalitem_price(self):
        meal_total, drink_total = Meal(), Drink()

        meal = meal_total.cost_of_meals(self.item1_spinbox.value(),self.item2_spinbox.value(),self.item3_spinbox.value(),self.item4_spinbox.value(),self.item5_spinbox.value(), self.meal_cost_price)
        drink = drink_total.cost_of_drinks(self.drink1_spinbox.value(),self.drink2_spinbox.value(),self.drink3_spinbox.value(),self.drink4_spinbox.value(),self.drink5_spinbox.value(),self.drink_cost_price)

        self.tax_info = round((meal + drink) * 0.10, 2)
        self.tax_box.setText(f'${self.tax_info}')
        self.total_info = self.total_cost_price.setText(f'${round(meal + drink, 2)}')
        self.subtotal_info = round(meal + drink, 2)
        self.subtotal_box.setText(f'${self.subtotal_info}')
        self.final_info = round((meal + drink) * 0.10 + (meal + drink),2)
        self.final_total_box.setText(f'${self.final_info}')


    def receipt_print(self):
        receipt_send = ReceiptPrint()
        items = {self.item1.text():self.item1_spinbox.value(),
                 self.item2.text():self.item2_spinbox.value(),
                 self.item3.text():self.item3_spinbox.value(),
                 self.item4.text():self.item4_spinbox.value(),
                 self.item5.text():self.item5_spinbox.value(),
                 self.drink1.text(): self.drink1_spinbox.value(),
                 self.drink2.text():self.drink2_spinbox.value(),
                 self.drink3.text():self.drink3_spinbox.value(),
                 self.drink4.text():self.drink4_spinbox.value(),
                 self.drink5.text():self.drink5_spinbox.value()
                 }

        receipt_send.item_load(items, self.receipt_label,self.tax_info, self.subtotal_info, self.final_info, str(datetime.datetime.now().date()))

    def reset(self):
        Ui_MainWindow.setupUi(self, MainWindow)
        self.switch_tabs.setCurrentIndex(self.switch_tabs.currentIndex() + 2)

    def sysexit(self):
        sys.exit()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
