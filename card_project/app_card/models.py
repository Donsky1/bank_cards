from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from app_user.models import MyUser
from app_product.models import Product


class Card(models.Model):
    series = models.PositiveIntegerField(unique=False)
    # example 1111 2222 3333 4444
    number = models.PositiveBigIntegerField(unique=True)
    date_open = models.DateTimeField(blank=True, null=True)
    date_close = models.DateTimeField(blank=True, null=True)
    activated = models.BooleanField(default=False)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=50, default='default', blank=True, null=True)
    balance = models.PositiveIntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Карточки'
        verbose_name = 'Карточка'

    def __str__(self):
        return str(self.number)

    @admin.display(ordering='number')
    def split_number(self):
        result = []
        for n, el in enumerate(str(self.number)):
            if n % 4 == 0:
                result.append(' ')
            result.append(el)
        return ''.join(result)

    @admin.display(boolean=True)
    def overdue(self):
        return timezone.now() > self.date_close if self.date_close else False

    def _validate_open_close_dates(self):
        if self.date_close and self.date_open:
            if self.date_close < self.date_open:
                raise ValidationError(_("Дата закрытия карты не может быть раньше даты открытия"))

    def save(self, *args, **kwargs):
        self._validate_open_close_dates()
        return super().save(*args, **kwargs)

    def buy(self, value: float):
        if self.activated:
            try:
                value = float(value)
            except Exception:
                raise ValueError(_('Значение должно быть числом'))
            self.balance -= value
        else:
            raise _('Карта не активирована')

    def up_balance(self, value: float):
        if self.activated:
            try:
                value = float(value)
            except Exception:
                raise ValueError(_('Значение должно быть числом'))
            self.balance += value
        else:
            raise _('Карта не активирована')


class CardLog(models.Model):
    date = models.DateTimeField(auto_now=True)
    card = models.ForeignKey(Card, on_delete=models.PROTECT,
                             related_name='logs')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.card.number) + ' ' + str(self.product.name)

    class Meta:
        verbose_name_plural = 'История покупок всех карт'
        verbose_name = 'история'