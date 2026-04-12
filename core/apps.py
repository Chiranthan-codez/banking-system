import os
from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        # Only start the pinger if not in reloader thread (Django dev server)
        # and if PING_URL is set.
        if os.environ.get('RUN_MAIN') != 'true':
            from .cron import start_pinger
            start_pinger()
