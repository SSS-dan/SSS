from django import forms
from django.contrib.auth import get_user_model
from .models import UserProfile
User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']
