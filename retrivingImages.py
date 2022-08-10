# -*- encoding: UTF-8 -*-
#
# This is a tiny example that shows how to show live images from Nao using PyQt.
# You must have python-qt4 installed on your system.
#

import sys
from PyQt4.QtGui import QWidget, QImage, QApplication, QPainter, QMainWindow
from naoqi import ALProxy
import time
# To get the constants relative to the video.
import vision_definitions
from PIL import Image
import cv2
import numpy as np

from tensorflow.python.keras.models import load_model
# Para salvar o modelo no formato json
from tensorflow.python.keras.models import model_from_json

class NAOimageRetriving(QWidget):
    """
    Tiny widget to display camera images from Naoqi.
    """
    def __init__(self, IP, PORT, CameraID, parent=None):
        """
        Initialization.
        """
        super(QWidget, self).__init__(parent)
        QWidget.__init__(self, parent)
        self._image = QImage()
        self.setWindowTitle('Nao')

        self._imgWidth = 160
        self._imgHeight = 120
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

        self.tempoI = time.strftime("%H:%M:%S", time.gmtime())
        
        arquivo_modelo = 'cnn_expressoes.h5' # referente aos pesos
        arquivo_modelo_json = 'cnn_expressoes.json' # referente a arquitetura da Rede Neural
        
        # Código para recepção do open (carregando o modelo salvo no item 6)
        json_file = open(arquivo_modelo_json, 'r')
        loaded_model_json = json_file.read()
        json_file.close() # liberação de memória 

        # Fazendo a leitura do arquivo json para transformar esse para o modelo Tensorflow
        self.expressoes = ['Medo','Feliz','Triste','Neutro']
        self.loaded_model = model_from_json(loaded_model_json)
        self.loaded_model.load_weights(arquivo_modelo)

        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
        

    def _registerImageClient(self, IP, PORT):
        """
        Register our video module to the robot.
        """
        self._videoProxy = ALProxy("ALVideoDevice", IP, PORT)
        resolution = vision_definitions.kQQVGA  
        colorSpace = vision_definitions.kBGRColorSpace
        self._imgClient = self._videoProxy.subscribe("_client", resolution, colorSpace, 30)

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
        imageWidth = self._alImage[0] # Width.
        imageHeight = self._alImage[1] # Height.
        array = self._alImage[6] # Pixel array.        
        image = np.fromstring(array, np.uint8).reshape(imageHeight, imageWidth, 3 )
        opencvImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        tempoF= time.strftime("%H:%M:%S", time.gmtime()) 
        
        faces = self.face_cascade.detectMultiScale(opencvImage, 1.04, 5)
        frame = 0
        lista_frames = []
        
        if len(faces) == 0:
                    pass
        else:
            for x,y,w,h in faces:
                # cv2.rectangle(naoImage,(x,y),(x+w, y+h),(0,255,0),1)
                roi_gray = opencvImage[y:y+h,x:x+w]
                resized = cv2.resize(roi_gray, (160, 160))
                roi_gray = resized.astype('float')/255
                if frame%5 == 0:
                    lista_frames.append(roi_gray)
                try:                        
                    prediction = self.loaded_model.predict(np.array(lista_frames)) 
                    emotion = self.expressoes[int(np.argmax(prediction[-1]))]
                    cv2.putText(opencvImage,emotion , (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
                    legenda=time.strftime("%H-%M-%S", time.gmtime())
                    cv2.imwrite('./imagensSessao/Frame'+legenda+'_'+emotion+'.png',opencvImage)#Path to save your image
                except:
                    pass 
        cv2.putText(opencvImage,"Inicio: "+self.tempoI,(5,10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.putText(opencvImage,"Hora: "+tempoF,(5,20), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1, cv2.LINE_AA)
        self._image =  QImage(opencvImage,           # Pixel array.
                             self._alImage[0],           # Width.
                             self._alImage[1],           # Height.
                             QImage.Format_RGB888)
        
        # print(type(self._image))


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
        
        
        
   


if __name__ == '__main__':
    IP = "192.168.0.141"  # Replace here with your NaoQi's IP address.
    PORT = 9559
    CameraID = 0


    app = QApplication(sys.argv)
    myWidget = NAOimageRetriving(IP, PORT, CameraID)
    myWidget.show()
    sys.exit(app.exec_())