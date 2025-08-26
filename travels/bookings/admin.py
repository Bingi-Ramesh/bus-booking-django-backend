from django.contrib import admin
from .models import Bus,Seat 


class BusAdmin(admin.ModelAdmin):
    list_display=('bus_name','number','origin','destination','price')

class SeatAdmin(admin.ModelAdmin):
    list_display=('bus','seat_number')

admin.site.register(Bus,BusAdmin) 
admin.site.register(Seat)
