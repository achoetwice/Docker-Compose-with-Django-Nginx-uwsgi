# Generated by Django 2.2 on 2019-06-10 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_auto_20190610_0415'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='line_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
