from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from portfolio.models import Skills, ExperienceCompany, ExperienceItem, Project


def index(request):
    title = 'Igor Garmatenko - Portfolio'
    name = 'Igor Garmatenko'
    about_me = 'lorem a;sljd fas;kjda skjasl kdj asldkjsa lkdjaslkdj askldjask ldjalskjd fas;kjda skjasl kdj asldkjsa lkdjaslkdj askldjask ldjalskjd'
    university = 'Donetsk National Technical University'
    faculty = 'Faculty of Computer Information Technologies and Automation'
    speciality = 'Speciality: Control systems and automation'
    years = '2010 - 2016'

    skills = Skills.objects.all()
    companies = ExperienceCompany.objects.all()
    responsibilities = ExperienceItem.objects.all()
    projects = Project.objects.all()

    context = {
        'title': title,
        'name': name,
        'about_me': about_me,
        'skills': skills,
        'projects': projects,
        'companies': companies,
        'responsibilities': responsibilities,
        'university': university,
        'faculty': faculty,
        'speciality': speciality,
        'years': years,
    }
    return render(request, 'portfolio/index.html', context=context)
