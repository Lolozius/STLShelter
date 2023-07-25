from django import forms
from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        labels = {
            'name': 'Имя обьекта',
            'text': 'Описание обьекта',
            'document': 'Stl файл'
        }
        help_texts = {
            'name': 'Загрузите документ',
            'text': 'Введите описание обьекта',
            'document': 'Укажите путь к файлу'
        }
        fields = ('name', 'text', 'document')

        widgets = {
            'name': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'document': forms.FileInput(attrs={'class': 'form-control'})
        }
