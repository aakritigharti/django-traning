from django.urls import path
from .import views

urlpatterns = [
   
     path('student', views.student_api, name='students'),
      path('department', views.department_api, name='departments'),

]
