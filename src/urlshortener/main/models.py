# from django.utils import timezone
from django.db import models

# Create your models here.
class ShortUrl(models.Model):
    original_url = models.CharField(max_length=256)             # URL to be shortened
    short_url_code = models.CharField(max_length=6)             # Shortened URL code (length: 6)
    created_at = models.DateTimeField(auto_now_add=True)        # Creation time
    times_used = models.IntegerField(default=0)                 # Number of times a short URL has been used
