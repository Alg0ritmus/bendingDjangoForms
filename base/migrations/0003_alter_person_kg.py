# Generated by Django 4.0.5 on 2022-07-23 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_person_kg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='kg',
            field=models.IntegerField(null=True),
        ),
    ]
