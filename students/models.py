from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.IntegerField()
    faculty = models.CharField(max_length=100)
    resume = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Студенты"
        verbose_name = "Студент"