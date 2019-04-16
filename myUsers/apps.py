from django.apps import AppConfig


class MyusersConfig(AppConfig):
    name = 'myUsers'

    def ready(self):
        import myUsers.signals