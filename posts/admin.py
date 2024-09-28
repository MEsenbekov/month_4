from django.contrib import admin

from posts.models import Post, Category, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'rate', 'created', 'updated']
    list_display_links = ['title', 'content', 'created', 'updated']
    list_editable = ['rate']
    list_per_page = 2


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'post']
    list_display_links = ['text', 'post']

# Register your models here.
