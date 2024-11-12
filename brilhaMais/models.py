from django.db import models

# Create your models here.

class Vendedores(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.IntegerField( verbose_name= 'CPF')
    rg = models.IntegerField(  verbose_name='RG')
    is_term = models.BooleanField(default=True, verbose_name='Termo assinado')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_inactive = models.BooleanField(verbose_name='Inativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Vendedore'

    def __str__(self):
        return self.name