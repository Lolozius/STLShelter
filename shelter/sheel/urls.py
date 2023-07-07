from django.urls import path

from . import views

app_name = 'shel'


urlpatterns = [
    path('', views.index, name='index'),
]