from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериалазер модели 'User' для работы с эндпоинтами пользователей"""

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "last_name",
            "first_name",
            "phone",
            "city",
            "avatar",
            "password",
            "password2",
        )


class UserAdminSerializer(serializers.ModelSerializer):
    """Сериализатор Администратора для изменения поля 'role' у пользователя"""

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "last_name",
            "first_name",
            "phone",
            "city",
            "role",
            "avatar",
            "username",
        )


class PasswordResetRequestSerializer(serializers.Serializer):
    """Сериализатор для сброса пароля"""

    email = serializers.EmailField(required=True)


class PasswordResetConfirmSerializer(serializers.Serializer):
    """Сериализатор для подтверждения сброса пароля"""

    uid = serializers.CharField(required=True)
    token = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=8)


class RegisterUserSerializer(serializers.ModelSerializer):
    """Сериалазер для регистрации пользователей"""

    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    password2 = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "last_name",
            "first_name",
            "phone",
            "city",
            "avatar",
            "password",
            "password2",
        )

    def validate(self, data):
        """Проверка, что пароли совпадают"""

        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return data

    def create(self, validated_data):
        """Создание нового пользователя"""
        validated_data.pop("password2")
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
