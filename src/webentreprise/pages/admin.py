from django.contrib import admin

# Register your models here.
from .models import page

class pageAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(page,pageAdmin)