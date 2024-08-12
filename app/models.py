from django.db import models


class Query(models.Model):
    cadastral_number = models.CharField(max_length=255, verbose_name='Кадастровый номер')
    latitude = models.IntegerField(verbose_name='Широта')
    longitude = models.IntegerField(verbose_name='Долгота')
    result = models.BooleanField(null=True, verbose_name='Результат запроса')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время запроса')

    class Meta:
        verbose_name = "Запрос"
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return f"{self.cadastral_number} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
