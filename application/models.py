from django.db import models

from students.models import Student
from vacancy.models import Vacancy


class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,
                              choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])

    class Meta:
        verbose_name_plural = "Заявки"
        verbose_name = "Заявка"
