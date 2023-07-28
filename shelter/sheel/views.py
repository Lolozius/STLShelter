from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from .paginator import func_paginator
from .models import Post
from django.http import HttpResponse


def index(request):
    posts = Post.objects.all()
    page_obj = func_paginator(request, posts)
    return render(request, 'page/index.html', {'posts': posts})


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

    # Замените 'yourfile.txt' на имя файла, которое хотите видеть при скачивании
    response = HttpResponse(post.document, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="yourfile.stl"'
    return response
