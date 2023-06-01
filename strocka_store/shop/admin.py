from django.contrib import admin

from shop.models import Clothes, Category, Size


class ClothesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'pre_description', 'quantity', 'category', 'size', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'pre_description', 'description', 'price', 'quantity', 'category', 'size')
    list_editable = ('is_published', )
    list_filter = ('is_published', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'size')
    list_display_links = ('id', 'size')
    search_fields = ('size',)


admin.site.register(Clothes, ClothesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
