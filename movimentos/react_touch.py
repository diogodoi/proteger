from naoqi import ALProxy

import time

ip_robot = "169.254.178.70"
port_robot = 9559

basic_awareness = ALProxy("ALBasicAwareness", ip_robot, port_robot)
motion = ALProxy("ALMotion", ip_robot, port_robot)
def faceDetector(self):
        try:
            faceProxy = ALProxy("ALFaceDetection", ip_robot, port_robot)
            period = 500
            faceProxy.subscribe("Test_Face", period, 0.0 )
        except Exception:
            aviso = "Erro na criação do faceproxy "
            self.enviarAviso(aviso)
        try:
            memoryProxy = ALProxy("ALMemory", ip_robot, port_robot)
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

            except Exception, e:
                    aviso = "faces detected, but it seems getData is invalid. ALValue ="
                    self.enviarAviso(aviso)
        else:
                # print "No face detected"
                return False
        faceProxy.unsubscribe("Test_Face")


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
    
    motion.angleInterpolation(names, keys, times, True)       

def face_fun(self):
    basic_awareness.startAwareness()
    Face = False
    while Face !=True:
        Face = self.faceDetector()            
        if (Face == True):
            basic_awareness.stopAwareness()        
        else:        
            self.olhaPraFrente()
            time.sleep(5)
    time.sleep(5)
    self.face_fun()
    
face_fun()

# class GeneratedClass:
#     pass
# global faces
# faces=0
# class MyClass(GeneratedClass):
#     def _init_(self):
#         GeneratedClass._init_(self)

#     def onLoad(self):
#         try:
#             self.faceC = ALProxy("ALFaceCharacteristics","169.254.178.70",9559)
#         except Exception as e:
#             raise RuntimeError(str(e) + "Make sure you're not connected to a virtual robot." )
#         self.confidence = self.getParameter("Confidence Threshold")
#         self.threshNeutralEmotion = self.confidence + 0.15
#         self.threshHappyEmotion = self.confidence
#         self.threshSurprisedEmotion = self.confidence + 0.05
#         self.threshAngryEmotion = self.confidence + 0.2
#         self.threshSadEmotion = self.confidence + 0.15
#         self.emotions = ["neutral", "happy", "surprised", "angry", "sad"]
#         self.counter = 0
#         self.bIsRunning = False
#         self.delayed = []
#         self.errorMes = ""

#     def onUnload(self):
#         self.counter = 0
#         self.tProperties = [0,0,0,0,0]
#         self.bIsRunning = False
#         self.cancelDelays()

#     def onInput_onStart(self):
#         try:
#             #start timer
#             import qi
#             import functools
#             delay_future = qi.async(self.onTimeout, delay=int(self.getParameter("Timeout (s)") * 1000 * 1000))
#             self.delayed.append(delay_future)
#             bound_clean = functools.partial(self.cleanDelay, delay_future)
#             delay_future.addCallback(bound_clean)

#             self.tProperties = [0,0,0,0,0]
#             self.bIsRunning = True
#             while self.bIsRunning:
#                 if self.counter < 4:
#                     try:
#                         #identify user
#                         ids = ALMemory.getData("PeoplePerception/PeopleList","169.254.178.70",9559)
#                         if len(ids) == 0:
#                             self.errorMes = "No face detected"
#                             self.onUnload()
#                         elif len(ids) > 1:
#                             self.errorMes = "Multiple faces detected"
#                             self.onUnload()
#                         else:
#                             #analyze age properties
#                             self.faceC.analyzeFaceCharacteristics(ids[0])
#                             time.sleep(0.2)
#                             properties = ALMemory.getData("PeoplePerception/Person/"+str(ids[0])+"/ExpressionProperties")
#                             self.tProperties[0] += properties[0]
#                             self.tProperties[1] += properties[1]
#                             self.tProperties[2] += properties[2]
#                             self.tProperties[3] += properties[3]
#                             self.tProperties[4] += properties[4]
#                             self.counter += 1
#                     except:
#                         ids = []
#                 else:
#                     self.counter = 0
#                     recognized = [0,0,0,0,0]
#                     #calculate mean value for neutral, happy, surprised, angry or sad
#                     self.tProperties[0] /= 4
#                     self.tProperties[1] /= 4
#                     self.tProperties[2] /= 4
#                     self.tProperties[3] /= 4
#                     self.tProperties[4] /= 4

#                     if self.getParameter("neutral") and self.tProperties[0] > self.threshNeutralEmotion:
#                         recognized[0] = self.tProperties[0]
#                     if self.getParameter("happy") and self.tProperties[1] >self.threshHappyEmotion:
#                         recognized[1] = self.tProperties[1]
#                     if self.getParameter("surprised") and self.tProperties[2] > self.threshSurprisedEmotion:
#                         recognized[2] = self.tProperties[2]
#                     if self.getParameter("angry") and self.tProperties[3] > self.threshAngryEmotion:
#                         recognized[3] = self.tProperties[3]
#                     if self.getParameter("sad") and self.tProperties[4] > self.threshSadEmotion:
#                         recognized[4] = self.tProperties[4]

#                     self.tProperties = [0,0,0,0,0]
#                     try:
#                         if recognized != [0,0,0,0,0]:
#                             emotion = self.emotions[recognized.index(max(recognized))]
#                         else:
#                             emotion = None
#                     except:
#                         emotion = None
#                     try:
#                         ALMemory.removeData("PeoplePerception/Person/"+str(ids[0])+"/ExpressionProperties")
#                     except:
#                         pass
#                     if emotion != None:
#                         self.onStopped(emotion)
#                         self.onUnload()
#                         return
#             raise RuntimeError(self.errorMes)
#         except Exception as e:
#             raise RuntimeError(str(e))
#             self.onUnload()

#     def onTimeout(self):
#         self.errorMes = "Timeout"
#         self.onUnload()

#     def cleanDelay(self, fut, fut_ref):
#         self.delayed.remove(fut)

#     def cancelDelays(self):
#         cancel_list = list(self.delayed)
#         for d in cancel_list:
#             d.cancel()

#     def onInput_onStop(self):
#         self.onUnload()

    
    