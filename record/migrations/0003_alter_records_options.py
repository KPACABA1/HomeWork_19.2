# Generated by Django 4.2.1 on 2024-08-07 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("record", "0002_alter_records_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="records",
            options={
                "permissions": [
                    ("may_cancel_publication_record", "may cancel publication record")
                ],
                "verbose_name": "блоговая запись",
                "verbose_name_plural": "блоговые записи",
            },
        ),
    ]
