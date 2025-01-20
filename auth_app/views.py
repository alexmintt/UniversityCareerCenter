from pyexpat.errors import messages

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404

from application.models import Application
from vacancy.models import Vacancy
from .forms import StudentRegistrationForm, StudentLoginForm
from students.models import Student


def index(request):
    vacancies = Vacancy.objects.select_related('company').all().order_by('-created_at')

    # Последние отклики текущего студента
    recent_applications = []
    if request.user.is_authenticated and hasattr(request.user, 'student'):
        student = request.user.student
        recent_applications = Application.objects.filter(student=student).select_related('vacancy').order_by('-created_at')[:3]

    query = request.GET.get('q', '')  # Search query
    company_name = request.GET.get('company', '')  # Company filter
    min_salary = request.GET.get('min_salary', '')  # Minimum salary filter

    # Apply search filter (by title)
    if query:
        vacancies = vacancies.filter(title__icontains=query)

    # Apply company filter
    if company_name:
        vacancies = vacancies.filter(company__name__icontains=company_name)

    # Apply minimum salary filter
    if min_salary:
        vacancies = vacancies.filter(salary__gte=min_salary)

    vacancies = vacancies.values_list('id', 'salary', 'company__name', 'title', 'description')


    # Передача данных в шаблон
    return render(request, 'index.html', {
        'vacancies': vacancies,
        'recent_applications': recent_applications,
    })

def register_view(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            name = request.POST.get('name')
            Student.objects.create(user=user, name=name)
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return HttpResponseRedirect("/")  # Redirect to a protected page after login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = StudentLoginForm()
    return render(request, 'auth/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('main')
