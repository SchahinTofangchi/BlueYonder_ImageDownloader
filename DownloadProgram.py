'''
Created on 10.07.2015

@author: Schahin Tofangchi

Main module: Controls everything related to the download process.
Run as follows: python DownloadProgram.py urlFilePath [outputFolder]
or: python DownloadProgram.py resume
to resume the previous download process.
'''

import sys
import os
from Tkinter import Tk
from tkMessageBox import askyesnocancel

from ErrorRecovery import DownloadResumer, LogfileIO
from Parser.DownloadFileParser import DownloadFileParser
from Download import FileDownloader, DownloadErrors 
    

def printHelp ():
    print "Usage: python DownloadProgram.py urlFilePath [outputFolder]"
    print "To resume the previous download process run \"python DownloadProgram.py resume\""
    return
    
def downloadFiles (downloadFileParser, outputFolder):
    """
    Downloads all files to the outputFolder, starting at the current position of the downloadFileParser.
    @param downloadFileParser: Object of the type Parser.DownloadFileParser with an instantiated fileReader
    @param outputFolder: Folder, to which the files are to be downloaded 
    """
    counter = 0
    errorCounter = 0     
    url = downloadFileParser.getNextUrl()
    while (url != None):
        outputPath = FileDownloader.getOutputPath(url, outputFolder)
        LogfileIO.writeLogfile(downloadFileParser._filePath, counter, outputFolder, outputPath)
        downloadSuccessful = FileDownloader.downloadFile(url, outputPath)
        if (downloadSuccessful == False):
            DownloadErrors.writeLink(url)
            errorCounter += 1
        counter += 1
        url = downloadFileParser.getNextUrl()
    
    print str(counter-errorCounter) + " file(s) downloaded"
    print "Failed to download " + str(errorCounter) + " file(s) - see erroneousLinks.txt"   
    return
    
if __name__ == "__main__":
    
    if (len(sys.argv) == 0 or len(sys.argv) > 3):
        # Too few or too many arguments provided
        printHelp()
        sys.exit(0)
    else:
        outputFolder = ""
        if (sys.argv[1].lower() == "resume"):
            # User requested resumption
            # Try to resume the last job
            downloadFileParser, outputFolder, msg = DownloadResumer.resume()
            filePath = downloadFileParser._filePath
            if (downloadFileParser == None):
                print msg
                sys.exit(1)
        else:
            userWantsToResume = False
            if (DownloadResumer.isResumable()):
                Tk().withdraw()
                userWantsToResume = askyesnocancel("Resume download?", "The previous job has been unexpectedly interrupted. Would you like to resume the job?")
                if (userWantsToResume):
                    downloadFileParser, outputFolder, msg = DownloadResumer.resume()
                elif (userWantsToResume == None):
                    # Abort
                    sys.exit(0)
            if (userWantsToResume == False):
                # Regular program start
                if (len(sys.argv) == 2):
                    filePath = sys.argv[1]
                    downloadFileParser = DownloadFileParser(filePath)
                else:
                    # Exactly three arguments have been provided
                    filePath = sys.argv[1]
                    if (os.path.abspath(filePath) == os.path.abspath(LogfileIO.LOGFILE_PATH) or
                        os.path.abspath(filePath) == os.path.abspath(DownloadErrors.ERRORFILE_PATH)):
                        # Logfile and Errorfile should not be used as input files
                        print "Please choose a different input file!"
                        sys.exit(1)
                    outputFolder = sys.argv[2]
                    if (outputFolder[-1] == "\\"):
                        outputFolder = outputFolder.replace("\\", "/")
                    if (outputFolder[-1] != '/'):
                        outputFolder = outputFolder + "/"  
                    if (os.path.exists(outputFolder) == False):
                        os.mkdir(outputFolder)             
                    downloadFileParser = DownloadFileParser(filePath)
                DownloadErrors.deleteErrorfile()
                
        downloadFiles(downloadFileParser, outputFolder)
        # Log not needed anymore after all files have been downloaded
        LogfileIO.deleteLogfile()
            