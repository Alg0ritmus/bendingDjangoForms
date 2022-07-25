# Generated by Django 4.0.5 on 2022-07-24 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_person_secrets_secret_owner_secret_person1'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persons', models.ManyToManyField(to='base.person')),
            ],
        ),
        migrations.AlterField(
            model_name='secret',
            name='person1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='involved', to='base.friendship'),
        ),
    ]
