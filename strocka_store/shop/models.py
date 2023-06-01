from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


def validate_image_count(value):
    if value and len(value) > 5:
        raise ValidationError("Максимальное количество изображений - 5.")


class Clothes(models.Model):
    name = models.CharField(max_length=150, blank=False, verbose_name='Имя товара')
    pre_photo = models.ImageField(upload_to='images/', blank=False, null=True, verbose_name='Фото для каталога')
    # photo = models.ImageField(upload_to="images", validators=[validate_image_count], null=True, verbose_name='Фото для страницы о товаре')
    pre_description = models.CharField(blank=True, max_length=50, verbose_name='Небольшое описание товара')
    description = models.TextField(blank=True, null=True, verbose_name='Главное описание товара')
    quantity = models.IntegerField(default=0, blank=False, verbose_name='Количество товара')
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False, verbose_name='Цена товара')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория товара')
    size = models.ForeignKey('Size', on_delete=models.PROTECT, null=True, verbose_name='Размер товара')
    is_published = models.BooleanField(default=True, verbose_name='Выставить на продажу')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товары"

    def get_absolute_url_product(self):
        return reverse('product_info', kwargs={'product_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Имя категории')

    def __str__(self):
        return self.name

    def get_absolute_url_product(self):
        return reverse('category_link', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"
        ordering = ['id']


class Size(models.Model):
    size = models.CharField(max_length=50, verbose_name='Размер')

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = "Размеры"
        verbose_name_plural = "Размеры"
        ordering = ['id']
