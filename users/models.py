from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField




def user_directory_path(instance, filename):
    return 'user/{0}/{1}'.format(instance.user.id, filename)

class UserProfile(models.Model):
    CategoryChoices = [
        ('egitim', 'Eğitim'),  
        ('saglik' ,'Sağlık' ),
        ('insaat' ,'İnşaat '),
        ('gida' , 'Gıda'),
        ('ulasim' ,'Ulaşım' ),
        ('diger' , 'Diğer')
    ]
    CityChoices = [
        ('istanbul' , 'İstanbul'),
        ('sinop' ,'Sinop' ),
        ('ankara' ,'Ankara' )
    ]
    OPTIONS = (
        ('e', 'odendi'),
        ('h', 'odenmedi')
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField( max_length=30)
    last_name = models.CharField( max_length=30)
    firm_name = models.CharField( max_length=25, null=True, blank=True) 
    biography = models.TextField(max_length=50000, blank=True, null=True ) 
    phone_number = models.IntegerField( blank=True, null=True)
    category = models.CharField( max_length=20,  blank=True, null=True, choices=CategoryChoices)
    city = models.CharField( max_length=20,  blank=True, null=True, choices=CityChoices)
    web_adres = models.URLField(blank=True, null=True, default='')
    profile_pic1 = ResizedImageField(upload_to=user_directory_path, crop=['middle', 'center'])
    profile_pic2 = ResizedImageField(upload_to=user_directory_path, crop=['middle', 'center'])
    profile_pic3 = ResizedImageField(upload_to=user_directory_path, crop=['middle', 'center'])
    avatar = ResizedImageField(size=[150, 150], upload_to=user_directory_path, crop=['middle', 'center'], blank=True, null=True)
    register_date = models.DateTimeField(verbose_name = 'kayıt tarihi', auto_now_add = True)
    instagram = models.URLField( max_length=100, blank=True)
    facebook = models.URLField( max_length=100, blank=True)
    twitter = models.URLField( max_length=100, blank=True)
    youtube = models.URLField( max_length=100, blank=True, null=True)
    linkedin = models.URLField( max_length=100, blank=True, null=True)
    pinterest = models.URLField( max_length=100, blank=True, null=True)
    paid_status = models.CharField(max_length=10, choices=OPTIONS, default='e')
    age = models.IntegerField(blank=True, null=True) 
    interests = models.CharField(max_length = 255, null = True, blank = True )
    my_checkbox = models.BooleanField()
    FilterFields = ['category', 'city']
    slug = models.SlugField( blank=True, unique=True )



    def view_count(self):
        return self.profileview_set.all().count()

    def like_count(self):
        return self.like_set.all().count()
        

    def save(self, *args, **kwargs):
        try:
            this = UserProfile.objects.get(id=self.id)
            if this.profile_pic1 != self.profile_pic1:
                this.profile_pic1.delete()
            try:
                this = UserProfile.objects.get(id=self.id)
                if this.profile_pic2 != self.profile_pic2:
                    this.profile_pic2.delete()
                try:
                    this = UserProfile.objects.get(id=self.id)
                    if this.profile_pic3 != self.profile_pic3:
                        this.profile_pic3.delete()
                    try:
                        this = UserProfile.objects.get(id=self.id)
                        if this.avatar != self.avatar:
                            this.avatar.delete()
                    except: pass
                    super(UserProfile, self).save(*args, **kwargs)
                except: pass
                super(UserProfile, self).save(*args, **kwargs)
            except: pass
            super(UserProfile, self).save(*args, **kwargs)
        except: pass
        super(UserProfile, self).save(*args, **kwargs)


 

    def __str__(self):
        return f" {self.register_date} - {self.user_id} - {self.user.username} - {self.first_name} - {self.last_name} - {self.user.email} - {self.firm_name}"
    

    class Meta:
        ordering = ["register_date"]
        verbose_name_plural = "sinoplu listesi"



class Contact(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    guess_email = models.EmailField(max_length = 100)
    guess_number = models.IntegerField()
    message = models.TextField()
    # message_date = models.DateTimeField(verbose_name = 'mesaj tarihi', auto_now_add = True)



    def __str__(self):
        return f" {self.first_name} - {self.last_name} - {self.guess_email} - {self.guess_number} - {self.message}  "



    class Meta:
        verbose_name_plural = "Mesajlar"
    



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    view_and_like = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Like sayısı"

class ProfileView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    view_and_like = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
 
    
    def __str__(self):
        return self.user.username  

    class Meta:
        verbose_name_plural = "Görülme sayısı"
    