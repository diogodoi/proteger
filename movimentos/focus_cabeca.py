from naoqi import ALProxy
class Focus():
    def __init__(self,IP,PORT):
        self.IP = IP
        self.PORT = PORT

        
        try:
            self.motionProxy = ALProxy("ALMotion",self.IP,self.PORT)
        except Exception,e:
            pass
    
    def faceDetector(self):
        try:
            self.faceProxy = ALProxy("ALFaceDetection", self.IP, self.PORT)
            self.period = 500
            self.faceProxy.subscribe("Test_Face", self.period, 0.0 )
        except Exception, e:
            print "Error when creating face detection proxy:"
            print str(e)
            exit(1) 
        
        try:
            self.memoryProxy = ALProxy("ALMemory", self.IP,self.PORT)
            self.memValue = "FaceDetected"
            val = self.memoryProxy.getData(self.memValue) 
        except Exception, e:
            print "Error when creating memory proxy:"
            print str(e)
            exit(1)

       
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

                            print "  alpha %.3f - beta %.3f" % (faceShapeInfo[1], faceShapeInfo[2])
                            print "  width %.3f - height %.3f" % (faceShapeInfo[3], faceShapeInfo[4])
                            return True

            except Exception, e:
                    print "faces detected, but it seems getData is invalid. ALValue ="
                    print val
                    print "Error msg %s" % (str(e))
        else:
                print "No face detected"
                return False
        self.faceProxy.unsubscribe("Test_Face")
        
    
    def grauZero(self):

        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.84])
        keys.append([0.00149202])

        names.append("HeadYaw")
        times.append([0.84])
        keys.append([-0.0061779])


        return names,times, keys

    def esquerda25(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.84])
        keys.append([0.00302601])

        names.append("HeadYaw")
        times.append([0.84])
        keys.append([0.44175])
        
        return names,times,keys

    def esquerda50(self):

        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.84])
        keys.append([0.00302601])

        names.append("HeadYaw")
        times.append([0.84])
        keys.append([0.875872])


        return names,times,keys

    def esquerda75(self):

        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.84])
        keys.append([0.00302601])

        names.append("HeadYaw")
        times.append([0.84])
        keys.append([1.309])

        return names,times,keys

    def direita25(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.84])
        keys.append([0.00302601])

        names.append("HeadYaw")
        times.append([0.84])
        keys.append([-0.44175])

        return names,times,keys

    def direita50(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.84])
        keys.append([0.00302601])

        names.append("HeadYaw")
        times.append([0.84])
        keys.append([-0.875872])

        return names,times,keys

    def direita75(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.84])
        keys.append([0.00302601])

        names.append("HeadYaw")
        times.append([0.84])
        keys.append([-1.309])

        return names,times,keys

    def faceDetecting(self):
        listaMov = [self.esquerda25,self.esquerda50,self.direita25,self.direita50,self.esquerda75,self.direita75]        
        Face = False        
        while (Face!=True):
            for item in listaMov:
                names, times, keys = item()
                # self.motionProxy.wakeUp()
                Face = self.faceDetector()
                if (Face == True):                                   
                    return
                else:
                    self.motionProxy.angleInterpolation(names, keys, times, True)
                


                
        # self.motionProxy.setBreathConfig([['Bpm', 20.0], ['Amplitude', 0.3]])
        # self.motionProxy.setBreathEnabled('Body',True)

ip = "192.168.137.183"
port = 9559

teste = Focus(ip,port)
teste.faceDetecting()

        



        
            

        




        
