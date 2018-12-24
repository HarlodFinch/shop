from django.contrib import admin
from .models import TypeInfo, GoodsInfo

@admin.register(TypeInfo)
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ttitle',)

@admin.register(GoodsInfo)
class GoodInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('id', 'gtitle', 'gpic', 'gprice', 'gunit', 'gclick', 'gstorage', 'gdesc', 'gcontent','gtype',)
