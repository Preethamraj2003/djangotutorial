# Generated by Django 5.1.6 on 2025-03-02 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_employee_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='image',
            new_name='photo',
        ),
    ]
