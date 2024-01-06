from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Team

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

@login_required
def create_team(request):
    if request.method == 'POST':
        team_name = request.POST['team_name']
        new_team = Team(name=team_name)
        new_team.save()
        new_team.members.add(request.user)
        return HttpResponse("Hello World")#redirect('team_detail', team_id=new_team.id)
    return render(request, 'teams/create_team.html')