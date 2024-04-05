from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'trainee_labs'
    verbose_name = 'Trainee Labs'