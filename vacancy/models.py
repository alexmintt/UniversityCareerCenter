from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()

    class Meta:
        verbose_name_plural = "Вакансии"
        verbose_name = "Вакансия"