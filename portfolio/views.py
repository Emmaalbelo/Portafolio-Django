from django.shortcuts import render, redirect
from .models import Project
from .forms import Contact

# Create your views here.
def home (request):
    project = Project.objects.all()
    
    return render(request, 'home.html', {'projects': project})
