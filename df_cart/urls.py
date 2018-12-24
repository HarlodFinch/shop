from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('',views.cart,name='cart'),
    path('add<int:id>_<int:count>_<int:pindex>/',views.add,name='add'),
    path('edit/',views.edit,name='edit'),
    path('delete<int:id>/',views.delete,name='delete'),
    path('place_order/',views.place_order,name='place_order'),
    path('addcount_<int:id>/',views.addcount,name='addcount'),
    path('descount_<int:id>/',views.descount,name='descount'),
]