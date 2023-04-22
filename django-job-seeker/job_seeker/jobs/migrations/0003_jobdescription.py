# Generated by Django 4.2 on 2023-04-22 22:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0002_alter_technology_options'),
        ('companies', '0006_alter_softwarecompany_options'),
        ('jobs', '0002_alter_message_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('id', models.UUIDField(db_comment='Primary key for all the models', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_comment='Object creation date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_comment='Object updating date')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('minimum_salary', models.IntegerField(blank=True, null=True)),
                ('maximum_salary', models.IntegerField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('schema', models.CharField(choices=[('Payroll', 'Payroll'), ('Contractor', 'Contractor')], default='Contractor', max_length=20)),
                ('location', models.CharField(choices=[('Remote', 'Remote'), ('On-site', 'On-site'), ('Hybrid', 'Hybrid')], default='Remote', max_length=20)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=20)),
                ('description', models.TextField(blank=True)),
                ('software_company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.softwarecompany')),
                ('technologies', models.ManyToManyField(to='technologies.technology')),
            ],
            options={
                'verbose_name_plural': 'Job descriptions',
                'ordering': ['title'],
            },
        ),
    ]