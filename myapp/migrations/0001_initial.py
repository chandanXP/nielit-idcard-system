# Generated by Django 4.1 on 2024-02-01 11:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=255, null=True, unique=True)),
                ('job_title', models.CharField(max_length=100)),
                ('join_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('work_location', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='employee_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2200), django.core.validators.MinValueValidator(2000)])),
                ('enrollment_number', models.CharField(max_length=10, unique=True)),
                ('branch', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=255, null=True, unique=True)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('valid_date_from', models.DateField(default=django.utils.timezone.now)),
                ('date_upto', models.DateField(blank=True, null=True)),
                ('location', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='employee_images/')),
                ('course', models.ForeignKey(blank=True, help_text='Select course', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.course', verbose_name='Course')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
            ],
        ),
    ]
