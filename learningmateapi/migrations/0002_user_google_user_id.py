# Generated by Django 5.1.1 on 2024-09-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningmateapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='google_user_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
