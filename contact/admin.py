from django.contrib import admin
from django import forms
from contact.models import Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message','date')


admin.site.register(Comment, CommentAdmin)
