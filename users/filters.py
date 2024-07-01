import django_filters
from .models import UserProfile


class SinopluFilter(django_filters.FilterSet):
    class Meta:
        model = UserProfile
        fields = ['category' ,'city',]     

    def __init__(self, *args, **kwargs):
        super(SinopluFilter, self).__init__(*args, **kwargs)
        self.filters['category'].label=" Faaliet Alanı "
        self.filters['city'].label=" Şehir "




