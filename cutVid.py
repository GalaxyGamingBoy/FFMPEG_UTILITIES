import sys
import os

def runCMD(cmd):
    os.system(cmd)

commandArgs = sys.argv

cmdRunStr = "ffmpeg -ss " + commandArgs[1] + " -to " + commandArgs[2] + " -i " + commandArgs[3] + " -c copy " + commandArgs[4]
runCMD(cmdRunStr)
