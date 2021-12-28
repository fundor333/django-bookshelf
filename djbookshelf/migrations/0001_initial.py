# Generated by Django 4.0 on 2021-12-28 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                    "title",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                ("image", models.URLField(blank=True, null=True)),
                (
                    "room",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "shelf",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "book_code",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djbookshelf.author",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ISBN",
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
                    "isbn",
                    models.CharField(blank=True, max_length=13, null=True),
                ),
                ("searched_google", models.BooleanField(default=False)),
                (
                    "book",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djbookshelf.book",
                    ),
                ),
            ],
        ),
    ]
