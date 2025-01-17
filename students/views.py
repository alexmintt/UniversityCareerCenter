from pyexpat.errors import messages

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404

from application.models import Application
from students.forms import StudentForm, ResumeForm, CertificateForm
from students.models import Student, Resume, Certificate, Faculty
from vacancy.models import Vacancy


def index(request):
    vacancies = Vacancy.objects.select_related('company').all()


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

    faculties_with_counts = Faculty.objects.annotate(student_count=Count('student')).values_list('name',
                                                                                                 'student_count')

    total = Student.objects.count()
    visit_count = request.session.get('visit_count', 0)
    return render(request, 'students/list.html', {'students': students, 'total': total, "visit_count": visit_count,
                                                  'faculties': faculties_with_counts})


@login_required
def detail_view(request):
    student = Student.objects.get(user=request.user)
    applications = Application.objects.filter(student=student)
    return render(request, 'students/detail.html', {'student': student, 'applications': applications})


@login_required
def edit_view(request):
    student = Student.objects.get(user=request.user)

    form = StudentForm(request.POST or None, request.FILES or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student-profile')
    return render(request, 'students/update.html', {'form': form})


def create_view(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/students/')
    return render(request, 'students/create.html', {'form': form})


def delete_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student-list-view')
    return render(request, 'students/delete.html', {'student': student})


@login_required
def create_or_update_resume_view(request, resume_id=None):
    student = Student.objects.get(user=request.user)
    if resume_id:
        resume = get_object_or_404(Resume, id=resume_id)
        success_message = "Resume updated successfully!"

    else:
        resume = None
        success_message = "Resume created successfully!"

    resume_form = ResumeForm(request.POST, instance=resume)
    certificate_form = CertificateForm()

    if request.method == 'POST':
        # Handle ResumeForm
        if 'resume_form' in request.POST:
            resume_form = ResumeForm(request.POST, instance=resume)
            if resume_form.is_valid():
                resume = resume_form.save()
                student.resume.add(resume)
                return redirect('resume_edit', resume.pk)  # Redirect after successful save

        # Handle CertificateForm
        elif 'certificate_form' in request.POST:
            certificate_form = CertificateForm(request.POST, request.FILES)
            if certificate_form.is_valid():
                certificate = certificate_form.save(commit=False)
                certificate.resume = resume
                certificate.save()
                return redirect(request.path)  # Refresh the page after uploading

    else:
        resume_form = ResumeForm(instance=resume)
        certificate_form = CertificateForm()

    certificates = Certificate.objects.filter(resume=resume)  # Fetch all certificates

    return render(request, 'students/resume/create_or_update.html', {
        'resume_form': resume_form,
        'student': student,
        'certificate_form': certificate_form,
        'certificates': certificates,
        'resume': resume,
    })


def delete_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    resume.delete()
    return redirect("student-profile")


def delete_certificate(request, pk):
    if request.method == 'POST':
        certificate = get_object_or_404(Certificate, id=pk)
        certificate.delete()
        messages.success(request, f"Certificate '{certificate.name}' has been deleted successfully.")
    return redirect(request.META.get('HTTP_REFERER', '/'))  # Redirect to the previous page


def student_search(request):
    query = request.GET.get('q', '')  # Get the search query
    faculty_id = request.GET.get('faculty', '')  # Get the selected faculty filter
    resume_title = request.GET.get('resume_title', '')  # Get the resume title filter
    enrollment_year = request.GET.get('enrollment_year', '')  # Get the enrollment year filter

    # Base QuerySet
    students = Student.objects.all()

    # Apply search query
    if query:
        students = students.filter(name__contains=query)

    # Apply faculty filter
    if faculty_id:
        students = students.filter(faculty__id=faculty_id)

    # Apply enrollment year filter
    if enrollment_year:
        students = students.filter(enrollment_year__year=enrollment_year)

    # Apply resume title filter
    if resume_title:
        students = students.filter(resume__title__icontains=resume_title)

    # Get all faculties for the filter dropdown
    faculties = Faculty.objects.values('id', 'name')

    return render(request, 'students/search.html', {
        'students': students[:10],
        'faculties': faculties,
        'query': query,
        'selected_faculty': faculty_id,
        'selected_year': enrollment_year,
    })
