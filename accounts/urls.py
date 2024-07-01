from django.urls import path
from .views import  register
from django.contrib.auth import views as auth_views
from .forms import PasswordResetEmailCheck

app_name:"accounts"
urlpatterns = [
path('register/', register, name='register'),
# path('login/', user_login, name='user_login'),
# path('logout/', user_logout, name='user_logout'),
# path("accounts_profile/", accounts_profile, name="accounts_profile"),
path("password-reset/", auth_views.PasswordResetView.as_view(template_name="users/password_reset_email.html", form_class=PasswordResetEmailCheck), name="password_reset"),
path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
path("password-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),
path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),
]