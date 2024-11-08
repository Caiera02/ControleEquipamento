import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Cooperado,Brand, Category, Product, Branch, Controle,Phone

@admin.register(Cooperado)
class CooperadoAdmin(admin.ModelAdmin):
    list_display = ('name','mat','cpf','rg','is_active','is_inactive',)
    search_fields = ('name' ,)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="brands.csv"'
        writer = csv.writer(response)
        writer.writerow(['nome', 'ativo', 'descrição', 'cirado em', 'atualizado em'])
        for brand in queryset:
            writer.writerow([brand.name, brand.is_active, brand.description,
                             brand.created_at, brand.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]

@admin.register(Category)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="categories.csv"'
        writer = csv.writer(response)
        writer.writerow(['nome', 'ativo', 'descrição', 'cirado em', 'atualizado em'])
        for category in queryset:
            writer.writerow([category.name, category.is_active, category.description,
                             category.created_at, category.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]

#Maquina, Celular etc
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category','processor','memory_ram','storage','description',
                    'is_active', 'created_at')
    search_fields = ('title', 'brand__name', 'category__name')
    list_filter = ('is_active', 'brand', 'category')

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        writer = csv.writer(response)
        writer.writerow(['título', 'marca', 'categoria', 'preço',
                         'ativo', 'descrição', 'criado em', 'atualizado em'])
        for product in queryset:
            writer.writerow([product.title, product.brand.name, product.category.name,
                             product.price, product.is_active, product.description,
                             product.created_at, product.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]
    
@admin.register(Branch)# Filiais
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at',)
    search_fields = ('name',)

@admin.register(Controle)#Controles de de notebooks e celular
class ControleAdmin(admin.ModelAdmin):
    list_display = ('name','laptop','phones','branch','delivery','description','created_at',)
    # result = Controle.objects.filter(cooperado__name__icontains="an")
    #search_fields = ['cooperado__nome']
    search_fields = ('description',)
    list_filter = ('phones', 'category')


@admin.register(Phone)#Celulares
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('title','category','brand','imei',)
    search_fields = ('title',)
    list_filter = ('is_active', 'brand', 'category')

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'

        writer = csv.writer(response)
        writer.writerow(['nome', 'marca', 'categoria', 'preço',
                         'ativo', 'descrição', 'criado em', 'atualizado em'])
        for product in queryset:
            writer.writerow([product.title, product.brand.name, product.imei.name,
                             product.price, product.is_active, product.description,
                             product.created_at, product.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]