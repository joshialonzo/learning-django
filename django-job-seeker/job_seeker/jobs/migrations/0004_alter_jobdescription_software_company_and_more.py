# Generated by Django 4.2 on 2023-04-22 23:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_alter_softwarecompany_options'),
        ('jobs', '0003_jobdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdescription',
            name='software_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.softwarecompany'),
        ),
        migrations.CreateModel(
            name='SelectionProcess',
            fields=[
                ('id', models.UUIDField(db_comment='Primary key for all the models', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_comment='Object creation date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_comment='Object updating date')),
                ('status', models.IntegerField(choices=[(0, 'Zero'), (1, 'Started'), (2, 'Waiting'), (3, 'Rejected'), (4, 'Offer'), (5, 'Accepted')], default='Zero')),
                ('headhunting_firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.headhuntingfirm')),
                ('job_description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobdescription')),
            ],
            options={
                'verbose_name_plural': 'Selection processes',
                'ordering': ['job_description', 'status'],
            },
        ),
    ]