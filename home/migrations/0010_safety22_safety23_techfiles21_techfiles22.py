# Generated by Django 4.0.1 on 2022-01-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_newsevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Safety22',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/safety_drive_2022_pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='Safety23',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/safety_drive_2023_pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='Techfiles21',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/technical_files_2021_pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='Techfiles22',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/technical_files_2022_pdf/')),
            ],
        ),
    ]