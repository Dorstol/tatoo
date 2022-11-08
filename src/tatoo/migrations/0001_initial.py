# Generated by Django 4.1.1 on 2022-10-30 18:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import core.validators.ImageSizeValidator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_datetime",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("last_update", models.DateTimeField(auto_now=True, null=True)),
                ("name", models.CharField(max_length=32)),
                ("pins_count", models.IntegerField()),
                (
                    "pinner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Pinner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_datetime",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("last_update", models.DateTimeField(auto_now=True, null=True)),
                ("avatar", models.ImageField(blank=True, upload_to="media/avatars/")),
                ("username", models.CharField(blank=True, max_length=32)),
                ("about", models.CharField(blank=True, max_length=512, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Pin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_datetime",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("last_update", models.DateTimeField(auto_now=True, null=True)),
                ("description", models.CharField(blank=True, max_length=255)),
                ("like_count", models.IntegerField(blank=True)),
                ("title", models.CharField(blank=True, max_length=128)),
                ("price", models.PositiveIntegerField(blank=True, default=0)),
                (
                    "board",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="tatoo.board"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_datetime",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("last_update", models.DateTimeField(auto_now=True, null=True)),
                (
                    "image",
                    models.ImageField(
                        upload_to="static/images/",
                        validators=[core.validators.ImageSizeValidator.validate_image],
                    ),
                ),
                (
                    "pin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="tatoo.pin",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_datetime",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("last_update", models.DateTimeField(auto_now=True, null=True)),
                ("text", models.CharField(max_length=250)),
                (
                    "pin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="tatoo.pin",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="all_comments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
