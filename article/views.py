from django.shortcuts import render
from article.models import Article
from article.serializers import ArticleSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ArticleView(APIView):
    def get(self, requset, format = None):
        article = Article.objects.all()
        serializer = ArticleSerializers(article, many =True)
        return Response(serializer.data)

    def post(self, request , format = None):
        serializer = ArticleSerializers(date= request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetail(APIView):

    def get(self, request, article_id, format=None):
        article = self.get_object(article_id)
        serializer = ArticleSerializers(article)
        return Response(serializer.data)

    def put(self, request, article_id, format=None):
        article = self.get_object(article_id)
        serializer = ArticleSerializers(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = self.get_object(article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)