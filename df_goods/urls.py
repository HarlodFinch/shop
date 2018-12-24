from django.urls import path
from . import views

app_name = 'goods'
urlpatterns = [
    path('',views.index,name='index'),
    path('list<int:tid>_<int:pindex>_<int:sort>/',views.list,name='list'),
    path('<int:id>/',views.detail,name='detail'),
]