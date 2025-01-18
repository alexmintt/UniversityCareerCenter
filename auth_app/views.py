from pyexpat.errors import messages

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect, render, get_object_or_404

from .forms import StudentRegistrationForm, StudentLoginForm
from students.models import Student




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
                return redirect('vacancy-list-view')  # Redirect to a protected page after login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = StudentLoginForm()
    return render(request, 'auth/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('vacancy-list-view')
