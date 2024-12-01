from django.shortcuts import render

from django.views.generic import ListView, CreateView

from .models import Order
from .forms import OrderForm

from django.urls import reverse_lazy

class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_create.html'
    success_url = reverse_lazy('order_list')