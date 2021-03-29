from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to InstaAge'
    sender = 'dsamfan@gmail.com'
    
    text_content = render_to_string('email/instaemail.txt',{'name':name})
    html_content = render_to_string('email/instaemail.html',{'name':name})
    
    msg = EmailMultiAlternatives(subject,text_content,sender,[reciever])
    
    msg.attach_alternative(html_content,'text/html')
    msg.send()    