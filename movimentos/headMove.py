# Choregraphe simplified export in Python.
from naoqi import ALProxy
import time
def moveHead(ver=0.0,hor=0.0):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1])
    keys.append([0.5])

    names.append("HeadYaw")
    times.append([1])
    keys.append([hor])
    
    return names,times,keys



names  = ['HeadYaw']
stiffnessLists  = [0.25, 0.5, 1.0, 0.0]
timeLists  = [1.0, 2.0, 3.0, 4.0]

IP = "192.168.0.141"
# uncomment the following line and modify the IP if you use this script outside Choregraphe.
motion = ALProxy("ALMotion", IP , 9559)
tracker = ALProxy("ALTracker",IP,9559)
motion.setStiffnesses("Head", 1.0)
targetName = "Face"
faceWidth = 0.5
tracker.registerTarget(targetName, faceWidth)
tracker.track(targetName)

time.sleep(3)
print(tracker.getActiveTarget())
# motion.stiffnessInterpolation(names, stiffnessLists, timeLists)
# commandAngles = motion.getAngles("HeadPitch",False)
# print(commandAngles)
