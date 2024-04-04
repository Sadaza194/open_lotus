from django.views.generic import FormView, ListView
from django.shortcuts import HttpResponseRedirect, reverse
from .forms import FragenBeantwortenForm  # Import custom form
from datetime import date, timedelta, timezone
from .models import Frage  # Import the Frage model
from django.db import models  # Import the Django models module


class FragenBeantwortenView(FormView):
    template_name = 'fragen_beantworten.html'
    form_class = FragenBeantwortenForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('home'))

class FragenListView(ListView):
    template_name = 'fragen_liste.html'
    model = Frage

    def get_queryset(self):
        heute = date.today()
        if self.request.user.is_superuser:
            return self.model.objects.all()  # All questions for admin
        else:
            return self.model.objects.filter(
                models.Q(frequenz='taegllich') |
                models.Q(frequenz='woechentlich', letzte_beantwortung__lt=heute - timedelta(days=7)) |
                models.Q(frequenz='monatlich', letzte_beantwortung__lt=heute - timedelta(days=30))
            )
