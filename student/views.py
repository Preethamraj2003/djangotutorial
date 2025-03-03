from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from .models import student
from django.db.models import Avg
from student.models import Result, student, semester
from .forms import StudentSearchForm

    

def stu_index(request):
    student_list = student.objects.all()
    template = loader.get_template("student.html")
    context = {
        "latest_question_list": student_list,
    }
    return HttpResponse(template.render(context, request))


def student_sem(request,st_id) : 
    average_marks =Result.objects.filter(student_id=st_id).values('student_id', 'sem_id').annotate(average_marks=Avg('marks')).order_by('student_id', 'sem_id')
    template = loader.get_template("student_sem.html")
    context = {'average_marks': average_marks}
    return HttpResponse(template.render(context, request))


def student_results_view(request):
    results = None
    student_instance = None
    average = None
    no_usn_found = False

    if request.method == 'POST':
        form = StudentSearchForm(request.POST)
        
        if form.is_valid():
            usn = form.cleaned_data['usn']
            sem_id = form.cleaned_data['sem_id']
            
            try:
                student_instance = student.objects.get(usn=usn)
            except student.DoesNotExist:
                student_instance = None
                no_usn_found = True  

            if student_instance:
                results = Result.objects.filter(student=student_instance, sem_id=sem_id)
                
                if results.exists():
                    total_marks = sum(result.marks for result in results)
                    average = total_marks / len(results)
    else:
        form = StudentSearchForm()

    return render(request, 'forminput.html', {
        'form': form,
        'results': results,
        'student': student_instance,
        'average': average,
        'no_usn_found': no_usn_found  
    })

def student_results_dropdown(request):
    results = None
    student_instance = None
    average = None
    no_usn_found = False
    results_with_subjects = []  

    usn = request.GET.get('usn')
    sem_id = request.GET.get('sem_id')
    
    students = student.objects.all()
    semesters = semester.objects.all()

    if usn and sem_id:
        try:
            student_instance = student.objects.get(usn=usn)
        except student.DoesNotExist:
            student_instance = None
            no_usn_found = True  

        if student_instance:
            results = Result.objects.filter(student=student_instance, sem_id=sem_id)
            
            if results.exists():
                total_marks = sum(result.marks for result in results)
                average = total_marks / len(results)
                
                results_with_subjects = []
                for result in results:
                    subject_info = {
                        'subject_id': result.sub.id,  
                        'subject_name': result.sub.name,  
                        'marks': result.marks
                    }
                    results_with_subjects.append(subject_info)

    else:
        no_usn_found = True

    return render(request, 'studentdropdown.html', {
        'students': students,
        'semesters': semesters,
        'results_with_subjects': results_with_subjects,
        'student': student_instance,
        'average': average,
        'no_usn_found': no_usn_found,  
    })





