from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer
# Create your views here.


class BlogListView(APIView):
    def get(self, request, *args, **kwargs):

        # get post                  #los promeros 5
        posts = Post.postobjects.all()[0:5]
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)


class BlogDetailView(APIView):
    def get(self, request, post_slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=post_slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)
