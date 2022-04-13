# Generated by Django 2.1.7 on 2022-04-13 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookroom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='rental_id',
        ),
        migrations.AddField(
            model_name='reservation',
            name='rental_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookroom.Rental'),
        ),
    ]