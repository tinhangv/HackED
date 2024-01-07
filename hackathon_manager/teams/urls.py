from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'core'


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name="teams/login.html", authentication_form=LoginForm), name='login'),
<<<<<<< Updated upstream
=======
    path('view_project/<int:pk>/', views.view_project, name='view_proj'),
    path('dashboard/', views.dashboard, name='dashboard'),
>>>>>>> Stashed changes
]