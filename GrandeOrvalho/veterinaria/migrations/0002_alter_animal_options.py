# Generated by Django 4.2.3 on 2023-08-01 12:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("veterinaria", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="animal",
            options={"verbose_name": "Animal", "verbose_name_plural": "Animais"},
        ),
    ]
