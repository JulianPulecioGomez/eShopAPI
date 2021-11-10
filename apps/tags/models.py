from django.db import models
from apps.products.models import Product


class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    is_active = models.BooleanField(default=True, )
    products = models.ManyToManyField(Product, blank=True)
    depp = 1

    def __str__(self):
        return self.name
