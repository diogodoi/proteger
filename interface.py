# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QTableWidgetItem, QWidget, QImage, QApplication, QPainter,QFileDialog, QDialog,QWidget,QTableView
from PyQt4.QtCore import QTimer, QBasicTimer, QObject, Qt,QThread, pyqtSignal
from naoqi import ALProxy, ALBroker, ALModule
from movimentos import beijos,comemorar,concordar,nossa,duvida,discordar,empatia,palmas,tchau,toca_aqui,focus,arm_pose
import vision_definitions
import sqlite3
import time
import random
import os


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


#Verifica se o banco de dados existe, se não existir ele é criado.
try:
    bd = open('BdProteger.db')
    bd.close()
except:
    conn = sqlite3.connect('BdProteger.db')
    conn.execute(''' CREATE TABLE "IpRobot" (
	"id"	INTEGER,
	"IpRobot"	TEXT UNIQUE,
	PRIMARY KEY("id"))
                 ''')
    conn.execute(''' 
    CREATE TABLE "Sessao" (
	"ip"	INTEGER UNIQUE,
	"Data"	TEXT NOT NULL,
	"Hora"	TEXT NOT NULL,
	"Aviso"	TEXT NOT NULL,
	PRIMARY KEY("ip" AUTOINCREMENT))    
''')
    conn.execute("INSERT INTO IpRobot (IpRobot) VALUES ('192.168.0.1')");
    conn.commit()
    conn.close()
    
try:
    os.mkdir("Logs")
except:
    pass
#Abre Banco de dados e adiciona os valores no completer, e pega o ultimo valor de IP inserido.
conn = sqlite3.connect('BdProteger.db')
cursor = conn.cursor()
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

iprobo = ""
jan = None

