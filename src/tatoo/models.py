from django.contrib.auth import get_user_model
from django.db import models

from core.validators.ImageSizeValidator import validate_image


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_datetime = models.DateTimeField(null=True, auto_now_add=True)
    last_update = models.DateTimeField(null=True, auto_now=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Pinner(BaseModel):
    avatar = models.ImageField(upload_to="media/avatars/", blank=True)
    full_name = models.CharField(max_length=256, blank=True)
    username = models.CharField(max_length=32, blank=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} pinner"

    def save(self, *args, **kwargs):
        super(Pinner, self).save(*args, **kwargs)


class Board(BaseModel):
    BOARD_MAX_PINS = 100

    name = models.CharField(max_length=32)
    pins_count = models.IntegerField()
    pinner = models.ForeignKey(Pinner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Pin(BaseModel):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    like_count = models.IntegerField(blank=True)
    title = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.title


class Image(BaseModel):
    pin = models.ForeignKey(Pin, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/images/", validators=[validate_image])


class Comment(BaseModel):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(Pinner, on_delete=models.CASCADE, related_name="all_comments")
    text = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.user} says {self.text}"
