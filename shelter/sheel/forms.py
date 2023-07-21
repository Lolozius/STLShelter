from django import forms
from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        labels = {'text': 'Описание обьекта', 'document': 'Stl файл'}
        help_texts = {'text': 'Введите описание обьекта', 'document': 'Загрузите документ'}
        fields = ('text', 'document',)

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'document': forms.FileInput(attrs={'class': 'form-control'})
        }
