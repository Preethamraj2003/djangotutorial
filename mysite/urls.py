"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from employee import views as emp
from student import views as stu
from product import views as pro
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Employee', emp.EmployeeviewSet)
router.register(r'department', emp.DepartmentviewSet)
router.register(r'location', emp.LocationviewSet)
router.register(r'contact', emp.ContactviewSet)

router.register(r'semester', stu.SemesterviewSet)
router.register(r'subject', stu.subjectviewSet)
router.register(r'student', stu.studentviewSet)
router.register(r'result', stu.ResultviewSet)

router.register(r'brand', pro.BrandviewSet)
router.register(r'category', pro.CategoryviewSet)
router.register(r'product', pro.ProductviewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('',include('student.urls')),

    path('department/<int:id>/employee/', emp.DepartmentviewSet.as_view({'get': 'departmentRetrival'})),
    path('student/<str:usn>/<int:sem>/', stu.studentviewSet.as_view({'get': 'studentmarks'})),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]

# urlpatterns = [
#     path('detail/', include('employee.urls')),
#     path('admin/', admin.site.urls),
#     path('display/', include('employee.urls')),
#     path('',include('student.urls')),
#     path('product_detail/', include('product.urls')),
#     # path('categories/', include('product.urls')),

# ]
