from django import forms
from django.forms import inlineformset_factory
from .models import DisputeCase

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class DisputeCaseForm(forms.ModelForm):
    class Meta:
        model = DisputeCase
        fields = ['order', 'return_request', 'dispute_reason', 'status', 'resolved_at', 'resolution_notes']
        widgets = {
            'dispute_reason': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('order', css_class='form-group col-md-6'),
                Column('return_request', css_class='form-group col-md-6'),
            ),
            Column('dispute_reason', css_class='form-group'),
            Column('status', css_class='form-group'),
            Submit('submit', 'Create Dispute Case')
        )
