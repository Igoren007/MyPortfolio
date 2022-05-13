from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=250)
    descr = models.CharField(max_length=700)
    link_source = models.CharField(max_length=250)
    link_web = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title


class Skills(models.Model):
    skill = models.CharField(max_length=150)

    def __str__(self):
        return self.skill


class ExperienceCompany(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    years = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.position} at {self.name}.  {self.years}"


class ExperienceItem(models.Model):
    company = models.ForeignKey(ExperienceCompany, on_delete=models.CASCADE)
    responsibility = models.CharField(max_length=500)


class CertificateImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class MyInfo(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.key}: {self.value}'