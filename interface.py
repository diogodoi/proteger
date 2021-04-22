# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QTableWidgetItem, QWidget, QImage, QApplication, QPainter,QFileDialog, QDialog,QWidget,QTableView
from PyQt4.QtCore import QTimer, QBasicTimer, QObject, Qt,QThread, pyqtSignal
from naoqi import ALProxy, ALBroker, ALModule
# from avRecording import VideoRecorder,AudioRecorder,start_audio_recording,start_AVrecording,start_video_recording,file_manager,stop_AVrecording
from movimentos import beijos,comemorar,concordar,nossa,duvida,discordar,empatia,palmas,tchau,toca_aqui,focus,arm_pose
import vision_definitions
import sys
import sqlite3
import time
import threading
import pysftp
import subprocess
import random


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
nomeS = ""
pastaS = ""
class Ui_MainWindow(object):
    def __init__(self):
        self.val_ip = ""
        self.aux = False
        
        self.AuxLeds = False
        self.pasta = ""
        self.robotIP = ""
        self.PORT = 9559
        self.bateria = ""
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))        
        
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/02.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("""
                        QPushButton{ background:#FFF;
                                    border-radius:15px;
                                    font:16px;                                
                                 }
                        QPushButton:hover{ background-color:#F79F81;                   
                        }         
                        color: darkgreen;
                        background:#F1F8E0;
                        border-radius:15px;     
                          """)        
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

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
        self.Menu.setStyleSheet("""                                
                                font:16px;
                                border-radius:15px;
                                border:2px solid darkgreen;
                                """)
        self.gridMenu = QtGui.QGridLayout(self.Menu)
        self.gridMenu.setObjectName(_fromUtf8("gridMenu"))
        self.Menu.setMinimumSize(200,200)
        self.Menu.setMaximumSize(500,500)
        
        self.label_Ip = QtGui.QLabel(self.Menu)        
        self.label_Ip.setObjectName(_fromUtf8("label_Ip"))
        self.label_Ip.setStyleSheet("border:None")
        self.gridMenu.addWidget(self.label_Ip, 0, 1, 1, 1)        
      
        self.inputIP = QtGui.QLineEdit(self.Menu)                        
        self.inputIP.setObjectName(_fromUtf8("inputIP"))
        self.gridMenu.addWidget(self.inputIP, 0, 2, 1, 1)       
              
        self.BtnConn = QtGui.QPushButton(self.Menu)               
        self.BtnConn.setObjectName(_fromUtf8("BtnConn"))
        self.BtnConn.setStyleSheet("""
                                   QPushButton#hover {
                                       background:#F5F6CE;
                                   }
                                background:#FFF;
                                border:None;     
                                   """)
        self.gridMenu.addWidget(self.BtnConn, 1, 2, 1, 1)
        
        self.BtnNaoView = QtGui.QPushButton(self.Menu)        
        self.BtnNaoView.setObjectName(_fromUtf8("BtnNaoView"))
        self.BtnNaoView.setEnabled(False)
        self.BtnNaoView.setStyleSheet("""
                                   QPushButton#hover {
                                       background:#F5F6CE;
                                   }
                                background:#FFF;
                                border:None;     
                                   """)
        self.gridMenu.addWidget(self.BtnNaoView, 2, 2, 1, 1)
       
        self.BtnEnc = QtGui.QPushButton(self.Menu)        
        self.BtnEnc.setObjectName(_fromUtf8("BtnEnc"))
        self.BtnEnc.setEnabled(False)
        self.BtnEnc.setStyleSheet("border:None;")
        self.gridMenu.addWidget(self.BtnEnc, 3, 2, 1, 1)
        

        #### BOX MOVIMENTOS
        self.Movimentos = QtGui.QGroupBox(self.centralwidget)        
        self.Movimentos.setObjectName(_fromUtf8("Movimentos"))
        self.Movimentos.setStyleSheet("""
                                        border:2px dotted darkgreen;
                                        border-radius:15px;
                                        font:16px;

                                        
                                        """)
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
        
        # self.btn4x3 = QtGui.QPushButton(self.Movimentos)
        # self.btn4x3.setObjectName(_fromUtf8("btn4x3"))
        # self.gridLayout_2.addWidget(self.btn4x3, 3, 8, 1, 1)
        
        ##AREA DE AVISOS
        self.Avisos = QtGui.QGroupBox(self.centralwidget)
        self.Avisos.setObjectName(_fromUtf8("Avisos"))
        self.Avisos.setStyleSheet("""
                                  font:20px;                                  
                                  font-weight: bold;
                                  color:#FF0000;
                                  """)
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
        self.logo_Unesp.resize(100,60)
        self.logo_Unesp.setMaximumSize(100,60)              
        self.logo_Unesp.setText(_fromUtf8(""))
        self.logo_Unesp.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/unesp-full-center.png")))
        self.logo_Unesp.setScaledContents(True)
        self.logo_Unesp.setObjectName(_fromUtf8("logo_Unesp"))
        self.gridAvisos.addWidget(self.logo_Unesp, 3, 5, 1, 1)
        
       #Gravação
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox.setStyleSheet("""
                                    QGroupBox {
                                        padding-top:10px;
                                        };
                                    border:2px dotted darkgreen;
                                    border-radius:10px;                                      
                                    font:16px;
                                    """)        
        self.gridLayout_GB = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_GB.setObjectName(_fromUtf8("gridLayout_GB"))
        
        
        self.groupBox.setMinimumSize(200,200)
        self.groupBox.setMaximumSize(500,500)
        
        # self.label_id = QtGui.QLabel(self.groupBox)
        # self.label_id.setObjectName(_fromUtf8("label_id"))
        # self.label_id.setStyleSheet("border:None")
        # self.gridLayout_GB.addWidget(self.label_id, 0, 1, 1, 1)
        
        # self.inputIDC = QtGui.QLineEdit(self.groupBox)
        # self.inputIDC.setObjectName(_fromUtf8("inputIDC"))
        # self.inputIDC.setEnabled(False)
        # self.inputIDC.setStyleSheet(_fromUtf8("background:#A4A4A4;\n" "\n" ""))
        # self.gridLayout_GB.addWidget(self.inputIDC, 0, 2, 1, 1)
        
        # self.label_dir = QtGui.QLabel(self.groupBox)
        # self.label_dir.setObjectName(_fromUtf8("label_dir"))
        # self.label_dir.setStyleSheet("border:None")
        # self.gridLayout_GB.addWidget(self.label_dir, 1, 1, 1, 1)
        
        # self.inputDir = QtGui.QLineEdit(self.groupBox)
        # self.inputDir.setEnabled(True)
        # self.inputDir.setStyleSheet(_fromUtf8("background:#A4A4A4;\n" "\n" ""))
        # self.inputDir.setText(_fromUtf8(""))
        # self.inputDir.setReadOnly(True)
        # self.inputDir.setObjectName(_fromUtf8("inputDir"))
        # self.gridLayout_GB.addWidget(self.inputDir, 1, 2, 1, 1)
        
        # self.BtnDir = QtGui.QPushButton(self.groupBox)
        # self.BtnDir.setObjectName(_fromUtf8("BtnConn"))
        # self.BtnDir.setStyleSheet(_fromUtf8("""
        #                                     QPushButton {                                                
        #                                         background-image: url(imagens/dir.png);
        #                                         background-repeat: no-repeat;
        #                                         border:None;
        #                                         border-radius:15px;
        #                                         background-color:#F1F8E0;
                                                
        #                                     }
        #                                     QPushButton:hover{
        #                                         padding:2px;
        #                                         background-image: url(imagens/dir.png);
        #                                         background-repeat: no-repeat;
        #                                         background-color:#F79F81;
        #                                         border-radius:15px;
        #                                     }
        #                                     """))
        # self.gridLayout_GB.addWidget(self.BtnDir, 1, 3, 1, 1) 
        
        # self.label_sessao = QtGui.QLabel(self.groupBox)       
        # self.label_sessao.setObjectName(_fromUtf8("label_sessao"))
        # self.label_sessao.setStyleSheet("border:None")
        # self.gridLayout_GB.addWidget(self.label_sessao, 2, 1, 1, 1)
        
        # self.inputSessao = QtGui.QLineEdit(self.groupBox)
        # self.inputSessao.setEnabled(True)                      
        # self.inputSessao.setStyleSheet(_fromUtf8("background:#A4A4A4;\n" "\n" ""))
        # self.inputSessao.setText(_fromUtf8(""))
        # self.inputSessao.setReadOnly(True)
        # self.inputSessao.setObjectName(_fromUtf8("inputSessao"))
        # self.gridLayout_GB.addWidget(self.inputSessao, 2, 2, 1, 1)  
        
        self.btnGB1x1 = QtGui.QPushButton(self.groupBox)
        self.btnGB1x1.setObjectName(_fromUtf8("btnGB1x1"))
        
        self.gridLayout_GB.addWidget(self.btnGB1x1, 1, 1, 1, 2)
        
        self.btnGB2x1 = QtGui.QPushButton(self.groupBox)
        self.btnGB2x1.setObjectName(_fromUtf8("btnGB2x1"))
        
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
        # self.btn4x3.clicked.connect(self.focus)
        #Botão Emergência
        self.EMG.clicked.connect(self.desligar)
        
        #Botões Sessão
        # self.BtnDir.clicked.connect(self.getDir)
        self.btnGB1x1.clicked.connect(self.startNaoRecording)        
        self.btnGB2x1.clicked.connect(self.stopNaoRecording)
        self.btnGB3x1.clicked.connect(self.virarDireita)
        self.btnGB4x1.clicked.connect(self.virarEsquerda)

        
        #Recupera o ultimo ip adicionado na lista.
        self.inputIP.setText(last_ip)
        #Cria uma lista para completar ip
        completerip = QtGui.QCompleter(lista_ip)
        completerip.setCompletionMode(2)
        self.inputIP.setCompleter(completerip)
 
        #Posições das box em grid
        # self.gridMain.addWidget(self.menubar, 0, 1, 1, 2)
        self.gridMain.addWidget(self.Menu, 1, 1, 1, 1)
        self.gridMain.addWidget(self.groupBox,2,1,1,1)
        self.gridMain.addWidget(self.Movimentos, 1, 2, 2, 1)
        self.gridMain.addWidget(self.EMG, 3, 1, 1, 2)        
        self.gridMain.addWidget(self.Avisos, 4, 1, 1, 2)                        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)    
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "GUIPsyin - Interface Gráfica de Interação Psicológica Infantil ", None))
                        
        #menu
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))        
        self.actionSobre.setText(_translate("MainWindow", "Sobre", None))
        self.Menu.setTitle(_translate("MainWindow", "Configurações", None))
        # self.label_id.setText(_translate("MainWindow", "ID Criança", None))
        self.label_Ip.setText(_translate("MainWindow", "IP Robô", None))
        # self.label_sessao.setText(_translate("MainWindow", "ID Sessão", None))
        # self.label_dir.setText(_translate("MainWindow", "Diretório", None))
        self.BtnConn.setText(_translate("MainWindow", "Conectar", None))
        self.BtnEnc.setText(_translate("MainWindow", "Desconectar", None))
        
        #Avisos
        self.label_avisos.setText(_translate("MainWindow", "Avisos", None))
        
        #Gravação
        self.groupBox.setTitle(_translate("ChatWindow", "Sessão", None))
        self.btnGB1x1.setText(_translate("MainWindow", "Iniciar Vida", None))
        self.btnGB2x1.setText(_translate("MainWindow", "Encerrar Vida", None))
        self.BtnNaoView.setText(_translate("MainWindow", "Câmera NAO", None))
        self.btnGB3x1.setText(_translate("MainWindow","Girar para direita",None))
        self.btnGB4x1.setText(_translate("MainWindow","Girar para esquerda",None))
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
        # self.btn4x3.setText(_translate("MainWindow", "Focar", None))
        
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hora", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mensagens", None))
        self.EMG.setText(_translate("MainWindow", "DESLIGAR/EMERGÊNCIA", None))        
    
    #Funções complementares
    
    def gera_id_sessao(self):
        val = str(_fromUtf8(self.inputIDC.text()))
        t = time.localtime()
        id_da_sessao = time.strftime("%Y%m%d"+ "_" + val , t)        
        self.inputSessao.setText(str(id_da_sessao))
        self.inputSessao.setEnabled(False)
        global nomeS
        nomeS = id_da_sessao        
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
            self.proxyBattery = ALProxy("ALBattery",self.robotIP,self.PORT)
            self.bateria = self.proxyBattery.post.getBatteryCharge()
            self.motion = ALProxy("ALMotion", self.robotIP, self.PORT)
            self.posture = ALProxy("ALRobotPosture", self.robotIP, self.PORT)
            self.bateria = str(self.bateria)
            self.BatThread = QThread()
            self.BatThread.started.connect(self.nivelBateria)
            self.BatThread.start()
            aviso = "AVISO: Conexão estabelecida com "+self.robotIP+" bateria "+ self.bateria +"%"+ " carregada."
            self.enviarAviso(aviso)
        except BaseException:
            aviso = "ERROR: Falha na conexão com "+ self.robotIP +"."
            self.enviarAviso(aviso)
            return
        try:
            self.basic_awareness = ALProxy("ALBasicAwareness", self.robotIP, self.PORT)
            self.motion = ALProxy("ALMotion", self.robotIP, self.PORT)
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
            self.BtnConn.setStyleSheet("background-color:#40FF00;") 
            # self.inputIDC.setEnabled(True)
        except BaseException:
            aviso = "ERROR: Falha na configuração."
            self.enviarAviso(aviso)
            return

    def desconectar(self):
        try:            
            self.BatThread.exit()
        except BaseException:
            aviso = "ERROR:Falha ao encerrar thread nível de bateria."
            self.enviarAviso(aviso) 
        # try:
        #     if self.jan != None:            
        #         self.jan.destroy()
        #         self.jan = None
        # except BaseException:
        #     aviso = "ERROR:Falha ao fechar janelas."
        #     self.enviarAviso(aviso)        
        try:
            self.salva_log()
        except BaseException:
            aviso = "ERROR:Falha ao salvar log."
            self.enviarAviso(aviso) 
        try:           
            # self.desligar()
            self.robotIP = ""
            self.BtnConn.setText("Conectar")
            self.BtnConn.setEnabled(True)
            self.BtnEnc.setEnabled(False)
            # self.inputSessao.setEnabled(True)
            self.BtnNaoView.setEnabled(False)
            # self.inputIDC.setEnabled(False)
            self.BtnConn.setStyleSheet("background:#FFF;border:None;")
            aviso = "AVISO: Sessão encerrada com sucesso."
            self.enviarAviso(aviso)                  
        except BaseException:
            aviso = "ERROR: Falha na conexão com o robô."
            self.enviarAviso(aviso)            
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
                    aviso = "faces detected, but it seems getData is invalid. ALValue ="
                    self.enviarAviso(aviso)
        else:
            return False
        faceProxy.unsubscribe("Test_Face")
    def face_fun(self):
        Face = self.faceDetector()
        self.aux = self.basic_awareness.isAwarenessRunning()
        # if (Face == True):
        #     self.faceThread.exit()             
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
      
    def naoVideoRecording(self):        
        filename = self.gera_id_sessao()
        videoRecorderProxy = ALProxy("ALVideoRecorder", self.robotIP, self.PORT)
        voiceProxy = ALProxy("ALAudioRecorder",self.robotIP,self.PORT)

        videoRecorderProxy.setResolution(2)
        videoRecorderProxy.setFrameRate(24)
        videoRecorderProxy.setVideoFormat("MJPG")
        videoRecorderProxy.post.startRecording("/home/nao/recordings/cameras", str(filename)+"_NAO")
        voiceProxy.post.startMicrophonesRecording("/home/nao/recordings/cameras/"+str(filename)+"_NAO.wav",
                                             "wav",
                                             48000,
                                             [0,0,1,0])
    def stopVideoRecording(self):               
        videoRecorderProxy = ALProxy("ALVideoRecorder", self.robotIP, self.PORT)
        voiceProxy = ALProxy("ALAudioRecorder",self.robotIP,self.PORT)
        voiceProxy.post.stopMicrophonesRecording()
        videoRecorderProxy.post.stopRecording()                
       
    def nivelBateria(self):
        status = ""
        status = self.proxyBattery.post.getBatteryCharge()
        self.bateria = str(status)
        if status <= 30:
            aviso = "AVISO: Nível baixo de bateria: "+ status+ " % "+ "restantes."
            self.enviarAviso(str(aviso))
            
        self.TMb = QTimer(self)
        self.TMb.timeout.connect(self.nivelBateria)
        self.TMb.start(180000)
    
    def newTreadVision(self):
        self.naovisionThread = QThread()
        self.worker1 = VisionNAO()
        self.worker1.moveToThread(self.naovisionThread)
        self.naovisionThread.started.connect(self.worker1.naoVision)
        self.worker1.finished.connect(self.naovisionThread.quit)
        self.worker1.finished.connect(self.worker1.deleteLater)
        self.naovisionThread.finished.connect(self.naovisionThread.deleteLater)        
        self.naovisionThread.start()
        
    def newTreadFiles(self):
        self.filesThread = QThread()
        self.worker = ConexaoSftp()
        self.worker.moveToThread(self.filesThread)
        self.filesThread.started.connect(self.worker.getfiles)
        self.worker.finished.connect(self.filesThread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.filesThread.finished.connect(self.filesThread.deleteLater)        
        self.filesThread.start()   
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
    def getDir(self):
        folder = QFileDialog.getExistingDirectory(self,"Selecione um pasta para salvar o video.")            
        if folder != None:
            self.pasta = str(folder)
            global pastaS
            pastaS = self.pasta
            self.inputDir.setText(self.pasta)
            
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
        for name in names:
            leds.post.on(name)
        motion = ALProxy("ALMotion", self.robotIP, self.PORT)
        motion.post.wakeUp()
        # motion.post.goToPosture("Stand",0.3)
        motion.post.setBreathEnabled("Body",True)
    
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
        # try:
        #     if (self.inputIDC.text() != ""):
        #         IDC = self.inputIDC.text()
        #         aviso = "AVISO: ID " + IDC + " criado com sucesso."
        #         aviso = str(aviso)
        #         self.enviarAviso(aviso)
        # except BaseException:
        #     aviso = "ERROR: Campo ID Criança precisa ser preenchido."
        #     self.enviarAviso(aviso)
        #     return
        # try:
        #     if (self.pasta != ""):
        #         pass 
        # except BaseException:
        #         aviso = "AVISO: Nenhuma pasta foi selecionada."
        #         self.enviarAviso(aviso)
        #         return
        try:
            self.startLife()
            aviso = "AVISO: Iniciando a vida, ligando leds e levantando."
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
        except BaseException:
            aviso = "ERROR: Falha na inicialização do detector de face."
            self.enviarAviso(aviso)
            return 
        # try:
        #     # self.naoVideoRecording()
        #     # aviso = "AVISO: Inicio da gravação do NAO."
        #     # self.enviarAviso(aviso)
        #     self.inputIDC.setEnabled(False)
        #     self.btnGB1x1.setEnabled(False)            
        #     self.btnGB1x1.setStyleSheet("background-color:#40FF00;")
        #     self.btnGB1x1.setText("Gravando...")
        #     self.btnGB2x1.setEnabled(True)
        # except BaseException:
        #     aviso = "ERROR: Falha no incio da gravação do NAO."
        #     self.enviarAviso(aviso)
        #     return    
    def stopNaoRecording(self):
        # try:            
        #     self.stopVideoRecording()
        #     aviso = "AVISO: Fim da gravação do NAO."
        #     self.enviarAviso(aviso)
        # except BaseException:
        #     aviso = "ERROR:Falha ao encerrar a gravação do NAO."
        #     self.enviarAviso(aviso)
        try:
            self.TMf.stop()
            self.ledsOff()          
        except BaseException:
            aviso = "ERROR:Falha ao encerrar detector de face."
            self.enviarAviso(aviso)
            return
            
        # try:            
        #     self.newTreadFiles()
        #     aviso = "AVISO:Início do download dos arquivos."
        #     self.enviarAviso(aviso)
        #     self.btnGB1x1.setEnabled(True)
        #     self.btnGB1x1.setText(_fromUtf8("Iniciar Gravação"))
        #     self.btnGB1x1.setStyleSheet("background:#FFF;border:None;")
        #     self.btnGB2x1.setEnabled(False)
        #     self.inputIDC.setEnabled(True)
        #     self.inputIDC.setText("")  
        # except BaseException:
        #     aviso = "ERROR:Falha no download dos arquivos."
        #     self.enviarAviso(aviso)         
    #Funções Movimentos
    def levantar(self):
        try:            
            motionProxy = ALProxy("ALMotion",self.robotIP,9559)
            motionProxy.post.wakeUp()
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
        if (self.BtnConn.text() == "Conectar"):
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
            self.posture.post.goToPosture("Stand",0.25)
            aviso = "AVISO: Comando "+nomefunc+" enviado com sucesso."
            if (self.btn3x1.text()== "Levantar"):
                self.btn3x1.setText("Sentar")
            self.enviarAviso(str(aviso))
        except BaseException:
            aviso = "ERROR:Falha na execução do comando "+nomefunc+"."
            self.enviarAviso(str(aviso))
            return
    def concordar(self):
        if (self.BtnConn.text() == "Conectar"):
            return
        else:
            self.btn1x1.setEnabled(False)
            self.movimento(concordar.sim)
            self.btn1x1.setEnabled(True)
    def discordar(self):
        if (self.BtnConn.text() == "Conectar"):
            return
        else:
            self.btn1x2.setEnabled(False)
            self.movimento(discordar.nao)
            self.btn1x2.setEnabled(True)
    def nossa(self):
        if (self.BtnConn.text() == "Conectar"):
            return
        else:
            self.movimento(nossa.nossa)
    def comemorar(self):
        if (self.BtnConn.text() == "Conectar"):
            return
        else:        
            self.movimento(comemorar.comemorar)
    def empatia(self):
        if (self.BtnConn.text() == "Conectar"):
            return
        else:
            self.movimento(empatia.empatia)
    def duvida(self):
        if (self.BtnConn.text() == "Conectar"):
            return
        else:
            self.movimento(duvida.duvida)
    def palmas(self):
        if (self.BtnConn.text() == "Conectar"):
            return
        else:
            self.movimento(palmas.palmas)
    def tocaqui(self):
        if (self.BtnConn.text() == "Conectar"):
            return
        else:
            self.movimento(toca_aqui.tocaAqui)
    def tchau(self):
        if (self.BtnConn.text() == "Conectar"):
            return
        else:
            self.movimento(tchau.tchau)
    def beijos(self):
        if (self.BtnConn.text() == "Conectar"):
            return
        else:
            self.motion.wakeUp()
            self.movimento(beijos.beijos)
    
    #extras
    
    def virarDireita(self):
        if (self.BtnConn.text() == "Conectar"):
            return
        else:
            self.motion.wakeUp()
            self.motion.moveInit()
            self.motion.moveTo(0,0,0.1)
    def virarEsquerda(self):
        if (self.BtnConn.text() == "Conectar"):
            return
        else:
            self.motion.wakeUp()
            self.motion.moveInit()
            self.motion.moveTo(0,0,-0.1)
    
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
            self.IP = iprobo
            self.PORT = 9559
            self.CameraID = 0 
            self.jan = ImageWidget(self.IP, self.PORT, self.CameraID)
            self.jan.show()
        except Exception:
            aviso = "ERROR: Falha na conexão com a câmera do NAO."
            print(aviso)

class ConexaoSftp(QObject):
    finished = pyqtSignal()    
       
    def id_sessao(self):        
        idsessao = str(nomeS)
        print(idsessao)        
        return idsessao
    def ipname(self):
        ipsessao = str(iprobo)
        print(ipsessao)        
        return ipsessao
    def getfolder(self):
        return pastaS
        
    def getfiles(self):
        try:
            myHostname = str(self.ipname())
            print(self.ipname())
            myUsername = "nao"
            myPassword = "nao"
            with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
                print("AVISO:Conexão com " + myHostname + " estabelecida com sucesso.")
                # self.enviarAviso(aviso)
                
                filename = self.id_sessao()
                print(filename)
                # Define the file that you want to download from the remote directory
                videopath = '/home/nao/recordings/cameras/'+filename+'_NAO.avi'
                audiopath = '/home/nao/recordings/cameras/'+filename+'_NAO.wav'

                # Define the local path where the file will be saved
                # or absolute "C:\Users\sdkca\Desktop\TUTORIAL.txt"
                localFilePath = self.getfolder()             
                arqWav = localFilePath+"\\"+filename+"_NAO.wav"
                arqAvi = localFilePath+"\\"+filename+"_NAO.avi"                
                if localFilePath != "":
                    try:
                        print("AVISO:Início do download do vídeo e do audio da sessão " + filename +".")
                        # self.enviarAviso(aviso)
                        sftp.get(videopath, arqAvi)
                        sftp.get(audiopath, arqWav)
                        print("AVISO:Video e audio da sessão " + filename + " salvos com sucesso.")
                        # self.enviarAviso(aviso)
                    except BaseException:
                        print "ERROR:Falha no inicio do download dos arquivos."
                        # self.enviarAviso(aviso)
                        sftp.close()
                        return             
                    #print "Muxing"
                    try:
                        print("AVISO:Mixando audio e vídeo.") 
                        # self.enviarAviso(aviso)
                        cmd = "ffmpeg -ac 1 -channel_layout stereo -i " +arqWav+ " -i "+arqAvi+" -pix_fmt yuv420p " +localFilePath+"\\"+filename + "_First.avi"
                        subprocess.call(cmd, shell=True)
                        print("AVISO:Audio e video mixados com sucesso.")
                        # self.enviarAviso(aviso)
                        sftp.remove(videopath)
                        sftp.remove(audiopath)
                        file_manager(filename,localFilePath)
                        sftp.close()
                    except BaseException:
                        print("ERROR:Falha na mixagem do vídeo e audio dos arquivos.")
                        # self.enviarAviso(aviso)
                        sftp.close()
                        return 
        except BaseException:
            print("ERROR:Falha na inicialização do download dos arquivos.")
            # self.enviarAviso(aviso)
            return
          



    