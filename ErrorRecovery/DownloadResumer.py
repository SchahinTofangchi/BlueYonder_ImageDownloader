'''
Created on 10.07.2015

@author: Schahin Tofangchi

Resumes the download process, if it has been unexpectedly interrupted.
'''

import os

from Parser.DownloadFileParser import DownloadFileParser
import LogfileIO


def isResumable ():
    """
    @return: True, if a logfile exists (i.e. there is something that can be resumed)
    """
    isResumable, _, _, _, _ = LogfileIO.getResumptionInfo()
    return isResumable
    
def resume ():
    """
    Checks, if there are incomplete download jobs, and resumes them, if necessary.
    @return: downloadFile - the download file parser
    @return: downloadFolder - the folder, to which the files are to be downloaded
    @return: msg - additional comment/error message
    """
    isResumable, source_filePath, lineNumber, downloadFolder, lastDownload = LogfileIO.getResumptionInfo()
    if (isResumable == False):
        return None, None, "No Logfile found!"
    else:
        downloadFile = DownloadFileParser(source_filePath, fileOffset=lineNumber)
        # Remove the last download
        if (os.path.exists(lastDownload)):
            os.remove(lastDownload)
        return downloadFile, downloadFolder, "Success!"
    
