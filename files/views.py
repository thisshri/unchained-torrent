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
    return render(request, 'files/index.html',{'tFiles':torrentFile})

def register(request):
    return render(request, 'files/register.html')

@login_required(login_url="/login/")
def model_form_upload(request):
    print("\n\n\n\n")
    print(request.user.username)
    print("\n\n\n\n")

    if request.method == 'POST':
        form = TorrentFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TorrentFileForm()
    return render(request, 'torrentFileUpload.html', {
        'form': form
    })

def search(request, q):
    userQuery = request.GET['q']
    #print('\n')

    #print('USER QUERY IS :{0}'.format(userQuery))


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
