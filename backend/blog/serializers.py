from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        model = Post
        fields = ('id', 'title', 'thumbnail', 'excerpt', 'content', 'slug', 'published', 'author', 'status')
