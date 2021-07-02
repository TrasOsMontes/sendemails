import smtplib
from email.message import EmailMessage
import random
import time


'''
' 1. Update the parameters.  You will need to set email you will send from, 
' the credentials required (You may need to remove two factor auth or use an app password), the port your email allows you to send from (mine is tls, 465) and who you want to send the emails to.
'''
email = 'from@example.com'
password = 'app password here'
port = 465
sendTo = ['one@example.com','two@example.com','three@example.com']
smtpHost = 'smtp.mail.example.com'


''''
' 2. Update the emails.  Add as many as you want within your list within the {} and using the same format.
'''
emails = [
	{
	'Subject':'Hello! Is it me your looking for?',
	'Body':
'''Write your simple email content formatted here. 

Line breakes will work as will tabs. 
 - This is how you would add a bullet'''
	},
	{'Subject':'Wow, isn\'t this wonderful?',
	'Body':'''
If you want to send another email you can create another item like this.  

This will send to whoever you add to the to portion of your email
				'''
	}
]


'''
' sendRandomMessage: Randomizes which of the emails from the list will be sent. 
'''
def sendRandomMessage(emails):
	random_email = random.randrange(len(emails))
	message = {}
	message['subject'] = emails[random_email]['Subject']
	message['body'] = emails[random_email]['Body']
	return message

'''
' sendEmail: Sends the email based on the parameters set above.   
'''
def sendEmail(email,sendTo,password,subject,body,smtpHost,port):

	msg = EmailMessage()
	msg.set_content(body)

	msg['Subject'] = subject
	msg['From'] = email
	msg['To'] = sendTo

	# Send the message via our own SMTP server.
	server = smtplib.SMTP_SSL(smtpHost, port)
	server.login(msg['From'], password)
	server.send_message(msg)
	server.quit()

'''
' This will loop through and send the email hourly, ie every 3600 seconds.
'''
while True:
	starttime = time.time()
    message = sendRandomMessage(emails)
    sendEmail(email,sendTo,password,message['subject'],message['body'],smtpHost,port)
    nextRun = 3600.0 - ((time.time() - starttime) % 60.0)
    print('message sent with subject: '+message['subject']+' at '+ str(time.time()) + ' Sending the next message in:'+str(nextRun) + ' seconds.')
    time.sleep(nextRun)
