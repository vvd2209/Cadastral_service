from rest_framework import status
from rest_framework.test import APITestCase
from .models import Query


class QueryViewTests(APITestCase):
    def test_valid_query_creation(self):
        """ Тест на успешное создание запроса """
        data = {
            'cadastral_number': '123456',
            'latitude': '50',
            'longitude': '100'
        }
        response = self.client.post('/api/query/', data, format='json')

        # Проверка статуса ответа и данных
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('result', response.data)
        self.assertIn('cadastral_number', response.data)

    def test_invalid_query_creation(self):
        """ Тест на создание запроса с неверными данными """
        data = {'invalid_field': 'value'}
        response = self.client.post('/api/query/', data, format='json')

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ResultViewTests(APITestCase):
    def setUp(self):
        """ Создание тестового запроса """
        self.query = Query.objects.create(cadastral_number='123456', latitude='40', longitude='100',)

    def test_valid_result_submission(self):
        """ Тест на успешную отправку результата """
        data = {'cadastral_number': '123456'}
        response = self.client.post('/api/result/', data, format='json')

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'status': 'Запрос выполнен'})

    def test_invalid_result_submission(self):
        """ Тест на отправку результата для несуществующего запроса """
        data = {'cadastral_number': '654321'}
        response = self.client.post('/api/result/', data, format='json')

        # Проверка статуса ответа
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, {'error': 'Запрос не найден'})


class PingViewTests(APITestCase):
    def test_ping(self):
        """ Тест на проверку запуска сервера """
        response = self.client.get('/api/ping/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "Сервер запущен"})


class HistoryViewTests(APITestCase):
    def setUp(self):
        """ Создание нескольких запросов для проверки истории """
        Query.objects.create(cadastral_number='123456', result=True, latitude='40', longitude='100',)
        Query.objects.create(cadastral_number='654321', result=False, latitude='70', longitude='80',)

    def test_get_history(self):
        """ Тест на получение истории запросов """
        response = self.client.get('/api/history/')

        # Проверка статуса ответа и данных
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Должно быть 2 запроса
