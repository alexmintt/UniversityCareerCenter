from django.core.cache import cache

from .models import UserLog


def log_to_cache(data):
    log_id = f"log_{data['date'].timestamp()}"
    cache.set(log_id, data, timeout=60 * 60)


def save_log_from_cache():
    logs = UserLog.objects.all()
    keys = cache.keys("log_*")
    for key in keys:
        try:
            data = cache.get(key)
            if data:
                UserLog.objects.create(**data)

                cache.delete(key)
        except Exception as e:
            print(e)
