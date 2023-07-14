from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse


def index(request):
    return render(request, 'includes/header.html')


def post(request):

    pass
