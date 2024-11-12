from django.contrib import admin
from .models import Vendedores

# Register your models here.

@admin.register(Vendedores)
class Vendedores(admin.ModelAdmin):
    list_display = ('name','cpf','is_term' )
    search_fields = ('name',)