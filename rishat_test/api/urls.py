from django.urls import path

from .views import item_buy, item_view

app_name = 'api'

urlpatterns = [
    path('item/<int:pk>', item_view, name='item_view'),
    path('buy/<int:pk>', item_buy, name='item_buy'),
]
