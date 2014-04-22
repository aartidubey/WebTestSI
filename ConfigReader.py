#-------------------------------------------------------------------------------
# Name:        ConfigReader
# Purpose:     This module reads and returns the login information from
#              a config file based on specific domain.
#
# Author:      Artee
#
# Created:     03/04/2014
#-------------------------------------------------------------------------------
import ConfigParser

class ConfigReader:

    def __init__(self,config_file):
        self.information = {}
        self.loginInfo = {}
        self.config_file = config_file
        self.cf = ConfigParser.ConfigParser()

    def readConfigFile(self):
        return self.cf.read(self.config_file)

    def getDomainSpecificInfo(self, domain):
        if domain == 'stage':
            return self.cf.items("login_stage")
        elif domain == 'test':
            return self.cf.items("login_test")

    def getLoginInfo(self, domain):
        self.readConfigFile()
        loginInfo = self.getDomainSpecificInfo(domain)
        return loginInfo

    def getUsernamePassword(self, domain):
        for userNameAndPwd in self.getLoginInfo(domain):
            self.information[userNameAndPwd[0]] = userNameAndPwd[1]
        return self.information

