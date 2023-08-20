from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from .paginator import func_paginator
from .models import Post
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests
from requests.exceptions import RequestException
import os
User = get_user_model()

SKETCHFAB_API_URL = 'https://api.sketchfab.com/v3'
SKETCHFAB_API_TOKEN = 'XXXXXXXXXXXXXX'


def index(request):
    posts = Post.objects.all()
    page_obj = func_paginator(request, posts)
    return render(request, 'page/index.html', {'page_obj': page_obj})


def upload_stl_to_sketchfab(stl_file_path):
    model_endpoint = f'{SKETCHFAB_API_URL}/models'

    headers = {'Authorization': f'Token {SKETCHFAB_API_TOKEN}'}
    files = {'modelFile': open(stl_file_path, 'rb')}

    data = {
        'name': 'My Uploaded Model',
        'description': 'Description of the uploaded model',
        'tags': ['tag1', 'tag2'],
        # Дополнительные параметры для модели
    }

    try:
        response = requests.post(model_endpoint, data=data, files=files, headers=headers)
        response_data = response.json()

        if response.status_code == requests.codes.created:
            model_id = response_data['uid']
            return model_id
        else:
            print(f'Upload failed with error: {response_data}')
            return None
    except RequestException as exc:
        print(f'An error occurred: {exc}')
        return None


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
    sketchfab_model = upload_stl_to_sketchfab(post.document.path)
    if sketchfab_model:
        print(sketchfab_model)
        post.sketchfab_model_id = sketchfab_model
        post.save()  # Сохраняем uid модели обратно в объект поста

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
