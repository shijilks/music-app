# api/models.py
from django.db import models

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True, default=None)  # renamed 'categorie' to 'category'
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/')
    audio_img = models.FileField(upload_to='audio_img/')
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Optional: Add a timestamp for when the song was uploaded

    def __str__(self):
        return f"{self.title} by {self.artist}"
