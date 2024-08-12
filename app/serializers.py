from rest_framework import serializers
from .models import Query


class QuerySerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Запрос """
    class Meta:
        model = Query
        fields = ['id', 'cadastral_number', 'latitude', 'longitude', 'result', 'created_at']


class QueryResultSerializer(serializers.Serializer):
    """ Сериализатор для контроллера отправки результата """
    cadastral_number = serializers.CharField()
