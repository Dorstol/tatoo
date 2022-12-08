from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED,
                                   HTTP_404_NOT_FOUND)
from rest_framework.test import APIClient

from tatoo.models import Board
from tatoo.tests import sample_board, sample_pin


class TestAPI(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create(email="testApi@mail.com")
        self.user.set_password("123123")
        self.user.save()
        self.board = sample_board(name="Chicano", pins_count=1)
        self.signup_url = reverse("rest_framework:login")

    def tearDown(self) -> None:
        del self.user
        del self.client

    def test_get_board_detail(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.get(reverse("api:board_detail", kwargs={"pk": self.board.pk}))
        self.assertEqual(result.status_code, HTTP_200_OK)
        self.assertEqual(result.data, {"name": "Chicano", "pins_count": 1, "pinner_id": 1})

    def test_get_invalid_board_detail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("api:board_detail", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_board_detail_without_access(self):
        result = self.client.get(reverse("api:board_detail", kwargs={"pk": self.board.pk}))
        self.assertEqual(result.status_code, HTTP_401_UNAUTHORIZED)

    def test_user_correct_login(self):
        response = self.client.login(email=self.user.email, password="123123")
        self.assertEqual(response, True)

    def test_login_user_with_wrong_data(self):
        response = self.client.login(email="admin@admin.com", password="123qwe")
        self.assertEqual(response, False)
