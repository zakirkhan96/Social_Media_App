from . import views
from .views import like_post, add_comment
from django.urls import path
from .views import feed, create_post

urlpatterns = [
    path('', feed, name='feed'),
    path('create/', create_post, name='create'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.add_comment, name='comment'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
