from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import DisputeCase
from .forms import DisputeCaseForm


class DisputeCaseListView(ListView):
    model = DisputeCase
    template_name = 'disputes/dispute_list.html'
    context_object_name = 'dispute_cases'

    def get_queryset(self):
        return DisputeCase.objects.all().select_related('order', 'return_request').all();


def create_dispute_case(request):
    form = DisputeCaseForm()
    
    if request.method == 'POST':
        form = DisputeCaseForm(request.POST)
        
        if form.is_valid():
            dispute_case = form.save()

            context = {
                'dispute_cases': DisputeCase.objects.all()
            }
        else:
            context = {'form': form}
    
        return render(request, 'disputes/partials/dispute_list_body.html', context)
    
    context = {'form': DisputeCaseForm()}
    return render(request, 'disputes/modals/create_dispute_case.html', context)