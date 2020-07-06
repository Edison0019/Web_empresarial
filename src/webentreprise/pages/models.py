from django.db import models

# Create your models here.
class page(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200)
    content = models.TextField(verbose_name='Write the name content of the page')
    order = models.SmallIntegerField(verbose_name='ordering',default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creation date')
    updated = models.DateTimeField(auto_now=True,verbose_name='Last change date')

    class Meta():
        ordering = ['order','-created']

    def __str__(self):
        return self.title    