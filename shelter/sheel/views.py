from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from django.http import HttpResponse


def index(request):
    return render(request, 'page/index.html')


def post(request):
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if not form.is_valid():
        return render(request, 'page/create_post.html', {'form': form})
    post = form.save(commit=False)
    post.author = request.user
    post.save()
    return redirect('page/index.html')
