from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import UserProfile
from .utils import get_random_code



@receiver(pre_save, sender=UserProfile)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.first_name.replace('ı', 'i') +"-"+ instance.last_name.replace('ı', 'i') +"-" + get_random_code())
