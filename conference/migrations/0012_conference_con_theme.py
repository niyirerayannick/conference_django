# Generated by Django 4.0.6 on 2022-07-28 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0011_conference_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='con_theme',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]