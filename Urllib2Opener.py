#-------------------------------------------------------------------------------
# Name:        Urllib2Opener
# Purpose:     This module sets and installs an opener for urllib2
#              It will be used to open the URLs with basic authentication
# Author:      Artee
#
# Created:     10/04/2014
#-------------------------------------------------------------------------------

import urllib2

class Urllib2Opener:
    def __init__(self,url,username,password):
        self.url = url
        self.username = username
        self.password = password

    def getOpener(self):
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
            # this creates a password manager
        passman.add_password(None, self.url, self.username, self.password)

        auth_handler = urllib2.HTTPBasicAuthHandler(passman)
            # create the AuthHandler
        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)
            # all the calls to urllib2.urlopen will now use the handler
        return urllib2