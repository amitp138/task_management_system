from django.urls import path
from .views import TasksManagement
urlpatterns = [
  path('task',TasksManagement.as_view(),name="tasks")
]