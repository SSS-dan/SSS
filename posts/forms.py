from django import forms
from .models import Comment, Post
from users.models import User


class NicknameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
