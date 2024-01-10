from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConversationForm
from accounts.models import Profile
from .models import Conversation
from django.contrib import messages


# Create your views here.
def inbox(request):
    profile = request.user
    conversation_requests = profile.conversations.all()
    unread_count = conversation_requests.filter(is_read=False).count()
    context = {"conversation_requests": conversation_requests, "unread_count": unread_count}
    return render(request, "conversations/inbox.html", context)


def conversation_list(request, pk):
    profile = request.user
    conversation = profile.conversations.get(id=pk)
    if conversation.is_read == False:
        conversation.is_read = True
        conversation.save()
    context = {"conversation": conversation}
    return render(request, "conversations/conversation.html", context)


def conversation_create(request, profile_id):
    recipient = get_object_or_404(Profile, pk=profile_id)
    form = ConversationForm()

    try:
        sender = request.user
    except:
        sender = None

    if request.method == "POST":
        form = ConversationForm(request.POST)
        if form.is_valid():
            conversation = form.save(commit=False)
            conversation.sender = sender
            conversation.recipient = recipient.user
            conversation.save()

            messages.success(request, "Votre message été envoyé !")
            return redirect("home")

    context = {"recipient": recipient, "form": form}
    return render(request, "conversations/conversation_form.html", context)
