#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os 
import smtplib
#from  email.MIMEText import MIMEText
#from  email.Header import Header

mulu =  os.getcwd()
print(mulu)
fp = open('textfile', 'rb')
# # Create a text/plain message
msg = MIMEText(fp.read())
fp.close()
#
# # me == the sender's email address
# # you == the recipient's email address
sender = '916716421@qq.com'
receiver = '916716421@qq.com'
msg['Subject'] = 'The contents of %s' % 'textfile'
msg['From'] =  sender
msg['To'] = receiver
#
# # Send the message via our own SMTP server, but don't include the
# # envelope header.
s = smtplib.SMTP()
s.connect('smtp.qq.com')
s.login('916716421','m0nkey320wasd#')
s.sendmail(sender , receiver , msg.as_string())
s.quit()
