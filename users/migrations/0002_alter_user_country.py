# Generated by Django 4.2 on 2024-07-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="country",
            field=models.CharField(
                blank=True, max_length=15, null=True, verbose_name="Страна"
            ),
        ),
    ]
