from django.urls import path,include

from .views import (
    PostUpdateView,
    PostDeleteView,
    TagPostListView,
    UserPostListView,
    post_create,
)
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('<post_id>/detail_view/', views.post_detail, name='post-detail'),
    path('post/new/', views.post_create, name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('tag/<str:tagname>',TagPostListView.as_view(),name='tag_posts'),
]