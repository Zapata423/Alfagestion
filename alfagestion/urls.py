
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('accounts.urls')),
    re_path('', include('students.urls')),
    re_path('', include('teachers.urls')),
    re_path('', include('institutions.urls')),
    re_path('', include('evidence.urls')),

    # path('', include('teachers.urls')),
    # path('', include('evidence.urls')),
    # path('', include('reports.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
