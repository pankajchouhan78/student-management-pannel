# Generated by Django 3.2.16 on 2023-08-21 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_collage_degree_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collage',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]
