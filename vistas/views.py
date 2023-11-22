from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import CustomUserCreationForm
# Views here.


def inicio(request):

    return render(
        request,
        'base.html',
    )


def home(request):

    return render(
        request,
        'home.html',
    )


@login_required
def atletas(request):

    return render(
        request,
        'atletas.html'
    )


def info(request):

    return render(
        request,
        'info.html',
    )


def acceder(request):

    return render(
        request,
        './registration/login.html',
    )


def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        create_new_user = CustomUserCreationForm(data=request.POST)
        if create_new_user.is_valid():
            create_new_user.save()
            user = authenticate(
                username=create_new_user.cleaned_data['username'], password=create_new_user.cleaned_data['password1'])
            login(request, user)
            return redirect('home')

    return render(
        request,
        './registration/register.html',
        data,

    )


def salir(request):
    logout(request)

    return redirect('home')
