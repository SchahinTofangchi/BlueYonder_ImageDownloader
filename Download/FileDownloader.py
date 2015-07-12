'''
Created on 10.07.2015

@author: Schahin Tofangchi

Downloads a file, given a URL, into an output folder.
'''

import os
import sys
import urllib


def downloadFile (url, outputPath):
    """
    Downloads a file from an URL to the location specified by outputPath.
    @param url: URL to the file that is to be downloaded
    @param outputPath: Path to the location, at which the downloaded file is to be stored
    @return: Whether the download was successful or not
    """
    connection = urllib.URLopener()
    try:
        connection.retrieve(url, outputPath)
    except IOError, errorInfo:
        if (errorInfo.errno == "socket error"):
            return False
        else:
            print errorInfo
            sys.exit(1)
    return True

def getOutputPath (url, outputFolder=""):
    """
    Builds the complete output path, given the output folder and the URL of the file that is to be downloaded.
    @param url: URL to the file that is to be downloaded
    @param outputFolder: Folder, within which the downloaded file is to be stored  
    """
    # Get the file name
    lastIndexOfSlash = url.rfind("/")
    fileName = url[lastIndexOfSlash + 1:]
    
    # Split file name in prefix and suffix
    lastIndexOfDot = fileName.rfind(".")
    if (lastIndexOfDot == -1):
        prefix = fileName
        suffix = ""
    else:
        prefix = fileName[:lastIndexOfDot]
        suffix = fileName[lastIndexOfDot:]
    
    # If a file with the same name exists, add a counter to the file name
    counter = 0
    newPrefix = prefix
    while (os.path.exists(outputFolder + newPrefix + suffix)):
        counter += 1
        newPrefix = prefix + "(" + str(counter) + ")"
    
    return (outputFolder + newPrefix + suffix)
