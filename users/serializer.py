
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериалазер модели 'User' для работы с эндпоинтами пользователей"""

    class Meta:
        model = User
        fields = ('id','email','last_name','first_name','phone','city','avatar','password')

class UserAdminSerializer(serializers.ModelSerializer):
    """ Сериализатор Администратора для изменения поля 'role' у пользователя """

    class Meta:
        model = User
        fields = ('id','email','last_name','first_name','phone','city','role','avatar', 'username')


class PasswordResetRequestSerializer(serializers.Serializer):
    """ Сериализатор для сброса пароля """

    email = serializers.EmailField(required=True)


class PasswordResetConfirmSerializer(serializers.Serializer):
    """ Сериализатор для подтверждения сброса пароля """

    uid = serializers.CharField(required=True)
    token = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=8)