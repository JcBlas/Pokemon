from django.contrib import admin
from .models import PokemonCard, Trainer
# Register your models here.
@admin.register(PokemonCard)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity")
    search_fields = ("name",)

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "email")
    search_fields = ("name",)