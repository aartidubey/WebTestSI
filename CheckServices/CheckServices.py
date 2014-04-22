#-------------------------------------------------------------------------------
# Name:        CheckServices
# Purpose:     Tests all the services by checking the status code (200 or 404).
#
# Author:      Artee
#
# Created:     08/04/2014
#-------------------------------------------------------------------------------

from Urllib2Opener import Urllib2Opener
from TextFileReader import TextFileReader

class CheckServices():
    def __init__(self,url,username, password, domain, serviceUrl, errorLog):
        self.logMsg=""
        urllibOpener = Urllib2Opener(url, username, password)
        self.opener = urllibOpener.getOpener()
        self.urlReader = TextFileReader(serviceUrl)
        self.errorLog = TextFileReader(errorLog)
        self.domain = domain

    def checkDashboardService(self):
        print "*** Checking Dashboard service.\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg + "\nError code: "+str(e.code)+\
            self.errorLog.next() + link_url

    def checkHomeTimelineEvents(self):
        print "*** Checking HomeTimelineEvents service.\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg + "\nError code: "+str(e.code)+\
            self.errorLog.next() + link_url

    def checkDashboardServiceOnIntelligenceCampaign(self):
        print "*** Checking Dashboard service on Intelligence/Campaign page.\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg +"\nError code: "+ str(e.code)+\
            self.errorLog.next()+ link_url

    def checkProfilePicture(self):
        print "*** Checking Profile pictures. \nStatus:"
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            if (e.code != 404):
                self.logMsg = self.logMsg + "\nError code: "+ str(e.code) +\
                self.errorLog.next() + link_url

    def checkBeginSurvey(self):
        print "*** Checking the service of the 'Begin' button present on Home"+\
                " and Profile/task page.\nStatus: "
        link_url = self.urlReader.next()
        try:
            print  self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg + "\nError code: "+str(e.code)+\
            self.errorLog.next()+link_url

    def checkLearnAboutConflictMineralsResourceCenter(self):
        print "*** Checking 'Learn About Conflict Minerals Service'\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg + "\nError code: "+str(e.code)+\
            self.errorLog.next()+ link_url

    def checkSupplierTabService(self):
        print "*** Checking Supplier tab on 'Intelligence/Conflict Minerals'\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg + "\nError code: "+str(e.code)+\
            self.errorLog.next()+ link_url

    def checkConflictMineralDetails(self):
        print "*** Checking Conflict Mineral details service\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg + "\nError code: "+str(e.code)+\
            self.errorLog.next()+ link_url

    def checkNetworkSupplierService(self):
        print "*** Checking Network Supplier Service\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg + "\nError code: "+str(e.code)+\
            self.errorLog.next()+ link_url

    def checkNetworkCustomersService(self):
        print "*** Checking Network Customers Service \nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg + "\nError code: "+str(e.code)+\
            self.errorLog.next()+ link_url

    def checkIntelligenceBrowsersService(self):
        print "*** Checking IntelligenceBrowser Service\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg + "\nError code: "+str(e.code)+\
            self.errorLog.next()+ link_url

    def checkInvitationCompanyListOnNetwork(self):
        print "*** Checking Company list on Network page.\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg +"\nError code: "+str(e.code)+\
            self.errorLog.next() +  link_url

    def checkInvitaionListOnNetwork(self):
        print "*** Checking Company list on Network page.\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg +"\nError code: "+str(e.code)+\
            self.errorLog.next() +  link_url

    def checkViewLegalDataService(self):
        print "*** Checking 'View Legal Data'(a table element) on Intelligence/Campaigns page\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg + "\nError code: "+str(e.code)+\
            self.errorLog.next() + link_url

    def checkViewLegalDataOnCM(self):
        print "*** Checking 'ViewLegalDataOnCM'\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg +"\nError code: "+str(e.code)+\
            self.errorLog.next() + link_url

    def checkShowCampaignOnHomePage(self):
        print "*** Checks the 'Show this Campaign on Home Page?' option on Intelligence/Campaigns.\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg +"\nError code: "+str(e.code)+\
            self.errorLog.getUrl()+  link_url

    def checkProfileActivity(self):
        print "*** Checking Profile Activity service.\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg +"\nError code: "+str(e.code)+\
            self.errorLog.next()+  link_url

    def checkProfileTaskDatatableIncomplete(self):
        print "*** Checking Profile Task DatatableIncomplete service.\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg +"\nError code: "+str(e.code)+\
            self.errorLog.next()+  link_url

    def checkProfileTaskDatatableComplete(self):
        print "*** Checking Profile Task DatatableComplete service.\nStatus: "
        link_url = self.urlReader.next()
        try:
            print  self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg +"\nError code: "+str(e.code)+\
            self.errorLog.next()+  link_url

    def checkCompleteDatatableOnIntelligenceCampaign(self):
        print "*** Checking 'Complete Datatable' service on Intelligence/Campaign page.\nStatus: "
        link_url = self.urlReader.next()
        try:
            print  self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg +"\nErrot code: "+ str(e.code)+\
            self.errorLog.next()+link_url

    def checkIncompleteDatatableOnIntelligenceCampaign(self):
        print "*** Checking 'Incomplete Datatable' service on Intelligence/Campaign page.\nStatus: "
        link_url = self.urlReader.next()
        try:
            print self.opener.urlopen(link_url).getcode()
            self.errorLog.next()
        except self.opener.HTTPError as e:
            print e.code
            self.logMsg = self.logMsg +"\nErrot code: "+ str(e.code)+\
            self.errorLog.next()+link_url

    def getLogMsg(self):
        return self.logMsg