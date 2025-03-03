from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.display, name='display'),  
    path('employee_view/', views.employee_view, name='employee_view'),  
    path("<int:em_id>/", views.detail, name='detail'),

]

