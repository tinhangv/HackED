from django.urls import path
from . import views

app_name = 'chatroom'

urlpatterns = [
    path('channels/', views.channel_list, name='channel_list'),
    path('channels/<int:channel_id>/', views.channel_message, name='channel_message'),
]