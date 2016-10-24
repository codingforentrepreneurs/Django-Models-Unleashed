from django.db import models
# Create your models here.

class PostModel(models.Model):
    id          = models.BigAutoField(primary_key=True)
    active      = models.BooleanField(default=True) #empty in the database
    #id = models.IntegerField(primary_key=True) #auto increments 1, 2, 3, 4, 
    pass



'''
python manage.py makemigrations #every time you change models.py
python manage.py migate

'''