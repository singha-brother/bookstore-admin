from django.urls import path 
from .views import BookAPIView

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='api_book_list'),
]