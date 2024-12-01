from django.urls import path
from . import views

urlpatterns = [
    path('', views.DisputeCaseListView.as_view(), name='dispute_case_list'),
    path('create/', views.create_dispute_case, name='create_dispute_case_modal'),
]