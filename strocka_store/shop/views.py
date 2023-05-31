from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Clothes, Category


def index(request):
    return redirect('/strochka-store/')


def home_page(request):
    category = Category.objects.all()
    return render(request, 'shop/index.html', {'category': category})


def show_category(request, category_id):
    content_clothes = Clothes.objects.filter(category_id=category_id)
    category = Category.objects.all()
    context = {
        'content_clothes': content_clothes,
        'category': category,
    }
    return render(request, 'shop/magazine.html', context=context)


def magazine(request):
    content_clothes = Clothes.objects.all()
    return render(request, 'shop/magazine.html', {'content_clothes': content_clothes, 'Title': 'Strochka Store'})


def about_store(request):
    return render(request, 'shop/about-store.html', {'Title': 'Strochka Store'})


def product_info(request, product_id):
    print(request.GET)
    content_clothes = Clothes.objects.all()
    return render(request, 'shop/about-product.html', {'content_clothes': content_clothes})
