from django.db import models
from django.utils.encoding import smart_text
# Create your models here.

PUBLISH_CHOICES = [
        ('draft', 'Draft'),
        ('publish', 'Publish'),
        ('private', 'Private'),
    ]

class PostModel(models.Model):
    id          = models.BigAutoField(primary_key=True)
    active      = models.BooleanField(default=True) #empty in the database
    title       = models.CharField(max_length=240, verbose_name='Post title')
    content     = models.TextField(null=True, blank=True)
    publish     = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    #id = models.IntegerField(primary_key=True) #auto increments 1, 2, 3, 4, 

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __unicode__(self): #python 2
        return smart_text(self.title) #self.title

    def __str__(self): #python 3
        return smart_text(self.title)



'''
python manage.py makemigrations #every time you change models.py
python manage.py migate


ModelForm
forms.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')

'''