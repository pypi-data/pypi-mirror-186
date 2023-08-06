from django.apps import AppConfig


class NemoReportsConfig(AppConfig):
    name = "NEMO_reports"
    verbose_name = "NEMO Reports"

    def ready(self):
        """
        This code will be run when Django starts.
        """
        pass
