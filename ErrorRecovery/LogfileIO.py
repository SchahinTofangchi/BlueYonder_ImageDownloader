'''
Created on 10.07.2015

@author: Schahin Tofangchi

Writes and reads from the log file.
'''

import os

LOGFILE_PATH = "log.txt"


def writeLogfile (sourceFilePath, lineNumber, downloadFolder, downloadFilePath):
    """
    Creates a new log file with the provided contents.
    @param sourceFilePath: Path to the file containing the URLs
    @param lineNumber: Line that is currently being processed by the downloader
    @param downloadFilePath: Location, at which the download is to be stored   
    """
    logfile = open(LOGFILE_PATH, 'w')
    logfile.write(sourceFilePath + "\n")
    logfile.write(str(lineNumber) + "\n")
    logfile.write(downloadFolder + "\n")
    logfile.write(downloadFilePath + "\n")    
    logfile.close()
    
    return

def getResumptionInfo ():
    """
    @return: isResumable - download has not been completed yet
    @return: source_filePath - file containing the URLs
    @return: lineNumber - line, at which the download is to be resumed
    @return: lastDownload - name of the last downloaded file
    """
    if (os.path.exists(LOGFILE_PATH)):
        isResumable = True
        logReader = open(LOGFILE_PATH, 'r')
        source_filePath = logReader.readline().replace("\n", "")
        lineNumber = int(logReader.readline().replace("\n", ""))
        downloadFolder = logReader.readline().replace("\n", "")
        lastDownload = logReader.readline().replace("\n", "")
        logReader.close()
    else:
        isResumable = False
        source_filePath = None
        lineNumber = None
        downloadFolder = None
        lastDownload = None
    
    return isResumable, source_filePath, lineNumber, downloadFolder, lastDownload

def deleteLogfile ():
    if (os.path.exists(LOGFILE_PATH)):
        os.remove(LOGFILE_PATH)
    return
    