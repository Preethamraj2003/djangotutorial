# Generated by Django 5.1.6 on 2025-03-02 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0012_rename_image_employee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.CharField(default='', max_length=254, null=True),
        ),
    ]
