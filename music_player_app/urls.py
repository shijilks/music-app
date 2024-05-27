# music_player_app/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from music_player_app.views import register, user_login, index, update_song, add_song

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('', index, name='home'),
    path('update-song/<int:pk>/', update_song, name='update_song'),  # Ensure consistency in URL patterns
    path('add-song/', add_song, name='add_song'),  # Ensure consistency in URL patterns
]
