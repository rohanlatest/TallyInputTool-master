# Generated by Django 3.2 on 2021-06-25 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='Invoice_Model',
        ),
    ]