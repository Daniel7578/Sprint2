from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.historiaClinicas_view, name='historiaClinicas_view'),
    path('<int:pk>', views.historiaClinica_view, name='historiaClinica_view')
]