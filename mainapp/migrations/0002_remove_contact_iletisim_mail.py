# Generated by Django 2.1.7 on 2019-07-22 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='iletisim_mail',
        ),
    ]