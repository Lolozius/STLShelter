from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse


def index(request):
    return render(request, 'page/index.html')


def post(request):
    return render(request, 'page/create_post.html')
