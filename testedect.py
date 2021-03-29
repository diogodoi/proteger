from naoqi import ALProxy
motion = ALProxy("ALMotion", "192.168.137.166", 9559)
movimento = ALProxy("ALRobotPosture","192.168.137.166",9559)
val = movimento.getPostureList()
levantar = movimento.post.goToPosture("Stand",0.5)
# motion.post.setBreathConfig([['Bpm', 20.0], ['Amplitude', 0.5]])
motion.wait(levantar,0)
motion.post.setBreathConfig([['Bpm', 20.0], ['Amplitude', 0.3]])
motion.post.setBreathEnabled("Body",True)
# motion.post.rest()

