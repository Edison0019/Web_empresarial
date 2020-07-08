from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ['-created']

    def __str__(self):
        return self.name

class post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    published = models.DateTimeField(verbose_name="Enter the published date",auto_now=False, auto_now_add=False,default=now)
    image = models.ImageField(verbose_name="Enter image",upload_to="blog",null=True,blank=True)
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    categories = models.ManyToManyField(category, verbose_name="Categories",related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ['-created']

    def __str__(self):
        return self.title