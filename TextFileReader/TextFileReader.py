#-------------------------------------------------------------------------------
# Name:        TextFileReader
#
# Purpose:     This module reads and returns the next line from a file
#
# Author:      Artee
#
# Created:     18/04/2014
#-------------------------------------------------------------------------------


class TextFileReader:
    def __init__(self, ServiceUrlFile):
        self.fname = open(ServiceUrlFile, "r")

    def next(self):
        return self.fname.next()








