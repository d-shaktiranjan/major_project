# Generated by Django 3.2.9 on 2021-12-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20211205_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='reactionRecord',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teachers',
            name='reactionRecord',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
