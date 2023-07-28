from django.urls import path

from . import views

app_name = 'shells'


urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.post, name='form'),
    path('download/<int:post_id>/', views.download_file, name='download_file'),
]
