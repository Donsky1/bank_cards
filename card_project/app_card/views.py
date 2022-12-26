import random
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views import generic
from django.utils import timezone

from .models import CardLog, Card
from .forms import GenerateCardForm


class CardLogView(generic.DetailView):
    model = Card
    template_name = 'app_card/history_sell.html'

    def get_context_data(self, **kwargs):
        context = super(CardLogView, self).get_context_data(**kwargs)
        card = get_object_or_404(Card, id=self.kwargs['pk'])
        context['logs'] = CardLog.objects.filter(card=card)
        print(context['logs'])
        return context


class GenerateCardView(generic.FormView):
    template_name = 'app_card/generate_card.html'
    form_class = GenerateCardForm
    success_url = '../'

    def form_valid(self, form):
        a = 1000000000000000
        b = 9999999999999999
        count = form.cleaned_data['count']
        series = form.cleaned_data['series']
        life_time = form.cleaned_data['life_time']
        card_list = []
        for i in range(count):
            number = random.randint(a, b)
            date_open = timezone.now()
            date_close = timezone.now() + timezone.timedelta(days=int(life_time))
            card_list.append(Card(series=series, number=number, date_open=date_open,
                                  date_close=date_close))
        Card.objects.bulk_create(card_list)
        return super(GenerateCardView, self).form_valid(form)