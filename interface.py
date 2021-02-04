# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QTableWidgetItem, QWidget, QImage, QApplication, QPainter,QFileDialog, QDialog
from naoqi import ALProxy, ALBroker, ALModule
from avRecording import VideoRecorder,AudioRecorder,start_audio_recording,start_AVrecording,start_video_recording,file_manager,stop_AVrecording
from movimentos import beijos,comemorar,concordar,conversar,duvida,discordar,empatia,palmas,tchau,toca_aqui
import vision_definitions
import sys
import sqlite3
import time
import pyautogui
import threading
import pysftp
import subprocess

width , height = pyautogui.size()

if height < 1080:
    height = 800
    hMovimentos = 221
    posYEMG = 430
    posYAVISOS = 490
    
else:
    height = 900
    hMovimentos = 280
    posYEMG = 500
    posYAVISOS = 580 


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

#Abre Banco de dados e adiciona os valores no completer, e pega o ultimo valor de IP inserido.
conn = sqlite3.connect('BdProteger.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM IdKids")
listaId = cursor.fetchall()
lista_id = []
for i,j in listaId:
    lista_id.append(j)
cursor.execute("SELECT * FROM IpRobot ORDER BY id DESC;")
listaIp = cursor.fetchall()
lista_ip = []
for i,j in listaIp:
    lista_ip.append(j)
cursor.execute("SELECT * FROM IpRobot ORDER BY id DESC LIMIT 1")
lastIp = cursor.fetchall()
for i,j in lastIp:
    last_ip = str(j)      
conn.close()
PORT = 9559
class Ui_MainWindow(object):
    def __init__(self):
        self.val_ip = ""
        self.aux = False
        self.jan = None
        self.pasta = ""
        self.robotIP = "" 

    def setupUi(self, MainWindow,height=height):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        
        MainWindow.resize(400, height)
        MainWindow.setMinimumSize(QtCore.QSize(400, height))
        MainWindow.setMaximumSize(QtCore.QSize(400, height))
        self.centralwidget = QtGui.QWidget(MainWindow)
        
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Menu = QtGui.QGroupBox(self.centralwidget)
        self.Menu.setGeometry(QtCore.QRect(10, 10, 381, 181))
        self.Menu.setMinimumSize(QtCore.QSize(0, 0))
        self.Menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Menu.setObjectName(_fromUtf8("Menu"))
    
        
        self.label_id = QtGui.QLabel(self.Menu)
        self.label_id.setGeometry(QtCore.QRect(10, 27, 50, 23))
        self.label_id.setMinimumSize(QtCore.QSize(50, 23))
        self.label_id.setMaximumSize(QtCore.QSize(80, 23))
        self.label_id.setObjectName(_fromUtf8("label_id"))
        self.inputIDC = QtGui.QLineEdit(self.Menu)
        self.inputIDC.setGeometry(QtCore.QRect(70, 27, 250, 20))
        self.inputIDC.setMinimumSize(QtCore.QSize(200, 0))
        self.inputIDC.setMaximumSize(QtCore.QSize(250, 25))
        self.inputIDC.setObjectName(_fromUtf8("inputIDC"))
        self.inputIP = QtGui.QLineEdit(self.Menu)
        self.inputIP.setGeometry(QtCore.QRect(70, 60, 250, 20))
        self.inputIP.setMinimumSize(QtCore.QSize(0, 0))
        self.inputIP.setMaximumSize(QtCore.QSize(300, 25))
        self.inputIP.setObjectName(_fromUtf8("inputIP"))
        self.inputSessao = QtGui.QLineEdit(self.Menu)
        self.inputSessao.setEnabled(True)
        self.inputSessao.setGeometry(QtCore.QRect(70, 93, 250, 20))
        self.inputSessao.setMinimumSize(QtCore.QSize(0, 0))
        self.inputSessao.setMaximumSize(QtCore.QSize(250, 25))
        self.inputSessao.setStyleSheet(_fromUtf8("background:#A4A4A4;\n" "\n" ""))
        self.inputSessao.setText(_fromUtf8(""))
        self.inputSessao.setReadOnly(True)
        self.inputSessao.setObjectName(_fromUtf8("inputSessao"))
        self.label_Ip = QtGui.QLabel(self.Menu)
        self.label_Ip.setGeometry(QtCore.QRect(10, 60, 50, 23))
        self.label_Ip.setMinimumSize(QtCore.QSize(50, 23))
        self.label_Ip.setMaximumSize(QtCore.QSize(80, 23))
        self.label_Ip.setObjectName(_fromUtf8("label_Ip"))
        self.label_sessao = QtGui.QLabel(self.Menu)
        self.label_sessao.setGeometry(QtCore.QRect(10, 93, 50, 23))
        self.label_sessao.setMinimumSize(QtCore.QSize(50, 23))
        self.label_sessao.setMaximumSize(QtCore.QSize(80, 23))
        self.label_sessao.setObjectName(_fromUtf8("label_sessao"))
        self.BtnConn = QtGui.QPushButton(self.Menu)
        self.BtnConn.setGeometry(QtCore.QRect(70, 120, 265, 23))
        self.BtnConn.setMinimumSize(QtCore.QSize(265, 0))
        self.BtnConn.setMaximumSize(QtCore.QSize(350, 25))
        self.BtnConn.setObjectName(_fromUtf8("BtnConn"))
        self.BtnEnc = QtGui.QPushButton(self.Menu)
        self.BtnEnc.setGeometry(QtCore.QRect(70, 150, 265, 23))
        self.BtnEnc.setMinimumSize(QtCore.QSize(265, 0))
        self.BtnEnc.setMaximumSize(QtCore.QSize(350, 25))
        self.BtnEnc.setObjectName(_fromUtf8("BtnEnc"))
        self.Status = QtGui.QLabel(self.Menu)
        self.Status.setEnabled(False)
        self.Status.setGeometry(QtCore.QRect(340, 120, 25, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Status.sizePolicy().hasHeightForWidth())
        self.Status.setSizePolicy(sizePolicy)
        self.Status.setMaximumSize(QtCore.QSize(30, 30))
        self.Status.setMouseTracking(True)
        self.Status.setStyleSheet(_fromUtf8("background: #fff"))
        self.Status.setText(_fromUtf8(""))
        self.Status.setObjectName(_fromUtf8("Status"))
        #### BOX MOVIMENTOS
        self.Movimentos = QtGui.QGroupBox(self.centralwidget)
        self.Movimentos.setGeometry(QtCore.QRect(10, 190, 381, hMovimentos))
        self.Movimentos.setObjectName(_fromUtf8("Movimentos"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Movimentos)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btn1x1 = QtGui.QPushButton(self.Movimentos)
        self.btn1x1.setObjectName(_fromUtf8("btn1x1"))
        self.gridLayout_2.addWidget(self.btn1x1, 0, 3, 1, 1)
        self.btn1x2 = QtGui.QPushButton(self.Movimentos)
        self.btn1x2.setObjectName(_fromUtf8("btn1x2"))
        self.gridLayout_2.addWidget(self.btn1x2, 0, 6, 1, 1)
        self.btn2x2 = QtGui.QPushButton(self.Movimentos)
        self.btn2x2.setObjectName(_fromUtf8("btn2x2"))
        self.gridLayout_2.addWidget(self.btn2x2, 1, 6, 1, 1)
        self.btn2x1 = QtGui.QPushButton(self.Movimentos)
        self.btn2x1.setObjectName(_fromUtf8("btn2x1"))
        self.gridLayout_2.addWidget(self.btn2x1, 1, 3, 1, 1)
        self.btn1x3 = QtGui.QPushButton(self.Movimentos)
        self.btn1x3.setObjectName(_fromUtf8("btn1x3"))
        self.gridLayout_2.addWidget(self.btn1x3, 0, 8, 1, 1)
        self.btn3x3 = QtGui.QPushButton(self.Movimentos)
        self.btn3x3.setObjectName(_fromUtf8("btn3x3"))
        self.gridLayout_2.addWidget(self.btn3x3, 2, 8, 1, 1)
        self.btn2x3 = QtGui.QPushButton(self.Movimentos)
        self.btn2x3.setObjectName(_fromUtf8("btn2x3"))
        self.gridLayout_2.addWidget(self.btn2x3, 1, 8, 1, 1)
        self.btn3x2 = QtGui.QPushButton(self.Movimentos)
        self.btn3x2.setObjectName(_fromUtf8("btn3x2"))
        self.gridLayout_2.addWidget(self.btn3x2, 2, 6, 1, 1)
        self.btn3x1 = QtGui.QPushButton(self.Movimentos)
        self.btn3x1.setObjectName(_fromUtf8("btn3x1"))
        self.gridLayout_2.addWidget(self.btn3x1, 2, 3, 1, 1)
        self.btn4x1 = QtGui.QPushButton(self.Movimentos)
        self.btn4x1.setObjectName(_fromUtf8("btn4x1"))
        self.gridLayout_2.addWidget(self.btn4x1, 3, 3, 1, 1)
        self.btn4x2 = QtGui.QPushButton(self.Movimentos)
        self.btn4x2.setObjectName(_fromUtf8("btn4x2"))
        self.gridLayout_2.addWidget(self.btn4x2, 3, 6, 1, 1)
        ##AREA DE AVISOS
        self.Avisos = QtGui.QGroupBox(self.centralwidget)
        self.Avisos.setGeometry(QtCore.QRect(9, posYAVISOS, 380, 300))
        self.Avisos.setMinimumSize(QtCore.QSize(0, 0))
        self.Avisos.setMaximumSize(QtCore.QSize(16777215, 300))
        self.Avisos.setAlignment(QtCore.Qt.AlignCenter)
        self.Avisos.setObjectName(_fromUtf8("Avisos"))
        self.logo_cti = QtGui.QLabel(self.Avisos)
        self.logo_cti.setGeometry(QtCore.QRect(10, 250, 85, 50))
        self.logo_cti.setMinimumSize(QtCore.QSize(85, 50))
        self.logo_cti.setMaximumSize(QtCore.QSize(0, 0))
        self.logo_cti.setText(_fromUtf8(""))
        self.logo_cti.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/LogoCTIcampinas.jpeg")))
        self.logo_cti.setScaledContents(True)
        self.logo_cti.setObjectName(_fromUtf8("logo_cti"))
        self.tableWidget = QtGui.QTableWidget(self.Avisos)
        self.tableWidget.setGeometry(QtCore.QRect(10, 23, 361, 211))
        self.tableWidget.setMinimumSize(QtCore.QSize(361, 211))
        self.tableWidget.setMaximumSize(QtCore.QSize(361, 211))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(70)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.logo_icmc = QtGui.QLabel(self.Avisos)
        self.logo_icmc.setGeometry(QtCore.QRect(290, 250, 85, 50))
        self.logo_icmc.setMinimumSize(QtCore.QSize(85, 50))
        self.logo_icmc.setMaximumSize(QtCore.QSize(0, 0))
        self.logo_icmc.setText(_fromUtf8(""))
        self.logo_icmc.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/LogoICMC.png")))
        self.logo_icmc.setScaledContents(True)
        self.logo_icmc.setObjectName(_fromUtf8("logo_icmc"))
        self.logo_lar = QtGui.QLabel(self.Avisos)
        self.logo_lar.setGeometry(QtCore.QRect(200, 250, 85, 50))
        self.logo_lar.setMinimumSize(QtCore.QSize(85, 50))
        self.logo_lar.setMaximumSize(QtCore.QSize(0, 0))
        self.logo_lar.setText(_fromUtf8(""))
        self.logo_lar.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/LogoLars.png")))
        self.logo_lar.setScaledContents(True)
        self.logo_lar.setObjectName(_fromUtf8("logo_lar"))
        self.logo_Unesp = QtGui.QLabel(self.Avisos)
        self.logo_Unesp.setGeometry(QtCore.QRect(110, 250, 85, 50))
        self.logo_Unesp.setMinimumSize(QtCore.QSize(85, 50))
        self.logo_Unesp.setMaximumSize(QtCore.QSize(0, 0))
        self.logo_Unesp.setText(_fromUtf8(""))
        self.logo_Unesp.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/unesp-full-center.png")))
        self.logo_Unesp.setScaledContents(True)
        self.logo_Unesp.setObjectName(_fromUtf8("logo_Unesp"))
        self.logo_cti.raise_()
        self.logo_icmc.raise_()
        self.logo_lar.raise_()
        self.logo_Unesp.raise_()
        self.tableWidget.raise_()
        ### BOTAO EMERGENCIA
        self.EMG = QtGui.QPushButton(self.centralwidget)
        self.EMG.setGeometry(QtCore.QRect(10, posYEMG, 380, 40))
        self.EMG.setMinimumSize(QtCore.QSize(0, 0))
        self.EMG.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.EMG.setStyleSheet(_fromUtf8("color: rgb(255, 255, 0);\n""background-color: rgb(255, 0, 0)"))
        self.EMG.setObjectName(_fromUtf8("EMG"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.BtnEnc.setEnabled(False)
        
        #Botões
        self.BtnConn.clicked.connect(self.conexao)
        self.BtnEnc.clicked.connect(self.desconectar)
        self.btn1x1.clicked.connect(self.concordar)
        self.btn1x2.clicked.connect(self.discordar)
        self.btn1x3.clicked.connect(self.conversar)
        self.btn2x1.clicked.connect(self.comemorar)
        self.btn2x2.clicked.connect(self.empatia)
        self.btn2x3.clicked.connect(self.duvida)
        self.btn3x1.clicked.connect(self.funcSentarLevantar)
        self.btn3x2.clicked.connect(self.palmas)
        self.btn3x3.clicked.connect(self.tocaqui)
        self.btn4x1.clicked.connect(self.tchau)
        self.btn4x2.clicked.connect(self.beijos)
        self.EMG.clicked.connect(self.desligar)
        
        
        #Recupera o ultimo ip adicionado na lista.
        self.inputIP.setText(last_ip)
        #Cria uma lista para completar o id ou o ip
        completerid = QtGui.QCompleter(lista_id)
        self.inputIDC.setCompleter(completerid)
        completerip = QtGui.QCompleter(lista_ip)
        self.inputIP.setCompleter(completerip)        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)    
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Menu.setTitle(_translate("MainWindow", "Menu", None))
        self.label_id.setText(_translate("MainWindow", "ID Criança", None))
        self.label_Ip.setText(_translate("MainWindow", "IP Robô", None))
        self.label_sessao.setText(_translate("MainWindow", "ID Sessão", None))
        self.BtnConn.setText(_translate("MainWindow", "Conectar", None))
        self.BtnEnc.setText(_translate("MainWindow", "Encerrar Sessão", None))
        self.Movimentos.setTitle(_translate("MainWindow", "Movimentos", None))
        self.btn1x1.setText(_translate("MainWindow", "Concordar", None))
        self.btn1x2.setText(_translate("MainWindow", "Discordar", None))
        self.btn2x2.setText(_translate("MainWindow", "Empatia", None))
        self.btn2x1.setText(_translate("MainWindow", "Comemorar", None))
        self.btn1x3.setText(_translate("MainWindow", "Conversar", None))
        self.btn3x3.setText(_translate("MainWindow", "Toca aqui", None))
        self.btn2x3.setText(_translate("MainWindow", "Duvida", None))
        self.btn3x2.setText(_translate("MainWindow", "Palmas", None))
        self.btn3x1.setText(_translate("MainWindow", "Sentar", None))
        self.btn4x1.setText(_translate("MainWindow", "Oi/Tchau", None))
        self.btn4x2.setText(_translate("MainWindow", "Beijos", None))
        self.Avisos.setTitle(_translate("MainWindow", "Avisos", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hora", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mensagens", None))
        self.EMG.setText(_translate("MainWindow", "EMERGÊNCIA", None))
    
    #Funções complementares
    def gera_id_sessao(self):
        val = str(_fromUtf8(self.inputIDC.text()))
        t = time.localtime()
        id_da_sessao = time.strftime("%Y%m%d"+ "_" + val , t)        
        self.inputSessao.setText(str(id_da_sessao))
        self.inputSessao.setEnabled(False)
        return id_da_sessao
    def salva_ip(self):
        conn = sqlite3.connect('BdProteger.db')
        cursor = conn.cursor()
        NEWIP = str(self.inputIP.text())
        cursor.execute("""INSERT OR IGNORE INTO IpRobot (IpRobot) VALUES(?);""",[NEWIP])
        conn.commit()
        conn.close()
    def conexao(self):
        try:
            self.robotIP = self.setIP()
            self.naoVision()
            aviso = "Aviso: Conexão estabelecida com robô."
            self.enviarAviso(aviso)
            # nivelBateria = threading.Thread(target=self.nivelBateria)
            # nivelBateria.start()
        except BaseException:
            aviso = "ERROR: Falha na conexão com robô."
            self.enviarAviso(aviso)
            self.Status.setStyleSheet(_fromUtf8("background:#FF0000"))
        try:
            folder = QFileDialog.getExistingDirectory(self,"Selecione um pasta para salvar o video.")            
            if folder != None:
                self.pasta = str(folder)
                session_ID = self.gera_id_sessao()
                file_manager(session_ID,self.pasta)
            session_ID = self.gera_id_sessao()         
            start_AVrecording(session_ID)
            aviso = "AVISO: Conexão feita com webcam."
            self.enviarAviso(aviso)
        except BaseException:
            aviso = "ERROR: Falha na conexão com Webcam."
            self.enviarAviso(aviso)
            self.Status.setStyleSheet(_fromUtf8("background:#FF0000"))
        try:
            self.naoVideoRecording()
            self.naoAudioRecording ()        
            aviso = "AVISO: Inicio da gravação do NAO."
            self.enviarAviso(aviso)           
        except BaseException:
            aviso = "ERROR: Falha na gravação do NAO."
            self.enviarAviso(aviso)
            self.Status.setStyleSheet(_fromUtf8("background:#FF0000"))            
        try:    
            self.salva_ip()                        
            aviso = "AVISO: Sessão iniciada com sucesso."
            self.enviarAviso(aviso)        
            self.BtnConn.setText("Conectado")
            self.Status.setStyleSheet(_fromUtf8("background:#40FF00"))
            self.BtnConn.setEnabled(False)
            self.BtnEnc.setEnabled(True) 
        except BaseException:
            aviso = "ERROR: Falha na configuração."
            self.enviarAviso(aviso)
            self.Status.setStyleSheet(_fromUtf8("background:#FF0000"))
    def desconectar(self):
        try:
            self.salva_log()
            self.jan.destroy()
            self.jan = None
            self.stopVideoRecording()
            self.stopAudioRecording()
        except BaseException:
            aviso = "ERROR:Falha ao fechar janelas."
            self.enviarAviso(aviso)
        try:
            self.getNAOfiles()
            aviso = "AVISO:Video NAO salvo com sucesso."
            self.enviarAviso(aviso)
        except BaseException:
            aviso = "ERROR:Não foi possível salvar o video do NAO."
            self.enviarAviso(aviso)
        try:
            nomeSessao = self.gera_id_sessao()
            stop_AVrecording(nomeSessao,self.pasta)
            file_manager(nomeSessao,self.pasta)
            aviso = "AVISO: Video Webcam salva com sucesso."
            self.enviarAviso(aviso)
        except BaseException:
            aviso = "ERROR: Não foi possível salvar o video da WebCam."
            self.enviarAviso(aviso) 
        try:           
            #self.desligar()
            self.robotIP = ""
            self.BtnConn.setText("Conectar")
            self.BtnConn.setEnabled(True)
            self.BtnEnc.setEnabled(False)
            self.inputSessao.setEnabled(True)
            aviso = "AVISO: Sessão encerrada com sucesso."
            self.enviarAviso(aviso)
            self.Status.setStyleSheet(_fromUtf8("background:#fff"))        
        except BaseException:
            aviso = "ERROR: Falha na conexão com o robô."
            self.enviarAviso(aviso)
            self.Status.setStyleSheet(_fromUtf8("background:#FF0000"))
    def enviarAviso(self,aviso):
        conn = sqlite3.connect('BdProteger.db')
        conn.text_factory = str
        self.aviso = aviso
        t = time.localtime()
        Data = str(t.tm_mday) + "/" + str(t.tm_mon) + "/" + str(t.tm_year) 
        hora = str(t.tm_hour) + ":" + str(t.tm_min) + ":" + str(t.tm_sec) 
        conn.execute("INSERT INTO Sessao (Data,Hora,Aviso) VALUES(?,?,?);",(Data,hora,self.aviso))
        conn.commit()
        query ="SELECT Hora, Aviso FROM Sessao ORDER BY ip DESC LIMIT 1"                
        result = conn.execute(query)
        for row, row_data in enumerate(result):
            self.tableWidget.insertRow(row)
            for col, data in enumerate(row_data):
                self.tableWidget.setItem(row,col, QTableWidgetItem(_fromUtf8(data) ))
        self.tableWidget.show()
        conn.close()
    def setIP(self):
            self.val_ip = str(self.inputIP.text())
            return self.val_ip
    def naoVision(self):
        if self.jan is None:
            IP = self.robotIP  # Replace here with your NaoQi's IP address.
            PORT = 9559
            CameraID = 0           
            self.jan = ImageWidget(IP, PORT, CameraID)
        self.jan.show()
    def piscar(self):
        pass
    def salva_log(self):
        conn = sqlite3.connect('BdProteger.db')
        cursor = conn.cursor()
        query= "SELECT * FROM Sessao;"
        cursor.execute(query)
        #Gera arquivo com o log dos arquivos
        listaLog = []
        t = time.localtime()
        val = str(_fromUtf8(self.inputIDC.text()))
        nome = "Log"+ str(time.strftime("%Y%m%d"+ "_" + val , t)) 
        arq = open("Logs/"+ nome +".txt",'w')
        for row, data in enumerate(cursor.fetchall()):              
            listaLog.append(data)
            arq.write(str(data) + "\n")
        arq.close()
        #Apaga os logs do banco de dados
        delete = "DELETE FROM Sessao;"
        cursor.execute(delete)
        conn.commit()
        conn.close()         
    def naoVideoRecording(self):        
        filename = self.gera_id_sessao()
        videoRecorderProxy = ALProxy("ALVideoRecorder", self.robotIP, PORT)
        
        # This records a 320*240 MJPG video at 10 fps.
        # Note MJPG can't be recorded with a framerate lower than 3 fps.
        videoRecorderProxy.setResolution(1)
        videoRecorderProxy.setFrameRate(10)
        videoRecorderProxy.setVideoFormat("MJPG")
        videoRecorderProxy.startRecording("/home/nao/recordings/cameras", str(filename)+"_NAO")
    def stopVideoRecording(self):               
        videoRecorderProxy = ALProxy("ALVideoRecorder", self.robotIP, PORT)        
        # Video file is saved on the robot in the
        # /home/nao/recordings/cameras/ folder.
        videoRecorderProxy.stopRecording()        
    def naoAudioRecording(self):        
        filename = self.gera_id_sessao()
        voiceProxy = ALProxy("ALAudioRecorder",self.robotIP,PORT)
        voiceProxy.startMicrophonesRecording("/home/nao/recordings/cameras/"+str(filename)+"_NAO.wav",
                                             "wav",
                                             48000,
                                             [0,0,1,0])
    def stopAudioRecording(self):        
        voiceProxy = ALProxy("ALAudioRecorder",self.robotIP,PORT)
        voiceProxy.stopMicrophonesRecording()
    def nivelBateria(self):
        try:        
            proxyBattery = ALProxy("ALBattery",self.robotIP,PORT)
            status = proxyBattery.getBatteryCharge()        
            if status <= 40:
                aviso = "Atenção: Nível da bateria em "+ status+"%."
                self.enviarAviso(str(aviso))
            else:
                time.sleep(600)
                self.nivelBateria()
        except BaseException:
            aviso = "ERROR:Não é possível encontrar o robô."
            self.enviarAviso(aviso)    
    def getNAOfiles(self):
        myHostname = str(self.setIP())
        myUsername = "nao"
        myPassword = "nao"
        with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
            print("Connection succesfully stablished ... ")
            filename = self.gera_id_sessao()
            # Define the file that you want to download from the remote directory
            videopath = '/home/nao/recordings/cameras/'+filename+'_NAO.avi'
            audiopath = '/home/nao/recordings/cameras/'+filename+'_NAO.wav'

            # Define the local path where the file will be saved
            # or absolute "C:\Users\sdkca\Desktop\TUTORIAL.txt"
            localFilePath = self.pasta             
            arqWav = localFilePath+"\\"+filename+"_NAO.wav"
            arqAvi = localFilePath+"\\"+filename+"_NAO.avi"
            if localFilePath != "":
                sftp.get(videopath, arqAvi)
                sftp.get(audiopath, arqWav)                
                #print "Muxing"
                cmd = "ffmpeg -ac 1 -channel_layout stereo -i " +arqWav+ " -i "+arqAvi+" -pix_fmt yuv420p " +localFilePath+"\\"+filename + "_First.avi"
                subprocess.call(cmd, shell=True)
                sftp.remove(videopath)
                sftp.remove(audiopath)

	   
            #Funções dos botões
    def desligar(self):
        try:            
            motionProxy = ALProxy("ALMotion",self.robotIP,9559)
            system = ALProxy("ALSystem", self.robotIP, 9559)            
            motionProxy.post.rest()      
            system.post.shutdown()
            aviso = "AVISO: Fim da conexão com o robô."
            self.enviarAviso(aviso)
        except BaseException:
            aviso = "ERROR:Falha na execução do comando."
            self.enviarAviso(aviso)

    def levantar(self):
        try:            
            motionProxy = ALProxy("ALMotion",self.robotIP,9559)
            aviso = "AVISO: Comando levantar enviado com sucesso."
            self.enviarAviso(aviso) 
            motionProxy.post.wakeUp()
        except BaseException:
            aviso = "ERROR:Falha na execução do comando levantar."
            self.enviarAviso(aviso)           

    def sentar(self):
        try:            
            motionProxy = ALProxy("ALMotion",self.robotIP,9559)
                        
            motionProxy.post.rest()
                         
            aviso = "AVISO: Comando sentar enviado com sucesso."
            self.enviarAviso(aviso) 
            
        except BaseException:
            aviso = "ERROR:Falha na execução do comando sentar."
            self.enviarAviso(aviso)

    def funcSentarLevantar(self):
        if self.aux == False:
            self.btn3x1.setEnabled(False)
            self.sentar()
            self.aux = True
            self.btn3x1.setText("Levantar")
            self.btn3x1.setEnabled(True)
        else:            
            self.aux = False
            self.btn3x1.setEnabled(False)
            self.levantar()
            self.btn3x1.setText("Sentar")
            self.btn3x1.setEnabled(True)

    def movimento(self,object):
        try:
            nomefunc = object.__name__
            names, times, keys = object()
        except BaseException:
            aviso = "Falha no envio dos dados."
            self.enviarAviso(aviso)
        try:                        
            motion = ALProxy("ALMotion", self.robotIP, PORT)  
            postureProxy = ALProxy("ALRobotPosture", self.robotIP, PORT)   
            postureProxy.post.goToPosture("Stand",0.1)
            aviso = "AVISO: Comando "+nomefunc+" enviado com sucesso."
            self.enviarAviso(str(aviso))
            motion.post.angleInterpolation(names, keys, times, True)            
            postureProxy.post.goToPosture("Stand",0.1)
            return        
        except BaseException:
            aviso = "ERROR:Falha na execução do comando "+nomefunc+"."
            self.enviarAviso(str(aviso))
    
    def concordar(self):
        self.movimento(concordar.sim)
    def discordar(self):
        self.movimento(discordar.nao)
    def conversar(self):
        self.movimento(conversar.conversar)
    def comemorar(self):
        self.movimento(comemorar.comemorar)
    def empatia(self):
        self.movimento(empatia.empatia)
    def duvida(self):
        self.movimento(duvida.duvida)
    def palmas(self):
        self.movimento(palmas.palmas)
    def tocaqui(self):
        self.movimento(toca_aqui.tocaAqui)
    def tchau(self):
        self.movimento(tchau.tchau)
    def beijos(self):
        self.movimento(beijos.beijos)
    
class ImageWidget(QWidget):
    """
    Tiny widget to display camera images from Naoqi.
    """
    def __init__(self, IP, PORT, CameraID, parent=None):
        """
        Initialization.
        """
        QWidget.__init__(self, parent)
        self._image = QImage()
        self.setWindowTitle('Nao')

        self._imgWidth = 640
        self._imgHeight = 480
        self._cameraID = CameraID
        self.resize(self._imgWidth, self._imgHeight)

        # Proxy to ALVideoDevice.
        self._videoProxy = None

        # Our video module name.
        self._imgClient = ""

        # This will contain this alImage we get from Nao.
        self._alImage = None

        self._registerImageClient(IP, PORT)

        # Trigget 'timerEvent' every 100 ms.
        self.startTimer(100)


    def _registerImageClient(self, IP, PORT):
        """
        Register our video module to the robot.
        """
        self._videoProxy = ALProxy("ALVideoDevice", IP, PORT)
        resolution = vision_definitions.kQVGA  # 320 * 240
        colorSpace = vision_definitions.kRGBColorSpace
        self._imgClient = self._videoProxy.subscribe("_client", resolution, colorSpace, 5)

        # Select camera.
        self._videoProxy.setParam(vision_definitions.kCameraSelectID,
                                  self._cameraID)


    def _unregisterImageClient(self):
        """
        Unregister our naoqi video module.
        """
        if self._imgClient != "":
            self._videoProxy.unsubscribe(self._imgClient)


    def paintEvent(self, event):
        """
        Draw the QImage on screen.
        """
        painter = QPainter(self)
        painter.drawImage(painter.viewport(), self._image)


    def _updateImage(self):
        """
        Retrieve a new image from Nao.
        """
        self._alImage = self._videoProxy.getImageRemote(self._imgClient)
        self._image = QImage(self._alImage[6],           # Pixel array.
                             self._alImage[0],           # Width.
                             self._alImage[1],           # Height.
                             QImage.Format_RGB888)


    def timerEvent(self, event):
        """
        Called periodically. Retrieve a nao image, and update the widget.
        """
        self._updateImage()
        self.update()


    def __del__(self):
        """
        When the widget is deleted, we unregister our naoqi video module.
        """
        self._unregisterImageClient()
