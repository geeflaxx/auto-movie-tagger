# Form implementation generated from reading ui file 'results.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_select = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_select.setGeometry(QtCore.QRect(490, 530, 75, 23))
        self.pushButton_select.setObjectName("pushButton_select")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(520, 100, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.tableView_movies = QtWidgets.QTableView(self.centralwidget)
        self.tableView_movies.setGeometry(QtCore.QRect(10, 10, 331, 581))
        self.tableView_movies.setObjectName("tableView_movies")
        self.label_imdbnr = QtWidgets.QLabel(self.centralwidget)
        self.label_imdbnr.setGeometry(QtCore.QRect(710, 20, 71, 16))
        self.label_imdbnr.setObjectName("label_imdbnr")
        self.label_rate = QtWidgets.QLabel(self.centralwidget)
        self.label_rate.setGeometry(QtCore.QRect(360, 120, 71, 16))
        self.label_rate.setObjectName("label_rate")
        self.label_genre = QtWidgets.QLabel(self.centralwidget)
        self.label_genre.setGeometry(QtCore.QRect(360, 70, 47, 13))
        self.label_genre.setObjectName("label_genre")
        self.label_regisseure = QtWidgets.QLabel(self.centralwidget)
        self.label_regisseure.setGeometry(QtCore.QRect(360, 170, 71, 16))
        self.label_regisseure.setObjectName("label_regisseure")
        self.lineEdit_regisseur = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_regisseur.setGeometry(QtCore.QRect(380, 190, 113, 20))
        self.lineEdit_regisseur.setObjectName("lineEdit_regisseur")
        self.lineEdit_rate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_rate.setGeometry(QtCore.QRect(380, 140, 113, 20))
        self.lineEdit_rate.setReadOnly(True)
        self.lineEdit_rate.setObjectName("lineEdit_rate")
        self.lineEdit_imdbnr = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_imdbnr.setGeometry(QtCore.QRect(710, 40, 61, 20))
        self.lineEdit_imdbnr.setReadOnly(True)
        self.lineEdit_imdbnr.setObjectName("lineEdit_imdbnr")
        self.lineEdit_genre = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_genre.setGeometry(QtCore.QRect(380, 90, 113, 20))
        self.lineEdit_genre.setObjectName("lineEdit_genre")
        self.label_produzenten = QtWidgets.QLabel(self.centralwidget)
        self.label_produzenten.setGeometry(QtCore.QRect(360, 220, 71, 16))
        self.label_produzenten.setObjectName("label_produzenten")
        self.label_titel = QtWidgets.QLabel(self.centralwidget)
        self.label_titel.setGeometry(QtCore.QRect(360, 20, 47, 13))
        self.label_titel.setObjectName("label_titel")
        self.label_year = QtWidgets.QLabel(self.centralwidget)
        self.label_year.setGeometry(QtCore.QRect(530, 20, 47, 13))
        self.label_year.setObjectName("label_year")
        self.label_cover = QtWidgets.QLabel(self.centralwidget)
        self.label_cover.setGeometry(QtCore.QRect(620, 70, 71, 16))
        self.label_cover.setObjectName("label_cover")
        self.lineEdit_titel = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_titel.setGeometry(QtCore.QRect(380, 40, 113, 20))
        self.lineEdit_titel.setObjectName("lineEdit_titel")
        self.lineEdit_producer = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_producer.setGeometry(QtCore.QRect(380, 240, 113, 20))
        self.lineEdit_producer.setObjectName("lineEdit_producer")
        self.lineEdit_year = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_year.setGeometry(QtCore.QRect(520, 40, 61, 20))
        self.lineEdit_year.setText("")
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.lineEdit_research = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_research.setGeometry(QtCore.QRect(400, 490, 161, 20))
        self.lineEdit_research.setObjectName("lineEdit_research")
        self.pushButton_research = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_research.setGeometry(QtCore.QRect(570, 490, 75, 23))
        self.pushButton_research.setObjectName("pushButton_research")
        self.label_research = QtWidgets.QLabel(self.centralwidget)
        self.label_research.setGeometry(QtCore.QRect(400, 470, 71, 16))
        self.label_research.setObjectName("label_research")
        self.listView_description = QtWidgets.QListView(self.centralwidget)
        self.listView_description.setGeometry(QtCore.QRect(370, 320, 401, 141))
        self.listView_description.setObjectName("listView_description")
        self.label_Description = QtWidgets.QLabel(self.centralwidget)
        self.label_Description.setGeometry(QtCore.QRect(380, 300, 71, 16))
        self.label_Description.setObjectName("label_Description")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_select.setText(_translate("MainWindow", "Select"))
        self.label_imdbnr.setText(_translate("MainWindow", "IMDB Number"))
        self.label_rate.setText(_translate("MainWindow", "IMDB Rate"))
        self.label_genre.setText(_translate("MainWindow", "Genre"))
        self.label_regisseure.setText(_translate("MainWindow", "Regisseur"))
        self.lineEdit_regisseur.setToolTip(_translate("MainWindow", "Regisseur"))
        self.lineEdit_rate.setToolTip(_translate("MainWindow", "IMDB Rate"))
        self.lineEdit_imdbnr.setToolTip(_translate("MainWindow", "Not Enabling"))
        self.lineEdit_genre.setToolTip(_translate("MainWindow", "Genre"))
        self.label_produzenten.setText(_translate("MainWindow", "Producer"))
        self.label_titel.setText(_translate("MainWindow", "Titel"))
        self.label_year.setText(_translate("MainWindow", "Year"))
        self.label_cover.setText(_translate("MainWindow", "Cover"))
        self.lineEdit_titel.setToolTip(_translate("MainWindow", "Titelname"))
        self.lineEdit_producer.setToolTip(_translate("MainWindow", "Producer"))
        self.lineEdit_year.setToolTip(_translate("MainWindow", "Year"))
        self.lineEdit_research.setToolTip(_translate("MainWindow", "Keyword for researching"))
        self.lineEdit_research.setPlaceholderText(_translate("MainWindow", "Keyword for researching"))
        self.pushButton_research.setText(_translate("MainWindow", "Research"))
        self.label_research.setText(_translate("MainWindow", "Research"))
        self.label_Description.setText(_translate("MainWindow", "Description"))
