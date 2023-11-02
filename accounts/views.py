from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserCreationForm, CustomUserUpdateForm, ProfileUpdateForm
from trips.models import Trip


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


@login_required
def profile_update(request):
    if request.method == "POST":
        u_form = CustomUserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            first_name = u_form.cleaned_data.get("first_name")
            messages.success(request, f"{first_name}, votre compte a été mis à jour")
            return redirect('dashboard')
    else:
        u_form = CustomUserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "accounts/update.html", context)


@login_required
def delete_user(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        messages.success(request, "Votre compte a été supprimé avec succès.")
        return redirect("home")

    return render(request, "accounts/delete.html")


@login_required
def dashboard(request):
    trips = Trip.objects.filter(author=request.user)
    context = {"trips": trips}
    return render(request, 'accounts/dashboard.html', context)
