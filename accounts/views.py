from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserCreationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = user.first_name.capitalize()
            user.last_name = user.last_name.capitalize()
            user.save()

            messages.success(request, 'Account created successfully')

            login(request, user)
            return redirect('home')
    else:
        messages.error(request, 'An error has occured during registration')
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_user(request):
    if request.method == "POST":
        email = request.POST["email"].lower()
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Erreur email ou mot de passe")

    return render(request, "accounts/login.html")
