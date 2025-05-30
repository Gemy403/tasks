# Generated by Django 5.2 on 2025-05-06 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Kpi",
            fields=[
                ("kpi_id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("kpi_name", models.CharField(max_length=64)),
            ],
            options={
                "db_table": "dim_kpi",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Regions",
            fields=[
                (
                    "region_id",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="SubRegions",
            fields=[
                (
                    "sub_region_id",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "amana",
                    models.ForeignKey(
                        db_column="region_id",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="tasks.regions",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="KpiValues",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("year", models.IntegerField()),
                ("month", models.IntegerField()),
                ("kpi_value", models.BigIntegerField(null=True)),
                (
                    "kpi",
                    models.ForeignKey(
                        db_column="kpi_id",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="tasks.kpi",
                    ),
                ),
                (
                    "sub_region",
                    models.ForeignKey(
                        db_column="sub_region_id",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="tasks.subregions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
