from django import forms
from django.forms import inlineformset_factory
from .models import ReturnRequest

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class ReturnRequestForm(forms.ModelForm):
    class Meta:
        model = ReturnRequest
        fields = ['order', 'return_tracking_number', 'reason', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('order', css_class='form-group col-md-6 mb-0'),
                Column('return_tracking_number', css_class='form-group col-md-6 mb-0'),
                Column('reason', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('status', css_class='form-group col-md-6 mb-0'),
                Submit('submit', 'Create Return Request')
            ),
        )