from django.apps import AppConfig


class QrAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    def ready(self):
        from .cron import run
        run()

