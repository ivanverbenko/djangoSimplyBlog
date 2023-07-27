from .models import *
from django import forms

class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'