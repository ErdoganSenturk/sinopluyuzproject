from django.contrib import admin
from .models import UserProfile, Contact, Like, ProfileView
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin


class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = ('biography')
    list_display = ( 'register_date', 'user', 'first_name', 'last_name', 'firm_name',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','guess_email', 'guess_number', 'message',)

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user','view_and_like', )

class ProfileViewAdmin(admin.ModelAdmin):
    list_display = ('user','view_and_like', )
    

admin.site.register(UserProfile,  SummerAdmin)   
admin.site.register(Contact, ContactAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(ProfileView, ProfileViewAdmin)
