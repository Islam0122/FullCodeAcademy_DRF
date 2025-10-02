from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'content',
            'is_archived',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at'
        )
