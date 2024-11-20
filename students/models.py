from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.IntegerField()
    faculty = models.CharField(max_length=100)
    resume = models.TextField()

    class Meta:
        verbose_name_plural = "Студенты"
        verbose_name = "Студент"