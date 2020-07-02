from django.contrib import admin
from .models import category, post

# Register your models here.
class postAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','author','published','post_admin')
    ordering = ('author','published')
    search_fields = ('title','content','author__username','categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')

    def post_admin(self,obj):
        return ', '.join([c.name for c in category.objects.all().order_by('name')])
    post_admin.short_description = "Categories" # this is for creating a custom field name in the admin panel, since it just shows the 
                                                # name of the class by default
class categoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(category,categoryAdmin)
admin.site.register(post,postAdmin)