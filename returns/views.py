from django.shortcuts import render

from django.views.generic import ListView, CreateView

from .models import ReturnRequest
from .forms import ReturnRequestForm

from django.urls import reverse_lazy

class ReturnListView(ListView):
    model = ReturnRequest
    template_name = 'returns/return_list.html'
    context_object_name = 'returns'


class ReturnCreateView(CreateView):
    model = ReturnRequest
    form_class = ReturnRequestForm
    template_name = 'returns/return_create.html'
    success_url = reverse_lazy('return_list')