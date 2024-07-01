from django.urls import path
from .views import register, user_login,  user_logout, sinoplu_detail,  kullanim_sartlari, sinoplu_update, filter_list, about, like,  sinop, contact, services,  sinop_detail
from django.contrib.auth import views as auth_views
from .forms import PasswordResetEmailCheck


urlpatterns = [
    path('', filter_list, name='list'),
    path('services/', services, name='services'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('about/', about, name='about'),
    path('sinop/', sinop, name='sinop'),
    path('sinop/sinop_detail/', sinop_detail, name='sinop_detail'),
    path('contact/', contact, name='contact'),
    path('register/kullanim_sartlari/', kullanim_sartlari, name='kullanim_sartlari'), 
    path('<slug:slug>/', sinoplu_detail, name='detail'),
    path('update/<slug:slug>/', sinoplu_update, name='update'),
    path('<slug:slug>/like',like, name="like"),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="users/password_reset_email.html", form_class=PasswordResetEmailCheck), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),
]