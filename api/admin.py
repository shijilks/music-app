# api/admin.py
from django.contrib import admin
from .models import Song

class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'artist', 'uploaded_at')  # Assuming 'category' is the correct field name

admin.site.register(Song, SongAdmin)
