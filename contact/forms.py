from django import forms
from .models import Comment
from django.core.mail import send_mail

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'