from django.shortcuts import render, get_object_or_404
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'personalPortfolio/home.html', context={'projects': projects})


def project_details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "personalPortfolio/project_details.html", {'project': project})
