import json
from datetime import datetime

from django.utils.deprecation import MiddlewareMixin

from .services import log_to_cache

EXCLUDE_PATHS = ["/admin/", "/login/"]


class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if any(request.path.startswith(path) for path in EXCLUDE_PATHS):
            return None
        data = {
            "email": request.user.email if request.user.is_authenticated else None,
            "date": datetime.now(),
            "url": request.path,
        }
        log_to_cache(data)


class VisitCountMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Initialize session key if not already present
        if 'visit_count' not in request.session:
            request.session['visit_count'] = 0

        # Increment the visit count
        request.session['visit_count'] += 1

        # Save the session data
        request.session.modified = True