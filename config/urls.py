from django.contrib import admin
from django.urls import path
from courses.views import courses_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', courses_list),
]