from django.db import models
# Create your models here.

class PostModel(models.Model):
    id          = models.BigAutoField(primary_key=True)
    active      = models.BooleanField(default=True) #empty in the database
    title       = models.CharField(max_length=240, verbose_name='Post title')
    content     = models.TextField(null=True, blank=True)
    #id = models.IntegerField(primary_key=True) #auto increments 1, 2, 3, 4, 

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'



'''
python manage.py makemigrations #every time you change models.py
python manage.py migate

'''