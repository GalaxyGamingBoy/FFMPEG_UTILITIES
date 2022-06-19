import os
import sys

commandArgs = sys.argv

class FFMPEG_RemoveAudio:
    def __init__(self, inputFile, outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile
    
    def removeAudio(self):
        return f"ffmpeg -i {self.inputFile} -vcodec copy -an  {self.outputFile}"

try:
    os.system(FFMPEG_RemoveAudio(commandArgs[1], commandArgs[2]).removeAudio())
    print("FINISHED REMOVING AUDIO")
except:
    print("Usage: removeAudio.py INPUT_FILE(in.mp4) OUTPUT_FILE(out.mp4)")