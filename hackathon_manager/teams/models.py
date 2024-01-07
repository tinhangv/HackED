from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    team_members = models.ManyToManyField(User, related_name='members')

class Members(models.Model):
    user = models.ManyToManyField(User, related_name='user')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team')
    role = models.CharField(max_length=200, choices=[
            ('team_leader', 'Team Leader'),
            ('team_member', 'Team Member'),
        ], default='team_member')

class ProjectDetails(models.Model):
#    team_name = ModelChoiceField(queryset=Team.objects.all(), empty_label=None)
    team_name = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='team_name')
    project_name = models.CharField(max_length=50)
    github_link = models.URLField(blank=False, null=False)
    project_description = models.CharField(max_length=1500)

    def __str__(self):
        return f"{self.project_name}"

class Submission(models.Model):
    team_member = models.ForeignKey(Members, on_delete=models.CASCADE)
    project = models.ForeignKey(ProjectDetails, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_member.user.username} - {self.project.name}"