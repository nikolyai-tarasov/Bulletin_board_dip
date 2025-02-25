from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from board.models import BulletinBoard, Review
from board.paginators import BulletinBoardPaginator
from board.permissions import IsManager, IsOwner
from board.serializer import AdSerializer, ReviewSerializer


class AdCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания объявления"""

    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]


class AdListAPIView(generics.ListAPIView):
    """Эндпоинт списка объявлений"""

    serializer_class = AdSerializer
    queryset = BulletinBoard.objects.all()
    pagination_class = BulletinBoardPaginator
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ("title", "author")




class AdUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования объявления"""

    serializer_class = AdSerializer
    queryset = BulletinBoard.objects.all()
    permission_classes = [IsOwner | IsManager]


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт вывода отдельного объявления"""

    serializer_class = AdSerializer
    queryset = BulletinBoard.objects.all()
    permission_classes = [IsOwner | IsManager]


class AdDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаление объявления"""

    queryset = BulletinBoard.objects.all()
    permission_classes = [IsOwner | IsManager]


class ReviewCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания отзыва"""

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


class ReviewListAPIView(generics.ListAPIView):
    """Эндпоинт списка отзывов"""

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    pagination_class = BulletinBoardPaginator
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ("ad", "author")


class ReviewUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования отзыва"""

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsOwner | IsManager]


class ReviewRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт вывода отдельного отзыва"""

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsOwner | IsManager]


class ReviewDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаление отзыва"""

    queryset = Review.objects.all()
    permission_classes = [IsOwner | IsManager]
