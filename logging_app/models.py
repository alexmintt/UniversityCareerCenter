from django.db import models
from django.contrib.auth.models import User


class UserLog(models.Model):
    email = models.CharField(max_length=64, null=True)
    date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.email} - {self.date}"
