from app.models import Query
from django.contrib import admin


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cadastral_number', 'latitude', 'longitude', 'result', 'created_at',)
