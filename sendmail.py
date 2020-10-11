import requests, json, os, time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, PlainTextContent
from python_http_client.exceptions import HTTPError
from helpers import emailcheck
from data import list_data


email_list=[]
def sendMail(mail):
    message = Mail(
    
        from_email = os.environ.get('hostemail'), # set sender email as envvar
        to_emails = mail,
        subject = "END FSARS NOW!! NO REDEPLOYMENT, END IT",  # You can edit this
        plain_text_content = open('message.txt','r').read()
    )
        
    try:
            sg = SendGridAPIClient(os.environ.get('API_KEY')) # add your sendgrid api-key
            resp = sg.send(message)
            print('sent mail')
            return True
    except HTTPError as e:
        print(e.to_dict)
        print('error')
        return False
    else:
        print(e.to_dict)
        print('error')
        return False


for i in list_data:
    for keys, value in dict(i).items():
        if keys == "email":
            print(value)
            #email_list.append(str(value))
            sendMail(value)
#print(email_list)
