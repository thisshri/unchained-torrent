from django.contrib.auth.models import User

from django.contrib.auth import  authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from files.models import TorrentFile

from django.contrib.auth.forms import UserCreationForm



from django.contrib.auth import authenticate, login, logout

def myLogin(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            #return render(request, profile)
            return redirect('profile')

        else:
            return redirect('urlLogin')

def myLogout(request):
    logout(request)
    return redirect('home')
    # Redirect to a success page.




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



@login_required(login_url="/login/")
def profile(request):
    torrentFile = TorrentFile.objects.filter(uploader__icontains=request.user.username)
    return render(request, 'profile.html',{'tFiles':torrentFile} )
