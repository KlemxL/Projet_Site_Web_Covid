
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,ProfileForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Votre compte a ete cree')
            return redirect('login')
    else:
        u_form = UserRegisterForm()
    return render(request, 'users/register.html', locals())


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Informations sauvegardees')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/edit_profile.html', locals())
def profile(request):
    return render(request,'users/profile.html')
