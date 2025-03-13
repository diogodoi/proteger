# -*- encoding: UTF-8 -*-
#
# This is a tiny example that shows how to show live images from Nao using PyQt.
# You must have python-qt4 installed on your system.
#

from datetime import datetime, timedelta
import sys
from PyQt4.QtGui import QWidget, QImage, QApplication, QPainter
from naoqi import ALProxy
import time
# To get the constants relative to the video.
import vision_definitions
import cv2
import numpy as np


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
        
        self.noSignal = cv2.imread('./imagens/NOSIGNAL.png')
        

    def _registerImageClient(self, IP, PORT):
        """
        Register our video module to the robot.
        """
        self._videoProxy = ALProxy("ALVideoDevice", IP, PORT)
        resolution = vision_definitions.kVGA  
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
        try:
            self._alImage = self._videoProxy.getImageRemote(self._imgClient)
            imageWidth = self._alImage[0] # Width.
            imageHeight = self._alImage[1] # Height.
            array = self._alImage[6] # Pixel array.        
            image = np.fromstring(array, np.uint8).reshape(imageHeight, imageWidth, 3 )
            opencvImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)                                    
             
        except: opencvImage = self.noSignal
        self._image =  QImage(opencvImage,           # Pixel array.
                             640,           # Width.
                             480,           # Height.
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
        
        
        
   