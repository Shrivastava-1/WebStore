from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'image']
        widgets = {
            'image': forms.FileInput(),
        }
