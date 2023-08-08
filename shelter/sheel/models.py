import os
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import FileExtensionValidator

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
    pub_date = models.DateTimeField(auto_now=True)
    text = models.TextField(
        verbose_name='Текст с описание',
        help_text='Распишите описание обьекта',
    )
    document = models.FileField(
        upload_to='documents/',
        validators=[FileExtensionValidator(
        allowed_extensions=['stl', 'jcode'])])
    #image = models.ImageField('Фото', blank=True, null=True,

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text

    def delete(self, *args, **kwargs):
        # Удаление связанного файла перед удалением объекта Post
        if self.document:
            os.remove(self.document.path)
        super().delete(*args, **kwargs)
