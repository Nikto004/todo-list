from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseForbidden
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from tasks.forms import TaskForm
from tasks.models import Task


@login_required
def get_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if not task:
        raise ValueError("Данной задачи не найдено")
    context = {
        'title': task.title,
        'task': task
    }
    return render(request, 'tasks/task_detail.html', context=context)


@login_required
def get_tasks(request):
    status = request.GET.get('status')
    if status == 'completed':
        tasks = Task.objects.filter(is_completed=True, user=request.user)
    elif status == 'active':
        tasks = Task.objects.filter(is_completed=False, user=request.user)
    else:
        tasks = Task.objects.filter(user=request.user)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('tasks/includes/task_list_items.html', {'tasks': tasks})
        return JsonResponse({'html': html})
    context = {
        'title': 'TODO List',
        'tasks': tasks
    }
    return render(request, 'tasks/task_list.html', context=context)


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    context = {
        'title': 'Добавления задачи',
        'form': form
    }
    return render(request, 'tasks/task_form.html', context=context)


@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task.user != request.user:
        return HttpResponseForbidden('Вы не можете редактировать чужую задачу')
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task', task_id=task.id)
    else:
        form = TaskForm(instance=task)
    
    context = {
        'title': f'Редактирование - {task.title}',
        'form': form
    }
    return render(request, 'tasks/task_form.html', context=context)


@login_required
def toggle_task_status(request, task_id):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        task = get_object_or_404(Task, id=task_id)
        if task.user != request.user:
            return HttpResponseForbidden('Вы не можете редактировать чужую задачу')
        task.is_completed = not task.is_completed
        task.save()
        return JsonResponse({
            'status': 'success',
            'task_id': task.id,
            'is_completed': task.is_completed
        })
    return JsonResponse({'status': 'error'}, status=400)


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task.user != request.user:
        return HttpResponseForbidden('Вы не можете удалить чужую задачу')
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    context = {
        'title': f'Удаление - {task.title}',
        'task': task
    }
    return render(request, 'tasks/task_confirm_delete.html', context=context)
