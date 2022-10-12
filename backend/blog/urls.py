from django.urls import path
from .views import BlogListView, BlogDetailView


app_name = "blog"

urlpatterns = [
    path('posts/', BlogListView.as_view(), name='blog-list'),
    path('post/<post_slug>/', BlogDetailView.as_view(), name='blog-detail'),
]