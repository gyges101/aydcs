from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as dj_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated_user
from .models import info, essai, coursVa
from .forms import infoRecu, essaiRecu

# Create your views here.

def home(request):
    coursList = coursVa.objects.all()
    if request.method == 'POST':
        form2 = essaiRecu(request.POST)
        if form2.is_valid():
            form2.save() 
    

    else:
        form2 = essaiRecu()

    return render(request, 'index.html', {'ess': essaiRecu, 'coursList': coursList})

def cours(request):
    coursList = coursVa.objects.all()
    if request.method == 'POST':
        form2 = essaiRecu(request.POST)
        if form2.is_valid():
            form2.save() 
    

    else:
        form2 = essaiRecu()

    return render(request, 'cours.html', {'ess': essaiRecu, 'coursList': coursList})

def a_propos(request):

    return render(request, 'about.html', {})

def galerie(request):

    return render(request, 'galerie.html', {})

def contact(request):
    if request.method == 'POST':
        form = infoRecu(request.POST)
        if form.is_valid():
            form.save() 
    

    else:
        form = infoRecu()

    return render(request, 'contact.html', {'msg': infoRecu})

#admin View

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
                dj_login(request, user)
                return redirect('/portail')
        else:
            return redirect('/login')
    return render(request, 'login/index.html', {})


def logoutPage(request):

    logout(request)
    return redirect('/')


@login_required
def portail(request):
    msg = info.objects.all()
    dmn = essai.objects.all()
    context = {
        'msg': msg,
        'dmn': dmn,
    }

    return render(request, 'portail/received.html', context)

@login_required
def message(request, pk):
    rec = info.objects.get(id=pk)

    return render(request, 'portail/message.html', {'rec': rec})

@login_required
def delete(request, pk):
    rec = get_object_or_404(info, pk=pk)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        rec.delete()                     # delete the cat.
        return redirect('/portail')             # Finally, redirect to the homepage.

    return render(request, 'portail/received.html', {'rec': rec})

@login_required
def delete_essai(request, pk):
    ess = get_object_or_404(essai, pk=pk)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        ess.delete()                     # delete the cat.
        return redirect('/portail')             # Finally, redirect to the homepage.

    return render(request, 'portail/received.html', {'ess': ess})

