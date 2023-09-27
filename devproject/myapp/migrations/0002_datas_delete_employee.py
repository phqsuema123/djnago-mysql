# Generated by Django 4.1 on 2023-09-27 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="datas",
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
                ("titile", models.CharField(max_length=100)),
                ("day_travel", models.IntegerField()),
                ("budget", models.IntegerField()),
                ("detail", models.TextField()),
            ],
            options={"db_table": "tbdatas",},
        ),
        migrations.DeleteModel(name="Employee",),
    ]