# Generated by Django 4.0.5 on 2022-07-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_rename_article_article_archive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='established',
            field=models.DateField(null=True),
        ),
    ]
