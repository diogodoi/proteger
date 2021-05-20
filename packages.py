from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QTableWidgetItem, QWidget, QImage, QApplication, QPainter,QFileDialog, QDialog,QWidget,QTableView
from PyQt4.QtCore import QTimer, QBasicTimer, QObject, Qt,QThread, pyqtSignal
from naoqi import ALProxy, ALBroker, ALModule
# from avRecording import VideoRecorder,AudioRecorder,start_audio_recording,start_AVrecording,start_video_recording,file_manager,stop_AVrecording
from movimentos import beijos,comemorar,concordar,nossa,duvida,discordar,empatia,palmas,tchau,toca_aqui,focus,arm_pose, fengshui
import vision_definitions
import sys
import sqlite3
import time
import threading
import pysftp
import subprocess
import random

