import json
from datetime import datetime

from django.utils.deprecation import MiddlewareMixin

from .services import log_to_cache

EXCLUDE_PATHS = ['/admin/', '/login/']


class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if any(request.path.startswith(path) for path in EXCLUDE_PATHS):
            return None
        data = {
            'email': request.user.email if request.user.is_authenticated else None,
            'date': datetime.now(),
            'url': request.path,
        }
        log_to_cache(data)
