from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('historias_list/', views.historias_list, name='historias_list'),
    path('', views.historiaClinicas_view, name='historiaClinicas_view'),
    path('<int:pk>', views.historiaClinica_view, name='historiaClinica_view'),
    path('<int:pk>/detail/', views.historia_detail, name='historia_detail'),

]
