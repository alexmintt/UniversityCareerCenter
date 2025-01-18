import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg
from django.urls import reverse
from django.utils import timezone

from vacancy.models import Vacancy


class Faculty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Факультеты"
        verbose_name = "Факультет"


class Resume(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)
    skills = models.TextField()
    experience = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.created_at}"

    class Meta:
        ordering = ['title']

        verbose_name_plural = "Резюме"
        verbose_name = "Резюме"


class StudentManager(models.Manager):
    def average_graduation_year(self):
         return self.aggregate(Avg('graduation_year'))


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    enrollment_year = models.DateField(null=True, blank=True)
    graduation_year = models.DateField(null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now())
    vacancies = models.ManyToManyField(Vacancy, through="application.Application")
    resume = models.OneToOneField(Resume, null=True, blank=True, on_delete=models.SET_NULL)

    objects = StudentManager()


    def save(self, *args, **kwargs):
        # Проверка и автоматическое заполнение поля graduation_year
        if self.enrollment_year and not self.graduation_year:
            self.graduation_year = self.enrollment_year + timedelta(days=4 * 365)

        # Приведение имени к формату "Первая буква заглавная"
        if self.name:
            self.name = self.name.title()

        # Вызов метода full_clean() для валидации данных
        self.full_clean()  # Проверит clean_<fieldname>(), если есть
        super().save(*args, **kwargs)  # Вызов стандартного сохранения


    def get_absolute_url(self):
        return reverse('student-detail-view', args=[str(self.id)])

    def is_graduated(self):
        return datetime.datetime.now().date() > self.graduation_year

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']        
        verbose_name_plural = "Студенты"
        verbose_name = "Студент"
