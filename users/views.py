from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework.response import Response

from rest_framework import generics, status

from rest_framework.views import APIView

from board.permissions import IsManager
from users.models import User, PasswordResetToken
from users.permissions import IsUserOwner
from users.serializer import (
    UserAdminSerializer,
    UserSerializer,
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer,
    RegisterUserSerializer,
)


class UserRegisterAPIView(generics.CreateAPIView):
    """Эндпоинт создания пользователя"""

    serializer_class = RegisterUserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования пользователя"""

    queryset = User.objects.all()
    permission_classes = [IsUserOwner | IsManager]

    def get_serializer_class(
        self,
    ):
        """Переопределение метода 'get_serializer_class' для определения сериализатора обратки"""

        if self.request.user.is_staff or self.request.user.role == "admin":
            return UserAdminSerializer
        return UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт вывода страницы пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUserOwner | IsManager]


class UserDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаления пользователя"""

    queryset = User.objects.all()
    permission_classes = [IsUserOwner | IsManager]


class PasswordResetRequestView(APIView):
    """Эндпоинт сброса пароля"""

    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        """ """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"detail": "Пользователя с таким email нет"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        PasswordResetToken.objects.filter(user=user).delete()

        reset_token = PasswordResetToken.objects.create(user=user)

        reset_url = f"{settings.FRONTEND_URL}/reset_password_confirm/{user.id}/{reset_token.token}/"

        message = f"Перейдите по ссылке для обновления пароля: {reset_url}"
        send_mail(
            "Password Reset Request",
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        return Response(
            {"detail": "На Вашу почту отправлено сообщение для обновления пароля"},
            status=status.HTTP_200_OK,
        )


class PasswordResetConfirmView(APIView):
    """Эндпоинт обновления пароля"""

    serializer_class = PasswordResetConfirmSerializer

    def post(self, request):
        """ """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        uid = serializer.validated_data["uid"]
        token = serializer.validated_data["token"]
        new_password = serializer.validated_data["new_password"]

        try:
            user = User.objects.get(pk=uid)
            reset_token = PasswordResetToken.objects.get(user=user, token=token)

            if reset_token.is_valid():

                user.password = make_password(new_password)
                user.save()

                reset_token.delete()

                return Response(
                    {"detail": "Пароль успешно обновлен"}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"detail": "Не действительный токен восстановления"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except (User.DoesNotExist, PasswordResetToken.DoesNotExist):
            return Response(
                {
                    "detail": "Не существует такого пользователя или токен не действителен"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
