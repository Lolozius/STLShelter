from django.db import models

# Create your models here.


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст с описание',
        help_text='Пропишите описание обьекта'
    )
