def focus():
    pass
# from naoqi import ALProxy
# import time

# ip_robot = "192.168.137.219"
# port_robot = 9559

# basic_awareness = ALProxy("ALBasicAwareness", ip_robot, port_robot)
# motion = ALProxy("ALMotion", ip_robot, port_robot)
# def faceDetector():
#         try:
#             faceProxy = ALProxy("ALFaceDetection", ip_robot, port_robot)
#             period = 500
#             faceProxy.subscribe("Test_Face", period, 0.0 )
#         except Exception, e:
#             print "Error when creating face detection proxy:"
#             print str(e)
#             exit(1) 
        
#         try:
#             memoryProxy = ALProxy("ALMemory", ip_robot, port_robot)
#             memValue = "FaceDetected"
#             val = memoryProxy.getData(memValue) 
#         except Exception, e:
#             print "Error when creating memory proxy:"
#             print str(e)
#             exit(1)

       
#         if(val and isinstance(val, list) and len(val) >= 2): 
                      
#             timeStamp = val[0]   
                     
#             faceInfoArray = val[1]

#             try:            
#                 for j in range( len(faceInfoArray)-1 ):
#                             faceInfo = faceInfoArray[j]

#                             # First Field = Shape info.
#                             faceShapeInfo = faceInfo[0]

#                             # Second Field = Extra info (empty for now).
#                             faceExtraInfo = faceInfo[1]

#                             print "  alpha %.3f - beta %.3f" % (faceShapeInfo[1], faceShapeInfo[2])
#                             print "  width %.3f - height %.3f" % (faceShapeInfo[3], faceShapeInfo[4])
#                             return True

#             except Exception, e:
#                     print "faces detected, but it seems getData is invalid. ALValue ="
#                     print val
#                     print "Error msg %s" % (str(e))
#         else:
#                 print "No face detected"
#                 return False
#         faceProxy.unsubscribe("Test_Face")


# def olhaPraFrente():

# # Choregraphe simplified export in Python.

#     names = list()
#     times = list()
#     keys = list()
    
#     names.append("HeadPitch")
#     times.append([0.52, 1.04])
#     keys.append([0.0950661, 0.0950661])
    
#     names.append("HeadYaw")
#     times.append([0.52, 1.04])
#     keys.append([0.0229681, 0.0229681])
    
#     motion.angleInterpolation(names, keys, times, True)       
# #wake up
# motion.wakeUp()
# basic_awareness.startAwareness()
# Face = False
# while Face !=True:
#     Face = faceDetector()            
#     if (Face == True):
#         basic_awareness.stopAwareness()        
#     else:        
#         olhaPraFrente()
#         time.sleep(5)