class Ui_MainWindow(object):
    def __init__(self):
        self.val_ip = ""
        self.aux = False        
        self.AuxLeds = False        
        self.robotIP = ""
        self.PORT = 9559
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))        
        
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/02.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("""
                        font:16px;                        
                          """)

        self.centralwidget = QtGui.QWidget(MainWindow)        
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridMain = QtGui.QGridLayout(self.centralwidget)
        self.gridMain.setObjectName(_fromUtf8("gridMain"))
        
        #Menu bar
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setObjectName(_fromUtf8("menubar"))                
        self.menuMenu = QtGui.QMenu(self.menubar)        
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSobre = QtGui.QAction(MainWindow)
        self.actionSobre.setObjectName(_fromUtf8("actionSobre"))
        self.menuMenu.addAction(self.actionSobre)
        self.menubar.addAction(self.menuMenu.menuAction())
        

        #Configurações
        self.Menu = QtGui.QGroupBox(self.centralwidget)        
        self.Menu.setObjectName(_fromUtf8("Menu"))

        self.gridMenu = QtGui.QGridLayout(self.Menu)
        self.gridMenu.setObjectName(_fromUtf8("gridMenu"))
        self.Menu.setMinimumSize(200,200)
        self.Menu.setMaximumSize(500,500)
        
        self.label_Ip = QtGui.QLabel(self.Menu)        
        self.label_Ip.setObjectName(_fromUtf8("label_Ip"))

        self.gridMenu.addWidget(self.label_Ip, 0, 1, 1, 1)        
      
        self.inputIP = QtGui.QLineEdit(self.Menu)                        
        self.inputIP.setObjectName(_fromUtf8("inputIP"))
        self.gridMenu.addWidget(self.inputIP, 0, 2, 1, 1)       
              
        self.BtnConn = QtGui.QPushButton(self.Menu)               
        self.BtnConn.setObjectName(_fromUtf8("BtnConn"))

        self.gridMenu.addWidget(self.BtnConn, 1, 2, 1, 1)
        
        self.BtnNaoView = QtGui.QPushButton(self.Menu)        
        self.BtnNaoView.setObjectName(_fromUtf8("BtnNaoView"))
        self.BtnNaoView.setEnabled(False)

        self.gridMenu.addWidget(self.BtnNaoView, 2, 2, 1, 1)
       
        self.BtnEnc = QtGui.QPushButton(self.Menu)        
        self.BtnEnc.setObjectName(_fromUtf8("BtnEnc"))
        self.BtnEnc.setEnabled(False)

        self.gridMenu.addWidget(self.BtnEnc, 3, 2, 1, 1)
        

        #### BOX MOVIMENTOS
        self.Movimentos = QtGui.QGroupBox(self.centralwidget)        
        self.Movimentos.setObjectName(_fromUtf8("Movimentos"))
        
        self.Movimentos.setMinimumWidth(450)
        self.Movimentos.setMaximumWidth(800)
        
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
        
        self.btn1x1.setEnabled(False)
        self.btn2x1.setEnabled(False)
        self.btn3x1.setEnabled(False)
        self.btn1x2.setEnabled(False)
        self.btn2x2.setEnabled(False)
        self.btn3x2.setEnabled(False)
        self.btn1x3.setEnabled(False)
        self.btn2x3.setEnabled(False)
        self.btn3x3.setEnabled(False)
        self.btn4x1.setEnabled(False)
        self.btn4x2.setEnabled(False)  

        ##AREA DE AVISOS
        self.Avisos = QtGui.QGroupBox(self.centralwidget)
        self.Avisos.setObjectName(_fromUtf8("Avisos"))
        self.Avisos.setMinimumHeight(300)
        self.Avisos.setMinimumWidth(300)

        self.gridAvisos = QtGui.QGridLayout(self.Avisos)
        self.gridAvisos.setObjectName(_fromUtf8("gridAvisos"))
        
        self.label_avisos = QtGui.QLabel(self.Avisos)
        self.label_avisos.setObjectName(_fromUtf8("Avisos"))        
        self.label_avisos.setStyleSheet("border:none")
        self.label_avisos.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.gridAvisos.addWidget(self.label_avisos, 0, 3, 1, 2)  
  
        self.tableWidget = QtGui.QTableWidget(self.Avisos)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(False)
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
        self.tableWidget.setStyleSheet("font:12px;text-decoration: none;color:black;")
        self.gridAvisos.addWidget(self.tableWidget, 1, 1, 2, 6)
      
        self.logo_cti = QtGui.QLabel(self.Avisos)
        self.logo_cti.setMaximumSize(100,60) 
        self.logo_cti.setText(_fromUtf8(""))
        self.logo_cti.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/LogoCTIcampinas.jpeg")))
        self.logo_cti.setScaledContents(True)
        self.logo_cti.setObjectName(_fromUtf8("logo_cti"))
        self.gridAvisos.addWidget(self.logo_cti, 3, 2, 1, 1)
              
        self.logo_icmc = QtGui.QLabel(self.Avisos)
        self.logo_icmc.setMaximumSize(100,60)            
        self.logo_icmc.setText(_fromUtf8(""))
        self.logo_icmc.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/LogoICMC.png")))
        self.logo_icmc.setScaledContents(True)
        self.logo_icmc.setObjectName(_fromUtf8("logo_icmc"))
        self.gridAvisos.addWidget(self.logo_icmc, 3, 3, 1, 1)
        
        self.logo_lar = QtGui.QLabel(self.Avisos)
        self.logo_lar.setMaximumSize(100,60)        
        self.logo_lar.setText(_fromUtf8(""))
        self.logo_lar.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/LogoLars.png")))
        self.logo_lar.setScaledContents(True)
        self.logo_lar.setObjectName(_fromUtf8("logo_lar"))
        self.gridAvisos.addWidget(self.logo_lar, 3, 4, 1, 1)
        
        self.logo_Unesp = QtGui.QLabel(self.Avisos)
        # self.logo_Unesp.resize(100,60)
        self.logo_Unesp.setMaximumSize(100,60)              
        self.logo_Unesp.setText(_fromUtf8(""))
        self.logo_Unesp.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/unesp-full-center.png")))
        self.logo_Unesp.setScaledContents(True)
        self.logo_Unesp.setObjectName(_fromUtf8("logo_Unesp"))
        self.gridAvisos.addWidget(self.logo_Unesp, 3, 5, 1, 1)
        
       #Gravação
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
    
        self.gridLayout_GB = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_GB.setObjectName(_fromUtf8("gridLayout_GB"))        
        
        self.groupBox.setMinimumSize(200,200)
        self.groupBox.setMaximumSize(500,500)        
        
        self.btnGB1x1 = QtGui.QPushButton(self.groupBox)
        self.btnGB1x1.setObjectName(_fromUtf8("btnGB1x1"))
        self.btnGB1x1.setEnabled(False)
        
        self.gridLayout_GB.addWidget(self.btnGB1x1, 1, 1, 1, 2)
        
        self.btnGB2x1 = QtGui.QPushButton(self.groupBox)
        self.btnGB2x1.setObjectName(_fromUtf8("btnGB2x1"))
        self.btnGB2x1.setEnabled(False)
        self.gridLayout_GB.addWidget(self.btnGB2x1, 2, 1, 1, 2)
        
        self.btnGB3x1 = QtGui.QPushButton(self.groupBox)
        self.btnGB3x1.setObjectName(_fromUtf8("btnGB2x1"))
        
        self.gridLayout_GB.addWidget(self.btnGB3x1, 3, 1, 1, 1)
        
        self.btnGB4x1 = QtGui.QPushButton(self.groupBox)
        self.btnGB4x1.setObjectName(_fromUtf8("btnGB2x1"))
        
        self.gridLayout_GB.addWidget(self.btnGB4x1, 3, 2, 1, 1)
       
                
        ### BOTAO EMERGENCIA
        self.EMG = QtGui.QPushButton(self.centralwidget)
        self.EMG.setStyleSheet(_fromUtf8("color: rgb(255, 255, 0);\n""background-color: rgb(255, 0, 0)"))
        self.EMG.setObjectName(_fromUtf8("EMG"))
        MainWindow.setCentralWidget(self.centralwidget)        
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.EMG.setFont(font)
        self.EMG.setMinimumHeight(50)
        
        
        #Botões Configurações
        self.BtnConn.clicked.connect(self.conexao)
        self.BtnNaoView.clicked.connect(self.newTreadVision)
        self.BtnEnc.clicked.connect(self.desconectar)

        #Botões Movimentos
        self.btn1x1.clicked.connect(self.concordar)
        self.btn1x2.clicked.connect(self.discordar)
        self.btn1x3.clicked.connect(self.nossa)
        self.btn2x1.clicked.connect(self.comemorar)
        self.btn2x2.clicked.connect(self.empatia)
        self.btn2x3.clicked.connect(self.duvida)
        self.btn3x1.clicked.connect(self.funcSentarLevantar)
        self.btn3x2.clicked.connect(self.palmas)
        self.btn3x3.clicked.connect(self.tocaqui)
        self.btn4x1.clicked.connect(self.tchau)
        self.btn4x2.clicked.connect(self.beijos)
        #Botão Emergência
        self.EMG.clicked.connect(self.desligar)
        
        #Botões Sessão
        self.btnGB1x1.clicked.connect(self.startNaoRecording)        
        self.btnGB2x1.clicked.connect(self.stopNaoRecording)
        self.btnGB3x1.clicked.connect(self.virarEsquerda)
        self.btnGB4x1.clicked.connect(self.virarDireita)

        
        #Recupera o ultimo ip adicionado na lista.
        self.inputIP.setText(last_ip)
        #Cria uma lista para completar ip
        completerip = QtGui.QCompleter(lista_ip)
        completerip.setCompletionMode(2)
        self.inputIP.setCompleter(completerip)
 
        #Posições das box em grid
        self.gridMain.addWidget(self.Menu, 1, 1, 1, 1)
        self.gridMain.addWidget(self.groupBox,2,1,1,1)
        self.gridMain.addWidget(self.Movimentos, 1, 2, 2, 1)
        self.gridMain.addWidget(self.EMG, 3, 1, 1, 2)        
        self.gridMain.addWidget(self.Avisos, 4, 1, 1, 2)                        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)    
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "V1.1.0 - GUIPsyin - Interface Gráfica de Interação Psicológica Infantil ", None))
                        
        #menu
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))        
        self.actionSobre.setText(_translate("MainWindow", "Sobre", None))
        self.Menu.setTitle(_translate("MainWindow", "Configurações", None))
        self.label_Ip.setText(_translate("MainWindow", "IP Robô", None))
        self.BtnConn.setText(_translate("MainWindow", "Conectar", None))
        self.BtnEnc.setText(_translate("MainWindow", "Desconectar", None))
        
        #Avisos
        self.label_avisos.setText(_translate("MainWindow", "Avisos", None))
        
        #Gravação
        self.groupBox.setTitle(_translate("ChatWindow", "Sessão", None))
        self.btnGB1x1.setText(_translate("MainWindow", "Iniciar Vida", None))
        self.btnGB2x1.setText(_translate("MainWindow", "Encerrar Vida", None))
        self.BtnNaoView.setText(_translate("MainWindow", "Câmera NAO", None))
        self.btnGB3x1.setText(_translate("MainWindow","Girar para esquerda",None))
        self.btnGB4x1.setText(_translate("MainWindow","Girar para direita",None))
        #Movimentos
        self.Movimentos.setTitle(_translate("MainWindow", "Movimentos", None))
        self.btn1x1.setText(_translate("MainWindow", "Concordar", None))
        self.btn1x2.setText(_translate("MainWindow", "Discordar", None))
        self.btn2x2.setText(_translate("MainWindow", "Empatia", None))
        self.btn2x1.setText(_translate("MainWindow", "Comemorar", None))
        self.btn1x3.setText(_translate("MainWindow", "Nossa", None))
        self.btn3x3.setText(_translate("MainWindow", "Toca aqui", None))
        self.btn2x3.setText(_translate("MainWindow", "Duvida", None))
        self.btn3x2.setText(_translate("MainWindow", "Palmas", None))
        self.btn3x1.setText(_translate("MainWindow", "Sentar", None))
        self.btn4x1.setText(_translate("MainWindow", "Oi/Tchau", None))
        self.btn4x2.setText(_translate("MainWindow", "Beijos", None))
        
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hora", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mensagens", None))
        self.EMG.setText(_translate("MainWindow", "DESLIGAR/EMERGÊNCIA", None))        
    
    #Funções complementares   
    
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
            self.motion = ALProxy("ALMotion", self.robotIP, self.PORT)
            self.posture = ALProxy("ALRobotPosture", self.robotIP, self.PORT)
            aviso = "AVISO: Conexão estabelecida com "+self.robotIP+" foi estabelecida." 
            self.enviarAviso(aviso)
        except BaseException:
            aviso = "ERROR: Falha na conexão com "+ self.robotIP +"."
            self.enviarAviso(aviso)
            return
        try:
            self.basic_awareness = ALProxy("ALBasicAwareness", self.robotIP, self.PORT)
        except BaseException:
            aviso = "ERROR: Falha na configuração da detecção de Face."
            self.enviarAviso(aviso)
            return        
        try:    
            self.salva_ip()
            self.BtnConn.setText("Conectado")            
            self.BtnConn.setEnabled(False)
            self.BtnEnc.setEnabled(True)
            self.BtnNaoView.setEnabled(True)
            self.btnGB1x1.setEnabled(True)
            self.BtnConn.setStyleSheet("background-color:#40FF00;") 
        except BaseException:
            aviso = "ERROR: Falha na configuração."
            self.enviarAviso(aviso)
            return

    def desconectar(self):
        try:
            global jan
            if jan != None:            
                jan.destroy()
                jan = None
        except BaseException:
            aviso = "ERROR:Falha ao fechar janelas."
            self.enviarAviso(aviso)        
        try:
            self.salva_log()
        except BaseException:
            aviso = "ERROR:Falha ao salvar log."
            self.enviarAviso(aviso)
            return 
        try:           
            self.robotIP = ""
            self.BtnConn.setText("Conectar")
            self.BtnConn.setEnabled(True)
            self.BtnEnc.setEnabled(False)
            self.BtnNaoView.setEnabled(False)
            self.BtnConn.setStyleSheet("background:#FFF;border:None;")
            self.btn1x1.setEnabled(False)
            self.btn2x1.setEnabled(False)
            self.btn3x1.setEnabled(False)

            self.btn1x2.setEnabled(False)
            self.btn2x2.setEnabled(False)
            self.btn3x2.setEnabled(False)

            self.btn1x3.setEnabled(False)
            self.btn2x3.setEnabled(False)
            self.btn3x3.setEnabled(False)

            self.btn4x1.setEnabled(False)
            self.btn4x2.setEnabled(False)
            aviso = "AVISO: Sessão encerrada com sucesso."
            self.enviarAviso(aviso)                  
        except BaseException:
            aviso = "ERROR: Falha na conexão com o robô."
            self.enviarAviso(aviso)
            return            
    
    def enviarAviso(self,aviso):
        conn = sqlite3.connect('BdProteger.db')
        conn.text_factory = str
        self.aviso = aviso
        t = time.localtime()
        Data = str(t.tm_mday) + "/" + str(t.tm_mon) + "/" + str(t.tm_year) 
        hora = str(t.tm_hour) + ":" + str(t.tm_min) + ":" + str(t.tm_sec)
        conn.execute("INSERT INTO Sessao (Data,Hora,Aviso) VALUES(?,?,?);",(Data,hora,self.aviso))
        conn.commit()
        
        # conn = sqlite3.connect('BdProteger.db')
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
            global iprobo
            iprobo = self.val_ip                                    
            return self.val_ip
    
    def salva_log(self):
        conn = sqlite3.connect('BdProteger.db')
        cursor = conn.cursor()
        query= "SELECT * FROM Sessao;"
        cursor.execute(query)
        #Gera arquivo com o log dos arquivos
        listaLog = []
        t = time.localtime()
        nome = "Log"+ str(time.strftime("%Y%m%d"+ "_" + "%H-%M-%S" , t)) 
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
            
    def faceDetector(self):
        try:
            faceProxy = ALProxy("ALFaceDetection", self.robotIP, self.PORT)
            period = 500
            faceProxy.subscribe("Test_Face", period, 0.0 )
            memoryProxy = ALProxy("ALMemory", self.robotIP, self.PORT)
            memValue = "FaceDetected"
            val = memoryProxy.getData(memValue) 
        except Exception:
            aviso = "ERROR:Não Foi possível criar o proxy de detecção de face."
            self.enviarAviso(aviso)
        try:    
            if(val and isinstance(val, list) and len(val) >= 2): 
                        
                timeStamp = val[0]   
                        
                faceInfoArray = val[1]

                try:            
                    for j in range( len(faceInfoArray)-1 ):
                                faceInfo = faceInfoArray[j]

                                # First Field = Shape info.
                                faceShapeInfo = faceInfo[0]

                                # Second Field = Extra info (empty for now).
                                faceExtraInfo = faceInfo[1]

                                # print "  alpha %.3f - beta %.3f" % (faceShapeInfo[1], faceShapeInfo[2])
                                # print "  width %.3f - height %.3f" % (faceShapeInfo[3], faceShapeInfo[4])
                                return True

                except Exception:
                        aviso = "faces detected, but it seems getData is invalid."
                        self.enviarAviso(aviso)
            else:
                return False
            faceProxy.unsubscribe("Test_Face")
        except Exception:
            pass

    def face_fun(self):
        Face = self.faceDetector()
        self.aux = self.basic_awareness.isAwarenessRunning()
        if (Face == True):
            self.faceThread.exit()             
        if (self.aux == False):
            self.basic_awareness.startAwareness()
           
        if (self.aux == True and Face == True):
            self.basic_awareness.stopAwareness()
            self.faceThread.exit()
            return           
        else:
            self.olhaPraFrente()
            self.faceThread.exit()            
            return        
    
    def newTreadVision(self):
        self.naovisionThread = QThread()
        self.worker1 = VisionNAO()
        # self.worker1.moveToThread(self.naovisionThread)
        self.naovisionThread.started.connect(self.worker1.naoVision)
        # self.worker1.finished.connect(self.naovisionThread.quit)
        # self.worker1.finished.connect(self.worker1.deleteLater)
        # self.naovisionThread.finished.connect(self.naovisionThread.deleteLater)        
        self.naovisionThread.start()
        
    #Funções dos botões
    def desligar(self):
        try:
            if (self.BtnConn.text() == "Conectar"):
                return
            else:            
                motionProxy = ALProxy("ALMotion",self.robotIP,9559)
                system = ALProxy("ALSystem", self.robotIP, 9559)            
                motionProxy.post.rest()      
                system.post.shutdown()
                aviso = "AVISO: Fim da conexão com o robô."
                self.enviarAviso(aviso)
        except BaseException:
            aviso = "ERROR:Falha na execução do comando."
            self.enviarAviso(aviso)
            
    def ledsOff(self):
        motion = ALProxy("ALMotion", self.robotIP, self.PORT)
        motion.post.rest() 
        leds = ALProxy("ALLeds", self.robotIP, self.PORT)        
        name = "AllLeds"        
        leds.post.off(name)
        
    def startLife(self):
        self.AuxLeds = True
        motion = ALProxy("ALMotion", self.robotIP, self.PORT)
        leds = ALProxy("ALLeds", self.robotIP, self.PORT)        
        names = ['BrainLeds','FaceLeds','ChestLeds','FeetLeds','EarLeds']
        for name in names: leds.post.on(name)            
        motion = ALProxy("ALMotion", self.robotIP, self.PORT)
        motion.post.wakeUp()
        # motion.post.goToPosture("Stand",0.3)
        motion.post.setBreathEnabled("Body",True)
        self.btn1x1.setEnabled(True)
        self.btn2x1.setEnabled(True)
        self.btn3x1.setEnabled(True)
        self.btn1x2.setEnabled(True)
        self.btn2x2.setEnabled(True)
        self.btn3x2.setEnabled(True)
        self.btn1x3.setEnabled(True)
        self.btn2x3.setEnabled(True)
        self.btn3x3.setEnabled(True)
        self.btn4x1.setEnabled(True)
        self.btn4x2.setEnabled(True)
    
    def olhaPraFrente(self):

        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([1])
        keys.append([-0.15708])

        names.append("HeadYaw")
        times.append([1])
        keys.append([0.00698132])
        
        self.motion.angleInterpolation(names, keys, times, True)
    
    def facedetector(self):
            self.faceThread = QThread()
            self.faceThread.started.connect(self.face_fun)
            self.faceThread.start()
        
    def startNaoRecording(self):
        if (self.BtnConn.text() == "Conectar"):
            return
        else:
            try:
                self.startLife()
                aviso = "AVISO: Iniciando a vida, ligando leds e levantando."
                self.enviarAviso(aviso)
            except BaseException:
                aviso = "ERROR: Falha na inicialização da vida."
                self.enviarAviso(aviso)
                return 
            try:
                self.TMf = QTimer(self)
                self.TMf.timeout.connect(self.facedetector)
                self.TMf.start(7000)
                aviso = "AVISO: Detector de face inicializado com sucesso."
                self.enviarAviso(aviso)
                self.btnGB1x1.setEnabled(False)
                self.btnGB1x1.setText("Conectado")
                self.btnGB1x1.setStyleSheet("background-color:#40FF00;") 
                self.btnGB2x1.setEnabled(True)
            except BaseException:
                aviso = "ERROR: Falha na inicialização do detector de face."
                self.enviarAviso(aviso)
                return     

    def stopNaoRecording(self):
        if (self.BtnConn.text() == "Conectar"):
            return
        else:
            try:
                self.TMf.stop()
                self.ledsOff()
                self.btnGB1x1.setEnabled(True)
                self.btnGB1x1.setText("Iniciar Vida")
                self.btnGB1x1.setStyleSheet("background:#FFF;border:None;")
                self.btnGB2x1.setEnabled(False)
                aviso = "AVISO: Detector de face encerrado com sucesso."
                self.enviarAviso(aviso)         
            except BaseException:
                aviso = "ERROR:Falha ao encerrar detector de face."
                self.enviarAviso(aviso)
                return
            try:
                self.salva_log()
                self.btn1x1.setEnabled(False)
                self.btn2x1.setEnabled(False)
                self.btn3x1.setEnabled(False)
                self.btn1x2.setEnabled(False)
                self.btn2x2.setEnabled(False)
                self.btn3x2.setEnabled(False)
                self.btn1x3.setEnabled(False)
                self.btn2x3.setEnabled(False)
                self.btn3x3.setEnabled(False)
                self.btn4x1.setEnabled(False)
                self.btn4x2.setEnabled(False)
            except BaseException:
                aviso = "ERROR:Falha ao salvar log."
                self.enviarAviso(aviso)
                return 

    #Funções Movimentos
    def levantar(self):
        try:            
            motion = ALProxy("ALMotion",self.robotIP,9559)
            motion.post.wakeUp()
            motion.post.setBreathEnabled("Body",True)
            aviso = "AVISO: Comando levantar enviado com sucesso."
            self.enviarAviso(aviso)
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
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:                        
            if (self.btn3x1.text() == "Sentar"):                
                self.btn3x1.setEnabled(False)
                self.sentar()
                self.aux = True
                self.btn3x1.setText("Levantar")
                self.btn3x1.setEnabled(True)
            else:
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
            return
        try:
            self.motion.post.wakeUp() 
            self.motion.post.angleInterpolation(names, keys, times, True)                        
            # self.posture.post.goToPosture("Stand",0.25)
            self.motion.post.setBreathEnabled("Body",True)
            if (self.btn3x1.text()== "Levantar"):
                self.btn3x1.setText("Sentar")
            aviso = "AVISO: Comando "+nomefunc+" enviado com sucesso."
            self.enviarAviso(str(aviso))
        except BaseException:
            aviso = "ERROR:Falha na execução do comando "+nomefunc+"."
            self.enviarAviso(str(aviso))
            return
    def concordar(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn1x1.setEnabled(False)
            self.movimento(concordar.sim)
            self.btn1x1.setEnabled(True)
    def discordar(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn1x2.setEnabled(False)
            self.movimento(discordar.nao)
            self.btn1x2.setEnabled(True)
    def nossa(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn1x3.setEnabled(False)
            self.movimento(nossa.nossa)
            self.btn1x3.setEnabled(True)
    def comemorar(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn2x1.setEnabled(False)        
            self.movimento(comemorar.comemorar)
            self.btn2x1.setEnabled(True)
    def empatia(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn2x2.setEnabled(False)
            self.movimento(empatia.empatia)
            self.btn2x2.setEnabled(True)
    def duvida(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn2x3.setEnabled(False)
            self.movimento(duvida.duvida)
            self.btn2x3.setEnabled(False)
    def palmas(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn3x2.setEnabled(False)
            self.movimento(palmas.palmas)
            self.btn3x2.setEnabled(True)
    def tocaqui(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn3x3.setEnabled(False)
            self.movimento(toca_aqui.tocaAqui)
            self.btn3x3.setEnabled(True)
    def tchau(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn4x1.setEnabled(False)
            self.movimento(tchau.tchau)
            self.btn4x1.setEnabled(True)
    def beijos(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn4x2.setEnabled(False)
            self.motion.wakeUp()
            self.movimento(beijos.beijos)
            self.btn4x2.setEnabled(True)

    #extras    
    def virarDireita(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text()== "Iniciar Vida"):
            return
        else:
            self.motion.post.wakeUp()
            self.motion.post.moveInit()
            self.motion.post.moveTo(0,0,0.1)
    def virarEsquerda(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text()== "Iniciar Vida"):
            return
        else:
            self.motion.post.wakeUp()
            self.motion.post.moveInit()
            self.motion.post.moveTo(0,0,-0.1)
    
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
        self.jan = None


    def _registerImageClient(self, IP, PORT):
        """
        Register our video module to the robot.
        """
        self._videoProxy = ALProxy("ALVideoDevice", IP, PORT)
        resolution = vision_definitions.kQVGA  # 320 * 240
        colorSpace = vision_definitions.kRGBColorSpace
        self._imgClient = self._videoProxy.subscribe("_client", resolution, colorSpace, 24)

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
    
class VisionNAO(QObject):
    finished = pyqtSignal()
        
    def naoVision(self):
        try:
            self.IP = str(iprobo)            
            self.CameraID = 0
            self.PORT= 9559
            global jan 
            jan = ImageWidget(self.IP, self.PORT, self.CameraID)
            jan.show()
        except Exception:
            aviso = "ERROR: Falha na conexão com a câmera do NAO."
            print(aviso)
            return
        
