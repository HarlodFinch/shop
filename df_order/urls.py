from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('',views.order_info,name='order_info'),
]