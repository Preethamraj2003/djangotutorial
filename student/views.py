from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from .models import student
from django.db.models import Avg
from student.models import Result, student, semester
from .forms import StudentSearchForm
from rest_framework import  viewsets
from rest_framework.response import Response
from student.models import semester,subject, student, Result
from student.serializers import SemesterSerializer, subjectSerializer, studentSerializer, ResultSerializer
    

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
    semFound = False
    if request.method == 'POST':
        form = StudentSearchForm(request.POST)
        
        if form.is_valid():
            usn = form.cleaned_data['usn']
            sem_id = int(form.cleaned_data['sem_id'])
            if sem_id< 1 and sem_id>8 : 
                semFound=True
            
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
        'no_usn_found': no_usn_found,
        'semFound' : semFound
    })

def student_results_dropdown(request):
    results = None
    student_instance = None
    average = None
    no_usn_found = False
    semFound = False
    results_with_subjects = [] 

    parametersAllowed = {'usn','sem_id'}
 
    invalidParameters = set(request.GET.keys()) - parametersAllowed
    if invalidParameters:
        return HttpResponse(f"Invalid query parameters: {invalidParameters}")
    

    usn = request.GET.get('usn')
    sem_id = int(request.GET.get('sem_id'))
    
    if sem_id >8 and sem_id<1 :
        semFound = True
    
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
        'semFound' : semFound 
    })

class SemesterviewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = semester.objects.all()
    serializer_class = SemesterSerializer

class subjectviewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = subject.objects.all()
    serializer_class = subjectSerializer

class studentviewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = student.objects.all()
    serializer_class = studentSerializer

    def studentmarks(self, request, **kwargs):
        usn = self.kwargs.get('usn')
        sem = self.kwargs.get('sem')

        student_obj = student.objects.filter(usn=usn).first()
        if student_obj is None:
            raise Http404("Student not found")

        semester_obj = semester.objects.filter(id=sem).first()
        if semester_obj is None:
            raise Http404("Semester not found")

        results = Result.objects.filter(student=student_obj, sem=semester_obj)

        subjects_data = []
        total_marks = 0
        no_subjects=0
        for result in results:
            no_subjects+=1
            subjects_data.append({
                'subject_id': result.sub.id,  
                'subject_name': result.sub.name,  
                'marks': result.marks  
            })
            total_marks += result.marks 

        return Response({
            'usn': usn,
            'semester': sem,
            'subjects': subjects_data,
            'total_marks': (total_marks/no_subjects ) 
        })


class ResultviewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    
   
        
