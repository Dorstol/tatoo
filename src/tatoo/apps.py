from django.apps import AppConfig


class TattoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tatoo"

    def ready(self):
        import accounts.signals
