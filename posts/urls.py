from django.urls import path
from . import views

app_name = 'posts'


urlpatterns = [
    path('', views.posts_list, name='list'),
    path('create/', views.post_create, name='create'),
    path('details/<str:slug>', views.post_detail, name='detail'),
]