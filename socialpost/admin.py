from django.contrib import admin

from .models import *

class PostPhotosInLine(admin.TabularInline):
    model = PostPhotos


class PostAdmin(admin.ModelAdmin):
    inlines = [PostPhotosInLine]


admin.site.register(Post, PostAdmin)