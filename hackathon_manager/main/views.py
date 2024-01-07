from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def main_page(request):
    return render(request, 'main/main_page.html')

@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')