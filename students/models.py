import datetime

from django.contrib.auth.models import User
from django.db import models

from vacancy.models import Vacancy


class Faculty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Факультеты"
        verbose_name = "Факультет"


class Resume(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    skills = models.TextField()
    experience = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.created_at}"

    class Meta:
        verbose_name_plural = "Резюме"
        verbose_name = "Резюме"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    enrollment_year = models.DateField()
    graduation_year = models.DateField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    vacancies = models.ManyToManyField(Vacancy, through='application.Application')
    resume = models.OneToOneField(Resume, null=True, on_delete=models.SET_NULL)

    def is_graduated(self):
        return datetime.datetime.now().date() > self.graduation_year

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Студенты"
        verbose_name = "Студент"
