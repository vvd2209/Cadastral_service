import random
import time
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Query
from .serializers import QuerySerializer, QueryResultSerializer


@api_view(['POST'])
def query_view(request):
    """ Контроллер для получения запроса """
    serializer = QuerySerializer(data=request.data)
    if serializer.is_valid():
        # Эмуляция задержки обработки
        time.sleep(60)
        # Эмуляция ответа внешнего сервера
        result = random.choice([True, False])
        query = serializer.save(result=result)
        return Response(QuerySerializer(query).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def result_view(request):
    """ Контроллер для отправки результата """
    serializer = QueryResultSerializer(data=request.data)
    if serializer.is_valid():
        cadastral_number = serializer.validated_data['cadastral_number']

        try:
            search_query = Query.objects.get(cadastral_number=cadastral_number)
            search_query.save()
            return Response({'status': 'Запрос выполнен'})
        except Query.DoesNotExist:
            return Response({'error': 'Запрос не найден'}, status=404)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
def ping_view(request):
    """ Контроллер проверки, что сервер запустился """
    return Response({"message": "Сервер запущен"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def history_view(request):
    """ Контроллер для получения истории запросов """
    queries = Query.objects.all()
    serializer = QuerySerializer(queries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
