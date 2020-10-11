import requests, json, os, time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, PlainTextContent
from python_http_client.exceptions import HTTPError
from helpers import emailcheck
from data import list_data
from sendmail import main

base_url = "http://ngleadersdb.herokuapp.com/api"

r = requests.get(f"{base_url}/senator/all")
data = r.json()
emails = [i['sen_email'] for i in data['data'] if emailcheck(i['sen_email'])]


def sendMail():
    message = Mail(
    
        from_email = os.getenv('hostemail'), # set sender email as envvar
        to_emails = emails,
        subject = "END FSARS NOW!!",  # You can edit this
        plain_text_content = open('message.txt','r').read()
    )
        
    try:
            sg = SendGridAPIClient(os.environ.get('API_KEY')) # add your sendgrid api-key
            resp = sg.send(message)
            return True
    except HTTPError as e:
        print(e.to_dict)
        return False
    else:
        print(e.to_dict)
        return False



for i in list_data:
    for keys, value in dict(i).items():
        if keys == "email":
            print(value)
            main(value)