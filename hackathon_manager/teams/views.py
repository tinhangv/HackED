from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Team
from .forms import SignupForm

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
    else:
        form = SignupForm()

    return render(request, 'teams/signup.html', {
        'form': form
    })

def submit_team(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        team_members = [
            request.POST.get('team_member_1'),
            request.POST.get('team_member_2'),
            request.POST.get('team_member_3'),
            request.POST.get('team_member_4'),
        ]
        # Now you can process the form data, save it to the database, etc.
        
        # After processing, you might want to redirect to a new page
        return redirect('submit_team')  # Replace 'success_page' with your actual success page URL name
    
    # If method is GET, just render the empty form
    return render(request, 'teamRegister.html')

'''
@login_required
def create_team(request):
    if request.method == 'POST':
        team_name = request.POST['team_name']
        new_team = Team(name=team_name)
        new_team.save()
        new_team.members.add(request.user)
        return HttpResponse("Hello World")#redirect('team_detail', team_id=new_team.id)
    return render(request, 'teams/create_team.html')
'''