from django.db import models
from django.contrib.auth.models import User

def user_profile_path(instance, filename):
    return 'user/{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to= user_profile_path)


    def __str__(self):
        return "{} {}".format(self.user, 'Profile')