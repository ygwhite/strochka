from django.db import models
from django.urls import reverse


class Clothes(models.Model):
    name = models.CharField(max_length=150, blank=False, verbose_name='Имя товара')
    pre_photo = models.CharField(max_length=350, blank=False)
    pre_description = models.CharField(blank=True, max_length=50, verbose_name='Небольшое описание товара')
    description = models.TextField(blank=False, null=True, verbose_name='Главное описание товара')
    quantity = models.IntegerField(default=0, blank=False, verbose_name='Количество товара')
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False, verbose_name='Цена товара')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория товара')
    size = models.ForeignKey('Size', on_delete=models.PROTECT, null=True, verbose_name='Размер товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товары"

    def get_absolute_url_product(self):
        return reverse('product_info', kwargs={'product_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url_product(self):
        return reverse('category_link', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"


class Size(models.Model):
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = "Размеры"
        verbose_name_plural = "Размеры"
