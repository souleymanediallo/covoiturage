from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete/', views.delete_user, name='delete'),
    path('update/', views.profile_update, name='profile-update'),
    path('password-reset/',
             auth_views.PasswordResetView.as_view(
                 template_name="accounts/password_reset.html"
             ),
             name="password_reset"),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="accounts/password_reset_done.html"
         ),
         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="accounts/password_reset_confirm.html"
         ),
         name="password_reset_confirm"),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="accounts/password_reset_complete.html"
         ),
         name="password_reset_complete"),
]