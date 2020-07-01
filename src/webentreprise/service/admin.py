from django.contrib import admin

# Register your models here.
from .models import service

class serviceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(service,serviceAdmin)