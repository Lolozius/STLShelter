from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from .paginator import func_paginator
from .models import Post
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os
User = get_user_model()


def index(request):
    posts = Post.objects.all()
    page_obj = func_paginator(request, posts)
    return render(request, 'page/index.html', {'page_obj': page_obj})


@login_required(login_url=settings.LOGIN_URL)
def post(request):
    form = PostForm(
        request.POST or None,
        request.FILES or None,
    )
    if not form.is_valid():
        return render(request, 'page/create_post.html', {'form': form})
    post = form.save(commit=False)
    post.author = request.user
    post.save()
    return redirect('shells:index')


def download_file(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    file_path = post.document.path  # Получаем путь к файлу
    file_name = os.path.basename(file_path)  # Извлекаем имя файла

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response


@login_required(login_url=settings.LOGIN_URL)
def delete_object(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('shells:index')
