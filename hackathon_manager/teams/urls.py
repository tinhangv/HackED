from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .forms import LoginForm, ProjectDetailsForm

app_name = 'core'


urlpatterns = [
    path('signup/', views.signup, name='signup'),
#     path('project_submission/', auth_views.LoginView.as_view(template_name="teams/project_submission.html", authentication_form=ProjectDetailsForm), name='project_submission'),
    path('project_submission/', views.project_submission, name='project'),
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name="teams/login.html", authentication_form=LoginForm), name='login'),
    path('view_project/<int:pk>/', views.view_project, name='view_proj'),
]