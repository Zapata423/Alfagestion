from django.urls import path
from . import views

app_name = 'teachers_app'

urlpatterns = [
    path('panelDocentes/', views.HomePageTeachers.as_view(), name='panelDocentes'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('home/', views.home_view, name='home'),
    # path('verificacion/', views.verificacion_view, name='verificacion'),
]