from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.timezone import now

from students.models import Student, Resume, Certificate


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['created_at']
        fields = ['user', 'name', 'enrollment_year', 'graduation_year', 'faculty', 'avatar']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),  # Avatar widget
            'user': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the student\'s full name',
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
            'user': 'Linked User',
            'name': 'Full Name',
            'enrollment_year': 'Enrollment Year',
            'graduation_year': 'Graduation Year',
            'faculty': 'Faculty',
        }
        help_texts = {
            'user': 'Select the associated user account.',
            'enrollment_year': 'Choose the year the student enrolled.',
            'graduation_year': 'Choose the year the student graduated (if applicable).',
            'faculty': 'Select the faculty the student belongs to.',
        }
        error_messages = {
            'name': {
                'required': 'The student name is required.',
                'max_length': 'Name cannot exceed 100 characters.',
            },
            'enrollment_year': {
                'invalid': 'Please select a valid enrollment year.',
            },
            'graduation_year': {
                'invalid': 'Please select a valid graduation year.',
            },
        }

    class Media:
        css = {
            'all': ('css/form.css')
        }

    def clean_enrollment_year(self):
        enrollment_year = self.cleaned_data.get('enrollment_year')
        if enrollment_year and enrollment_year.year > now().year:
            raise forms.ValidationError("Enrollment year cannot be in the future.")
        return enrollment_year

    def clean_graduation_year(self):
        enrollment_year = self.cleaned_data.get('enrollment_year')
        graduation_year = self.cleaned_data.get('graduation_year')
        if graduation_year and enrollment_year and graduation_year < enrollment_year:
            raise forms.ValidationError("Graduation year cannot be earlier than enrollment year.")
        return graduation_year

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['name', 'file', 'issued_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Certificate name'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'issued_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'text', 'skills', 'experience', 'portfolio_url']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title of the resume',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the full resume text',
                'rows': 5,
            }),
            'experience': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your experience',
                'rows': 5,
            }),
            'skills': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your skills',
            }),
            'portfolio_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter portfolio URL'}),

        }
        labels = {
            'title': 'Resume Title',
            'text': 'Resume Text',
            'skills': 'Skills',
            'experience': 'Experience',
        }
        help_texts = {
            'skills': 'Use "," to divide.',
        }
        error_messages = {
            'title': {
                'required': 'Please provide a title for the resume.',
                'max_length': 'Title cannot exceed 150 characters.',
            },
            'text': {
                'required': 'Please provide the full text for the resume.',
            },
        }
