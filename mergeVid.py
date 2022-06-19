import sys
import os

commandArgs = sys.argv
commandArgCount = len(commandArgs) 
commandArgInputs = commandArgCount - 2 # Remove Command Call and Output File Argument



class FFMPEG_MergeVideo:
    def __init__(self, outputFile):
        self.outputFile = outputFile
    
    def createTMPWithFilesToBeMerged(self):
        # Create a temporary file to store the files to be merged
        tmpFile = open('tmp.ffmpeg_utils', 'w')

        # Write the files to be merged to the temporary file
        for i in range(commandArgInputs):
            tmpFile.write(commandArgs[i + 2] + "\n")

        # Close the temporary file
        tmpFile.close()

    def merge(self):
        self.createTMPWithFilesToBeMerged()
        return f"ffmpeg -f concat -i tmp.ffmpeg_utils -c copy {self.outputFile}"

try:
    os.system(FFMPEG_MergeVideo(commandArgs[1]).merge())
    print("VIDEOS FINISHED MERGING")
except:
    print("Usage: mergeVid.py OUTPUT_FILE(out.mp4) INPUT_FILES (in_1.mp4 in_2.mp4 ...)")