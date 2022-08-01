CreateObject("Wscript.Shell").Run "your_batch_file.bat", 0, True
ECHO ON
REM A batch script to execute a Python script
SET PATH=%PATH%;C:\Python27
python ./Start.py
PAUSE