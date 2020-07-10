from django.contrib import admin

# Register your models here.
from .models import link

class linkAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    def get_readonly_fields(self,request,obj=None):
        if request.user.groups.filter(name='Personal'):
            return ('key','name')
        else:
            return ('created','updated')

admin.site.register(link,linkAdmin)