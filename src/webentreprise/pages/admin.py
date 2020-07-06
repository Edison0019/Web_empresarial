from django.contrib import admin

# Register your models here.
from .models import page

class pageAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','order')

admin.site.register(page,pageAdmin)