from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReturnListView.as_view(), name='return_list'),
    path('create/', views.ReturnCreateView.as_view(), name='return_create')
]