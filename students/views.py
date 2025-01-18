from pyexpat.errors import messages

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect, render, get_object_or_404

from students.forms import StudentForm
from students.models import Student


def list_view(request):
    students = Student.objects.prefetch_related('vacancies', 'resume').select_related('faculty')
    paginator = Paginator(students, 5)

    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/list.html', {'students': students})


def detail_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()

    return render(request, 'students/detail.html', {'student': student, 'form': form})


def create_view(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student-list-view')
    return render(request, 'students/create.html', {'form': form})

def delete_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student-list-view')
    return render(request, 'students/delete.html', {'student': student})
