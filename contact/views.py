from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from config.settings import dev
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method == "POST":
        sender = dev.EMAIL_HOST_USER
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        mail = send_mail(name, email, message, [sender], fail_silently=False)
        if mail:
            messages.success(request, 'Votre message a été envoyé.')
            return redirect('sent-email')
        else:
            return HttpResponse('Veuillez compléter tous les champs')
    else:
        return render(request, 'contact/contact.html')


def sent_email(request):
    return render(request, "contact/sent-email.html")