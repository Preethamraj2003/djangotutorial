from django.urls import include, path
from employee import views
from rest_framework import routers


# urlpatterns = [
#     path('', views.display, name='display'),  
#     path('employee_view/', views.employee_view, name='employee_view'),  
#     path("<int:em_id>/", views.detail, name='detail')
# ]

router = routers.DefaultRouter()
router.register(r'Employee', views.EmployeeviewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/employees/', views.create_employee, name='create_employee'),

]

