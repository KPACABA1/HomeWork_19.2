# Generated by Django 5.0.7 on 2024-07-17 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("record", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="records",
            options={
                "verbose_name": "блоговая запись",
                "verbose_name_plural": "блоговые записи",
            },
        ),
    ]
