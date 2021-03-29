        def faceDetector(self):
        try:
            faceProxy = ALProxy("ALFaceDetection", self.robotIP, self.PORT)
            period = 500
            faceProxy.subscribe("Test_Face", period, 0.0 )
        except Exception:
            aviso = "Erro na criação do faceproxy "
            self.enviarAviso(aviso)
        try:
            memoryProxy = ALProxy("ALMemory", self.robotIP, self.PORT)
            memValue = "FaceDetected"
            val = memoryProxy.getData(memValue) 
        except Exception:
            aviso = "Erro na criação do memory proxy:"
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
        self.aux = self.basic_awareness.isRunning() 
        if (self.aux == False):
            self.basic_awareness.startAwareness()
        Face = False
        while Face !=True:
            Face = self.faceDetector()            
            if (Face == True):
                self.basic_awareness.stopAwareness()
                return
            else:        
                self.olhaPraFrente()
        time.sleep(10)
        face_fun
        # self.TMf = QTimer(self)
        # self.TMf.timeout.connect(self.face_fun)
        # self.TMf.start(10000)