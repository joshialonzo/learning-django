# Generated by Django 4.2 on 2023-04-22 04:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.UUIDField(db_comment='Primary key for all the models', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_comment='Object creation date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_comment='Object updating date')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
