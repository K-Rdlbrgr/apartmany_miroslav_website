# Generated by Django 3.0.5 on 2020-04-30 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartmany', '0002_auto_20200430_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
