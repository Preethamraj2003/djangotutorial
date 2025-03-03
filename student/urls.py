from django.urls import include, path
from . import views


urlpatterns = [
    path('results/', views.student_results_view, name='student_results'),
    path('resultsdropdown/', views.student_results_dropdown, name='student_results_dropdown'),

]
