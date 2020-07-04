from .models import link
def context_processor(request):
    social_media = link.objects.all()
    social = {}
    for elm in social_media:
        social[elm.key] = elm.url
    return social