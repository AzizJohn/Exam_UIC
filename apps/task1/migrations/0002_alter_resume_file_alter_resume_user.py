# Generated by Django 4.2 on 2023-04-11 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='file',
            field=models.FileField(upload_to='resumes/%Y/%m/%d/', verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to=settings.AUTH_USER_MODEL),
        ),
    ]
