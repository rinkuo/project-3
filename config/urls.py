from django.contrib import admin
from django.urls import path
from students.views import student_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_list),
]