from multiprocessing import context
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from users.forms import UserForm, UserProfileForm, ContactForm
from .models import UserProfile, Like, ProfileView
from django.contrib.auth.decorators import login_required
from .filters import SinopluFilter
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage




# Create your views here.

def about(request):
    return render(request, 'users/about.html')

def sinop(request):
    return render(request, 'users/sinop.html')

def sinop_detail(request):
    return render(request, 'users/sinop_detail.html')

def services(request):
    return render(request, 'users/services.html')

def  kullanim_sartlari(request):
    return render(request, 'users/kullanim_sartlari.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Mesajınız alınmıştır. En kısa sürede size geri dönüş yapılacaktır.')
            return redirect('contact')
    context={
        'form':form  
    }
    return render(request,'users/contact.html',context)



def user_logout(request):
    logout(request)
    messages.success(request,'Sistemden çıktınız..')
    return redirect('list')



def register(request):
    form_user=UserForm()
    form_profile=UserProfileForm()
    if request.method=='POST':
        form_user=UserForm(request.POST)
        form_profile=UserProfileForm(request.POST,request.FILES)
        if form_user.is_valid() and form_profile.is_valid():
            user=form_user.save()
            # print(user)
            profile=form_profile.save(commit=False)  
            profile.user=user
            # print(profile.user)
            profile.save()
            login(request,user)
            messages.success(request,'Sisteme kayıt işleminiz başarı ile yapılmıştır...')
            username = request.POST['username']
            email = request.POST['email']
            subject = 'Welcome to My Site'
            message = 'Sayın Sinoplu hemşehrimiz {username} sitemize hoşgeldiniz...'
            from_email = 'erdsen57@gmail.com'
            recipient_list = [email]
            send_mail (subject, message, from_email, recipient_list)
            return redirect('list')

    context={
        'form_profile':form_profile,
        'form_user':form_user
    }
    return render(request,'users/register.html',context)




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.info(request, 'Sisteme giriş yaptınız...')
            return redirect('list')
        else:
            messages.info(request, 'Lütfen alanları doğru olacak şekilde doldurup tekrar deneyiniz...')
            return redirect('user_login')  
    return render(request, 'users/user_login.html')





def filter_list(request): 
    sinoplu = UserProfile.objects.filter()
    mainsponsor1 = sinoplu.get(user=6)
    mainsponsor2 = sinoplu.get(user=26)
    mainsponsor3 = sinoplu.get(user=21)
    sponsor4 = sinoplu.get(user=25)
    sponsor7 = sinoplu.get(user=7)
    sponsor8 = sinoplu.get(user=8)

    filtered_persons = SinopluFilter(request.GET, queryset=UserProfile.objects.all())
    paginator = Paginator(filtered_persons.qs,9 )
    page = request.GET.get('page')
    try:
        paginated_objects = paginator.page(page)
    except PageNotAnInteger:
        paginated_objects = paginator.page(1)
    except EmptyPage:
        paginated_objects = paginator.page(paginator.num_pages)
    
    context = {
        "filtered_persons": filtered_persons,
        "paginated_objects": paginated_objects,
        'mainsponsor1' : mainsponsor1,
        'mainsponsor2' : mainsponsor2,  
        'mainsponsor3' : mainsponsor3,  
        'sponsor4' : sponsor4,
        'sponsor7' : sponsor7,
        'sponsor8' : sponsor8,
    }
    
    return render(request, 'users/index.html', context)




def sinoplu_detail(request, slug):   
    sinoplulardan = UserProfile.objects.get(slug=slug)
    if sinoplulardan.interests:
        converted_interests = sinoplulardan.interests.replace("'", "").replace("[", "").replace("]", "").capitalize()
    else:
        converted_interests = sinoplulardan.interests
        
    if request.user.is_authenticated :
        ProfileView.objects.get_or_create(user=request.user, view_and_like = sinoplulardan)

    context = {
        'sinoplu': sinoplulardan,
        'converted_interests':converted_interests,
    }
    return render(request, 'users/sinoplu_details.html', context)




@login_required()
def sinoplu_update(request, slug ):
    sinoplu=UserProfile.objects.get(slug=slug)
    form=UserProfileForm(instance=sinoplu)
    if form.instance.user != request.user:
        messages.warning(request, "Sadece kendi profil sayfanızda güncelleme yapabilirsiniz...")
        return redirect('list')
    if request.method=='POST':
        form=UserProfileForm(request.POST or None, request.FILES or None, instance=sinoplu)
        if form.is_valid():
            form.save()
            messages.success(request, "Sistemdeki profil bilgilerinin başarılı bir şekilde güncellenmiştir.")
            return redirect('detail', slug=slug)
    else:
        form = UserProfileForm(instance=sinoplu)
    
    context={
        'form':form,
    }
    return render(request,'users/sinoplu_update.html',context)




@login_required()
def like(request, slug):
    if request.method == "POST":
        obj = get_object_or_404(UserProfile, slug=slug)
        like_qs = Like.objects.filter(user=request.user, view_and_like = obj)
        if like_qs.exists():
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, view_and_like = obj)
            messages.info(request, 'Profilimi beğendiğiniz için teşekkür ederim sayın...')
        return redirect("detail", slug=slug)
    return redirect("detail", slug=slug)



