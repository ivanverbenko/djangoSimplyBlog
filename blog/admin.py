from django.contrib import admin
from .models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'full_text', 'summary','category','slug']
    list_display=['title', 'full_text', 'summary','category','pubdate']
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)