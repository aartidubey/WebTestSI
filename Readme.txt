Software Used:
	Python 2.7
	Selenium Webdriver (version 2.40.0)
	PhantomJs (version 1.9) - a headless WebKit.
	Urllib2 - Python module
Test Details:
	Test has been divided in to two parts:
	1. Service test 
	2. Elements test
Details of the Service test:
	It uses a Opener 'Urllib2Opener.py', which uses the URL, user_name and password.
	'CheckServices.py' uses the above Opener for accessing/checking status/testing of authenticated URLs. 
	'RunCheckServices.py' Simply runs the services.
	It can be run form: Command_line 
Details of the Elements test: 
	Multiple Classes -  'WebTestS44.py', StageScraping.py, 'HelpingClassForStageScrapping.py' , 'SubHelperForStageScrapping.py'

Add new Service test:
	To add new Service test, one should always add an URL to serviceUrl.txt file.
	At the same time add a Error log message to ServiceErrorLog.txt file.
	Both the steps are necessary.
	Now add a function to CheckServices.py class.	
Note: 	ServiceUrlForStage.txt file contains all the service URLs for Stage domain. In order to add new domain one should create a
		new text file with domain specific URLs and should pass it to the CheckServices.py. At the same time Stage and Test domain 
		are sharing same error log file as they both are similar but you need to create a new error log file specific to the domain 
		if it different from the existing domain. 

List and purpose of Python Modules created:
1. "List" is file from where I am reading email address of the sender.
2. "config.properties" is a configuration file contains user_name and password for different Domains.
3. "ConfigReader" is class contains the code for reading the login information from different headers in config file.
4. "SendLogMsgViaEmail" contains the code for sending email. Takes log message as argument and sends it.
5. Created a separate class "CheckServices" for urllib_opener. Need to pass authentication opener as arguments to each function. 
6. "Urllib2Opener" module, contains the code for installing the opener, which will  be required by urllib2 to open the URLs which needs basic authentication. 	
7. "TextFileReader" reads and returns the lines from a text file in a recursive manner.



