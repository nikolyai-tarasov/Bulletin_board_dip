from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from users.models import User


class UserTestCase(APITestCase):
    """Тестирование эедоинтов модели 'User'"""

    def setUp(self):
        self.user = User.objects.create(
            email="kolya.tarasov2@mail.com",
            username="kuzon2",
            password="pass2",

            is_active=True,
        )

        self.client.force_authenticate(user=self.user)

    def test_retrieve_user(self):
        """Тестирование вывода страницы пользователя"""

        url = reverse("users:retrieve_user", args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("email"), self.user.email)

    def test_update_user(self):
        """Тестирование редактирование данных пользователя"""

        data = {"city": "test"}

        url = reverse("users:update_user", args=(self.user.pk,))
        response = self.client.patch(url, data)
        data_ = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data_.get("city"), "test")

    def test_register_user(self):
        """Тестирование создания пользователя"""

        data = {
            "username": "kolta",
            "email": "kol.tara@1.com",
            "password": "123321",
            "password2": "123321",
            "phone": "231298434",
            "city": "Mos",
            "last_name": "Doc",
            "first_name": "Dr",
        }

        url = reverse("users:register")

        response = self.client.post(url, data)
        data_ = response.json()


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(data_["email"], "kol.tara@1.com")

    def test_destroy_user(self):
        """Тестирование удаления пользователя"""

        url = reverse("users:destroy_user", args=(self.user.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(User.objects.all().count(), 0)
