# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QTableWidgetItem, QWidget, QImage, QApplication, QPainter,QFileDialog, QDialog,QWidget,QTableView
from PyQt4.QtCore import QTimer, QBasicTimer, QObject, Qt,QThread, pyqtSignal
from naoqi import ALProxy
from movimentos import beijos,comemorar,concordar,nossa,duvida,discordar,empatia,palmas,tchau,toca_aqui
from designSobre import Ui_Sobre
import sqlite3
import time
from retrivingImages import NAOimageRetriving



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
        
        MainWindow.setMinimumSize(QtCore.QSize(840, 840))
        
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
        
        self.actionSobre.triggered.connect(self.openSobre)
        
        

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
        self.BtnConn.setToolTip(_fromUtf8("Faz a conexão com o robô."))

        self.gridMenu.addWidget(self.BtnConn, 1, 2, 1, 1)
        
        self.BtnNaoView = QtGui.QPushButton(self.Menu)        
        self.BtnNaoView.setObjectName(_fromUtf8("BtnNaoView"))
        self.BtnNaoView.setEnabled(False)
        self.BtnNaoView.setToolTip(_fromUtf8("Faz a captura do vídeo do robô."))

        self.gridMenu.addWidget(self.BtnNaoView, 2, 2, 1, 1)
       
        self.BtnEnc = QtGui.QPushButton(self.Menu)        
        self.BtnEnc.setObjectName(_fromUtf8("BtnEnc"))
        self.BtnEnc.setEnabled(False)
        self.BtnEnc.setToolTip(_fromUtf8("Encerra a conexão com o robô."))

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
        self.btn1x1.setToolTip(_fromUtf8("Movimento a cabeça para baixo e para cima."))
        
        self.btn1x2 = QtGui.QPushButton(self.Movimentos)
        self.btn1x2.setObjectName(_fromUtf8("btn1x2"))
        self.gridLayout_2.addWidget(self.btn1x2, 0, 6, 1, 1)
        self.btn1x2.setToolTip(_fromUtf8("Movimenta a cabeça para os lados."))
                        
        self.btn1x3 = QtGui.QPushButton(self.Movimentos)
        self.btn1x3.setObjectName(_fromUtf8("btn1x3"))
        self.gridLayout_2.addWidget(self.btn1x3, 0, 8, 1, 1)
        self.btn1x3.setToolTip(_fromUtf8("Levanta a mão em direção a testa."))
        
        self.btn2x1 = QtGui.QPushButton(self.Movimentos)
        self.btn2x1.setObjectName(_fromUtf8("btn2x1"))
        self.gridLayout_2.addWidget(self.btn2x1, 1, 3, 1, 1)
        self.btn2x1.setToolTip(_fromUtf8("Faz uma dança de comemoração."))
        
        self.btn2x2 = QtGui.QPushButton(self.Movimentos)
        self.btn2x2.setObjectName(_fromUtf8("btn2x2"))
        self.gridLayout_2.addWidget(self.btn2x2, 1, 6, 1, 1)
        self.btn2x2.setToolTip(_fromUtf8("Movimenta a cabeça bem devagar para baixo.") )     
        
        self.btn2x3 = QtGui.QPushButton(self.Movimentos)
        self.btn2x3.setObjectName(_fromUtf8("btn2x3"))
        self.gridLayout_2.addWidget(self.btn2x3, 1, 8, 1, 1)
        self.btn2x3.setToolTip(_fromUtf8("Abre os braços em uma posição receptiva."))
                
        self.btn3x1 = QtGui.QPushButton(self.Movimentos)
        self.btn3x1.setObjectName(_fromUtf8("btn3x1"))
        self.gridLayout_2.addWidget(self.btn3x1, 2, 3, 1, 1)
        self.btn3x1.setToolTip(_fromUtf8("Faz o robô sentar/levantar"))
        
        self.btn3x2 = QtGui.QPushButton(self.Movimentos)
        self.btn3x2.setObjectName(_fromUtf8("btn3x2"))
        self.gridLayout_2.addWidget(self.btn3x2, 2, 6, 1, 1)
        self.btn3x2.setToolTip(_fromUtf8("Faz o robô bater palmas."))
                
        self.btn3x3 = QtGui.QPushButton(self.Movimentos)
        self.btn3x3.setObjectName(_fromUtf8("btn3x3"))
        self.gridLayout_2.addWidget(self.btn3x3, 2, 8, 1, 1)
        self.btn3x3.setToolTip(_fromUtf8("O robô levanta a mão para cumprimentar."))
        
        
        
        self.btn4x1 = QtGui.QPushButton(self.Movimentos)
        self.btn4x1.setObjectName(_fromUtf8("btn4x1"))
        self.gridLayout_2.addWidget(self.btn4x1, 3, 3, 1, 1)
        self.btn4x1.setToolTip(_fromUtf8("O robô acena."))
        
        self.btn4x2 = QtGui.QPushButton(self.Movimentos)
        self.btn4x2.setObjectName(_fromUtf8("btn4x2"))
        self.gridLayout_2.addWidget(self.btn4x2, 3, 6, 1, 1)
        self.btn4x2.setToolTip(_fromUtf8("O robô envia um beijo."))
        
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
        self.gridAvisos.addWidget(self.label_avisos, 0, 3, 1, 1)  
  
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
        self.gridAvisos.addWidget(self.tableWidget, 1, 1, 2, 5)
      
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
        
       #sessão
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
        self.btnGB3x1.setEnabled(False)
        self.btnGB4x1.setEnabled(False)       
                
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
        self.BtnNaoView.clicked.connect(self.retrivingImage)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "V1.0.7 - GUIPsyin: Interface Gráfica de Interação Psicológica Infantil ", None))
                        
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
        self.btnGB3x1.setText(_translate("MainWindow","Virar para esquerda",None))
        self.btnGB4x1.setText(_translate("MainWindow","Virar para direita",None))
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
    
    def openSobre(self):
        self.windowSobre = QtGui.QWidget()
        ui = Ui_Sobre()
        ui.setupUi(self.windowSobre)
        self.windowSobre.show()
        
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
            self.tracker = ALProxy("ALTracker", self.robotIP, self.PORT)
            aviso = "AVISO: Conexão com "+self.robotIP+" estabelecida." 
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

    def buttonsOff(self):
        self.BtnConn.setEnabled(True)
        self.BtnConn.setText("Conectar")
        self.BtnConn.setStyleSheet("background:#e1e1e1;")
        self.BtnEnc.setEnabled(False)
        self.BtnNaoView.setText(_fromUtf8("Câmera NAO"))
        self.BtnNaoView.setStyleSheet("background:#e1e1e1;")
        self.BtnNaoView.setEnabled(False)
        
        #Movimentos
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
        
        #sessão            
        self.btnGB1x1.setText("Iniciar Vida")
        self.btnGB1x1.setStyleSheet("background:#e1e1e1;")
        self.btnGB1x1.setEnabled(False)
        self.btnGB2x1.setEnabled(False)
        self.btnGB3x1.setEnabled(False)
        self.btnGB4x1.setEnabled(False)
        return
    def desconectar(self):
        try:
            self.TMf.stop()
        except:
            pass
        try:
            self.salva_log()
        except BaseException:
            aviso = "ERROR:Falha ao salvar log."
            self.enviarAviso(aviso)
            return 
        try:           
            self.robotIP = ""
            self.buttonsOff()
            self.cameraWindow.close()
            self.cameraWindow = None
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
        return
    
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
        
    def faceTracker(self):
        # Add target to track.
        targetName = "Face"
        faceWidth = 0.5
        self.tracker.registerTarget(targetName, faceWidth)

        # Then, start tracker.
        self.tracker.track(targetName)
        
    #Funções dos botões
    def desligar(self):
        try:
            if (self.BtnConn.text() == "Conectar"):
                return
            else:
                try:          
                    system = ALProxy("ALSystem", self.robotIP, 9559)
                    self.cameraWindow.close()
                    self.cameraWindow = None    
                    self.motion.post.rest()
                except:
                    pass
                
                system.post.shutdown()
                aviso = "AVISO: Fim da conexão com o robô."
                self.enviarAviso(aviso)
                self.buttonsOff()
                
        except BaseException:
            aviso = "ERROR:Falha na execução do comando."
            self.enviarAviso(aviso)
            
    def ledsOff(self):
        self.motion.post.rest() 
        leds = ALProxy("ALLeds", self.robotIP, self.PORT)        
        name = "AllLeds"        
        leds.post.off(name)
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
        self.btnGB3x1.setEnabled(False)
        self.btnGB4x1.setEnabled(False)
        self.btnGB1x1.setText("Iniciar Vida")
        self.btnGB1x1.setStyleSheet("background:#e1e1e1;border:None;")
        
    def startLife(self):
        self.AuxLeds = True        
        leds = ALProxy("ALLeds", self.robotIP, self.PORT)        
        names = ['BrainLeds','FaceLeds','ChestLeds','FeetLeds','EarLeds']
        for name in names: leds.post.on(name) 
        self.motion.post.wakeUp()
        # motion.post.goToPosture("Stand",0.3)
        self.motion.post.setBreathEnabled("Body",True)
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
        self.btnGB3x1.setEnabled(True)
        self.btnGB4x1.setEnabled(True)
     
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
                self.faceTracker()
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
                self.tracker.stopTracker()
                self.tracker.unregisterAllTargets()
                self.ledsOff()
                self.btnGB1x1.setEnabled(True)
                self.btnGB1x1.setText("Iniciar Vida")
                self.btnGB1x1.setStyleSheet("background:#e1e1e1;")
                self.btnGB2x1.setEnabled(False)
                aviso = "AVISO: Detector de face encerrado com sucesso."
                self.enviarAviso(aviso)         
            except BaseException:
                aviso = "ERROR:Falha ao encerrar detector de face."
                self.enviarAviso(aviso)
                return
            try:
                self.salva_log()                
            except BaseException:
                aviso = "ERROR:Falha ao salvar log."
                self.enviarAviso(aviso)
                return 

    def buttonEmotionOn(self):
        self.BtnNaoView.setStyleSheet("background-color:#40FF00;")
        self.BtnNaoView.setText(_fromUtf8("Câmera Ligada"))
        # self.BtnNaoView.setEnabled(False)
        return
    
    def retrivingImage(self):
        try:
            self.cameraWindow  = NAOimageRetriving(self.robotIP, self.PORT, 0)
            self.cameraWindow.show()
            self.buttonEmotionOn()
            self.cameraWindow.exec_()
        except:
            aviso = "Câmera já está em execução !"
            self.enviarAviso(aviso)
              
  
    #Funções Movimentos
    
    def buttonsLevantarOn(self):
            self.btn1x1.setEnabled(True)
            self.btn1x2.setEnabled(True)
            self.btn1x3.setEnabled(True)
            self.btn2x1.setEnabled(True)
            self.btn2x2.setEnabled(True)
            self.btn2x3.setEnabled(True)
            self.btn3x2.setEnabled(True)
            self.btn3x3.setEnabled(True)
            self.btn4x1.setEnabled(True)
            self.btn4x2.setEnabled(True)
            self.btnGB3x1.setEnabled(True)
            self.btnGB4x1.setEnabled(True)
            return
        
    def levantar(self):
        try:            
            # motion = ALProxy("ALMotion",self.robotIP,9559)
            self.motion.post.wakeUp()
            self.motion.post.setBreathEnabled("Body",True)
            self.buttonsLevantarOn()

            aviso = "AVISO: Comando Levantar enviado com sucesso."
            self.enviarAviso(aviso)
        except BaseException:
            aviso = "ERROR:Falha na execução do comando levantar."
            self.enviarAviso(aviso)
            
    def buttonsSentarOff(self):
            self.btn1x1.setEnabled(False)
            self.btn1x2.setEnabled(False)
            self.btn1x3.setEnabled(False)
            self.btn2x1.setEnabled(False)
            self.btn2x2.setEnabled(False)
            self.btn2x3.setEnabled(False)
            self.btn3x2.setEnabled(False)
            self.btn3x3.setEnabled(False)
            self.btn4x1.setEnabled(False)
            self.btn4x2.setEnabled(False)
            self.btnGB3x1.setEnabled(False)
            self.btnGB4x1.setEnabled(False)
            return
                  
    def sentar(self):
        try:            
            # motionProxy = ALProxy("ALMotion",self.robotIP,9559)
            self.motion.post.rest()
            self.buttonsSentarOff()

            aviso = "AVISO: Comando Sentar enviado com sucesso."
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
            self.movimento(concordar.Concordar)
            self.btn1x1.setEnabled(True)
    def discordar(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn1x2.setEnabled(False)
            self.movimento(discordar.Discordar)
            self.btn1x2.setEnabled(True)
    def nossa(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn1x3.setEnabled(False)
            self.movimento(nossa.Nossa)
            self.btn1x3.setEnabled(True)
    def comemorar(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn2x1.setEnabled(False)        
            self.movimento(comemorar.Comemorar)
            self.btn2x1.setEnabled(True)
    def empatia(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn2x2.setEnabled(False)
            self.movimento(empatia.Empatia)
            self.btn2x2.setEnabled(True)
    def duvida(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn2x3.setEnabled(False)
            self.movimento(duvida.Duvida)
            self.btn2x3.setEnabled(True)
    def palmas(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn3x2.setEnabled(False)
            self.movimento(palmas.Palmas)
            self.btn3x2.setEnabled(True)
    def tocaqui(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn3x3.setEnabled(False)
            self.movimento(toca_aqui.TocaAqui)
            self.btn3x3.setEnabled(True)
    def tchau(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn4x1.setEnabled(False)
            self.movimento(tchau.Tchau)
            self.btn4x1.setEnabled(True)
    def beijos(self):
        if (self.BtnConn.text() == "Conectar") or (self.btnGB1x1.text() == "Iniciar Vida"):
            return
        else:
            self.btn4x2.setEnabled(False)
            self.motion.wakeUp()
            self.movimento(beijos.Beijos)
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
    