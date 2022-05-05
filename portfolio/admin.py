from django.contrib import admin

# Register your models here.
from portfolio.models import *

admin.site.register(Project)
admin.site.register(Skills)
admin.site.register(ExperienceCompany)
admin.site.register(ExperienceItem)