from django import template
from pages.models import page

register = template.Library()

@register.simple_tag
def get_page_list():
    pages = page.objects.all()
    return pages