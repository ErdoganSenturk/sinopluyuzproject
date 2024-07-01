from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.forms import fields, ModelForm
from .models import Profile


class UserForm(UserCreationForm):
    email = forms.EmailField()
    # email.label="email"
    avatar = forms.ImageField(required=False)
    # avatar = label="avatar resminiz"

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        # for fieldname in ['username', 'avatar', 'password1', 'password2']:
        #     self.fields[fieldname].help_text = None

    class Meta():
        model=User
        fields=['username','email', 'avatar']
        labels = {'username' : 'Kullanıcı Adı',
                'password' : 'Şifre',
                'avatar' : 'avatar'
                }


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email daha önce sisteme kayıt edilmiştir. Başka bir email yazınız.")
        return email


class PasswordResetEmailCheck(PasswordResetForm):
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email sistemde yoktur.")
        return email




