import django_filters
from .models import PointOfInterest


class PointOfInterestFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__slug', lookup_expr='exact')
    region = django_filters.NumberFilter(field_name='region__id', lookup_expr='exact')

    class Meta:
        model = PointOfInterest
        fields = ['category', 'region']
