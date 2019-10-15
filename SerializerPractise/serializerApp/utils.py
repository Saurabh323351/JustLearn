from pyee import EventEmitter
from django.core.mail import send_mail

ee = EventEmitter()

@ee.on('event')
def event_handler(subject,message,recipient_list):

    print(message)
    status = send_mail(subject, message, 'singh.saurabh3333@gmail.com', recipient_list)
    print(status, '----status')

    return status

