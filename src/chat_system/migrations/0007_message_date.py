# Generated by Django 2.0.3 on 2018-04-02 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_system', '0006_messagenotification_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]