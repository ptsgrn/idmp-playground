# Generated by Django 5.1.6 on 2025-02-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_medicinalproduct_registration_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinalproduct',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
