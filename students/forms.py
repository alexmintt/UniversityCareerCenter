from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.timezone import now

from students.models import Student, Resume, Certificate


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['created_at']
        fields = [ 'name', 'enrollment_year', 'graduation_year', 'faculty', 'avatar']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),  # Виджет для аватара
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите полное имя студента',
            }),
            'enrollment_year': forms.SelectDateWidget(
                years=range(2000, 2030),
                attrs={'class': 'form-control'}
            ),
            'graduation_year': forms.SelectDateWidget(
                years=range(2000, 2030),
                attrs={'class': 'form-control'}
            ),
            'faculty': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'ФИО',
            'enrollment_year': 'Год поступления',
            'graduation_year': 'Год выпуска',
            'faculty': 'Факультет',
        }
        help_texts = {
            'enrollment_year': 'Выберите год поступления студента.',
            'graduation_year': 'Выберите год выпуска студента (если применимо).',
            'faculty': 'Выберите факультет студента.',
        }
        error_messages = {
            'name': {
                'required': 'Имя студента обязательно.',
                'max_length': 'Имя не может превышать 100 символов.',
            },
            'enrollment_year': {
                'invalid': 'Пожалуйста, выберите корректный год поступления.',
            },
            'graduation_year': {
                'invalid': 'Пожалуйста, выберите корректный год выпуска.',
            },
        }

    class Media:
        css = {
            'all': ['css/form.css']
        }

    def clean_enrollment_year(self):
        enrollment_year = self.cleaned_data.get('enrollment_year')
        if enrollment_year and enrollment_year.year > now().year:
            raise forms.ValidationError("Год поступления не может быть в будущем.")
        return enrollment_year

    def clean_graduation_year(self):
        enrollment_year = self.cleaned_data.get('enrollment_year')
        graduation_year = self.cleaned_data.get('graduation_year')
        if graduation_year and enrollment_year and graduation_year < enrollment_year:
            raise forms.ValidationError("Год выпуска не может быть раньше года поступления.")
        return graduation_year


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['name', 'file', 'issued_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название сертификата'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'issued_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'name': 'Название сертификата',
            'file': 'Файл сертификата',
            'issued_date': 'Дата выдачи',
        }
        help_texts = {
            'name': 'Введите название сертификата.',
            'file': 'Загрузите файл сертификата.',
            'issued_date': 'Выберите дату выдачи сертификата.',
        }
        error_messages = {
            'name': {
                'required': 'Название сертификата обязательно.',
            },
            'file': {
                'required': 'Файл сертификата обязателен.',
            },
        }


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'text', 'skills', 'experience', 'portfolio_url']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название резюме',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите полный текст резюме',
                'rows': 5,
            }),
            'experience': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш опыт работы',
                'rows': 5,
            }),
            'skills': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваши навыки',
            }),
            'portfolio_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Введите URL портфолио'}),
        }
        labels = {
            'title': 'Название резюме',
            'text': 'Текст резюме',
            'skills': 'Навыки',
            'experience': 'Опыт работы',
            'portfolio_url': 'URL портфолио',
        }
        help_texts = {
            'skills': 'Используйте "," для разделения навыков.',
        }
        error_messages = {
            'title': {
                'required': 'Пожалуйста, укажите название для резюме.',
                'max_length': 'Название не может превышать 150 символов.',
            },
            'text': {
                'required': 'Пожалуйста, укажите полный текст резюме.',
            },
        }