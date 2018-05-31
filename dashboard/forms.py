from django import forms
from crispy_forms.helper import FormHelper

from .models import Building

class BuildingForm(forms.Form):

    bdbid = forms.ModelChoiceField(queryset=Building.objects.all())

    def __init__(self, retrofit_type='Pump', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bdbid'].queryset = Building.objects.filter(retrofit_type=retrofit_type)

        self.helper = FormHelper()
        self.helper.form_id = '{}-dropdown'.format(retrofit_type.lower())
        self.helper.form_class = 'selectpicker'
        self.helper.form_method = 'get'
