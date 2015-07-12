'''
Created on 10.07.2015

@author: Schahin Tofangchi

Parses the file containing the URLs.
'''

import sys


class DownloadFileParser:
    
    def __init__ (self, filePath, replaceBackslashWithSlash=True, fileOffset=0):
        """
        Object constructor.
        @param filePath: Path to the file that contains the list of URLs (one per line)
        @param replaceBackslashWithSlash: Set to False, ONLY if there are no backslashes in the file.
        @param fileOffset: Line number at which we would like to start reading the file  
        """
        self._filePath = filePath
        try:
            self._fileReader = open(filePath, 'r')
        except IOError, errorInfo:
            if (errorInfo.errno == 2):
                # File does not exist
                print "File containing the URLs (" + filePath + ") does not exist!"
            else:
                print errorInfo
            sys.exit(1)
        self._replaceBackslashWithSlash = replaceBackslashWithSlash
        for _ in range(fileOffset):
            self._fileReader.readline()
        return
    
    def getNextUrl (self):
        """
        Reads the next line in the file and replaces backslashes with slashes, if replaceBackslashWithSlash is set accordingly.
        @return: The next URL from the file
        """
        url = self._fileReader.readline().replace("\n", "")
        if (url == ""):
            # End of file
            return None
        if (self._replaceBackslashWithSlash):
            return url.replace("\\", "/")
        else:
            return url
