from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConversationForm
from accounts.models import Profile
from .models import Conversation
from django.contrib import messages
from trips.models import Trip


@login_required
# Create your views here.
def inbox(request):
    profile = request.user
    conversation_requests = profile.conversations.all()
    unread_count = conversation_requests.filter(is_read=False).count()
    context = {"conversation_requests": conversation_requests, "unread_count": unread_count}
    return render(request, "conversations/inbox.html", context)


@login_required
def conversation_list(request, pk):
    profile = request.user
    conversation = profile.conversations.get(id=pk)
    if conversation.is_read == False:
        conversation.is_read = True
        conversation.save()
    context = {"conversation": conversation}
    return render(request, "conversations/conversation.html", context)


@login_required
def conversation_create(request, profile_id, trip_id):
    recipient = get_object_or_404(Profile, pk=profile_id)
    trip = get_object_or_404(Trip, pk=trip_id)

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

    context = {"recipient": recipient, "form": form, 'trip': trip}
    return render(request, "conversations/conversation_form.html", context)


@login_required
def reply_to_conversation(request, conversation_id):
    conversation = get_object_or_404(Conversation, pk=conversation_id)
    form = ConversationForm()
    if request.method == "POST":
        form = ConversationForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = request.user
            # Supposons que recipient est l'autre utilisateur dans la conversation
            new_message.recipient = conversation.get_other_participant(request.user)
            new_message.save()
            return redirect(conversation.get_absolute_url())  # Redirige vers la page de conversation

        # Récupérer tous les messages de la conversation pour l'utilisateur connecté
    conversation_messages = Conversation.objects.filter(
        Q(sender=request.user, recipient=conversation.get_other_participant(request.user)) |
        Q(sender=conversation.get_other_participant(request.user), recipient=request.user)
    ).order_by('created')
    context = {"conversation_messages": conversation_messages, "form": form, "conversation": conversation}
    return render(request, 'conversations/conversation.html', context)
    