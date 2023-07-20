from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Перечисляем поля, которые должны
    отображаться в админке.
    """

    list_display = (
        'pk',
        'text',
        'author',
        'pub_date',
    )
    search_fields = ('text',)
    empty_value_display = '-пусто-'
