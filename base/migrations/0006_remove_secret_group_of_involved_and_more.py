# Generated by Django 4.0.5 on 2022-07-24 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_secret_group_of_involved_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secret',
            name='group_of_involved',
        ),
        migrations.RemoveField(
            model_name='secret',
            name='owner_of_secret',
        ),
        migrations.AddField(
            model_name='person',
            name='secrets',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.secret'),
        ),
    ]
