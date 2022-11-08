import random

from celery import shared_task
from django.contrib.auth import get_user_model
from faker import Faker

from tatoo.models import Board, Image, Pin

fake = Faker()


@shared_task
def normalize_email_task(filter=None):
    query_set = get_user_model().objects.filter(**filter)
    if query_set:
        for user in query_set:
            print(f"working with user:{user.email}")
            user.save()
    else:
        print("empty data")


@shared_task
def generate_data():
    user = get_user_model().objects.create_user(
        email=fake.email(),
        first_name=fake.word().title(),
        last_name=fake.word().title(),
        password=fake.password(),
        phone=fake.phone_number(),
    )

    board = Board.objects.create(name=fake.name(), pins_count=random.randint(1, 10), pinner=user)
    for i in range(10):
        pin = Pin.objects.create(
            board=board,
            description=fake.text(max_nb_chars=160),
            like_count=random.randint(1, 100),
            title=fake.text(max_nb_chars=20),
            price=random.randint(25, 500),
            user=user,
        )

        Image.objects.create(pin=pin, image="452b9b18c9bcd1ed27a4d576cc393e17.jpg")
