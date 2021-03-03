# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:57:08 2021

@author: gbera

Este programa faz o robô buscar o humano e quando encontra
nada faz e encerra o programa.

Se não encontra o humano, o robô movimenta sua cabeça para frente, pois tem maior
chance de encontrar uma face, e diz, faz nova tentativa no proximo loop
caso encontre, encerra o programa.

O robô faz 5 tentativas para encontrar o humano.

Germano Beraldo Filho 19/02/2021, enviado ao Diogo para ser inserido
na Interface do Proteger.


"""


import time

from naoqi import ALProxy

IP = "192.168.137.219"  # Replace here with your NaoQi's IP address.
PORT = 9559
tts = ALProxy("ALTextToSpeech", IP, PORT)
motion = ALProxy("ALMotion", IP, PORT)
# Create a proxy to ALFaceDetection
try:
  faceProxy = ALProxy("ALFaceDetection", IP, PORT)
except Exception, e:
  print "Error when creating face detection proxy:"
  print str(e)
  exit(1)

# Subscribe to the ALFaceDetection proxy
# This means that the module will write in ALMemory with
# the given period below
period = 500
tentativas = 5

def olhaPraFrente():

# Choregraphe simplified export in Python.

    names = list()
    times = list()
    keys = list()
    
    names.append("HeadPitch")
    times.append([0.52, 1.04])
    keys.append([0.0950661, 0.0950661])
    
    names.append("HeadYaw")
    times.append([0.52, 1.04])
    keys.append([0.0229681, 0.0229681])
    
    try:
      #uncomment the following line and modify the IP if you use this script outside Choregraphe.
      #motion = ALProxy("ALMotion", IP, PORT)
      #motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err
 

faceProxy.subscribe("Test_Face", period, 0.0 )

# ALMemory variable where the ALFacedetection modules
# outputs its results
memValue = "FaceDetected"

# Create a proxy to ALMemory
try:
  memoryProxy = ALProxy("ALMemory", IP, PORT)
except Exception, e:
  print "Error when creating memory proxy:"
  print str(e)
  exit(1)


# A simple loop that reads the memValue and checks whether faces are detected.
for i in range(0, tentativas):  # default 0 a 20
  #time.sleep(0.5)
  val = memoryProxy.getData(memValue)

  print ""
  print "*****"
  print ""

  # Check whether we got a valid output.
  if(val and isinstance(val, list) and len(val) >= 2):

    # We detected faces !
    # For each face, we can read its shape info and ID.

    # First Field = TimeStamp.
    timeStamp = val[0]

    # Second Field = array of face_Info's.
    faceInfoArray = val[1]

    try:
      # Browse the faceInfoArray to get info on each detected face.
      
      for j in range( len(faceInfoArray)-1 ):
        faceInfo = faceInfoArray[j]

        # First Field = Shape info.
        faceShapeInfo = faceInfo[0]

        # Second Field = Extra info (empty for now).
        faceExtraInfo = faceInfo[1]
    
        #print "  alpha %.3f - beta %.3f" % (faceShapeInfo[1], faceShapeInfo[2])
        #print "  width %.3f - height %.3f" % (faceShapeInfo[3], faceShapeInfo[4])
    
        print " Face detectada"
        #tts.say("Achei")
        break
    except Exception, e:
      print "Face detectada, sem dados de posição"
      
  else:
      print "Face não detectada, virar rosto para frente"
      #tts.say("Sumiu")
      olhaPraFrente()


# Unsubscribe the module.
faceProxy.unsubscribe("Test_Face")

#print "Teste terminado com  successo."
#tts.say("Terminei")