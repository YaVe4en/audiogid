import math
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Region, Category, PointOfInterest
from .serializers import (
    RegionSerializer,
    CategorySerializer,
    PointOfInterestListSerializer,
    PointOfInterestDetailSerializer,
)
from .filters import PointOfInterestFilter

class RegionListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [AllowAny]

class RegionDetailView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [AllowAny]

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class PointOfInterestListView(generics.ListAPIView):
    serializer_class = PointOfInterestListSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PointOfInterestFilter
    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'name']
    ordering = ['-created_at']

    def get_queryset(self):
        return (
            PointOfInterest.objects
            .filter(is_published=True)
            .select_related('category', 'region')
            .prefetch_related('photos')
        )

class PointOfInterestDetailView(generics.RetrieveAPIView):
    queryset = PointOfInterest.objects.filter(is_published=True)
    serializer_class = PointOfInterestDetailSerializer
    permission_classes = [AllowAny]