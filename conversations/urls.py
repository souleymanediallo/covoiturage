from django.urls import path
from . import views

urlpatterns = [
    path("inbox/", views.inbox, name="inbox"),
    path("conversation/<uuid:pk>/", views.conversation_list, name="conversation"),
    path("conversation-create/<uuid:profile_id>/", views.conversation_create, name="conversation-create"),
    path("reply/<uuid:conversation_id>/", views.reply_to_conversation, name="reply_to_conversation"),
]
