from celery import Celery
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_task():
	send_mail('CELERY WORKED!',
		'this is the proof',
		'roshidubey2602@gmail.com',
		['roshidubey2602@gmail.com'],
		fail_silently=False,

		)


		