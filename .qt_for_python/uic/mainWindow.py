# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGroupBox, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTextEdit, QWidget)

from q1plotwidget import q1PlotWidget

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
        self.btnBitalinoConnect = QPushButton(self.tab_2)
        self.btnBitalinoConnect.setObjectName(u"btnBitalinoConnect")
        self.btnBitalinoConnect.setGeometry(QRect(10, 20, 161, 31))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.btnBitalinoConnect.setFont(font2)
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 290, 1041, 141))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 55, 16))
        font3 = QFont()
        font3.setBold(True)
        self.label.setFont(font3)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 80, 55, 16))
        self.label_2.setFont(font3)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 30, 71, 16))
        self.label_3.setFont(font3)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(610, 30, 111, 16))
        self.label_4.setFont(font3)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 80, 71, 16))
        self.label_5.setFont(font3)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(640, 80, 71, 16))
        self.label_6.setFont(font3)
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
        self.label_countdown_questions = QLabel(self.tab_2)
        self.label_countdown_questions.setObjectName(u"label_countdown_questions")
        self.label_countdown_questions.setGeometry(QRect(950, 70, 61, 31))
        self.label_countdown_questions.setFont(font2)
        self.btnStart = QPushButton(self.tab_2)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(180, 20, 141, 31))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(True)
        self.btnStart.setFont(font4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.btn_CalcularResultados = QPushButton(self.tab_3)
        self.btn_CalcularResultados.setObjectName(u"btn_CalcularResultados")
        self.btn_CalcularResultados.setGeometry(QRect(60, 30, 111, 41))
        self.btn_CalcularResultados.setFont(font2)
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
        self.label_34.setFont(font3)
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
        self.label_33.setFont(font3)
        self.label_29 = QLabel(self.groupBox_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(160, 20, 55, 16))
        self.label_29.setFont(font3)
        self.label_32 = QLabel(self.groupBox_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(330, 50, 71, 16))
        self.label_32.setFont(font3)
        self.label_31 = QLabel(self.groupBox_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(340, 20, 71, 16))
        self.label_31.setFont(font3)
        self.label_30 = QLabel(self.groupBox_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(160, 50, 55, 16))
        self.label_30.setFont(font3)
        self.tabWidget_2 = QTabWidget(self.tab_3)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 120, 1011, 321))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.label_41 = QLabel(self.tab_5)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(20, 70, 55, 16))
        self.label_41.setFont(font3)
        self.label_42 = QLabel(self.tab_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(320, 40, 111, 16))
        self.label_42.setFont(font3)
        self.label_43 = QLabel(self.tab_5)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(350, 70, 71, 16))
        self.label_43.setFont(font3)
        self.label_Mediana_RQ1 = QLabel(self.tab_5)
        self.label_Mediana_RQ1.setObjectName(u"label_Mediana_RQ1")
        self.label_Mediana_RQ1.setGeometry(QRect(240, 70, 55, 16))
        self.label_Maximo_RQ1 = QLabel(self.tab_5)
        self.label_Maximo_RQ1.setObjectName(u"label_Maximo_RQ1")
        self.label_Maximo_RQ1.setGeometry(QRect(80, 70, 55, 16))
        self.label_Resultado_Q1 = QLabel(self.tab_5)
        self.label_Resultado_Q1.setObjectName(u"label_Resultado_Q1")
        self.label_Resultado_Q1.setGeometry(QRect(20, 150, 471, 51))
        self.input_ResultadoFinal_Q1 = QLabel(self.tab_5)
        self.input_ResultadoFinal_Q1.setObjectName(u"input_ResultadoFinal_Q1")
        self.input_ResultadoFinal_Q1.setGeometry(QRect(10, 10, 981, 21))
        self.input_ResultadoFinal_Q1.setFont(font2)
        self.label_desvioPadrao_RQ1 = QLabel(self.tab_5)
        self.label_desvioPadrao_RQ1.setObjectName(u"label_desvioPadrao_RQ1")
        self.label_desvioPadrao_RQ1.setGeometry(QRect(440, 40, 55, 16))
        self.label_44 = QLabel(self.tab_5)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(170, 40, 71, 16))
        self.label_44.setFont(font3)
        self.label_45 = QLabel(self.tab_5)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(20, 110, 111, 31))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.label_45.setFont(font5)
        self.label_46 = QLabel(self.tab_5)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(20, 40, 55, 16))
        self.label_46.setFont(font3)
        self.label_Minimo_RQ1 = QLabel(self.tab_5)
        self.label_Minimo_RQ1.setObjectName(u"label_Minimo_RQ1")
        self.label_Minimo_RQ1.setGeometry(QRect(80, 40, 55, 16))
        self.label_Media_RQ1 = QLabel(self.tab_5)
        self.label_Media_RQ1.setObjectName(u"label_Media_RQ1")
        self.label_Media_RQ1.setGeometry(QRect(240, 40, 55, 16))
        self.label_Variancia_RQ1 = QLabel(self.tab_5)
        self.label_Variancia_RQ1.setObjectName(u"label_Variancia_RQ1")
        self.label_Variancia_RQ1.setGeometry(QRect(440, 70, 55, 16))
        self.label_47 = QLabel(self.tab_5)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(160, 70, 71, 16))
        self.label_47.setFont(font3)
        self.q1PlotWidget = q1PlotWidget(self.tab_5)
        self.q1PlotWidget.setObjectName(u"q1PlotWidget")
        self.q1PlotWidget.setGeometry(QRect(530, 50, 461, 231))
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.graphicsView_Q2 = QGraphicsView(self.tab_6)
        self.graphicsView_Q2.setObjectName(u"graphicsView_Q2")
        self.graphicsView_Q2.setGeometry(QRect(520, 40, 471, 251))
        self.label_28 = QLabel(self.tab_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(20, 70, 55, 16))
        self.label_28.setFont(font3)
        self.label_35 = QLabel(self.tab_6)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(320, 40, 111, 16))
        self.label_35.setFont(font3)
        self.label_36 = QLabel(self.tab_6)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(350, 70, 71, 16))
        self.label_36.setFont(font3)
        self.label_Mediana_RQ2 = QLabel(self.tab_6)
        self.label_Mediana_RQ2.setObjectName(u"label_Mediana_RQ2")
        self.label_Mediana_RQ2.setGeometry(QRect(240, 70, 55, 16))
        self.label_Maximo_RQ2 = QLabel(self.tab_6)
        self.label_Maximo_RQ2.setObjectName(u"label_Maximo_RQ2")
        self.label_Maximo_RQ2.setGeometry(QRect(80, 70, 55, 16))
        self.label_Resultado_Q2 = QLabel(self.tab_6)
        self.label_Resultado_Q2.setObjectName(u"label_Resultado_Q2")
        self.label_Resultado_Q2.setGeometry(QRect(20, 150, 471, 51))
        self.input_ResultadoFinal_Q2 = QLabel(self.tab_6)
        self.input_ResultadoFinal_Q2.setObjectName(u"input_ResultadoFinal_Q2")
        self.input_ResultadoFinal_Q2.setGeometry(QRect(10, 10, 981, 21))
        self.input_ResultadoFinal_Q2.setFont(font2)
        self.label_desvioPadrao_RQ2 = QLabel(self.tab_6)
        self.label_desvioPadrao_RQ2.setObjectName(u"label_desvioPadrao_RQ2")
        self.label_desvioPadrao_RQ2.setGeometry(QRect(440, 40, 55, 16))
        self.label_37 = QLabel(self.tab_6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(170, 40, 71, 16))
        self.label_37.setFont(font3)
        self.label_38 = QLabel(self.tab_6)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(20, 110, 111, 31))
        self.label_38.setFont(font5)
        self.label_39 = QLabel(self.tab_6)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(20, 40, 55, 16))
        self.label_39.setFont(font3)
        self.label_Minimo_RQ2 = QLabel(self.tab_6)
        self.label_Minimo_RQ2.setObjectName(u"label_Minimo_RQ2")
        self.label_Minimo_RQ2.setGeometry(QRect(80, 40, 55, 16))
        self.label_Media_RQ2 = QLabel(self.tab_6)
        self.label_Media_RQ2.setObjectName(u"label_Media_RQ2")
        self.label_Media_RQ2.setGeometry(QRect(240, 40, 55, 16))
        self.label_Variancia_RQ2 = QLabel(self.tab_6)
        self.label_Variancia_RQ2.setObjectName(u"label_Variancia_RQ2")
        self.label_Variancia_RQ2.setGeometry(QRect(440, 70, 55, 16))
        self.label_40 = QLabel(self.tab_6)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(160, 70, 71, 16))
        self.label_40.setFont(font3)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.input_ResultadoFinal_Q3 = QLabel(self.tab_7)
        self.input_ResultadoFinal_Q3.setObjectName(u"input_ResultadoFinal_Q3")
        self.input_ResultadoFinal_Q3.setGeometry(QRect(10, 10, 981, 21))
        self.input_ResultadoFinal_Q3.setFont(font2)
        self.label_23 = QLabel(self.tab_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 40, 55, 16))
        self.label_23.setFont(font3)
        self.label_desvioPadrao_RQ3 = QLabel(self.tab_7)
        self.label_desvioPadrao_RQ3.setObjectName(u"label_desvioPadrao_RQ3")
        self.label_desvioPadrao_RQ3.setGeometry(QRect(440, 40, 55, 16))
        self.label_25 = QLabel(self.tab_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(170, 40, 71, 16))
        self.label_25.setFont(font3)
        self.label_21 = QLabel(self.tab_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(320, 40, 111, 16))
        self.label_21.setFont(font3)
        self.label_Maximo_RQ3 = QLabel(self.tab_7)
        self.label_Maximo_RQ3.setObjectName(u"label_Maximo_RQ3")
        self.label_Maximo_RQ3.setGeometry(QRect(80, 70, 55, 16))
        self.label_Variancia_RQ3 = QLabel(self.tab_7)
        self.label_Variancia_RQ3.setObjectName(u"label_Variancia_RQ3")
        self.label_Variancia_RQ3.setGeometry(QRect(440, 70, 55, 16))
        self.label_Resultado_Q3 = QLabel(self.tab_7)
        self.label_Resultado_Q3.setObjectName(u"label_Resultado_Q3")
        self.label_Resultado_Q3.setGeometry(QRect(20, 150, 471, 51))
        self.label_Media_RQ3 = QLabel(self.tab_7)
        self.label_Media_RQ3.setObjectName(u"label_Media_RQ3")
        self.label_Media_RQ3.setGeometry(QRect(240, 40, 55, 16))
        self.label_26 = QLabel(self.tab_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(160, 70, 71, 16))
        self.label_26.setFont(font3)
        self.label_Mediana_RQ3 = QLabel(self.tab_7)
        self.label_Mediana_RQ3.setObjectName(u"label_Mediana_RQ3")
        self.label_Mediana_RQ3.setGeometry(QRect(240, 70, 55, 16))
        self.label_27 = QLabel(self.tab_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(20, 110, 111, 31))
        self.label_27.setFont(font5)
        self.label_24 = QLabel(self.tab_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 70, 55, 16))
        self.label_24.setFont(font3)
        self.label_Minimo_RQ3 = QLabel(self.tab_7)
        self.label_Minimo_RQ3.setObjectName(u"label_Minimo_RQ3")
        self.label_Minimo_RQ3.setGeometry(QRect(80, 40, 55, 16))
        self.label_22 = QLabel(self.tab_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(350, 70, 71, 16))
        self.label_22.setFont(font3)
        self.graphicsView_Q3 = QGraphicsView(self.tab_7)
        self.graphicsView_Q3.setObjectName(u"graphicsView_Q3")
        self.graphicsView_Q3.setGeometry(QRect(520, 40, 471, 251))
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

        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)


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
        self.label_countdown_questions.setText("")
        self.btnStart.setText(QCoreApplication.translate("MainWindowUi", u"Come\u00e7ar", None))
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
        self.label_41.setText(QCoreApplication.translate("MainWindowUi", u"M\u00e1ximo:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindowUi", u"Desvio-Padr\u00e3o:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindowUi", u"Vari\u00e2ncia:", None))
        self.label_Mediana_RQ1.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Maximo_RQ1.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Resultado_Q1.setText(QCoreApplication.translate("MainWindowUi", u"...", None))
        self.input_ResultadoFinal_Q1.setText(QCoreApplication.translate("MainWindowUi", u"TextLabel", None))
        self.label_desvioPadrao_RQ1.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_44.setText(QCoreApplication.translate("MainWindowUi", u"M\u00e9dia:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindowUi", u"Resultado:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindowUi", u"M\u00ednimo:", None))
        self.label_Minimo_RQ1.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Media_RQ1.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Variancia_RQ1.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_47.setText(QCoreApplication.translate("MainWindowUi", u"Mediana:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindowUi", u"Quest\u00e3o 1", None))
        self.label_28.setText(QCoreApplication.translate("MainWindowUi", u"M\u00e1ximo:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindowUi", u"Desvio-Padr\u00e3o:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindowUi", u"Vari\u00e2ncia:", None))
        self.label_Mediana_RQ2.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Maximo_RQ2.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Resultado_Q2.setText(QCoreApplication.translate("MainWindowUi", u"...", None))
        self.input_ResultadoFinal_Q2.setText(QCoreApplication.translate("MainWindowUi", u"TextLabel", None))
        self.label_desvioPadrao_RQ2.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_37.setText(QCoreApplication.translate("MainWindowUi", u"M\u00e9dia:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindowUi", u"Resultado:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindowUi", u"M\u00ednimo:", None))
        self.label_Minimo_RQ2.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Media_RQ2.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_Variancia_RQ2.setText(QCoreApplication.translate("MainWindowUi", u"0.00uS", None))
        self.label_40.setText(QCoreApplication.translate("MainWindowUi", u"Mediana:", None))
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

