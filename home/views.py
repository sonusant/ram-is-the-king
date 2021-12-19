from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm , UsernameField
from django.contrib.auth import get_user_model
from home.forms import SignUpForm
from home.models import Incident
from django.contrib.auth.decorators import user_passes_test




def role_check(user):
    return user.role.endswith('ster')



def index(request):
    # if request.user.is_anonymous:
    #     return redirect('/signin')
    
    all_users= get_user_model().objects.all()
    
    context= {'allusers': all_users}
       
    
    
    return render (request, 'index.html', context)


def ram(request):

    if not request.user.role.endswith('ing'):
       return redirect('/signin')

    if request.method == 'POST':
        incidt = request.POST.get('incidt')
        place = request.POST.get('place')
        date = request.POST.get('date')
        king_inci = Incident.objects.create(inc_desc=incidt, inc_place=place,inc_date=date)
        king_inci.save()
        return redirect ('/')

    return render (request, 'ram.html')

    
@user_passes_test(role_check)
def laxman(request):
    # if request.user.is_anonymous:
    #     return redirect('/signin')

    context = {    
    'incident': Incident.objects.all()
    }    
    
    return render (request, 'laxman.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect ( '/signin')
    return render (request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('/signin')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Create your views here.
