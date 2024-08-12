from django.urls import path
from .views import query_view, result_view, ping_view, history_view

urlpatterns = [
    path('query/', query_view),
    path('result/', result_view),
    path('ping/', ping_view),
    path('history/', history_view),
]
