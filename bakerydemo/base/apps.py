from django.apps import AppConfig


class BaseAppConfig(AppConfig):
    name = "bakerydemo.base"

    def ready(self):
        from . import signals
