import sys
import os

commandArgs = sys.argv

class FFMPEG_CutVideo:
    def __init__(self, inputFile, outputFile, startTime, endTime):
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.startTime = startTime
        self.endTime = endTime

    def cut(self):
        return f"ffmpeg -ss {self.startTime} -to {self.endTime} -i {self.inputFile} -c copy {self.outputFile}"

try:
    os.system(FFMPEG_CutVideo(commandArgs[1], commandArgs[2], commandArgs[3], commandArgs[4]).cut())
except:
    print("Usage: cutVid.py START_TIME(00:00:00) END_TIME(00:10:00) INPUT_FILE(cut.mp4) OUTPUT_FILE(cutOut.mp4)")
