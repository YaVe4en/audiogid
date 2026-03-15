from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True,
        verbose_name='Аватар',
    )
    bio = models.TextField(
        blank=True,
        verbose_name='О себе',
    )
    is_guest = models.BooleanField(
        default=False,
        verbose_name='Гостевой аккаунт',
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
