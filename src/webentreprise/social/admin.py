from django.contrib import admin

# Register your models here.
from .models import link

class linkAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(link,linkAdmin)