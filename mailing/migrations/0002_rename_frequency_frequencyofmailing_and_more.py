# Generated by Django 4.2.1 on 2024-08-16 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Frequency",
            new_name="FrequencyOfMailing",
        ),
        migrations.RenameField(
            model_name="mailing",
            old_name="frequency",
            new_name="frequency_of_mailing",
        ),
    ]