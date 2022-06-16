import sys
import os

commandArgs = sys.argv

def cutVidFFMPEG(startTime, endTime, inputFile, outputFile):
    return cmdRunStr = "ffmpeg -ss " + startTime + " -to " + endTime + " -i " + inputFile + " -c copy " + outputFile

try:
    cmdRunStr = cutVidFFMPEG(commandArgs[1], commandArgs[2], commandArgs[3], commandArgs[4])
    os.system(cmdRunStr)
except:
    print("Usage: cutVid.py START_TIME(00:00:00) END_TIME(00:10:00) INPUT_FILE(cut.mp4) OUTPUT_FILE(cutOut.mp4)")
