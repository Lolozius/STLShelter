from django.conf import settings
from django.core.paginator import Paginator


def func_paginator(request, posts):
    paginator = Paginator(posts, settings.POSTS_LIMIT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
