from rest_framework import serializers
from portfolio import models

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'descriptions',
            'is_completed',
            'created_at',
            'updated_at',
        )
        model = models.Todo

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'contents',
            'created_at',
            'updated_at',
        )
        model = models.Comment