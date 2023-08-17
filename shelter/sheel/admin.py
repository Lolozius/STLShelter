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
        'name',
        'text',
        'document',
        'pub_date',
        'sketchfab_model_id',
    )
    search_fields = ('text',)
    empty_value_display = '-пусто-'
