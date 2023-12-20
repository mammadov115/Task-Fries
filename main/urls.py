from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("project-dashboard", views.project_dashboard, name='project_dashboard'),
    path('tasks/', views.task, name='task')
]
