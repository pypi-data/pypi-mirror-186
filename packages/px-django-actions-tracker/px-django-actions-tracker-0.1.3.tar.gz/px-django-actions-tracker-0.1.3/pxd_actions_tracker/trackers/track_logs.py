import logging
from typing import Optional
from copy import copy
from px_domains import Domain

from django.conf import settings
from django.utils.module_loading import import_string


__all__ = 'EXCEPTION_LOG_DOMAIN', 'ActionsTrackerHandler',

logger = logging.getLogger(__name__)
EXCEPTION_LOG_DOMAIN = Domain('LOG')


class ActionsTrackerHandler(logging.Handler):
    domain: Domain = EXCEPTION_LOG_DOMAIN

    def __init__(self, domain: Optional[Domain] = None, reporter_class=None):
        super().__init__()
        self.domain = domain if domain is not None else self.domain
        self.reporter_class = import_string(
            reporter_class
            or
            getattr(settings, 'DEFAULT_EXCEPTION_REPORTER', None)
            or
            'django.views.debug.ExceptionReporter'
        )

    def emit(self, record):
        try:
            request = record.request
        except Exception:
            request = None

        # Since we add a nicely formatted traceback on our own, create a copy
        # of the log record without the exception data.
        no_exc_record = copy(record)
        no_exc_record.exc_info = None
        no_exc_record.exc_text = None

        if record.exc_info:
            exc_info = record.exc_info
        else:
            exc_info = (None, record.getMessage(), None)

        reporter = self.reporter_class(request, is_email=False, *exc_info)
        message = self.format(no_exc_record)
        traceback = reporter.get_traceback_text()
        self.log(
            self.domain | record.levelname | record.name,
            '%s: %s' % (record.levelname, message),
            {
                'request': self.resolve_request_data(request) if request else None,
                'message': message,
                'traceback': traceback,
            }
        )

    def resolve_request_data(self, request):
        from . import track_views

        return track_views.resolve_request_data(request)

    def log(self, domain, message, detail):
        from ..cases import log

        return log(domain, message.format(**detail), detail=detail)
