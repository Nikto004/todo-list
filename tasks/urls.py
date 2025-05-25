from django.urls import path

from tasks.views import get_task, get_tasks, create_task, delete_task, update_task, toggle_task_status


urlpatterns = [
    path('', get_tasks, name='tasks'),
    path('<int:task_id>/', get_task, name='task'),
    path('create/', create_task, name='create_task'),
    path('<int:task_id>/edit/', update_task, name='update_task'),
    path('<int:task_id>/delete/', delete_task, name='delete_task'),
    path('<int:task_id>/toggle/', toggle_task_status, name='toggle_task_status')
]