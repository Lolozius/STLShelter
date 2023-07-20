from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст с описание',
        help_text='Распишите описание обьекта',
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author',
    )
    pub_date = models.DateField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    document = models.FileField(upload_to='documents/')
    #image = models.ImageField('Фото', blank=True, null=True,)
