from distutils.sysconfig import get_makefile_filename
import yagmail

subject = 'subject here'
spam = int(input("How many emails would you like to spam?\n-> "))
reciever_email = input("Who would you llike to spam?\n-> ")

contents = ['Hey!!', 'Wasup?', 'Bye']

GMAIL = input('Enter your email adress here\n-> ')
PASSWORD = input('Enter your password here\n->')

sentEmails = 0
def sendEMail():
    global sentEmails

    sender_email = GMAIL
    yag = yagmail.SMTP(sender_email, PASSWORD)
    yag.send(to=reciever_email, subject=subject, contents=contents) 
    sentEmails += 1
    print(f'email {sentEmails} sent!')

for i in range(spam):
    sendEMail()