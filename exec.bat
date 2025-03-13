CreateObject("Wscript.Shell").Run "your_batch_file.bat", 0, True
ECHO ON
REM A batch script to execute a Python script
SET PATH=%PATH%;C:\Python27
pip install opencv-contrib-python==4.1.0.25
python ./Start.py
PAUSE