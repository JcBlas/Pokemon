from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from cardqquest.models import PokemonCard

class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context