from celery import shared_task

from .services import save_log_from_cache


@shared_task
def save_logs_to_db():
    save_log_from_cache()
