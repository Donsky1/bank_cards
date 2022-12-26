from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    price = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.name
