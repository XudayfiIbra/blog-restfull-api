from rest_framework import serializers
from . models import Blog



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'description', 'body', 'date_created', 'is_published']
        