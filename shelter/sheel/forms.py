from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        labels = {'text': 'Описание обьекта'}
        help_texts = {'text': 'Введите описание обьекта'}
        fields = ('text', 'document',)
