"""
def naoVideoRecording(self):        
    filename = self.gera_id_sessao()
    videoRecorderProxy = ALProxy("ALVideoRecorder", self.robotIP, self.PORT)
    videoRecorderProxy.setResolution(2)
    videoRecorderProxy.setFrameRate(24)
    videoRecorderProxy.setVideoFormat("MJPG")
    videoRecorderProxy.post.startRecording("/home/nao/recordings/cameras", str(filename)+"_NAO")
    
    
def stopVideoRecording(self):               
    videoRecorderProxy = ALProxy("ALVideoRecorder", self.robotIP, self.PORT)
    videoRecorderProxy.post.stopRecording()

def getDir(self):
    folder = QFileDialog.getExistingDirectory(self,"Selecione um pasta para salvar o video.")            
    if folder != None:
        self.pasta = str(folder)
        global pastaS
        pastaS = self.pasta
        self.inputDir.setText(self.pasta)    
    
    
"""
