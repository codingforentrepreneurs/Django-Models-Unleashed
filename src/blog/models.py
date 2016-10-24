from django.db import models
from django.db.models.signals import pre_save, post_save
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
    title           = models.CharField(
                            max_length=240, 
                            verbose_name='Post title', 
                            unique=True,
                            error_messages={
                                "unique": "This title is not unique, please try again.",
                                "blank": "This field is not full, please try again."
                            },
                            help_text='Must be a unique title.')
    slug            = models.SlugField(null=True, blank=True)
    content         = models.TextField(null=True, blank=True)
    publish         = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count      = models.IntegerField(default=0)
    publish_date    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email    = models.EmailField(max_length=240, validators=[validate_justin], null=True, blank=True)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        # if not self.slug and self.title:
        #     self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        #unique_together = [('title', 'slug')]

    def __unicode__(self): #python 2
        return smart_text(self.title) #self.title

    def __str__(self): #python 3
        return smart_text(self.title)


def blog_post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    print("before save")
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title) 

pre_save.connect(blog_post_model_pre_save_receiver, sender=PostModel)



def blog_post_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    print("after save")
    print(created)
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()

post_save.connect(blog_post_model_post_save_receiver, sender=PostModel)







'''
python manage.py makemigrations #every time you change models.py
python manage.py migate


ModelForm
forms.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')

'''