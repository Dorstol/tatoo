from rest_framework.serializers import ModelSerializer

from accounts.models import Customer
from tatoo.models import *


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email", "is_staff")


class PinnerSerializer(ModelSerializer):
    class Meta:
        model = Pinner
        fields = ("full_name", "username", "user")


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ("name", "pins_count", "pinner_id")


class PinSerializer(ModelSerializer):
    class Meta:
        model = Pin
        fields = ("title", "board", "description", "like_count")


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ("pins", "image")


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ("pins", "user", "text")
