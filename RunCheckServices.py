#-------------------------------------------------------------------------------
# Name:        RunCheckServices
#
# Purpose:     This module takes Domain name from command line and
#              runs the service tests for specified domain.
#
# Author:      Artee
#
# Created:     10/04/2014
#-------------------------------------------------------------------------------

import sys
import time
from ConfigReader import ConfigReader
from CheckServices import CheckServices
from SendLogMsgViaEmail import SendLogMsgViaEmail

def main():

    if len(sys.argv) <= 1:
        print "Please enter domain."
        sys.exit()

    domain = sys.argv[1]
    domain = domain.lower()
    domain = domain.strip()

    configFile = 'config.properties'
    configReader = ConfigReader(configFile)
    information = configReader.getUsernamePassword(domain)

    username = information['user_name']
    password = information['password']

    if domain == 'stage':
        serviceUrlFile = 'serviceUrlForStage.txt'
    elif domain == 'test':
        serviceUrlFile = 'serviceUrlForTest.txt'
    errorLogFile = 'ServiceErrorLog.txt'

    url = "http://"+sys.argv[1]+".sourceintelligence.net/"

    dateTime = time.strftime('%a, %d %b %Y %H:%M:%S')
    logMsg = "Log report for "+domain.title() +" on "+dateTime+"\n\n"
    checkLogMsg = logMsg

    checkservices = CheckServices(url,username,password,domain,serviceUrlFile,errorLogFile)

    sendEmail = SendLogMsgViaEmail()

    checkservices.checkDashboardService()
    checkservices.checkHomeTimelineEvents()
    checkservices.checkDashboardServiceOnIntelligenceCampaign()
    checkservices.checkProfilePicture()
    checkservices.checkBeginSurvey()
    checkservices.checkLearnAboutConflictMineralsResourceCenter()
    checkservices.checkSupplierTabService()
    checkservices.checkConflictMineralDetails()
    checkservices.checkNetworkSupplierService()
    checkservices.checkNetworkCustomersService()
    checkservices.checkIntelligenceBrowsersService()
    checkservices.checkInvitationCompanyListOnNetwork()
    checkservices.checkInvitaionListOnNetwork()
    checkservices.checkViewLegalDataService()
    checkservices.checkViewLegalDataOnCM()
    checkservices.checkShowCampaignOnHomePage()
    checkservices.checkProfileActivity()
    checkservices.checkProfileTaskDatatableIncomplete()
    checkservices.checkProfileTaskDatatableComplete()
    checkservices.checkCompleteDatatableOnIntelligenceCampaign()
    checkservices.checkIncompleteDatatableOnIntelligenceCampaign()

    logMsg = logMsg + checkservices.getLogMsg()
    logMsg = logMsg.strip()

    if (logMsg == checkLogMsg):
        logMsg = logMsg + "\nEverything is working fine! "
        sendEmail.send_email(logMsg)
    else:
        sendEmail.send_email(logMsg)

if __name__ == '__main__':
    main()
