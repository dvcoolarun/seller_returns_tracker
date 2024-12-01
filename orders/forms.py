from django import forms
from django.forms import inlineformset_factory
from .models import Order, OrderItem

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_id', 'customer_name', 'customer_email', 'total_amount', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('order_id', css_class='form-group col-md-6 mb-0'),
                Column('customer_name', css_class='form-group col-md-6 mb-0'),
                Column('customer_email', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('total_amount', css_class='form-group col-md-6 mb-0'),
                Column('status', css_class='form-group col-md-6 mb-0'),
            ),
            Submit('submit', 'Save Order')
        )
    