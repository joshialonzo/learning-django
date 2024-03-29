# Generated by Django 4.2 on 2023-04-22 06:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.UUIDField(db_comment='Primary key for all the models', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_comment='Object creation date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_comment='Object updating date')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('linkedin_id', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'workers',
                'ordering': ['first_name', 'last_name'],
            },
        ),
    ]
