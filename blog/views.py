from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog
from . serializers import BlogSerializer
from rest_framework import viewsets


class Blog(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()



