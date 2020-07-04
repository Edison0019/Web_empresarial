from django.db import models

# Create your models here.
class link(models.Model):
    key = models.SlugField(verbose_name="Password",unique=True,max_length=100)
    name = models.CharField(verbose_name="username", max_length=200)
    url = models.URLField(verbose_name="Link", max_length=200,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ['-created']

    def __str__(self):
        return self.name    