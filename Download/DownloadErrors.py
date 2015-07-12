'''
Created on 12.07.2015

@author: Schahin Tofangchi

Stores links belonging to failed download attempts in a text file.
'''

import os

ERRORFILE_PATH = "erroneousLinks.txt"

def writeLink (url):
    """
    Appends the URL to the error file.
    """
    errorfile = open(ERRORFILE_PATH, 'a')
    errorfile.write(url + "\n")
    errorfile.close()
    return
    
def deleteErrorfile ():
    if (os.path.exists(ERRORFILE_PATH)):
        os.remove(ERRORFILE_PATH)
    return