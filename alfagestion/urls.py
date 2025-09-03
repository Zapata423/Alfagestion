
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('institutions.urls')),
    path('students/', include('students.urls', namespace='students')),
    path('teachers/', include('teachers.urls', namespace='teachers')),

    # path('', include('teachers.urls')),
    # path('', include('evidence.urls')),
    # path('', include('reports.urls')),
]
