from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from users.forms import CustomUserCreationForm, UserUpdateForm, ProfileForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аккаунт создан! Теперь можно войти.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    context = {
        'title': 'Регистрация',
        'form': form
    }
    
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    context = {
        'title': f'Профиль {request.user.username}',
        'user': request.user
    }
    
    return render(request, 'users/profile.html', context)


def public_profile(request, username):
    user = get_object_or_404(User, username=username)
    
    context = {
        'title': f'Профиль {user.username}',
        'user_profile': user.profile
    }
    return render(request, 'users/public_profile.html', context)


@login_required
def edit_profile(request):
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        form = ProfileForm(instance=request.user.profile)
    
    context = {
        'title': f'Редактирование профиля {request.user.username}',
        'form': form,
        'user_form': user_form
    }
    return render(request, 'users/edit_profile.html', context)
