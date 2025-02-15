from django.apps import AppConfig
from django.db.models.signals import post_migrate


class WordsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'words'

    def ready(self):
        from words import schedule
        schedule.start()
