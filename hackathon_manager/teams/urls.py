from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_team, name='create_team'),
    path('',views.index)
]