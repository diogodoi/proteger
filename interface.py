# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from naoqi import ALProxy
from movimentos import acenar, beijos,comemorar,concordar,nossa,duvida,discordar, respiracao,standard,palmas,toca_aqui,receberItem,pegaItem,brincadeira_1,brincadeira_2
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


# Conecta ao banco de dados
conn = sqlite3.connect('BdProteger.db')
cursor = conn.cursor()

# Obtém todos os registros da tabela IpRobot
cursor.execute("SELECT IpRobot FROM IpRobot ORDER BY id DESC;")
lista_ip = [registro[0] for registro in cursor.fetchall()]

# Obtém o último registro da tabela IpRobot
cursor.execute("SELECT IpRobot FROM IpRobot ORDER BY id DESC LIMIT 1")
last_ip = str(cursor.fetchone()[0])

# Fecha a conexão com o banco de dados
conn.close()


iprobo = ""
jan = None

class Ui_MainWindow(object):
    def __init__(self):
        self.val_ip = ""
        self.robotIP = ""
        self.PORT = 9559
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setMinimumSize(QtCore.QSize(840, 840))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/02.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("""
                                 QPushButton{
                                     font-size:24px;
                                 };
                                 background-color:#F5F5F5;font:16px;""")               

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
        
        self.label_Ip = QtGui.QLabel(self.Menu)        
        self.label_Ip.setObjectName(_fromUtf8("label_Ip"))
        self.gridMenu.addWidget(self.label_Ip, 0, 1, 1, 1)        
      
        self.inputIP = QtGui.QLineEdit(self.Menu)                        
        self.inputIP.setObjectName(_fromUtf8("inputIP"))
        self.gridMenu.addWidget(self.inputIP, 0, 2, 1, 1)  
        
        self.label_Status = QtGui.QLabel(self.Menu)
        self.label_Status.setObjectName(_fromUtf8("label_status"))
        self.gridMenu.addWidget(self.label_Status,1,1,1,1)
        
        self.label_BarStatus = QtGui.QLabel(self.Menu)
        self.label_BarStatus.setObjectName(_fromUtf8("label_status"))
        self.label_BarStatus.setText("")
        self.label_BarStatus.setStyleSheet("background-color:gray;")
        self.label_BarStatus.setMaximumHeight(30)
        self.gridMenu.addWidget(self.label_BarStatus,1,2,1,1)
        
              
        self.BtnConn = QtGui.QPushButton(self.Menu)               
        self.BtnConn.setObjectName(_fromUtf8("BtnConn"))
        self.BtnConn.setToolTip(_fromUtf8("Faz a conexão com o robô."))
        self.gridMenu.addWidget(self.BtnConn, 2, 1, 1, 2)

        #### BOX MOVIMENTOS
        self.Movimentos = QtGui.QGroupBox(self.centralwidget)        
        self.Movimentos.setObjectName(_fromUtf8("Movimentos"))
        
        
        self.gridLayout_2 = QtGui.QGridLayout(self.Movimentos)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        
        self.btn1x1 = QtGui.QPushButton(self.Movimentos)
        self.btn1x1.setObjectName(_fromUtf8("btn1x1"))
        self.gridLayout_2.addWidget(self.btn1x1, 1, 1, 1, 1)
        self.btn1x1.setToolTip(_fromUtf8("Movimento a cabeça para baixo e para cima."))
        
        self.btn1x2 = QtGui.QPushButton(self.Movimentos)
        self.btn1x2.setObjectName(_fromUtf8("btn1x2"))
        self.gridLayout_2.addWidget(self.btn1x2, 1, 2, 1, 1)
        self.btn1x2.setToolTip(_fromUtf8("Movimenta a cabeça para os lados."))
                        
        self.btn1x3 = QtGui.QPushButton(self.Movimentos)
        self.btn1x3.setObjectName(_fromUtf8("btn1x3"))
        self.gridLayout_2.addWidget(self.btn1x3, 1, 3, 1, 1)
        self.btn1x3.setToolTip(_fromUtf8("Levanta a mão em direção a testa."))
        
        self.btn2x1 = QtGui.QPushButton(self.Movimentos)
        self.btn2x1.setObjectName(_fromUtf8("btn2x1"))
        self.gridLayout_2.addWidget(self.btn2x1, 2, 1, 1, 1)
        self.btn2x1.setToolTip(_fromUtf8("Faz uma dança de comemoração."))
        
        self.btn2x2 = QtGui.QPushButton(self.Movimentos)
        self.btn2x2.setObjectName(_fromUtf8("btn2x2"))
        self.gridLayout_2.addWidget(self.btn2x2, 2, 2, 1, 1)
        self.btn2x2.setToolTip(_fromUtf8("Esconde/Mostra o rosto com as mãos.") )     
        
        self.btn2x3 = QtGui.QPushButton(self.Movimentos)
        self.btn2x3.setObjectName(_fromUtf8("btn2x3"))
        self.gridLayout_2.addWidget(self.btn2x3, 2, 3, 1, 1)
        self.btn2x3.setToolTip(_fromUtf8("Abre os braços em uma posição receptiva."))
                
        self.btn3x1 = QtGui.QPushButton(self.Movimentos)
        self.btn3x1.setObjectName(_fromUtf8("btn3x1"))
        self.gridLayout_2.addWidget(self.btn3x1, 3, 1, 1, 1)
        self.btn3x1.setToolTip(_fromUtf8("Senta ou Levanta."))
        
        self.btn3x2 = QtGui.QPushButton(self.Movimentos)
        self.btn3x2.setObjectName(_fromUtf8("btn3x2"))
        self.gridLayout_2.addWidget(self.btn3x2, 3, 2, 1, 1)
        self.btn3x2.setToolTip(_fromUtf8("Bate palmas."))
                
        self.btn3x3 = QtGui.QPushButton(self.Movimentos)
        self.btn3x3.setObjectName(_fromUtf8("btn3x3"))
        self.gridLayout_2.addWidget(self.btn3x3, 3, 3, 1, 1)
        self.btn3x3.setToolTip(_fromUtf8("Levanta a mão para cumprimentar."))       
        
        
        self.btn4x1 = QtGui.QPushButton(self.Movimentos)
        self.btn4x1.setObjectName(_fromUtf8("btn4x1"))
        self.gridLayout_2.addWidget(self.btn4x1, 4, 1, 1, 1)
        self.btn4x1.setToolTip(_fromUtf8("Acena com a mão direita."))
        
        self.btn4x2 = QtGui.QPushButton(self.Movimentos)
        self.btn4x2.setObjectName(_fromUtf8("btn4x2"))
        self.gridLayout_2.addWidget(self.btn4x2, 4, 2, 1, 1)
        self.btn4x2.setToolTip(_fromUtf8("Envia um beijo."))
        
        
        self.btn4x3 = QtGui.QPushButton(self.Movimentos)
        self.btn4x3.setObjectName(_fromUtf8("btn4x3"))        
        self.gridLayout_2.addWidget(self.btn4x3, 4, 3, 1, 1)
        self.btn4x3.setToolTip(_fromUtf8("Estende a mão esquerda para receber algum item."))
        
        self.btn5x1 = QtGui.QPushButton(self.Movimentos)
        self.btn5x1.setObjectName(_fromUtf8("btn5x1"))
        self.gridLayout_2.addWidget(self.btn5x1,5,1,1,1)
        self.btn5x1.setText(_fromUtf8("Respiração")) 
        self.btn5x1.setToolTip(_fromUtf8("Executa a respiração diafragmática."))
        
        self.Movimentos.setEnabled(False)
        
    
        
        ##AREA DE AVISOS
        self.Avisos = QtGui.QGroupBox(self.centralwidget)
        self.Avisos.setObjectName(_fromUtf8("Avisos"))


        self.gridAvisos = QtGui.QGridLayout(self.Avisos)
        self.gridAvisos.setObjectName(_fromUtf8("gridAvisos"))
        
        self.label_avisos = QtGui.QLabel(self.Avisos)
        self.label_avisos.setObjectName(_fromUtf8("Avisos"))        
        self.label_avisos.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_avisos.setStyleSheet(_fromUtf8("font-size:30px;"))
        self.gridAvisos.addWidget(self.label_avisos, 0, 1, 1, 5)        
      
        self.logo_cti = QtGui.QLabel(self.Avisos)
        self.logo_cti.setMaximumSize(100,60) 
        self.logo_cti.setText(_fromUtf8(""))
        self.logo_cti.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/LogoCTIcampinas.jpeg")))
        self.logo_cti.setScaledContents(True)
        self.logo_cti.setObjectName(_fromUtf8("logo_cti"))
        self.gridAvisos.addWidget(self.logo_cti, 2, 2, 1, 1)
              
        self.logo_icmc = QtGui.QLabel(self.Avisos)
        self.logo_icmc.setMaximumSize(100,60)            
        self.logo_icmc.setText(_fromUtf8(""))
        self.logo_icmc.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/LogoICMC.png")))
        self.logo_icmc.setScaledContents(True)
        self.logo_icmc.setObjectName(_fromUtf8("logo_icmc"))
        self.gridAvisos.addWidget(self.logo_icmc, 2, 3, 1, 1)
        
        self.logo_lar = QtGui.QLabel(self.Avisos)
        self.logo_lar.setMaximumSize(100,60)        
        self.logo_lar.setText(_fromUtf8(""))
        self.logo_lar.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/LogoLars.png")))
        self.logo_lar.setScaledContents(True)
        self.logo_lar.setObjectName(_fromUtf8("logo_lar"))
        self.gridAvisos.addWidget(self.logo_lar, 2, 4, 1, 1)
        
       #sessão
        self.sessionBox = QtGui.QGroupBox(self.centralwidget)
        self.sessionBox.setObjectName(_fromUtf8("sessionBox"))
    
        self.gridLayout_GB = QtGui.QGridLayout(self.sessionBox)
        self.gridLayout_GB.setObjectName(_fromUtf8("gridLayout_GB"))       
        
        self.btnLife = QtGui.QPushButton(self.sessionBox)
        self.btnLife.setObjectName(_fromUtf8("btnLife"))
        self.btnLife.setIcon(QtGui.QIcon('imagens/icons/face_tracker.png'))        
        self.gridLayout_GB.addWidget(self.btnLife, 1, 1, 1, 3)
        self.btnLife.setToolTip(_fromUtf8("Inicia o contato visual com a pessoa."))
        
        self.label_olhar = QtGui.QLabel(self.sessionBox)
        self.label_olhar.setObjectName(_fromUtf8("labelGirar"))
        self.label_olhar.setText(_fromUtf8("Movimentar a cabeça:"))
        self.label_olhar.setAlignment( Qt.AlignVCenter)
        self.label_olhar.setStyleSheet("font:24px;")
        self.gridLayout_GB.addWidget(self.label_olhar, 2, 1, 1, 3)
        
        self.btnGB1x1 = QtGui.QPushButton(self.sessionBox)
        self.btnGB1x1.setObjectName(_fromUtf8("btnGB1x1"))        
        self.gridLayout_GB.addWidget(self.btnGB1x1, 3, 2, 1, 1)
        iconBtgn1x1 = QtGui.QIcon()
        iconBtgn1x1.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/icons/upArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGB1x1.setIcon(iconBtgn1x1)
        self.btnGB1x1.setToolTip(_fromUtf8("Olha para cima."))
        # self.btnGB1x1.setText("Cima")
        
        self.btnGB2x1 = QtGui.QPushButton(self.sessionBox)
        self.btnGB2x1.setObjectName(_fromUtf8("btnGB2x1"))        
        self.gridLayout_GB.addWidget(self.btnGB2x1, 4, 1, 1, 1)
        iconBtgn2x1 = QtGui.QIcon()
        iconBtgn2x1.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/icons/leftArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGB2x1.setIcon(iconBtgn2x1)
        self.btnGB2x1.setToolTip(_fromUtf8("Olha para esquerda."))
        # self.btnGB2x1.setText("Esquerda")
        
        self.btnGB3x1 = QtGui.QPushButton(self.sessionBox)
        self.btnGB3x1.setObjectName(_fromUtf8("btnGB3x1"))        
        self.gridLayout_GB.addWidget(self.btnGB3x1, 4, 3, 1, 1)
        iconBtgn3x1 = QtGui.QIcon()
        iconBtgn3x1.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/icons/rightArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGB3x1.setIcon(iconBtgn3x1)
        self.btnGB3x1.setToolTip(_fromUtf8("Olha para direita."))
        # self.btnGB3x1.setText("Direita")
        
        self.btnGB4x1 = QtGui.QPushButton(self.sessionBox)
        self.btnGB4x1.setObjectName(_fromUtf8("btnGB4x1"))        
        self.gridLayout_GB.addWidget(self.btnGB4x1, 5, 2, 1, 1)
        iconBtgn4x1 = QtGui.QIcon()
        iconBtgn4x1.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/icons/downArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGB4x1.setIcon(iconBtgn4x1)
        self.btnGB4x1.setToolTip(_fromUtf8("Olha para baixo."))
        
        # self.btnGB4x1.setText("Baixo")
        
        self.sessionBox.setEnabled(False)   
                
        ### BOTAO EMERGENCIA
        self.btnRest = QtGui.QPushButton(self.centralwidget)
        self.btnRest.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(0, 0, 150);font-weight:75;font-style:bold;")
        self.btnRest.setObjectName(_fromUtf8("Descansar"))
        self.btnRest.setToolTip(_fromUtf8("Posição de descanso dos braços."))
        MainWindow.setCentralWidget(self.centralwidget)        
        self.btnRest.setMinimumHeight(50)
        
        
        #Botões Configurações
        self.BtnConn.clicked.connect(self.fazerConexao)
        self.btnLife.clicked.connect(self.ligaDesligaEngajamento)


        #Botões Movimentos
        self.btn1x1.clicked.connect(self.concordar)
        self.btn1x2.clicked.connect(self.discordar)
        self.btn1x3.clicked.connect(self.nossa)
        self.btn2x1.clicked.connect(self.comemorar)
        self.btn2x2.clicked.connect(self.esconderRosto)
        self.btn2x3.clicked.connect(self.duvida)
        self.btn3x1.clicked.connect(self.funcSentarLevantar)
        self.btn3x2.clicked.connect(self.palmas)
        self.btn3x3.clicked.connect(self.tocaqui)
        self.btn4x1.clicked.connect(self.acenar)
        self.btn4x2.clicked.connect(self.beijos)
        self.btn4x3.clicked.connect(self.receberItem)
        self.btn5x1.clicked.connect(self.respirar)
        self.btnRest.clicked.connect(self.descansar)
        
        #Botões Sessão
        self.btnGB1x1.clicked.connect(self.moveHeadUp)
        self.btnGB2x1.clicked.connect(self.moveHeadLeft)
        self.btnGB3x1.clicked.connect(self.moveHeadRight)
        self.btnGB4x1.clicked.connect(self.moveHeadDown)
        
        #Recupera o ultimo ip adicionado na lista.
        self.inputIP.setText(last_ip)
        #Cria uma lista para completar ip
        completerip = QtGui.QCompleter(lista_ip)
        completerip.setCompletionMode(2)
        self.inputIP.setCompleter(completerip)
 
        #Posições das box em grid
        self.gridMain.addWidget(self.Menu, 1, 1, 1, 1)
        self.gridMain.addWidget(self.sessionBox,2,1,1,1)
        self.gridMain.addWidget(self.Movimentos, 1, 2, 2, 2)
        self.gridMain.addWidget(self.btnRest, 3, 1, 1, 3)        
        self.gridMain.addWidget(self.Avisos, 4, 1, 1, 3)                        

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
        self.label_Status.setText(_translate("MainWindow","Status:",None))
        #Avisos
        self.label_avisos.setText(_translate("MainWindow", "Bem vindo a GUIPsyin! \n Para iniciar insira o ip do robô em configurações.", None))
        #Sessão
        self.sessionBox.setTitle(_translate("ChatWindow", "Sessão", None))
        self.btnLife.setText(_translate("MainWindow", "Iniciar contato visual", None))
        #Movimentos
        self.Movimentos.setTitle(_translate("MainWindow", "Movimentos", None))
        self.btn1x1.setText(_translate("MainWindow", "Concordar", None))
        self.btn1x2.setText(_translate("MainWindow", "Discordar", None))
        self.btn2x2.setText(_translate("MainWindow", "Esconder", None))
        self.btn2x1.setText(_translate("MainWindow", "Comemorar", None))
        self.btn1x3.setText(_translate("MainWindow", "Nossa", None))
        self.btn3x3.setText(_translate("MainWindow", "Toca aqui", None))
        self.btn2x3.setText(_translate("MainWindow", "Duvida", None))
        self.btn3x2.setText(_translate("MainWindow", "Palmas", None))
        self.btn3x1.setText(_translate("MainWindow", "Sentar", None))
        self.btn4x1.setText(_translate("MainWindow", "Acenar", None))
        self.btn4x2.setText(_translate("MainWindow", "Beijos", None))
        self.btn4x3.setText(_translate("MainWindow", "Receber",None))        
        self.btnRest.setText(_translate("MainWindow", "DESCANSAR", None))        
    
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
        except BaseException:
            aviso = "ERROR: Falha na conexão com "+ self.robotIP +"."            
            return False , aviso
        try:
            self.tracker = ALProxy("ALTracker", self.robotIP, self.PORT)
        except BaseException:
            aviso = "ERROR: Falha na configuração da detecção de Face."
            return False, aviso
        try:
            self.leds = ALProxy("ALLeds", self.robotIP, self.PORT)
        except BaseException:
            aviso = "Error: Falha na configuração dos leds."
            return False, aviso
        try:
            self.posture = ALProxy("ALRobotPosture", self.robotIP, self.PORT)
        except BaseException:
            aviso = "Error: Falha na configuração dos motores."
            return False, aviso
        try:    
            self.salva_ip()
            self.buttonsOn()
        except BaseException:
            aviso = "ERROR: Falha na configuração."
            self.enviarAviso(aviso)
            return False, aviso
        aviso = "AVISO: Conexão com "+self.robotIP+" estabelecida." 
        return True , aviso

    def buttonsOn(self):
        self.BtnConn.setText("Desconectar")
        self.inputIP.setEnabled(False)
        self.btnLife.setEnabled(True)
        self.Movimentos.setEnabled(True)
        self.sessionBox.setEnabled(True)
        self.ledsOn()
        
    def buttonsOff(self):
        self.BtnConn.setText("Conectar")
        self.btnLife.setText("Iniciar contato visual")
        self.inputIP.setEnabled(True)
        self.btnLife.setEnabled(False)        
        self.Movimentos.setEnabled(False)        
        self.sessionBox.setEnabled(False)
        self.ledsOff()
        
    def desconectar(self):
        try:
            self.cameraWindow.close()
            self.cameraWindow = None
        except:
            aviso = "Error: Falha ao encerrar a conexão de video."
            self.enviarAviso(aviso)
            return
        try:
            self.salva_log()
        except BaseException:
            aviso = "ERROR:Falha ao salvar log."
            self.enviarAviso(aviso)
            return 
        try:
            self.motion.rest()
            self.buttonsOff()
            self.robotIP = ""
            self.inputIP.setEnabled(True)
            aviso = "AVISO: Sessão encerrada com sucesso."
            self.enviarAviso(aviso)                  
        except BaseException:
            aviso = "ERROR: Falha na conexão com o robô."
            self.enviarAviso(aviso)
            return            
    
    def fazerConexao(self):
        self.value = str(self.BtnConn.text())
        if self.value == "Conectar":
            self.conn , aviso = self.conexao()
            if self.conn:                
                self.retrivingImage()
                self.enviarAviso(aviso)
                self.label_BarStatus.setStyleSheet("background-color:rgb(0,255,0);")
                self.label_BarStatus.setText("CONECTADO!")
                self.BtnConn.setText("Desconectar")
                # self.motion.setStiffnesses("Body",1.0)
                self.motion.setSmartStiffnessEnabled(True)
                self.posture.post.goToPosture("Stand",0.5)
                # self.motion.setBreathEnabled("Legs",True)
            else:
                self.enviarAviso(aviso)

        else:
            self.desconectar()
            self.label_BarStatus.setStyleSheet("background-color:gray;")
            self.label_BarStatus.setText("")
            
    def enviarAviso(self,aviso):
        if 'ERROR' in aviso:
            self.label_avisos.setStyleSheet("background-color:rgb(255,0,0);font-size:32px;")
            self.label_BarStatus.setStyleSheet("background-color:rgb(255,255,0);")
            self.label_BarStatus.setText(_fromUtf8("Falha na conexão!"))            
            self.buttonsOff()  
        else:
            self.label_avisos.setStyleSheet("background-color:rgb(0,255,0);font-size:32px;")      
        self.label_avisos.setText(_fromUtf8(aviso))        
        conn = sqlite3.connect('BdProteger.db')
        conn.text_factory = str
        self.aviso = aviso
        t = time.localtime()
        Data = str(t.tm_mday) + "/" + str(t.tm_mon) + "/" + str(t.tm_year) 
        hora = str(t.tm_hour) + ":" + str(t.tm_min) + ":" + str(t.tm_sec)
        conn.execute("INSERT INTO Sessao (Data,Hora,Aviso) VALUES(?,?,?);",(Data,hora,self.aviso))
        conn.commit()
    
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
    def descansar(self):
        try:             
            names,times,keys, _ = standard.RestPosition()
            self.motion.post.angleInterpolation(names,keys,times, True) 
            aviso = "AVISO: Comando Descansar enviado com sucesso."
            self.enviarAviso(aviso)
        except BaseException:
            aviso = "ERROR:Falha na execução do comando."
            self.enviarAviso(aviso)
    def ledsOff(self):
        name = "AllLeds"        
        self.leds.post.off(name)
        
    def ledsOn(self):
        name = "AllLeds"
        self.leds.post.on(name)        
     
    def ligaDesligaEngajamento(self):
        self.value = str(self.btnLife.text())
        if self.value == 'Iniciar contato visual':
            conn,aviso = self.ligaEngajamento()
            if conn:
                self.Movimentos.setEnabled(True)
                self.btnLife.setText("Encerrar contato visual")                
                self.enviarAviso(aviso)
            else:
                self.enviarAviso(aviso)
        else:
            conn, aviso = self.desligaEngajamento()
            if conn:
                self.btnLife.setText('Iniciar contato visual')
                self.enviarAviso(aviso)
            else:
                self.enviarAviso(aviso)            
              
    def ligaEngajamento(self):
        try:
            self.faceTracker()
        except BaseException:
            aviso = "ERROR: Falha na ao iniciar o contato visual."
            return False, aviso
        aviso = "AVISO: Contato visual iniciado."
        return True,  aviso

    def desligaEngajamento(self):
        try:
            self.tracker.stopTracker()
            self.tracker.unregisterAllTargets()
        except BaseException:
            aviso = "ERROR:Falha ao encerrar o contato visual."
            return False, aviso
        aviso = "AVISO: Contato visual encerrado com sucesso."
        return True, aviso
    
    def retrivingImage(self):
        try:
            self.cameraWindow  = NAOimageRetriving(self.robotIP, self.PORT, 0)
            self.cameraWindow.show()
            self.buttonEmotionOn()
            # self.cameraWindow.exec_()
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
            self.btn4x3.setEnabled(True)
            self.btn5x1.setEnabled(True)

    def levantar(self):
        try:            
            self.motion.setSmartStiffnessEnabled(True)
            self.posture.post.goToPosture("Stand",0.5)
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
            self.btn4x3.setEnabled(False)
            self.btn5x1.setEnabled(False)
              
    def sentar(self):
        try:            
            self.motion.post.rest()
            self.motion.post.setStiffnesses("Head", 1.0)
            self.buttonsSentarOff()
            aviso = "AVISO: Comando Sentar enviado com sucesso."
            self.enviarAviso(aviso)             
        except BaseException:
            aviso = "ERROR:Falha na execução do comando sentar."
            self.enviarAviso(aviso)
    def funcSentarLevantar(self):
        if (self.btn3x1.text() == "Sentar"):                
            self.sentar()
            self.btn3x1.setText("Levantar")
        else:
            self.levantar()
            self.btn3x1.setText("Sentar")
    def movimento(self,object):
        try:           
            names, times, keys, nome = object()
        except BaseException:
            aviso = "Falha no envio dos dados."
            self.enviarAviso(aviso)
        try:
            self.motion.setSmartStiffnessEnabled(True)
            not_run = ["Toca aqui","Receber","Pegar","Esconder","Achou"]
            if(nome not in not_run):
                self.motion.setBreathEnabled('Legs',False)    
                self.motion.post.angleInterpolation(names, keys, times, True)  
                self.descansar()
                self.motion.setBreathEnabled('Legs',True)
                self.btn2x2.setText("Esconder")
                self.btn4x3.setText("Receber")               
            else:
                self.motion.setBreathEnabled('Legs',False)          
                self.motion.post.angleInterpolation(names, keys, times, True)
            if (self.btn3x1.text()== "Levantar"):
                self.btn3x1.setText("Sentar")
            aviso = "AVISO: Comando "+nome+" enviado com sucesso."
            self.enviarAviso(str(aviso))
        except BaseException:
            aviso = "ERROR:Falha na execução do comando "+nome+"."
            self.enviarAviso(str(aviso))
        
    def concordar(self):
        self.movimento(concordar.Concordar)
    def discordar(self):
        self.movimento(discordar.Discordar)
    def nossa(self):
        self.movimento(nossa.Nossa)
    def comemorar(self):
        self.movimento(comemorar.Comemorar)
    def esconderRosto(self):
        text = self.btn2x2.text()
        if text != "Esconder":
            self.movimento(brincadeira_2.Brincadeira_finished)
            self.btn2x2.setText("Esconder")
        else:
            self.movimento(brincadeira_1.Brincadeira_start)
            self.btn2x2.setText("Achou")
    def duvida(self):
        self.movimento(duvida.Duvida)
    def palmas(self):
        self.movimento(palmas.Palmas)
    def tocaqui(self):
        self.movimento(toca_aqui.TocaAqui)
    def acenar(self):
        self.movimento(acenar.Acenar)
    def beijos(self):
        self.movimento(beijos.Beijos)
    def receberItem(self):
        text = self.btn4x3.text()
        if text == "Receber":
            self.movimento(receberItem.ReceberItem)
            # self.motion.openHand("LHand")
            self.btn4x3.setText(_fromUtf8("Pegar"))
        else:
            self.movimento(pegaItem.PegarItem)
            # self.motion.post.closeHand("LHand")
            self.btn4x3.setText(_fromUtf8("Receber"))
    def respirar(self):
        self.movimento(respiracao.Respiracao)
    #extras    
    def virarDireita(self):
        self.motion.post.moveInit()
        self.motion.post.moveTo(0,0,-0.1)
    def virarEsquerda(self):
        self.motion.post.moveInit()
        self.motion.post.moveTo(0,0,0.1)
    def moveHead(self,ver=None,hor=None):
        if ver != None:
            try:
                self.key = self.motion.getAngles("HeadPitch",False)
                self.motion.post.angleInterpolation("HeadPitch", self.key[0]+ver, 1, True)
                return False, None
            except BaseException:
                aviso = "ERROR: Falha na conexão!"
                return True, aviso
        else:
            try:
                self.key = self.motion.getAngles("HeadYaw",False)
                angle = self.key[0] + hor
                if (angle>=0.8):
                    self.virarEsquerda()
                elif(angle<= -1.2):
                    self.virarDireita()
                else:
                    self.motion.post.angleInterpolation("HeadYaw", angle, 1, True)                    
                return False, None
            except BaseException:
                aviso = "ERROR: Falha na conexão!"
                return True, aviso
    def moveHeadUp(self):        
        conn, aviso = self.moveHead(ver=-0.2)
        if conn:
            self.enviarAviso(aviso)
    def moveHeadDown(self):
        conn, aviso = self.moveHead(ver=0.2)
        if conn:
            self.enviarAviso(aviso)
    def moveHeadLeft(self):
        conn, aviso = self.moveHead(hor=0.2)
        if conn:
            self.enviarAviso(aviso)          
    def moveHeadRight(self):
        conn, aviso = self.moveHead(hor=-0.2)
        if conn:
            self.enviarAviso(aviso)       