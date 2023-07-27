from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from .paginator import func_paginator
from .models import Post


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
