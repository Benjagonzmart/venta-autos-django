from django.contrib import admin
from .models import Auto



@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "year", "precio", "kilometraje")
    list_filter = ("marca", "year")
    search_fields = ("marca", "modelo")
# Register your models here.
