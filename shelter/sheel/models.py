from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class Post(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='Имя',
        help_text='Назовите обьект',
    )
    text = models.TextField(
        verbose_name='Текст с описание',
        help_text='Распишите описание обьекта',
    )
    document = models.FileField(upload_to='documents/')
    #image = models.ImageField('Фото', blank=True, null=True,)
