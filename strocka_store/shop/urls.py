from django.urls import path

from shop.views import magazine, about_store, home_page, product_info, show_category

urlpatterns = [
    path('', home_page),
    path('magazine/', magazine, name="magazine"),
    path('about-store/', about_store, name='about-store'),
    path('product/<int:product_id>/', product_info, name='product_info'),
    path('category/<int:category_id>/', show_category, name='category_link'),
]
