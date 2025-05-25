from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'is_completed')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'is_completed': 'Выполнено'
        }
