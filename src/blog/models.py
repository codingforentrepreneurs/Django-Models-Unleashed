from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone 
from django.utils.text import slugify
# Create your models here.


from .validators import validate_author_email, validate_justin

PUBLISH_CHOICES = [
        ('draft', 'Draft'),
        ('publish', 'Publish'),
        ('private', 'Private'),
    ]

class PostModel(models.Model):
    id              = models.BigAutoField(primary_key=True)
    active          = models.BooleanField(default=True) #empty in the database
    title           = models.CharField(max_length=240, verbose_name='Post title', unique=True)
    slug            = models.SlugField(null=True, blank=True)
    content         = models.TextField(null=True, blank=True)
    publish         = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count      = models.IntegerField(default=0)
    publish_date    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email    = models.EmailField(max_length=240, validators=[validate_justin], null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        #unique_together = [('title', 'slug')]

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