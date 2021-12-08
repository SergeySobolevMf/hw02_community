from django import forms  # Импортируем модуль forms, из него возьмём класс ModelForm

from .models import Post  # Импортируем модель, чтобы связать с ней форму


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
