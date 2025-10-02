# from django.shortcuts import render
# from rest_framework import generics
# from .serializers import NewsSerializer
# from .models import News
#
# class NewListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = NewsSerializer
#     queryset = News.objects.filter(is_archived=False)
#
# class NewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = NewsSerializer
#     queryset = News.objects.all()

from rest_framework import viewsets
from .serializers import NewsSerializer
from .models import News

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
