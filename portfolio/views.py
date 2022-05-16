from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from portfolio.models import Skills, ExperienceCompany, ExperienceItem, Project, CertificateImage, MyInfo


def index(request):

    skills = Skills.objects.all()
    companies = ExperienceCompany.objects.all()
    responsibilities = ExperienceItem.objects.all()
    projects = Project.objects.all()
    certificates  = CertificateImage.objects.all()

    my_info = list(MyInfo.objects.all())
    dic = {}
    for item in my_info:
        s = str(item).split(': ')
        dic[s[0]] = s[1]

    context = {
        'title': dic['title'],
        'name': dic['name'],
        'about_me': dic['about_me'],
        'skills': skills,
        'projects': projects,
        'companies': companies,
        'responsibilities': responsibilities,
        'university': dic['university'],
        'faculty': dic['faculty'],
        'speciality': dic['speciality'],
        'years': dic['years'],
        'certificates': certificates
    }

    return render(request, 'portfolio/index.html', context=context)
