from django.contrib import admin
from .models import Region, Category, PointOfInterest, Photo, AudioGuide


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


class AudioGuideInline(admin.StackedInline):
    model = AudioGuide
    extra = 0


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(PointOfInterest)
class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'region', 'is_published', 'created_at')
    list_filter = ('category', 'region', 'is_published')
    search_fields = ('name', 'description')
    inlines = [PhotoInline, AudioGuideInline]
    list_editable = ('is_published',)
