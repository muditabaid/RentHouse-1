from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('modal',views.modal, name='modal'),
    
]