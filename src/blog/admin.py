from django.contrib import admin

# Register your models here.

from .models import PostModel


class PostModelAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'content',
        'publish',
        'publish_date',
        'active',
        'updated',
        'timestamp',
        'new_content'
    ]
    readonly_fields = ['updated', 'timestamp', 'new_content']
    def new_content(self, obj, *args, **kwargs):
        return str(obj.title)
    
    class Meta:
        model = PostModel

admin.site.register(PostModel, PostModelAdmin)