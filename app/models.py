from django.db import models

class CustomUser(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(blank=True, max_length=100, verbose_name='Name')
    password = models.CharField(max_length=20, verbose_name='Password')
    def __str__(self):
        return self.email

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Company')
    field = models.CharField(max_length=100, verbose_name='Field of Internship')
    stipend = models.FloatField(verbose_name='Stipend')
    duration = models.CharField(max_length=50, verbose_name='Duration')
    location = models.CharField(max_length=100, verbose_name='Location')
    def __str__(self):
        return self.name

class Application(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='Company')
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, verbose_name='User')
    q1 = models.TextField(verbose_name='Question 1')
    q2 = models.TextField(verbose_name='Question 2')
    q3 = models.TextField(verbose_name='Question 3')
    def __str__(self):
        return self.company.name+'-'+self.user.name

class Resume(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, verbose_name='User')
    resume = models.FileField(upload_to='Resume', verbose_name='Resume')
    def __str__(self):
        return self.user.name
