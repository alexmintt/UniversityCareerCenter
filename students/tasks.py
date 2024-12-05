from datetime import date, timedelta

from celery import shared_task
from django.core.mail import send_mail

from students.models import Student


@shared_task
def send_reminder_emails():
    today = date.today()
    users = Student.objects.filter(user__last_login__lt=today + timedelta(days=-30))

    for user in users:
        send_mail(
            'Hello!',
            'Dear {}, we miss you!'.format(user.user.email),
            'career@mail.ru',
            [user.user.email],
            fail_silently=True
        )
