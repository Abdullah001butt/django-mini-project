# Generated by Django 5.1.4 on 2024-12-28 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0002_chaivarity_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
