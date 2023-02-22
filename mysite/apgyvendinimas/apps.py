from django.apps import AppConfig


class ApgyvendinimasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apgyvendinimas'

    def ready(self):
        from .signals import create_profile, save_profile
