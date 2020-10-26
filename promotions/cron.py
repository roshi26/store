import kronos
import random
from django.core.mail import send_mail
 

@kronos.register('* * * * *')
def talk():
    print ("cron works")
    send_mail(
    	'cron works!',
    	'message',
    	'roshidubey2602@gmail.com',
    	['roshidubey2602@gmail.com'])
    return None
