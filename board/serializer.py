from rest_framework import serializers
from board.models import BulletinBoard, Review


class AdSerializer(serializers.ModelSerializer):
    """Сериалазер модели 'BulletinBoard' для работы с эндпоинтами объявлений 'ad'"""

    class Meta:
        model = BulletinBoard
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = Review
        fields = "__all__"
