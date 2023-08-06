from django.contrib import admin
from .models import Mxpi_SArduino_in,Mxpi_SArduino_out

class Mxpi_SArduino_in_Admin(admin.ModelAdmin):
    list_display = ("data","publish")

class Mxpi_SArduino_out_Admin(admin.ModelAdmin):
    list_display = ("data","publish")

admin.site.register(Mxpi_SArduino_in,Mxpi_SArduino_in_Admin)
admin.site.register(Mxpi_SArduino_out,Mxpi_SArduino_out_Admin)