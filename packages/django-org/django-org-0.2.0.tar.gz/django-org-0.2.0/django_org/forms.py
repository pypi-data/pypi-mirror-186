from django.apps import apps
from django.conf import settings
from django import forms

try:
    from easy_select2 import Select2
except (ImportError, ModuleNotFoundError):
    Select2 = forms.Select

from django_org.settings import DJANGO_ORG_ENTERPRISE


__all__ = (
    'EnterpriseAdminForm',
)


class EnterpriseAdminForm(forms.ModelForm):
    class Meta:
        model = apps.get_model(DJANGO_ORG_ENTERPRISE)
        fields = '__all__'
        widgets = {
            'time_zone': Select2()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['time_zone'].default = settings.TIME_ZONE
