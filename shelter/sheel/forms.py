from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        labels = {
            'name': 'Имя объекта',
            'text': 'Описание объекта',
            'document': 'Stl файл'
        }
        error_messages = {
            'required': 'Поле "Имя обьекта" обязательно для заполнения.',
            'max_length': 'Длина имени не должна превышать 100 символов.',
        }
        help_texts = {
            'name': 'Загрузите документ',
            'text': 'Введите описание объекта',
            'document': 'Укажите путь к файлу'
        }
        fields = ('name', 'text', 'document')

        widgets = {
            'name': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Введите имя обьекта'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание обьекта'}),
            'document': forms.FileInput(attrs={'class': 'form-control'})
        }
