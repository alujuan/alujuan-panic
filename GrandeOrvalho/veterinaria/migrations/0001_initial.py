# Generated by Django 4.2.3 on 2023-08-01 11:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Animal",
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
                ("nome", models.CharField(max_length=100)),
                ("nome_dono", models.CharField(max_length=100)),
                ("especies", models.CharField(max_length=100)),
                ("raca", models.CharField( max_length=100)),
                ("sexo", models.CharField(max_length=100)),
                ("idade", models.DecimalField(decimal_places=3, max_digits=100)),
                ("tipo_sanguineo", models.CharField(max_length=100)),
            ],
        ),
    ]
