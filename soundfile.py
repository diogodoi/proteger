# -*- encoding: UTF-8 -*-

import sys
import time
from naoqi import ALProxy

IP = "192.168.137.54"
PORT = 9559
videoRecorderProxy = ALProxy("ALVideoRecorder", IP, PORT)        
# Video file is saved on the robot in the
# /home/nao/recordings/cameras/ folder.
videoRecorderProxy.stopRecording() 
voiceProxy = ALProxy("ALAudioRecorder",IP,PORT)
voiceProxy.stopMicrophonesRecording()
