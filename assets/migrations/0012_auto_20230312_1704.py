# Generated by Django 3.1.14 on 2023-03-12 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets', '0011_alter_message_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ManyToManyField(related_name='received_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]