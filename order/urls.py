from django.urls import path

from order.views import *

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('history/', order_history, name='order-history'),
    path('history/detail/<int:order_id>/', order_history_detail, name='order-detail'),
]