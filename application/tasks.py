from celery import shared_task
from application.models import Application
from datetime import date, timedelta


@shared_task
def remove_rejected_applications():
    Application.objects.filter(status='rejected').delete()

    return 'Rejected applications were removed'