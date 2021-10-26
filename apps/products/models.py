from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    tags = models.ManyToManyField('tags.Tag')
    stock = models.IntegerField(blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
