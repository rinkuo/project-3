from django.contrib import admin
from django.urls import path
from courses.views import task_list
from students.views import student_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list),
    path('student/', student_list),
]