# Generated by Django 4.2 on 2024-07-28 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="token",
            field=models.CharField(
                blank=True,
                max_length=10,
                null=True,
                verbose_name="Код подтверждения, который отправляется на почту",
            ),
        ),
    ]
