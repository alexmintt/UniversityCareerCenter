from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']        

        verbose_name_plural = "Компании"
        verbose_name = "Компания"


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

        verbose_name_plural = "Вакансии"
        verbose_name = "Вакансия"
