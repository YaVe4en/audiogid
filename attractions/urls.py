from django.urls import path
from .views import (
    RegionListView,
    RegionDetailView,
    CategoryListView,
    PointOfInterestListView,
    PointOfInterestDetailView,
)

urlpatterns = [
    path('regions/', RegionListView.as_view(), name='region-list'),
    path('regions/<int:pk>/', RegionDetailView.as_view(), name='region-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('points/', PointOfInterestListView.as_view(), name='point-list'),
    path('points/<int:pk>/', PointOfInterestDetailView.as_view(), name='point-detail'),
]
