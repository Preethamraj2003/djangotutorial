from django.shortcuts import render
from django.http import HttpResponse,Http404
from employee.models import Employee, Department
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from employee.models import Employee,Department, Location, Contact
from employee.serializers import EmployeeSerializer,DepartmentSerializer,LocationSerializer,ContactSerializer
from rest_framework import  viewsets




def detail(request,em_id) : 
    employees = Employee.objects.filter(id=em_id).values('id')
    template = loader.get_template("employeeinfo.html")
    if employees: 
        emp_info = Employee.objects.filter(id=em_id)
        context= {
            "emp_info" : emp_info,
        }
        return HttpResponse(template.render(context, request))
    else: 
        raise Http404(' Employee no found')
    

# def index(request):
#     employee_list = Employee.objects.all()
#     template = loader.get_template("index.html")
#     context = {
#         "latest_question_list": employee_list,
#     }
#     return HttpResponse(template.render(context, request))


def display(request):
    employee_list = Employee.objects.all()
    return render(request, 'employee.html', {
        'employee_list': employee_list,
        'employees': employee_list, 
        'selected_name': None,
        'selected_designation': None
    })

def employee_view(request):

    parametersAllowed = {'employeeselect','designation'}
 
    extraparameters = set(request.GET.keys()) - parametersAllowed
    if extraparameters:
        return HttpResponse(f"{extraparameters} -> invalid query parameter")
    
    employee_name = request.GET.get('employeeselect')
    designation = request.GET.get('designation')

    employees = Employee.objects.all()

    if employee_name:
        employees = employees.filter(name=employee_name)
    
    if designation:
        employees = employees.filter(designation=designation)

    return render(request, 'employee.html', {
        'employee_list': Employee.objects.all(),  
        'employees': employees,  
        'selected_name': employee_name,
        'selected_designation': designation
    })

class LocationviewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class DepartmentviewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def departmentRetrival(self,request, **kwargs) : 
        dept_id  = self.kwargs.get('id')  
        return Response(Employee.objects.filter(d_id= dept_id).values())
        
        

class EmployeeviewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ContactviewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


