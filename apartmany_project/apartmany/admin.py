from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'content', 'date_posted')
    list_filter = ('date_posted', 'rating')
    search_fields = ('name', 'title', 'content')
