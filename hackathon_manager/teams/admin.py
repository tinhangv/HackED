from django.contrib import admin
from .models import Team, Members, ProjectDetails, Submission

# Register your models here.
admin.site.register(Team)
admin.site.register(Members)
admin.site.register(ProjectDetails)
admin.site.register(Submission)
