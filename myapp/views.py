from django.shortcuts import render
from .models import About, Skill, Project, ProjectType


def get_home(request):
    project_types = ProjectType.objects.all()
    about = About.objects.all().first()
    return render(request, 'index.html', {"about": about, "project_types": project_types})


def get_about(request):
    project_types = ProjectType.objects.all()
    about = About.objects.all().first()
    skills = Skill.objects.all()
    return render(request, 'about.html', {"about": about, "skills": skills, "project_types": project_types})


def get_portfolio(request):
    project_types = ProjectType.objects.all()
    projects = Project.objects.filter(
        project_type__url='portfolio').filter(active=True).order_by('-date')
    about = About.objects.all().first()
    return render(request, 'reile.html', {"projects": projects, "about": about, "project_types": project_types})


def get_logos(request):
    project_types = ProjectType.objects.all()
    projects = Project.objects.filter(
        active=True).filter(project_type__url='logo').order_by('-date')
    about = About.objects.all().first()
    return render(request, 'logo.html', {"projects": projects, "about": about, "project_types": project_types})


def get_contact(request):
    project_types = ProjectType.objects.all()
    about = About.objects.all().first()
    return render(request, 'contact.html', {"about": about, "project_types": project_types})
