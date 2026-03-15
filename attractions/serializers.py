from rest_framework import serializers
from .models import Region, Category, PointOfInterest, Photo, AudioGuide


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class RegionSerializer(serializers.ModelSerializer):
    points_count = serializers.IntegerField(
        source='points.count',
        read_only=True,
    )

    class Meta:
        model = Region
        fields = ('id', 'name', 'description', 'image', 'points_count')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image', 'caption', 'order')


class AudioGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioGuide
        fields = ('id', 'audio_file', 'duration_seconds', 'language')


class PointOfInterestListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    region_name = serializers.CharField(source='region.name', read_only=True)
    cover_photo = serializers.SerializerMethodField()
    has_audio = serializers.SerializerMethodField()

    class Meta:
        model = PointOfInterest
        fields = (
            'id', 'name', 'category_name', 'region_name',
            'latitude', 'longitude', 'cover_photo', 'has_audio', 'created_at',
        )

    def get_cover_photo(self, obj):
        first_photo = obj.photos.first()
        if first_photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(first_photo.image.url)
        return None

    def get_has_audio(self, obj):
        return hasattr(obj, 'audio_guide')


class PointOfInterestDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    region = RegionSerializer(read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    audio_guide = AudioGuideSerializer(read_only=True)

    class Meta:
        model = PointOfInterest
        fields = (
            'id', 'name', 'description',
            'latitude', 'longitude',
            'category', 'region',
            'photos', 'audio_guide',
            'created_at', 'updated_at',
        )
