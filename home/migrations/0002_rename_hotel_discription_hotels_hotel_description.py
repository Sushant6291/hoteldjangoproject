# Generated by Django 4.0.4 on 2022-05-20 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotels',
            old_name='hotel_discription',
            new_name='hotel_description',
        ),
    ]
