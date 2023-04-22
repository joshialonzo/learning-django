# Generated by Django 4.2 on 2023-04-22 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_headhuntingfirm'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwareCompany',
            fields=[
                ('company_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='companies.company')),
                ('software_company_type', models.CharField(choices=[('StartUp', 'StartUp'), ('Factory', 'Factory'), ('Enterprise', 'Enterprise')], default='Enterprise', max_length=20)),
                ('industry', models.CharField(choices=[('Software', 'Software'), ('Education', 'Education'), ('Energy', 'Energy'), ('Manufacturing', 'Manufacturing'), ('Finance', 'Finance'), ('Social Media', 'Social Media'), ('Media', 'Media')], default='Software', max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('companies.company',),
        ),
    ]
