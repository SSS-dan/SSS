from django import forms
from .models import Comment, Post
from users.models import User


class NicknameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname']


class PostForm(forms.ModelForm):
    board_choices = [
        (0, '전체 게시판'),
        (1, '자유 게시판'),
        (2, '익명 게시판'),
        (3, '질의응답'),
        (4, '자료실'),
    ]
    mod = forms.ChoiceField(choices=board_choices)

    class Meta:
        model = Post
        fields = ['mod', 'title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }