#from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from files.forms import TorrentFileForm
from files.models import TorrentFile
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required

def index(request):
    torrentFile = TorrentFile.objects.all()
    return render(request, 'index.html',{'tFiles':torrentFile})

def register(request):
    return render(request, 'register.html')

@login_required(login_url="/login/")
def model_form_upload(request):
    if request.method == 'POST':
        fileUploadForm = TorrentFileForm(request.POST, request.FILES)


        if fileUploadForm.is_valid():
            torrentForm = fileUploadForm.save(commit = False)

            # name of the uploader
            torrentForm.uploader = request.user.username

            #name of the file
            torrentForm.name = request.FILES['location'].name #location being the name of input tag

            #torrentForm.name = fileUploadForm.fields['location'].files.name
            torrentForm.save()
            #return HttpResponse("form is valid")
            return redirect('profile')
        else:
            return HttpResponse("form is not valid")
        #    return HttpResponse("<h1>file not valid</h1>")
    else:
        fileUploadForm = TorrentFileForm()
    return render(request, 'torrentFileUpload.html', {'form': fileUploadForm})

def search(request, q):
    userQuery = request.GET['q']
    torrentFile = TorrentFile.objects.filter(name__icontains=userQuery)
    return render(request, 'search.html',{'tFiles':torrentFile} )

'''
def torrentDownload(request, torrentPath):
    file_path = os.torrentPath.join(settings.MEDIA_ROOT, torrentPath)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/x-bittorrent")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404
'''
