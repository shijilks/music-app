# music_player_app/forms.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser
from api.models import Song  # Import Song model from api app

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'category', 'artist', 'audio_file', 'audio_img']
