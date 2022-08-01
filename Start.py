# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import os
import sqlite3

from interface import Ui_MainWindow
import sys

class interface(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        

if __name__ == "__main__":
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
    try:
        os.mkdir("imagensSessao")       
    except:
        pass
    
    app = QtGui.QApplication(sys.argv)
    window = interface()
    window.show()
    sys.exit(app.exec_())