from django import forms


class GenerateCardForm(forms.Form):
    LIFE_TIME = [
        ('30', '1 месяц'),
        ('182', '6 месяцев'),
        ('365', '1 год'),
    ]
    series = forms.IntegerField(min_value=0, max_value=9999, label='Серия карт')
    count = forms.IntegerField(min_value=1, max_value=999, label='Кол-во генерируемых карт')
    life_time = forms.ChoiceField(choices=LIFE_TIME, label='Срок службы карты')