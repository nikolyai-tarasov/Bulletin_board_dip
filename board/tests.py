from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from board.models import BulletinBoard, Review
from users.models import User


class AdTestCase(APITestCase):
    """Тестирование эедоинтов модели 'BulletinBoard'"""

    def setUp(self):
        self.user = User.objects.create(
            email="kolya.tarasov1@mail.com", username="kuzon12", password="pass1"
        )
        self.ad = BulletinBoard.objects.create(
            title="RX 590 8GB", price=7890, description="Good", author=self.user
        )
        self.review = Review.objects.create(text="Интересная видеокарта",
            author=self.user,
            ad=self.ad,
        )
        self.client.force_authenticate(user=self.user)

    def test_create_ad(self):
        """Тестирование создания объявления"""

        data = {
            "title": "test",
            "price": 7890,
            "description": "testing",
            "author": 1,

        }

        response = self.client.post("/create_ad/", data=data)
        data_ = response.json()


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(BulletinBoard.objects.all().count(), 2)

    def test_retrieve_ad(self):
        """Тестирование вывода одного объявления"""

        url = reverse("board:retrieve_ad", args=(self.ad.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("title"), self.ad.title)

    def test_update_ad(self):
        """Тестирование редактирования объявления"""
        data = {"title": "test_update_1"}

        url = reverse("board:update_ad", args=(self.ad.pk,))
        response = self.client.patch(url, data)
        data_ = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data_.get("title"), "test_update_1")

    def test_destroy_ad(self):
        """Тестирование удаления объявления"""
        url = reverse("board:destroy_ad", args=(self.ad.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(BulletinBoard.objects.all().count(), 0)


class ReviewTestCase(APITestCase):
    """Тестирование эедоинтов модели 'Review'"""

    def setUp(self):
        self.user = User.objects.create(
            email="kolya.tarasov2@mail.com", username="kuzon2", password="pass2"
        )

        self.user_1 = User.objects.create(
            email="kolya.tarasov222@mail.com", username="kuzon222", password="pass234"
        )

        self.ad = BulletinBoard.objects.create(
            title="RXS 590 8GB", price=7999, description="Good", author=self.user
        )

        self.review = Review.objects.create(
            text="Интересная видеокарта",
            author=self.user_1,
            ad=self.ad,
        )

        self.client.force_authenticate(user=self.user)
        self.client.force_authenticate(user=self.user_1)

    def test_create_review(self):
        """Тестирование создания отзыва"""
        data = {
            "text": 1,
            "ad": 6,
            "author": 5,
        }

        response = self.client.post("/create_review/", data=data)
        data_ = response.json()



        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Review.objects.all().count(), 2)

    def test_retrieve_review(self):
        """Тестирование вывода одного отзыва"""

        url = reverse("board:retrieve_review", args=(self.review.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("text"), self.review.text)

    def test_update_review(self):
        """Тестирование редактирования отзыва"""

        data = {"text": "Testing"}

        url = reverse("board:update_review", args=(self.review.pk,))
        response = self.client.patch(url, data)
        data_ = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data_.get("text"), "Testing")

    def test_destroy_review(self):
        """Тестирование удаления отзыва"""

        url = reverse("board:destroy_review", args=(self.review.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Review.objects.all().count(), 0)
