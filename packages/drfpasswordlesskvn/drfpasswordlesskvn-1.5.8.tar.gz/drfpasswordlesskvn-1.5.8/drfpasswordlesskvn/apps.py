from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class DrfpasswordlessConfig(AppConfig):
    name = 'drfpasswordlesskvn'
    verbose = _("DRF Passwordless")

    def ready(self):
        import drfpasswordlesskvn.signals
