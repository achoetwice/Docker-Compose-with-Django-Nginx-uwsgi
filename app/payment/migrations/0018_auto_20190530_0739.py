# Generated by Django 2.2 on 2019-05-30 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0017_auto_20190530_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guesttemporaryinfo',
            name='id',
            field=models.CharField(default='3f110c78', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.CharField(db_column='pk', default='50f6a297-ed92-44de-806b-90f67e', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
