from users.apps import UsersConfig
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import (
    UserCreateAPIView,
    UserUpdateAPIView,
    UserRetrieveAPIView,
    UserDestroyAPIView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
)

app_name = UsersConfig.name


urlpatterns = [
    path("update_user/<int:pk>/", UserUpdateAPIView.as_view(), name="update_user"),
    path(
        "retrieve_user/<int:pk>/", UserRetrieveAPIView.as_view(), name="retrieve_user"
    ),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("destroy_user/<int:pk>/", UserDestroyAPIView.as_view(), name="destroy_user"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("reset_password/", PasswordResetRequestView.as_view(), name="reset_password"),
    path(
        "reset_password_confirm/",
        PasswordResetConfirmView.as_view(),
        name="reset_password_confirm",
    ),
]
