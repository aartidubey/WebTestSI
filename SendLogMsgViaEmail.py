#-------------------------------------------------------------------------------
# Name:        SendLogMsgViaEmail
# Purpose:	   Sends an email 
#
# Author:      Artee
#
# Created:     01/04/2014
#-------------------------------------------------------------------------------

import sys
import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import time

class SendLogMsgViaEmail:

    def getUserName(self):
        gmail_user= "username_goes_here"
        return gmail_user

    def getPassword(self):
        fo = open("C:/Python27/pwd.txt","r")
        gmail_pwd =  fo.read()
        fo.close()
        return gmail_pwd

    # function to send the email and attachment
    def mail(self, to, subject, text):
           msg = MIMEMultipart()

           msg['Subject'] = 'Log Report For Website Test'

           msg.attach(MIMEText(text))
           try:
               mailServer = smtplib.SMTP('smtp.gmail.com: 587')
               mailServer.ehlo()
               mailServer.starttls()
               mailServer.ehlo()
               gmail_user = self.getUserName()
               gmail_pwd = self.getPassword()
               mailServer.login(gmail_user, gmail_pwd)
               mailServer.sendmail(gmail_user, to, msg.as_string())
               mailServer.close()
               print("Email sent successfully")
           except:
              print("Unable to send Email")

    # reads list of emails to send the log report
    def send_email(self,logMsg):
        open_file = open('C:/Python27/list.txt','r')
        file_lines = open_file.readlines()
        for i in range(len(file_lines)):
           line = file_lines[i].strip()
           self.mail(line,
              'Log Report For Website Test',
              logMsg)

        open_file.close()

