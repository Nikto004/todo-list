from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import Profile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'avatar',)
        
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'О себе...'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
