from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок TODO')
    description = models.TextField(verbose_name='Описание для TODO')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
