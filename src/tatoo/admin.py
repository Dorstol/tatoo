from django.contrib import admin

from tatoo.models import Board, Comment, Image, Pin, Pinner

# Register your models here.
admin.site.register([Pinner, Board, Pin, Image, Comment])
