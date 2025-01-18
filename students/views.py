from pyexpat.errors import messages

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404

from students.forms import StudentForm, ResumeForm, CertificateForm
from students.models import Student, Resume, Certificate


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

    total = Student.objects.count()
    visit_count = request.session.get('visit_count', 0)
    return render(request, 'students/list.html', {'students': students, 'total': total, "visit_count": visit_count})


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
        return HttpResponseRedirect('/students/')
    return render(request, 'students/create.html', {'form': form})


def delete_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student-list-view')
    return render(request, 'students/delete.html', {'student': student})


def create_or_update_resume_view(request, student_id, resume_id=None):
    student = Student.objects.get(pk=student_id)
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
                return redirect('resume_edit', student_id, resume.pk)  # Redirect after successful save

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


def delete_resume(request, student_id, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    resume.delete()
    return redirect("student-detail-view", student_id)


def delete_certificate(request, pk):
    if request.method == 'POST':
        certificate = get_object_or_404(Certificate, id=pk)
        certificate.delete()
        messages.success(request, f"Certificate '{certificate.name}' has been deleted successfully.")
    return redirect(request.META.get('HTTP_REFERER', '/'))  # Redirect to the previous page
