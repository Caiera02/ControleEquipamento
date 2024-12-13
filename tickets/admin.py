from django.contrib import admin
from .models import ServiceChannel,Motive,Status,Ticket
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