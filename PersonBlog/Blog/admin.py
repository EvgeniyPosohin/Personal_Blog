from django.contrib import admin
from .models import Post, Blog, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created_at', 'updated_at']
    list_filter = ['author', 'title', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    raw_id_fields = ['author']
    ordering = ['created_at', 'updated_at']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    list_filter = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    ordering = ['created_at', 'updated_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'created_at']
    list_filter = ['author', 'content', 'created_at']
    search_fields = ['author', 'created_at']
    raw_id_fields = ['author']
    ordering = ['created_at']
