import sys
import os

def runCMD(cmd):
    os.system(cmd)

commandArgs = sys.argv

try:
    cmdRunStr = "ffmpeg -ss " + commandArgs[1] + " -to " + commandArgs[2] + " -i " + commandArgs[3] + " -c copy " + commandArgs[4]
    runCMD(cmdRunStr)
except:
    print("Usage: cutVid.py START_TIME(00:00:00) END_TIME(00:10:00) INPUT_FILE(cut.mp4) OUTPUT_FILE(cutOut.mp4)")
