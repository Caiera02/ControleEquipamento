from django.contrib import admin
from .models import ServiceChannel,Motive,Status,Ticket
from django.http import HttpResponse
from openpyxl import Workbook
import csv
from datetime import datetime
# Register your models here.

@admin.register(ServiceChannel)
class ServiceChannelAdmin(admin.ModelAdmin):
    list_display=('title',)

@admin.register(Motive)
class MotiveAdmin(admin.ModelAdmin):
    list_display=('title',)
    
@admin.register(Status)
class MotiveAdmin(admin.ModelAdmin):
    list_display=('title',)
    
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display=('name','branch','openTicket','assumid','serviceChannel','Description','status',)
    search_fields=('status',)
    list_filter=('status',)
    
    #importando para excel
    def export_controles_to_excel(request,self,queryset):
    # Cria o workbook e a planilha
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = "Abertura de Tickets"

        # Adiciona o cabeçalho
        headers = ['Nome','Filial','Abertura', 'Horario da Abertura','Assumido','Responsavel','Canal','Descrição','Status',]
        worksheet.append(headers)

        # Recupera os dados do modelo e preenche a planilha
        Tickets = Ticket.objects.all() #Busca em Controle todos o objetos
        data_atual = datetime.today()
        data = data_atual.strftime("%y-%m-%d-%H:%M:%S")

        for ticket in Tickets: #Percorre os objetos
            worksheet.append([
                # controle.id,
                str (ticket.name),
                str (ticket.branch),
                ticket.openTicket.strftime("%y-%m-%d"),
                ticket.openTicket.strftime("%H:%M:%S"),
                ticket.assumid.strftime("%y-%m-%d %H:%M:%S"),
                str (ticket.responseTIcket),
                str (ticket.motive),
                str (ticket.Description),
                str (ticket.status),
            ])

        # Configura a resposta HTTP para o download
        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = f"attachment; filename= Abertura_Ticket-{data}.xlsx"
        workbook.save(response)
        return response
    
    export_controles_to_excel.short_description = 'Exportar para excel'
    actions = [export_controles_to_excel]