# Form implementation generated from reading ui file 'c:\IPCA\BioInstr\Bitalino-EDA-Python\ui\uiConverter\mainWindowUi.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindowUi(object):
    def setupUi(self, MainWindowUi):
        MainWindowUi.setObjectName("MainWindowUi")
        MainWindowUi.resize(1094, 537)
        self.centralwidget = QtWidgets.QWidget(MainWindowUi)
        self.centralwidget.setObjectName("centralwidget")
        self.labelDetectorMentiras = QtWidgets.QLabel(self.centralwidget)
        self.labelDetectorMentiras.setGeometry(QtCore.QRect(80, 30, 921, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelDetectorMentiras.setFont(font)
        self.labelDetectorMentiras.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelDetectorMentiras.setObjectName("labelDetectorMentiras")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 90, 1041, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 40, 1011, 221))
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.inputPergunta = QtWidgets.QLabel(self.tab_2)
        self.inputPergunta.setGeometry(QtCore.QRect(10, 110, 1011, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.inputPergunta.setFont(font)
        self.inputPergunta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.inputPergunta.setObjectName("inputPergunta")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 20, 399, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnStart = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btnStart.setFont(font)
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnPergAnterior = QtWidgets.QPushButton(self.layoutWidget)
        self.btnPergAnterior.setObjectName("btnPergAnterior")
        self.horizontalLayout.addWidget(self.btnPergAnterior)
        self.btnPergSeguinte = QtWidgets.QPushButton(self.layoutWidget)
        self.btnPergSeguinte.setObjectName("btnPergSeguinte")
        self.horizontalLayout.addWidget(self.btnPergSeguinte)
        self.btnBitalinoConnect = QtWidgets.QPushButton(self.tab_2)
        self.btnBitalinoConnect.setGeometry(QtCore.QRect(10, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnBitalinoConnect.setFont(font)
        self.btnBitalinoConnect.setObjectName("btnBitalinoConnect")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(0, 240, 1041, 141))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(60, 30, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(330, 30, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(610, 30, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(320, 80, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(640, 80, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_Minimo = QtWidgets.QLabel(self.groupBox)
        self.label_Minimo.setGeometry(QtCore.QRect(130, 30, 55, 16))
        self.label_Minimo.setObjectName("label_Minimo")
        self.label_Maximo = QtWidgets.QLabel(self.groupBox)
        self.label_Maximo.setGeometry(QtCore.QRect(130, 80, 55, 16))
        self.label_Maximo.setObjectName("label_Maximo")
        self.label_Media = QtWidgets.QLabel(self.groupBox)
        self.label_Media.setGeometry(QtCore.QRect(410, 30, 55, 16))
        self.label_Media.setObjectName("label_Media")
        self.label_Mediana = QtWidgets.QLabel(self.groupBox)
        self.label_Mediana.setGeometry(QtCore.QRect(410, 80, 55, 16))
        self.label_Mediana.setObjectName("label_Mediana")
        self.label_desvioPadrao = QtWidgets.QLabel(self.groupBox)
        self.label_desvioPadrao.setGeometry(QtCore.QRect(740, 30, 55, 16))
        self.label_desvioPadrao.setObjectName("label_desvioPadrao")
        self.label_Variancia = QtWidgets.QLabel(self.groupBox)
        self.label_Variancia.setGeometry(QtCore.QRect(740, 80, 55, 16))
        self.label_Variancia.setObjectName("label_Variancia")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.input_ResultadoFinal_Q1 = QtWidgets.QLabel(self.tab_3)
        self.input_ResultadoFinal_Q1.setGeometry(QtCore.QRect(30, 30, 951, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.input_ResultadoFinal_Q1.setFont(font)
        self.input_ResultadoFinal_Q1.setObjectName("input_ResultadoFinal_Q1")
        self.input_ResultadoFinal_Q2 = QtWidgets.QLabel(self.tab_3)
        self.input_ResultadoFinal_Q2.setGeometry(QtCore.QRect(30, 150, 961, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.input_ResultadoFinal_Q2.setFont(font)
        self.input_ResultadoFinal_Q2.setObjectName("input_ResultadoFinal_Q2")
        self.input_ResultadoFinal_Q3 = QtWidgets.QLabel(self.tab_3)
        self.input_ResultadoFinal_Q3.setGeometry(QtCore.QRect(30, 270, 961, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.input_ResultadoFinal_Q3.setFont(font)
        self.input_ResultadoFinal_Q3.setObjectName("input_ResultadoFinal_Q3")
        self.label_Minimo_RQ1 = QtWidgets.QLabel(self.tab_3)
        self.label_Minimo_RQ1.setGeometry(QtCore.QRect(90, 60, 55, 16))
        self.label_Minimo_RQ1.setObjectName("label_Minimo_RQ1")
        self.label_Maximo_RQ1 = QtWidgets.QLabel(self.tab_3)
        self.label_Maximo_RQ1.setGeometry(QtCore.QRect(90, 90, 55, 16))
        self.label_Maximo_RQ1.setObjectName("label_Maximo_RQ1")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(30, 90, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(30, 60, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_Mediana_RQ1 = QtWidgets.QLabel(self.tab_3)
        self.label_Mediana_RQ1.setGeometry(QtCore.QRect(290, 90, 55, 16))
        self.label_Mediana_RQ1.setObjectName("label_Mediana_RQ1")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(220, 60, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_Media_RQ1 = QtWidgets.QLabel(self.tab_3)
        self.label_Media_RQ1.setGeometry(QtCore.QRect(290, 60, 55, 16))
        self.label_Media_RQ1.setObjectName("label_Media_RQ1")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(200, 90, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_desvioPadrao_RQ1 = QtWidgets.QLabel(self.tab_3)
        self.label_desvioPadrao_RQ1.setGeometry(QtCore.QRect(540, 60, 55, 16))
        self.label_desvioPadrao_RQ1.setObjectName("label_desvioPadrao_RQ1")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(410, 60, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(450, 90, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_Variancia_RQ1 = QtWidgets.QLabel(self.tab_3)
        self.label_Variancia_RQ1.setGeometry(QtCore.QRect(540, 90, 55, 16))
        self.label_Variancia_RQ1.setObjectName("label_Variancia_RQ1")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(750, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_Resultado_Q1 = QtWidgets.QLabel(self.tab_3)
        self.label_Resultado_Q1.setGeometry(QtCore.QRect(750, 80, 111, 21))
        self.label_Resultado_Q1.setObjectName("label_Resultado_Q1")
        self.label_Maximo_RQ2 = QtWidgets.QLabel(self.tab_3)
        self.label_Maximo_RQ2.setGeometry(QtCore.QRect(90, 210, 55, 16))
        self.label_Maximo_RQ2.setObjectName("label_Maximo_RQ2")
        self.label_Mediana_RQ2 = QtWidgets.QLabel(self.tab_3)
        self.label_Mediana_RQ2.setGeometry(QtCore.QRect(290, 210, 55, 16))
        self.label_Mediana_RQ2.setObjectName("label_Mediana_RQ2")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(410, 180, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(450, 210, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(30, 180, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_Resultado_Q2 = QtWidgets.QLabel(self.tab_3)
        self.label_Resultado_Q2.setGeometry(QtCore.QRect(750, 200, 111, 21))
        self.label_Resultado_Q2.setObjectName("label_Resultado_Q2")
        self.label_Minimo_RQ2 = QtWidgets.QLabel(self.tab_3)
        self.label_Minimo_RQ2.setGeometry(QtCore.QRect(90, 180, 55, 16))
        self.label_Minimo_RQ2.setObjectName("label_Minimo_RQ2")
        self.label_Variancia_RQ2 = QtWidgets.QLabel(self.tab_3)
        self.label_Variancia_RQ2.setGeometry(QtCore.QRect(540, 210, 55, 16))
        self.label_Variancia_RQ2.setObjectName("label_Variancia_RQ2")
        self.label_desvioPadrao_RQ2 = QtWidgets.QLabel(self.tab_3)
        self.label_desvioPadrao_RQ2.setGeometry(QtCore.QRect(540, 180, 55, 16))
        self.label_desvioPadrao_RQ2.setObjectName("label_desvioPadrao_RQ2")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(30, 210, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(220, 180, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(200, 210, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_Media_RQ2 = QtWidgets.QLabel(self.tab_3)
        self.label_Media_RQ2.setGeometry(QtCore.QRect(290, 180, 55, 16))
        self.label_Media_RQ2.setObjectName("label_Media_RQ2")
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(750, 170, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_Maximo_RQ3 = QtWidgets.QLabel(self.tab_3)
        self.label_Maximo_RQ3.setGeometry(QtCore.QRect(90, 330, 55, 16))
        self.label_Maximo_RQ3.setObjectName("label_Maximo_RQ3")
        self.label_Mediana_RQ3 = QtWidgets.QLabel(self.tab_3)
        self.label_Mediana_RQ3.setGeometry(QtCore.QRect(290, 330, 55, 16))
        self.label_Mediana_RQ3.setObjectName("label_Mediana_RQ3")
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(410, 300, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(450, 330, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(30, 300, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_Resultado_Q3 = QtWidgets.QLabel(self.tab_3)
        self.label_Resultado_Q3.setGeometry(QtCore.QRect(750, 320, 111, 21))
        self.label_Resultado_Q3.setObjectName("label_Resultado_Q3")
        self.label_Minimo_RQ3 = QtWidgets.QLabel(self.tab_3)
        self.label_Minimo_RQ3.setGeometry(QtCore.QRect(90, 300, 55, 16))
        self.label_Minimo_RQ3.setObjectName("label_Minimo_RQ3")
        self.label_Variancia_RQ3 = QtWidgets.QLabel(self.tab_3)
        self.label_Variancia_RQ3.setGeometry(QtCore.QRect(540, 330, 55, 16))
        self.label_Variancia_RQ3.setObjectName("label_Variancia_RQ3")
        self.label_desvioPadrao_RQ3 = QtWidgets.QLabel(self.tab_3)
        self.label_desvioPadrao_RQ3.setGeometry(QtCore.QRect(540, 300, 55, 16))
        self.label_desvioPadrao_RQ3.setObjectName("label_desvioPadrao_RQ3")
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setGeometry(QtCore.QRect(30, 330, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        self.label_25.setGeometry(QtCore.QRect(220, 300, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setGeometry(QtCore.QRect(200, 330, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_Media_RQ3 = QtWidgets.QLabel(self.tab_3)
        self.label_Media_RQ3.setGeometry(QtCore.QRect(290, 300, 55, 16))
        self.label_Media_RQ3.setObjectName("label_Media_RQ3")
        self.label_27 = QtWidgets.QLabel(self.tab_3)
        self.label_27.setGeometry(QtCore.QRect(750, 290, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textEdit = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit.setGeometry(QtCore.QRect(80, 50, 871, 291))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindowUi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindowUi)
        self.statusbar.setObjectName("statusbar")
        MainWindowUi.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowUi)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindowUi)

    def retranslateUi(self, MainWindowUi):
        _translate = QtCore.QCoreApplication.translate
        MainWindowUi.setWindowTitle(_translate("MainWindowUi", "Detector de Mentiras"))
        self.labelDetectorMentiras.setText(_translate("MainWindowUi", "Detector de Mentiras"))
        self.textEdit_2.setHtml(_translate("MainWindowUi", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Instruções para o teste:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1. Coloque os elétrodos na palma da mão</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2. Respire normalmente e tente abstrair-se do que lhe rodeia</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3. Serão usados 15seg antes de iniciar o teste, para fazer criar um padrão da sua resposta galvánica.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">4. Depois serão apresentadas 3 perguntas ao qual terá 15 segundos para responder a cada uma</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">5. Após o final das perguntas será apresentado os resultado do teste</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindowUi", "Introdução"))
        self.inputPergunta.setText(_translate("MainWindowUi", "Perguntas..."))
        self.btnStart.setText(_translate("MainWindowUi", "Começar"))
        self.btnPergAnterior.setText(_translate("MainWindowUi", "Anterior"))
        self.btnPergSeguinte.setText(_translate("MainWindowUi", "Próxima"))
        self.btnBitalinoConnect.setText(_translate("MainWindowUi", "Conectar Bitalino"))
        self.groupBox.setTitle(_translate("MainWindowUi", "Dados em tempo real"))
        self.label.setText(_translate("MainWindowUi", "Mínimo:"))
        self.label_2.setText(_translate("MainWindowUi", "Máximo:"))
        self.label_3.setText(_translate("MainWindowUi", "Média:"))
        self.label_4.setText(_translate("MainWindowUi", "Desvio-Padrão:"))
        self.label_5.setText(_translate("MainWindowUi", "Mediana:"))
        self.label_6.setText(_translate("MainWindowUi", "Variância:"))
        self.label_Minimo.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_Maximo.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_Media.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_Mediana.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_desvioPadrao.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_Variancia.setText(_translate("MainWindowUi", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindowUi", "Perguntas"))
        self.input_ResultadoFinal_Q1.setText(_translate("MainWindowUi", "TextLabel"))
        self.input_ResultadoFinal_Q2.setText(_translate("MainWindowUi", "TextLabel"))
        self.input_ResultadoFinal_Q3.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_Minimo_RQ1.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_Maximo_RQ1.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_7.setText(_translate("MainWindowUi", "Máximo:"))
        self.label_8.setText(_translate("MainWindowUi", "Mínimo:"))
        self.label_Mediana_RQ1.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_9.setText(_translate("MainWindowUi", "Média:"))
        self.label_Media_RQ1.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_10.setText(_translate("MainWindowUi", "Mediana:"))
        self.label_desvioPadrao_RQ1.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_11.setText(_translate("MainWindowUi", "Desvio-Padrão:"))
        self.label_12.setText(_translate("MainWindowUi", "Variância:"))
        self.label_Variancia_RQ1.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_13.setText(_translate("MainWindowUi", "Resultado:"))
        self.label_Resultado_Q1.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_Maximo_RQ2.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_Mediana_RQ2.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_14.setText(_translate("MainWindowUi", "Desvio-Padrão:"))
        self.label_15.setText(_translate("MainWindowUi", "Variância:"))
        self.label_16.setText(_translate("MainWindowUi", "Mínimo:"))
        self.label_Resultado_Q2.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_Minimo_RQ2.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_Variancia_RQ2.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_desvioPadrao_RQ2.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_17.setText(_translate("MainWindowUi", "Máximo:"))
        self.label_18.setText(_translate("MainWindowUi", "Média:"))
        self.label_19.setText(_translate("MainWindowUi", "Mediana:"))
        self.label_Media_RQ2.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_20.setText(_translate("MainWindowUi", "Resultado:"))
        self.label_Maximo_RQ3.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_Mediana_RQ3.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_21.setText(_translate("MainWindowUi", "Desvio-Padrão:"))
        self.label_22.setText(_translate("MainWindowUi", "Variância:"))
        self.label_23.setText(_translate("MainWindowUi", "Mínimo:"))
        self.label_Resultado_Q3.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_Minimo_RQ3.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_Variancia_RQ3.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_desvioPadrao_RQ3.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_24.setText(_translate("MainWindowUi", "Máximo:"))
        self.label_25.setText(_translate("MainWindowUi", "Média:"))
        self.label_26.setText(_translate("MainWindowUi", "Mediana:"))
        self.label_Media_RQ3.setText(_translate("MainWindowUi", "TextLabel"))
        self.label_27.setText(_translate("MainWindowUi", "Resultado:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindowUi", "Resultados"))
        self.textEdit.setHtml(_translate("MainWindowUi", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Projecto desenvolvido no âmbito da unidade curricular de </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Bioinstrumentação</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Realizado por:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Elson Simões - a20845</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Óscar Araújo - a20844</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Rui Lopes - a21674</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindowUi", "Sobre"))
