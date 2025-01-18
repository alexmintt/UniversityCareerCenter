from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.timezone import now

from students.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'name', 'enrollment_year', 'graduation_year', 'faculty', 'resume']
        widgets = {
            'enrollment_year': forms.SelectDateWidget(years=range(2000, 2030)),
            'graduation_year': forms.SelectDateWidget(years=range(2000, 2030)),
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