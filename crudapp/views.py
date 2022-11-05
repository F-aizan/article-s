from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Articles
from .serializers import ArticleSerializer
from rest_framework.response import Response
# Create your views here.

class Articleview(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]