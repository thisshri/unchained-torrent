from django.db import models

class TorrentFile(models.Model):
    name = models.CharField(max_length=255)
    uploader = models.CharField(max_length=25)
    location = models.FileField(upload_to='torrents/')
    uploadTime = models.DateTimeField(auto_now = False, auto_now_add = True)
