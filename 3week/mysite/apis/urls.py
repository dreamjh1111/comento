from django.urls import path

from .views import ListTodo, DetailTodo, ListComment, DetailComment

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
    path('<int:pk>/comments/', ListComment.as_view()),
    path('<int:pk>/comments/<int:Comment_id>', DetailComment.as_view()),
]


'''


from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.BigAutoField(help_text="Post ID", primary_key=True)
    title = models.CharField(help_text="Post title", max_length=100, blank=False, null=False)
    contents = models.TextField(help_text="post contents", blank=False, null=False)


class Comment(models.Model):
    id = models.BigAutoField(help_text="Comment ID", primary_key=True)
    post_id = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE, db_column="post_id")
    contents = models.TextField(help_text="Comment contents", blank=False, null=False)


from rest_framework import viewsets
from blog.models import Post
from blog.models import Comment
from blog.serializers import PostSerializer
from blog.serializers import CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


from rest_framework import serializers
from blog.models import Post
from blog.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post_id", "contents")


class PostSerializer(serializers.ModelSerializer):
    post = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "contents", "post")


from django.conf.urls import url
from blog.views import PostViewSet
from blog.views import CommentViewSet


urlpatterns = [
    url('post', PostViewSet.as_view({'get':'list', 'post':'create'})),
    url('comment', CommentViewSet.as_view({'get':'list', 'post':'create'})),
]
'''