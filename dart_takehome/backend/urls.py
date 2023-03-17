from django.urls import path

from backend import views


urlpatterns = [
    path('', views.home, name='home'),
    path('api/tasks/list', views.list_tasks, name='list_tasks'),
    path('api/tasks/edit', views.edit_tasks, name='edit_tasks'),
]
