from django import forms
from files.models import TorrentFile

class TorrentFileForm(forms.ModelForm):
    class Meta:
        model = TorrentFile
        fields = ('name', 'location', 'uploader',)
