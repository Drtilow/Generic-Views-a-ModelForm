from django.contrib import admin
from .models import Jacket

@admin.register(Jacket)
class JacketAdmin(admin.ModelAdmin):
    list_display = ('brand', 'color')
    search_fields = ('brand', 'color')
