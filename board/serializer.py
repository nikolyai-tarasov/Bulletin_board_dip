from isort.profiles import black
from rest_framework import serializers
from board.models import BulletinBoard, Review


class ReviewSerializer(serializers.ModelSerializer):
    """ Сериализатор модели 'Review' для работы с эндпоинтами отзывов """

    class Meta:
        model = Review
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    """Сериалазер модели 'BulletinBoard' для работы с эндпоинтами объявлений 'ad'"""
    review = ReviewSerializer(source='ad', many=True,  required=False, allow_null=True, default='')

    class Meta:
        model = BulletinBoard
        fields = "__all__"


