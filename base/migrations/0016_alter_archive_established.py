# Generated by Django 4.0.5 on 2022-07-24 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_article_established'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='established',
            field=models.DateField(null=True),
        ),
    ]