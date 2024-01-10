from django.db import models
from accounts.models import Profile
from django.conf import settings
import uuid
from django.urls import reverse


# Create your models here.
class Conversation(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="conversations",)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.sender} to {self.recipient}"

    def get_absolute_url(self):
        return reverse("conversation-create", kwargs={"pk": self.pk})

    def get_conversation_url(self):
        return reverse("conversation", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["is_read", "-created"]
