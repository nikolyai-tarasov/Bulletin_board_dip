from django.db import models
from django.db.models import CASCADE

from users.models import User


class BulletinBoard(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название товара",
        help_text="Введите название товара",
    )

    price = models.PositiveIntegerField(
        verbose_name="Стоймость товара", help_text="Введите стоймость товара"
    )

    description = models.TextField(
        verbose_name="Описание товара", help_text="Введите описание товара"
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author_ad",
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = [
            "title",
            "author",
        ]

    def __str__(self):
        return f"{self.title} - {self.author}"


class Review(models.Model):
    text = models.TextField(verbose_name="Текс отзыва", help_text="Введите Ваш отзыв")

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author_review",
    )

    ad = models.ForeignKey(BulletinBoard, on_delete=CASCADE, related_name="ad")

    created_at = models.DateTimeField(
        blank=True, null=True, help_text="Введите дату и время создания отзыва"
    )
