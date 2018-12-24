from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_exist/',views.register_exist, name='register_exist'),
    path('register_handler/',views.register_handler,name='register_handler'),
    path('login/',views.login, name='login'),
    path('login_handler/',views.login_handler,name='login_handler'),
    path('logout/',views.logout,name='logout'),
    path('info/',views.info,name='info'),
    path('order/',views.order,name='order'),
    path('site/',views.site,name='site'),
]