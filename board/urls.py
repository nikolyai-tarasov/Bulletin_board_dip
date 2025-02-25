from django.urls import path
from board.apps import BoardConfig
from board.views import (
    AdListAPIView,
    AdRetrieveAPIView,
    AdDestroyAPIView,
    AdCreateAPIView,
    AdUpdateAPIView,
    ReviewListAPIView,
    ReviewUpdateAPIView,
    ReviewCreateAPIView,
    ReviewDestroyAPIView,
    ReviewRetrieveAPIView,
)

app_name = BoardConfig.name

urlpatterns = [
    path("", AdListAPIView.as_view(), name="list_ad"),
    path("create_ad/", AdCreateAPIView.as_view(), name="create_ad"),
    path("retrieve_ad/<int:pk>/", AdRetrieveAPIView.as_view(), name="retrieve_ad"),
    path("update_ad/<int:pk>/", AdUpdateAPIView.as_view(), name="update_ad"),
    path("destroy_ad/<int:pk>/", AdDestroyAPIView.as_view(), name="destroy_ad"),
    path("list_review/", ReviewListAPIView.as_view(), name="list_review"),
    path("create_review/", ReviewCreateAPIView.as_view(), name="create_review"),
    path(
        "retrieve_review/<int:pk>/",
        ReviewRetrieveAPIView.as_view(),
        name="retrieve_review",
    ),
    path(
        "update_review/<int:pk>/", ReviewUpdateAPIView.as_view(), name="update_review"
    ),
    path(
        "destroy_review/<int:pk>/",
        ReviewDestroyAPIView.as_view(),
        name="destroy_review",
    ),
]
