from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название района')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(
        upload_to='regions/',
        null=True,
        blank=True,
        verbose_name='Изображение',
    )

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название категории')
    slug = models.SlugField(unique=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class PointOfInterest(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name='Широта',
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name='Долгота',
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.SET_NULL,
        null=True,
        related_name='points',
        verbose_name='Район',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='points',
        verbose_name='Категория',
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Photo(models.Model):
    point = models.ForeignKey(
        PointOfInterest,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='Достопримечательность',
    )
    image = models.ImageField(upload_to='photos/', verbose_name='Фото')
    caption = models.CharField(max_length=300, blank=True, verbose_name='Подпись')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['order']

    def __str__(self):
        return f'Фото [{self.point.name}] #{self.order}'


class AudioGuide(models.Model):
    point = models.OneToOneField(
        PointOfInterest,
        on_delete=models.CASCADE,
        related_name='audio_guide',
        verbose_name='Достопримечательность',
    )
    audio_file = models.FileField(upload_to='audio/', verbose_name='Аудиофайл')
    duration_seconds = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Длительность (сек)',
    )
    language = models.CharField(
        max_length=10,
        default='ru',
        verbose_name='Язык',
    )

    class Meta:
        verbose_name = 'Аудиогид'
        verbose_name_plural = 'Аудиогиды'

    def __str__(self):
        return f'Аудиогид: {self.point.name}'
