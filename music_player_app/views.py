# music_player_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm, SongForm
from api.models import Song  # Import Song model from api app
from django.conf import settings

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def index(request):
    return render(request, 'music_player_app/index.html')

@login_required
def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            # Validate file size
            uploaded_file = request.FILES['audio_file']
            if uploaded_file.size > settings.MAX_UPLOAD_SIZE:
                return HttpResponse('File size too large. Maximum allowed size is 5MB.')

            # Validate file type
            if uploaded_file.content_type not in settings.ALLOWED_FILE_TYPES:
                return HttpResponse('File type not allowed. Only MP3 and WAV files are accepted.')

            form.save()
            return redirect('index')  # Redirect to the index page or song list
    else:
        form = SongForm()
    return render(request, 'music_player_app/add_song.html', {'form': form})

@login_required
def update_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            # Validate file size if a new file is uploaded
            if 'audio_file' in request.FILES:
                uploaded_file = request.FILES['audio_file']
                if uploaded_file.size > settings.MAX_UPLOAD_SIZE:
                    return HttpResponse('File size too large. Maximum allowed size is 5MB.')

                # Validate file type
                if uploaded_file.content_type not in settings.ALLOWED_FILE_TYPES:
                    return HttpResponse('File type not allowed. Only MP3 and WAV files are accepted.')

            form.save()
            return redirect('index')  # Redirect to the index page or song list
    else:
        form = SongForm(instance=song)
    return render(request, 'music_player_app/update_song.html', {'form': form})
