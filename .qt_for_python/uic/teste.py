# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTextEdit, QWidget)

class Ui_MainWindowUi(object):
    def setupUi(self, MainWindowUi):
        if not MainWindowUi.objectName():
            MainWindowUi.setObjectName(u"MainWindowUi")
        MainWindowUi.resize(1094, 599)
        self.centralwidget = QWidget(MainWindowUi)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelDetectorMentiras = QLabel(self.centralwidget)
        self.labelDetectorMentiras.setObjectName(u"labelDetectorMentiras")
        self.labelDetectorMentiras.setGeometry(QRect(80, 30, 921, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.labelDetectorMentiras.setFont(font)
        self.labelDetectorMentiras.setAlignment(Qt.AlignCenter)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 90, 1041, 481))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.textEdit_2 = QTextEdit(self.tab)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(10, 50, 1011, 291))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.inputPergunta = QLabel(self.tab_2)
        self.inputPergunta.setObjectName(u"inputPergunta")
        self.inputPergunta.setGeometry(QRect(10, 120, 1011, 71))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.inputPergunta.setFont(font1)
        self.inputPergunta.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.tab_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(190, 20, 399, 30))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnStart = QPushButton(self.layoutWidget)
        self.btnStart.setObjectName(u"btnStart")
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        self.btnStart.setFont(font2)

        self.horizontalLayout.addWidget(self.btnStart)

        self.btnPergAnterior = QPushButton(self.layoutWidget)
        self.btnPergAnterior.setObjectName(u"btnPergAnterior")

        self.horizontalLayout.addWidget(self.btnPergAnterior)

        self.btnPergSeguinte = QPushButton(self.layoutWidget)
        self.btnPergSeguinte.setObjectName(u"btnPergSeguinte")

        self.horizontalLayout.addWidget(self.btnPergSeguinte)

        self.btnBitalinoConnect = QPushButton(self.tab_2)
        self.btnBitalinoConnect.setObjectName(u"btnBitalinoConnect")
        self.btnBitalinoConnect.setGeometry(QRect(10, 20, 161, 31))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.btnBitalinoConnect.setFont(font3)
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 270, 1041, 141))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 55, 16))
        font4 = QFont()
        font4.setBold(True)
        self.label.setFont(font4)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 80, 55, 16))
        self.label_2.setFont(font4)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 30, 71, 16))
        self.label_3.setFont(font4)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(610, 30, 111, 16))
        self.label_4.setFont(font4)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 80, 71, 16))
        self.label_5.setFont(font4)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(640, 80, 71, 16))
        self.label_6.setFont(font4)
        self.label_Minimo = QLabel(self.groupBox)
        self.label_Minimo.setObjectName(u"label_Minimo")
        self.label_Minimo.setGeometry(QRect(130, 30, 55, 16))
        self.label_Maximo = QLabel(self.groupBox)
        self.label_Maximo.setObjectName(u"label_Maximo")
        self.label_Maximo.setGeometry(QRect(130, 80, 55, 16))
        self.label_Media = QLabel(self.groupBox)
        self.label_Media.setObjectName(u"label_Media")
        self.label_Media.setGeometry(QRect(410, 30, 55, 16))
        self.label_Mediana = QLabel(self.groupBox)
        self.label_Mediana.setObjectName(u"label_Mediana")
        self.label_Mediana.setGeometry(QRect(410, 80, 55, 16))
        self.label_desvioPadrao = QLabel(self.groupBox)
        self.label_desvioPadrao.setObjectName(u"label_desvioPadrao")
        self.label_desvioPadrao.setGeometry(QRect(740, 30, 55, 16))
        self.label_Variancia = QLabel(self.groupBox)
        self.label_Variancia.setObjectName(u"label_Variancia")
        self.label_Variancia.setGeometry(QRect(740, 80, 55, 16))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.btn_CalcularResultados = QPushButton(self.tab_3)
        self.btn_CalcularResultados.setObjectName(u"btn_CalcularResultados")
        self.btn_CalcularResultados.setGeometry(QRect(60, 30, 111, 41))
        self.btn_CalcularResultados.setFont(font3)
        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(240, 10, 761, 81))
        self.label_Minimo_PR = QLabel(self.groupBox_2)
        self.label_Minimo_PR.setObjectName(u"label_Minimo_PR")
        self.label_Minimo_PR.setGeometry(QRect(220, 20, 55, 16))
        self.label_Media_PR = QLabel(self.groupBox_2)
        self.label_Media_PR.setObjectName(u"label_Media_PR")
        self.label_Media_PR.setGeometry(QRect(410, 20, 55, 16))
        self.label_34 = QLabel(self.groupBox_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(540, 50, 71, 16))
        self.label_34.setFont(font4)
        self.label_Variancia_PR = QLabel(self.groupBox_2)
        self.label_Variancia_PR.setObjectName(u"label_Variancia_PR")
        self.label_Variancia_PR.setGeometry(QRect(630, 50, 55, 16))
        self.label_Maximo_PR = QLabel(self.groupBox_2)
        self.label_Maximo_PR.setObjectName(u"label_Maximo_PR")
        self.label_Maximo_PR.setGeometry(QRect(220, 50, 55, 16))
        self.label_Mediana_PR = QLabel(self.groupBox_2)
        self.label_Mediana_PR.setObjectName(u"label_Mediana_PR")
        self.label_Mediana_PR.setGeometry(QRect(410, 50, 55, 16))
        self.label_desvioPadrao_PR = QLabel(self.groupBox_2)
        self.label_desvioPadrao_PR.setObjectName(u"label_desvioPadrao_PR")
        self.label_desvioPadrao_PR.setGeometry(QRect(630, 20, 55, 16))
        self.label_33 = QLabel(self.groupBox_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(510, 20, 111, 16))
        self.label_33.setFont(font4)
        self.label_29 = QLabel(self.groupBox_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(160, 20, 55, 16))
        self.label_29.setFont(font4)
        self.label_32 = QLabel(self.groupBox_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(330, 50, 71, 16))
        self.label_32.setFont(font4)
        self.label_31 = QLabel(self.groupBox_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(340, 20, 71, 16))
        self.label_31.setFont(font4)
        self.label_30 = QLabel(self.groupBox_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(160, 50, 55, 16))
        self.label_30.setFont(font4)
        self.tabWidget_2 = QTabWidget(self.tab_3)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 120, 1011, 321))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.label_Maximo_RQ1 = QLabel(self.tab_5)
        self.label_Maximo_RQ1.setObjectName(u"label_Maximo_RQ1")
        self.label_Maximo_RQ1.setGeometry(QRect(80, 80, 55, 16))
        self.label_9 = QLabel(self.tab_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(160, 50, 71, 16))
        self.label_9.setFont(font4)
        self.label_12 = QLabel(self.tab_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(330, 80, 71, 16))
        self.label_12.setFont(font4)
        self.label_7 = QLabel(self.tab_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 80, 55, 16))
        self.label_7.setFont(font4)
        self.label_Minimo_RQ1 = QLabel(self.tab_5)
        self.label_Minimo_RQ1.setObjectName(u"label_Minimo_RQ1")
        self.label_Minimo_RQ1.setGeometry(QRect(80, 50, 55, 16))
        self.label_10 = QLabel(self.tab_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(150, 80, 71, 16))
        self.label_10.setFont(font4)
        self.label_Variancia_RQ1 = QLabel(self.tab_5)
        self.label_Variancia_RQ1.setObjectName(u"label_Variancia_RQ1")
        self.label_Variancia_RQ1.setGeometry(QRect(420, 80, 55, 16))
        self.label_Resultado_Q1 = QLabel(self.tab_5)
        self.label_Resultado_Q1.setObjectName(u"label_Resultado_Q1")
        self.label_Resultado_Q1.setGeometry(QRect(20, 150, 461, 121))
        self.label_Mediana_RQ1 = QLabel(self.tab_5)
        self.label_Mediana_RQ1.setObjectName(u"label_Mediana_RQ1")
        self.label_Mediana_RQ1.setGeometry(QRect(230, 80, 55, 16))
        self.label_desvioPadrao_RQ1 = QLabel(self.tab_5)
        self.label_desvioPadrao_RQ1.setObjectName(u"label_desvioPadrao_RQ1")
        self.label_desvioPadrao_RQ1.setGeometry(QRect(420, 50, 55, 16))
        self.label_Media_RQ1 = QLabel(self.tab_5)
        self.label_Media_RQ1.setObjectName(u"label_Media_RQ1")
        self.label_Media_RQ1.setGeometry(QRect(230, 50, 55, 16))
        self.label_11 = QLabel(self.tab_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(300, 50, 111, 16))
        self.label_11.setFont(font4)
        self.label_8 = QLabel(self.tab_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 50, 55, 16))
        self.label_8.setFont(font4)
        self.input_ResultadoFinal_Q1 = QLabel(self.tab_5)
        self.input_ResultadoFinal_Q1.setObjectName(u"input_ResultadoFinal_Q1")
        self.input_ResultadoFinal_Q1.setGeometry(QRect(20, 20, 951, 20))
        self.input_ResultadoFinal_Q1.setFont(font3)
        self.label_13 = QLabel(self.tab_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 120, 111, 31))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.label_13.setFont(font5)
        self.graphicsView_Q1 = QGraphicsView(self.tab_5)
        self.graphicsView_Q1.setObjectName(u"graphicsView_Q1")
        self.graphicsView_Q1.setGeometry(QRect(520, 20, 471, 251))
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.label_Variancia_RQ2 = QLabel(self.tab_6)
        self.label_Variancia_RQ2.setObjectName(u"label_Variancia_RQ2")
        self.label_Variancia_RQ2.setGeometry(QRect(440, 80, 55, 16))
        self.label_Maximo_RQ2 = QLabel(self.tab_6)
        self.label_Maximo_RQ2.setObjectName(u"label_Maximo_RQ2")
        self.label_Maximo_RQ2.setGeometry(QRect(80, 80, 55, 16))
        self.label_18 = QLabel(self.tab_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(170, 50, 71, 16))
        self.label_18.setFont(font4)
        self.label_desvioPadrao_RQ2 = QLabel(self.tab_6)
        self.label_desvioPadrao_RQ2.setObjectName(u"label_desvioPadrao_RQ2")
        self.label_desvioPadrao_RQ2.setGeometry(QRect(440, 50, 55, 16))
        self.label_Media_RQ2 = QLabel(self.tab_6)
        self.label_Media_RQ2.setObjectName(u"label_Media_RQ2")
        self.label_Media_RQ2.setGeometry(QRect(240, 50, 55, 16))
        self.input_ResultadoFinal_Q2 = QLabel(self.tab_6)
        self.input_ResultadoFinal_Q2.setObjectName(u"input_ResultadoFinal_Q2")
        self.input_ResultadoFinal_Q2.setGeometry(QRect(20, 20, 961, 20))
        self.input_ResultadoFinal_Q2.setFont(font3)
        self.label_14 = QLabel(self.tab_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(320, 50, 111, 16))
        self.label_14.setFont(font4)
        self.label_17 = QLabel(self.tab_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 80, 55, 16))
        self.label_17.setFont(font4)
        self.label_Resultado_Q2 = QLabel(self.tab_6)
        self.label_Resultado_Q2.setObjectName(u"label_Resultado_Q2")
        self.label_Resultado_Q2.setGeometry(QRect(20, 150, 461, 121))
        self.label_19 = QLabel(self.tab_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(160, 80, 71, 16))
        self.label_19.setFont(font4)
        self.label_Mediana_RQ2 = QLabel(self.tab_6)
        self.label_Mediana_RQ2.setObjectName(u"label_Mediana_RQ2")
        self.label_Mediana_RQ2.setGeometry(QRect(240, 80, 55, 16))
        self.label_15 = QLabel(self.tab_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(350, 80, 71, 16))
        self.label_15.setFont(font4)
        self.label_20 = QLabel(self.tab_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 120, 111, 31))
        self.label_20.setFont(font5)
        self.label_16 = QLabel(self.tab_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 50, 55, 16))
        self.label_16.setFont(font4)
        self.label_Minimo_RQ2 = QLabel(self.tab_6)
        self.label_Minimo_RQ2.setObjectName(u"label_Minimo_RQ2")
        self.label_Minimo_RQ2.setGeometry(QRect(80, 50, 55, 16))
        self.graphicsView_Q2 = QGraphicsView(self.tab_6)
        self.graphicsView_Q2.setObjectName(u"graphicsView_Q2")
        self.graphicsView_Q2.setGeometry(QRect(520, 20, 471, 251))
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.input_ResultadoFinal_Q3 = QLabel(self.tab_7)
        self.input_ResultadoFinal_Q3.setObjectName(u"input_ResultadoFinal_Q3")
        self.input_ResultadoFinal_Q3.setGeometry(QRect(20, 20, 961, 20))
        self.input_ResultadoFinal_Q3.setFont(font3)
        self.label_23 = QLabel(self.tab_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 50, 55, 16))
        self.label_23.setFont(font4)
        self.label_desvioPadrao_RQ3 = QLabel(self.tab_7)
        self.label_desvioPadrao_RQ3.setObjectName(u"label_desvioPadrao_RQ3")
        self.label_desvioPadrao_RQ3.setGeometry(QRect(440, 50, 55, 16))
        self.label_25 = QLabel(self.tab_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(170, 50, 71, 16))
        self.label_25.setFont(font4)
        self.label_21 = QLabel(self.tab_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(320, 50, 111, 16))
        self.label_21.setFont(font4)
        self.label_Maximo_RQ3 = QLabel(self.tab_7)
        self.label_Maximo_RQ3.setObjectName(u"label_Maximo_RQ3")
        self.label_Maximo_RQ3.setGeometry(QRect(80, 80, 55, 16))
        self.label_Variancia_RQ3 = QLabel(self.tab_7)
        self.label_Variancia_RQ3.setObjectName(u"label_Variancia_RQ3")
        self.label_Variancia_RQ3.setGeometry(QRect(440, 80, 55, 16))
        self.label_Resultado_Q3 = QLabel(self.tab_7)
        self.label_Resultado_Q3.setObjectName(u"label_Resultado_Q3")
        self.label_Resultado_Q3.setGeometry(QRect(20, 150, 471, 121))
        self.label_Media_RQ3 = QLabel(self.tab_7)
        self.label_Media_RQ3.setObjectName(u"label_Media_RQ3")
        self.label_Media_RQ3.setGeometry(QRect(240, 50, 55, 16))
        self.label_26 = QLabel(self.tab_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(160, 80, 71, 16))
        self.label_26.setFont(font4)
        self.label_Mediana_RQ3 = QLabel(self.tab_7)
        self.label_Mediana_RQ3.setObjectName(u"label_Mediana_RQ3")
        self.label_Mediana_RQ3.setGeometry(QRect(240, 80, 55, 16))
        self.label_27 = QLabel(self.tab_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(20, 120, 111, 31))
        self.label_27.setFont(font5)
        self.label_24 = QLabel(self.tab_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 80, 55, 16))
        self.label_24.setFont(font4)
        self.label_Minimo_RQ3 = QLabel(self.tab_7)
        self.label_Minimo_RQ3.setObjectName(u"label_Minimo_RQ3")
        self.label_Minimo_RQ3.setGeometry(QRect(80, 50, 55, 16))
        self.label_22 = QLabel(self.tab_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(350, 80, 71, 16))
        self.label_22.setFont(font4)
        self.graphicsView_Q3 = QGraphicsView(self.tab_7)
        self.graphicsView_Q3.setObjectName(u"graphicsView_Q3")
        self.graphicsView_Q3.setGeometry(QRect(520, 20, 471, 251))
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.textEdit = QTextEdit(self.tab_4)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(80, 50, 871, 291))
        self.tabWidget.addTab(self.tab_4, "")
        MainWindowUi.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindowUi)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowUi.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowUi)

        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindowUi)
    # setupUi

    def retranslateUi(self, MainWindowUi):
        MainWindowUi.setWindowTitle(QCoreApplication.translate("MainWindowUi", u"Detector de Mentiras", None))
        self.labelDetectorMentiras.setText(QCoreApplication.translate("MainWindowUi", u"Detector de Mentiras", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindowUi", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Instru\u00e7\u00f5es para o teste:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1. Coloque os el\u00e9trodos na palma da m\u00e3o</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-botto"
                        "m:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2. Respire normalmente e tente abstrair-se do que lhe rodeia</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3. Ser\u00e3o usados 15seg antes de iniciar o teste, para fazer criar um padr\u00e3o da sua resposta galv\u00e1nica.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0"
                        "px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">4. Depois ser\u00e3o apresentadas 3 perguntas ao qual ter\u00e1 15 segundos para responder a cada uma</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">5. Ap\u00f3s o final das perguntas ser\u00e1 apresentado os resultado do teste</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindowUi", u"Introdu\u00e7\u00e3o", None))
        self.inputPergunta.setText(QCoreApplication.translate("MainWindowUi", u"Perguntas...", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindowUi", u"Come\u00e7ar", None))
        self.btnPergAnterior.setText(QCoreApplication.translate("MainWindowUi", u"Anterior", None))
        self.btnPergSeguinte.setText(QCoreApplication.translate("MainWindowUi", u"Pr\u00f3xima", None))
        self.btnBitalinoConnect.setText(QCoreApplication.translate("MainWindowUi", u"Conectar Bitalino", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindowUi", u"Dados em tempo real", None))
        self.label.setText(QCoreApplication.translate("MainWindowUi", u"M\u00ednimo:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindowUi", u"M\u00e1ximo:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindowUi", u"M\u00e9dia:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindowUi", u"Desvio-Padr\u00e3o:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindowUi", u"Mediana:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindowUi", u"Vari\u00e2ncia:", None))
        self.label_Minimo.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Maximo.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Media.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Mediana.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_desvioPadrao.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Variancia.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindowUi", u"Perguntas", None))
        self.btn_CalcularResultados.setText(QCoreApplication.translate("MainWindowUi", u"Calcular", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindowUi", u"Valores em Respouso", None))
        self.label_Minimo_PR.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Media_PR.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_34.setText(QCoreApplication.translate("MainWindowUi", u"Vari\u00e2ncia:", None))
        self.label_Variancia_PR.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Maximo_PR.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Mediana_PR.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_desvioPadrao_PR.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_33.setText(QCoreApplication.translate("MainWindowUi", u"Desvio-Padr\u00e3o:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindowUi", u"M\u00ednimo:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindowUi", u"Mediana:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindowUi", u"M\u00e9dia:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindowUi", u"M\u00e1ximo:", None))
        self.label_Maximo_RQ1.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_9.setText(QCoreApplication.translate("MainWindowUi", u"M\u00e9dia:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindowUi", u"Vari\u00e2ncia:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindowUi", u"M\u00e1ximo:", None))
        self.label_Minimo_RQ1.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_10.setText(QCoreApplication.translate("MainWindowUi", u"Mediana:", None))
        self.label_Variancia_RQ1.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Resultado_Q1.setText(QCoreApplication.translate("MainWindowUi", u"...", None))
        self.label_Mediana_RQ1.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_desvioPadrao_RQ1.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Media_RQ1.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_11.setText(QCoreApplication.translate("MainWindowUi", u"Desvio-Padr\u00e3o:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindowUi", u"M\u00ednimo:", None))
        self.input_ResultadoFinal_Q1.setText(QCoreApplication.translate("MainWindowUi", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindowUi", u"Resultado:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindowUi", u"Quest\u00e3o 1", None))
        self.label_Variancia_RQ2.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Maximo_RQ2.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_18.setText(QCoreApplication.translate("MainWindowUi", u"M\u00e9dia:", None))
        self.label_desvioPadrao_RQ2.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Media_RQ2.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.input_ResultadoFinal_Q2.setText(QCoreApplication.translate("MainWindowUi", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindowUi", u"Desvio-Padr\u00e3o:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindowUi", u"M\u00e1ximo:", None))
        self.label_Resultado_Q2.setText(QCoreApplication.translate("MainWindowUi", u"...", None))
        self.label_19.setText(QCoreApplication.translate("MainWindowUi", u"Mediana:", None))
        self.label_Mediana_RQ2.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_15.setText(QCoreApplication.translate("MainWindowUi", u"Vari\u00e2ncia:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindowUi", u"Resultado:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindowUi", u"M\u00ednimo:", None))
        self.label_Minimo_RQ2.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindowUi", u"Quest\u00e3o 2", None))
        self.input_ResultadoFinal_Q3.setText(QCoreApplication.translate("MainWindowUi", u"TextLabel", None))
        self.label_23.setText(QCoreApplication.translate("MainWindowUi", u"M\u00ednimo:", None))
        self.label_desvioPadrao_RQ3.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_25.setText(QCoreApplication.translate("MainWindowUi", u"M\u00e9dia:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindowUi", u"Desvio-Padr\u00e3o:", None))
        self.label_Maximo_RQ3.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Variancia_RQ3.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Resultado_Q3.setText(QCoreApplication.translate("MainWindowUi", u"...", None))
        self.label_Media_RQ3.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_26.setText(QCoreApplication.translate("MainWindowUi", u"Mediana:", None))
        self.label_Mediana_RQ3.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_27.setText(QCoreApplication.translate("MainWindowUi", u"Resultado:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindowUi", u"M\u00e1ximo:", None))
        self.label_Minimo_RQ3.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_22.setText(QCoreApplication.translate("MainWindowUi", u"Vari\u00e2ncia:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindowUi", u"Quest\u00e3o 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindowUi", u"Resultados", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindowUi", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Projecto desenvolvido no \u00e2mbito da unidade curricular de </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Bioinstrumenta\u00e7\u00e3o</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align"
                        "=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Realizado por:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Elson Sim\u00f5es - a20845</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u00d3scar Ara\u00fajo - a20844</span></p>\n"
""
                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Rui Lopes - a21674</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindowUi", u"Sobre", None))
    # retranslateUi
