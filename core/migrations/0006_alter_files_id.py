# Generated by Django 4.2 on 2023-05-05 06:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_files_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
