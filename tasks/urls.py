from django.urls import path

from .views import get_task, TaskListView, TaskCreateView, delete_task, TaskUpdateView, toggle_task_status


urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('<int:task_id>/', get_task, name='task'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('<int:task_id>/edit/', TaskUpdateView.as_view(), name='update_task'),
    path('<int:task_id>/delete/', delete_task, name='delete_task'),
    path('<int:task_id>/toggle/', toggle_task_status, name='toggle_task_status')
]