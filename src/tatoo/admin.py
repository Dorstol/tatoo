from django.contrib import admin

from tatoo.models import Board, Comment, Image, Pin, Pinner, Profile

# Register your models here.
admin.site.register([Pinner, Profile, Board, Pin, Image, Comment])
