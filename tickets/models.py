from django.db import models
from products.models import Cooperado,Branch

# Create your models here.
class ServiceChannel(models.Model):
    title= models.CharField(max_length=20,verbose_name='Titulo')
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Canal de atendimento'

    def __str__(self):
        return self.title

class Motive(models.Model):
    title= models.CharField(max_length=20,verbose_name='Titulo')
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Motivo do chamado'

    def __str__(self):
        return self.title

class Status (models.Model):
    title=models.CharField(max_length=30, verbose_name='Status')
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Statu'

    def __str__(self):
        return self.title

class Ticket (models.Model):
    name= models.ForeignKey(Cooperado, on_delete= models.PROTECT,
                            related_name='cooperado', verbose_name='Nome')
    branch=models.ForeignKey(Branch, on_delete= models.PROTECT,
                            related_name='filial', verbose_name='Filial')
    
    openTicket= models.DateTimeField(verbose_name='Abertura')
    assumid=models.DateTimeField(verbose_name='Assumido')
    responseTIcket=models.CharField(max_length=20, default='Caio')
    serviceChannel=models.ForeignKey(ServiceChannel, on_delete= models.PROTECT,
                            related_name='controls', verbose_name='Canal de atendimento')
    motive=models.ForeignKey(Motive, on_delete= models.PROTECT,
                             related_name='controls', verbose_name='Motivo')
    Description=models.TextField(verbose_name='Descrição')
    status=models.ForeignKey(Status, on_delete= models.PROTECT,
                             related_name='filial',verbose_name='Status')
    #finish=models.DateTimeField(auto_now_add=True, verbose_name='Finalizado')
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Abertura de Chamado'

    # def __str__(self):
    #     return self.name