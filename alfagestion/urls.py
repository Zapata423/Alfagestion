
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('accounts.urls')),
    re_path('', include('students.urls')),
    re_path('', include('teachers.urls')),

    # path('', include('teachers.urls')),
    # path('', include('evidence.urls')),
    # path('', include('reports.urls')),
]
