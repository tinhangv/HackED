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

<<<<<<< Updated upstream
=======
def project_submission(request):
    if request.method == 'POST':
        form = ProjectDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            team = form.cleaned_data['team_name']
            user = request.user
            if ProjectDetails.objects.filter(team_name=team).exists():
                return render(request, 'error.html', {'error': 'Only one member from a team can submit the project details.'})
            form.save()
            return redirect('view_project')
    else:
        form = ProjectDetailsForm()
    return render(request, 'teams/project_submission.html', {'form': form})


def view_project(request, pk):
    project = get_object_or_404(ProjectDetails, pk=pk)
#    project = ProjectDetails.objects.get(id=3)
    return render(request, 'view_project.html', {'project': project})

#    user_team = request.user.members.team  # Assuming you have a user associated with a team
#    projects = ProjectDetails.objects.filter(team=user_team)
#    return render(request, 'teams/view_project.html', {'projects': projects})

@login_required
def dashboard(request):
    # Your logic to display the dashboard
    return render(request, 'dashboard.html')

'''
def project_submission(request):
    if request.method == 'POST':
        form = ProjectDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            team = Team.objects.get(id=int(form.cleaned_data['team_name']))
            user = request.user
            if ProjectDetails.objects.filter(team=team).exists():
                return render(request, 'error.html', {'error': 'Only one member from a team can submit the project details.'})
            form.save()
            return redirect('view_project')
    else:
        form = ProjectDetailsForm()
    return render(request, 'teams/project_submission.html', {'form': form})
'''
'''
def project_submission(request):
#    team_queryset = Team.objects.all()
    if request.method == 'POST':
        form = ProjectDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            team_name = form.cleaned_data['team_name']
#            TeamIns = Team()
#            team = get_object_or_404(Team, name=team_name)
            if ProjectDetails.objects.filter(team_name=team_name).exists():
                return render(request, 'error.html', {'error': 'Only one member from a team can submit the project details.'})
            form.save()
            return redirect('view_project')
    else:
        form = ProjectDetailsForm()
    return render(request, 'teams/project_submission.html', {'form': form})
'''
>>>>>>> Stashed changes

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