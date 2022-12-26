from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Card, CardLog


@admin.action(description=_('Активировать карту'))
def activate_card(modeladmin, request, queryset):
    queryset.update(activated=True)


@admin.action(description=_('Деактивировать карту'))
def deactivate_card(modeladmin, request, queryset):
    queryset.update(activated=False)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('series', 'activated', 'split_number', 'date_open', 'date_close', 'overdue', 'balance')
    list_display_links = ('series', 'split_number')
    search_fields = ('series', 'number', 'date_open', 'date_close', 'activated')
    list_editable = ('activated', )
    actions = [activate_card, deactivate_card]


@admin.register(CardLog)
class CardLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'card', 'product')
    list_display_links = ('id', 'date', 'card', 'product')
