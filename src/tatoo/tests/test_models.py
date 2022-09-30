import random

from django.core.exceptions import ValidationError
from django.test import TestCase

from tatoo.models import Board, Pin, Pinner


def sample_pin(title, **params):
    defaults = {
        "description": "RandomText",
        "like_count": random.random() * 10,
        "board": Board.objects.create(
            name="test_name", pins_count=1, pinner=Pinner.objects.create(username="test_user", full_name="Rodriguez")
        ),
    }
    defaults.update(**params)
    return Pin.objects.create(title=title, **defaults)


def sample_board(pins_count, **params):
    defaults = {"name": "test123", "pinner": Pinner.objects.create(username="test_user", full_name="Rodriguez")}
    defaults.update(**params)
    return Board.objects.create(pins_count=pins_count, **defaults)


class TestBoardModel(TestCase):
    def setUp(self) -> None:
        self.pins_count = 100
        self.test_board = sample_board(pins_count=self.pins_count)

        for i in range(self.pins_count):
            sample_pin(board=self.test_board, title=f"test{i}")

    def tearDown(self) -> None:
        self.test_board.delete()

    def test_board_pins_count(self):
        self.assertEqual(self.pins_count, self.test_board.pins_count)

    def test_board_name_limit(self):
        with self.assertRaises(ValidationError):
            sample_board(pins_count=1, name="title" * 10000)


class TestPinModel(TestCase):
    def setUp(self) -> None:
        self.board = sample_board(pins_count=20)
        self.test_pin = sample_pin(board=self.board, title="test_title_pin")

    def tearDown(self) -> None:
        self.test_pin.delete()

    def test_validation_likes(self):
        with self.assertRaises(ValidationError):
            sample_pin(title="valid_title", like_count="invalid value")

    def test_pin_title_limit(self):
        self.assertTrue(len(self.test_pin.title) <= 128, True)
