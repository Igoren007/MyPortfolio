from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from portfolio.models import Skills, ExperienceCompany, ExperienceItem, Project, CertificateImage, MyInfo


def index(request):
    title = 'Igor Garmatenko - Portfolio'
    name = 'Igor Garmatenko'
    about_me = 'I am looking for a position as a back-end web developer. In recent years, I have worked as a system administrator. There is no commercial experience in development, but there is a technical background, a great desire to learn new things and develop. I took training courses on Stepik, Udemy, Coursera. You can see my pet projects below.'
    university = 'Donetsk National Technical University'
    faculty = 'Faculty of Computer Information Technologies and Automation'
    speciality = 'Speciality: Control systems and automation'
    years = '2010 - 2016'

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
