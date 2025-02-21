from django.contrib import admin

from board.models import BulletinBoard, Review


@admin.register(BulletinBoard)
class BulletinBoard(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "price",
        "description",
        "author",
    )



@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = (
        "id",
        "text",
        "author",
        "ad",
        "created_at",
    )