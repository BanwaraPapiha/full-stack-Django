from django.contrib import admin
from .models import *


class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination', 'duration')


class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ('flight',)


# Register your models here.
admin.site.register(Flights, FlightAdmin)
admin.site.register(Airports)
admin.site.register(Passengers, PassengerAdmin)