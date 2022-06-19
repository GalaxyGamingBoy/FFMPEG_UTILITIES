from hurry.filesize import size, si
import sys
import os

commandArgs = sys.argv

class FFMPEG_CompressVideo:
    def __init__(self, inputFile, outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile
    
    def compress(self):
        return f"ffmpeg -i {self.inputFile} {self.outputFile}"

try:
    os.system(FFMPEG_CompressVideo(commandArgs[1], commandArgs[2]).compress())

    oldSize = size(os.path.getsize(commandArgs[1]), system=si)
    newSize = size(os.path.getsize(commandArgs[2]), system=si)

    print("FILE COMPRESS COMPLETED!")
    print(f"OLD SIZE: {oldSize}, NEW SIZE: {newSize}")
except:
    print("Usage: compressVid.py INPUT_FILE(in.mp4) OUTPUT_FILE(out.mp4)")