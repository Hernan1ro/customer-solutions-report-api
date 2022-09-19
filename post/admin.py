from django.contrib import admin
from post.models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['index', 'strategy', 'process', 'people', 'customers']