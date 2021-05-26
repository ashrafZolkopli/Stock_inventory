from django.urls import path
from Product import views


urlpatterns = [
    path(
        'create/',
        views.StockCreateView,
        name='stock_create_view'
    ),
]
