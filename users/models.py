import uuid
import  datetime
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    STATUS_CHOICES = [
        ("user", "User"),
        ("admin", "Admin"),
    ]

    first_name = models.CharField(
        max_length=200,
        verbose_name="Имя",
        help_text="Укажите имя"
    )
    last_name = models.CharField(
        max_length=200,
        verbose_name="Фамилия",
        help_text="Укажите фамилию"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Почта",
        help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        help_text="Укажите телефон"
    )
    city = models.CharField(
        max_length=150,
        verbose_name="Город",
        help_text="Укажите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Загрузите аватар",
        blank=True, null=True
    )
    role = models.CharField(
        max_length=25,
        choices=STATUS_CHOICES,
        default="user"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", ]

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return f"{self.email}"


class PasswordResetToken(models.Model):
    """ Модуль сохранения токенов для пользователей """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    token = models.UUIDField(
        default=uuid.uuid4,
        editable=False, unique=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def is_valid(self, lifetime_minutes=settings.PASSWORD_RESET_TIMEOUT_MINUTES):
        """ Определение метода для проверки срока действия токена """

        expiration_time = self.created_at + datetime.timedelta(minutes=lifetime_minutes)
        return timezone.now() < expiration_time
