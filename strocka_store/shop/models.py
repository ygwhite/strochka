from django.db import models
from django.urls import reverse


class Clothes(models.Model):
    name = models.CharField(max_length=150, blank=False)
    pre_photo = models.CharField(max_length=350, blank=False)
    pre_description = models.CharField(blank=True, max_length=50)
    description = models.TextField(blank=False, null=True)
    quantity = models.IntegerField(default=0, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    size = models.ForeignKey('Size', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url_product(self):
        return reverse('product_info', kwargs={'product_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url_product(self):
        return reverse('category_link', kwargs={'category_id': self.pk})


class Size(models.Model):
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.size
