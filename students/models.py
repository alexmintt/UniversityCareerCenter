import datetime

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


class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment_year = models.DateField()
    graduation_year = models.DateField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    resume = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    vacancies = models.ManyToManyField(Vacancy, through='application.Application')

    def is_graduated(self):
        return datetime.datetime.now().date() > self.graduation_year


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Студенты"
        verbose_name = "Студент"