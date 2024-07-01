from django.contrib.auth.models import User
from .models import UserProfile, Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.forms import fields, ModelForm
# from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget



class UserForm(UserCreationForm):
    email = forms.EmailField()
    email.label="email"

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta():
        model=User
        fields=['username','email']
        labels = {'username' : 'Kullanıcı Adı',
                'password' : 'Şifre',
                }


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email daha önce sisteme kayıt edilmiştir. Başka bir email yazınız.")
        return email

class UserProfileForm(forms.ModelForm):
    interests_selection = (
        ('kitap okumak', 'kitap okumak'),
        ('müzik dinlemek', 'müzik dinlemek'),
        ('seyahat etmek', 'seyahat etmek'),
        ('internet', 'internet'),
        ('balık tutmak', 'balık tutmak'),
    )
    
    # biography = forms.CharField(widget=SummernoteWidget())
    interests = forms.MultipleChoiceField(choices = interests_selection, required=False, label='İlgi alanları', widget = forms.CheckboxSelectMultiple())

    class Meta():
        model=UserProfile
        fields=["first_name", "last_name", "firm_name", "biography", "phone_number", "category", "city", "web_adres", "profile_pic1", "profile_pic2", "profile_pic3", "avatar", 'instagram', 'facebook', 'twitter','youtube','linkedin','pinterest', 'interests', 'age', 'my_checkbox'] 
        labels = {'first_name' : 'Adı',
                'last_name' : 'Soyadı',
                'firm_name' : 'Firma Adı',
                'biography' : 'Biyografi',
                'phone_number' : 'Telefon',
                'category' : 'Faaliyet Alanı',
                'city' : 'Lokasyon',
                'web_adres' : 'Web Adresi (eğer sayfanız varsa başına http:// yazmayı unutmayınız)',
                'profile_pic1' : 'Resim 1',
                'profile_pic2' : 'Resim 2',
                'profile_pic3' : 'Resim 3',
                'avatar' : 'Profil Resmi',
                'instagram' : 'İnstagram',
                'facebook' : 'Facebook',
                'twitter' : 'Twitter',
                'youtube': 'youtube',
                'linkedin': 'linkedin',
                'pinterest':'pinterest',  
                'age' : 'Yaş',
                'my_checkbox': ''
                }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control custom-class'}),
            'city': forms.Select(attrs={'class': 'form-control custom-class'}),
            'my_checkbox' :forms.CheckboxInput(attrs={'class':'form-control', 'initial' : False, 'required' :True, 'label' : 'Kayıt olma şartlarını okunuduz mu' }),
            }

        def selected_interests_labels(self):
            return [label for value, label in self.fields['interests'].choices if value in self['interests'].value()]        

class PasswordResetEmailCheck(PasswordResetForm):
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email sistemde yoktur.")
        return email


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adı'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Soyadı'}))  
    guess_email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'})) 
    guess_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Telefon'})) 
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Buraya mesajınızı yazınız. Size daha hızlı ulaşmak için telefon bilgiside yazabilirsiniz.'}))

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'guess_email', 'guess_number', 'message']



