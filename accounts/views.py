from django.shortcuts import render
from multiprocessing import context
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.forms import UserForm



def register(request):
    form_user=UserForm()
    if request.method=='POST':
        form_user=UserForm(request.POST,request.FILES)
        if form_user.is_valid():
            user=form_user.save()
            profile=form_user.save(commit=False)  
            profile.user=user
            profile.save()
            login(request,user)
            messages.success(request,'Sisteme kayıt işleminiz başarı ile yapılmıştır...')
            # username = request.POST['username']
            # email = request.POST['email']
            # subject = 'Welcome to My Site'
            # message = 'Sayın Sinoplu hemşehrimiz {username} sitemize hoşgeldiniz...'
            # from_email = 'erdsen57@gmail.com'
            # recipient_list = [email]
            # send_mail (subject, message, from_email, recipient_list)
            return redirect('users:list')

    context={
        'form_user':form_user
    }
    return render(request,'users/register.html',context)