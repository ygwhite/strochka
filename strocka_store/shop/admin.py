from django.contrib import admin

from shop.models import Clothes, Category, Size


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'pre_description', 'quantity', 'category', 'size')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'pre_description', 'description', 'price', 'quantity', 'category', 'size')


admin.site.register(Clothes, ShopAdmin)
admin.site.register(Category)
admin.site.register(Size)
