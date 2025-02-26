# Generated by Django 4.0.1 on 2022-01-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_siemens'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACRetro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/data_book/ac_retro')),
            ],
        ),
        migrations.CreateModel(
            name='BTEMU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/data_book/bt_emu')),
            ],
        ),
        migrations.CreateModel(
            name='BTMEMU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/data_book/bt_memu')),
            ],
        ),
        migrations.CreateModel(
            name='CBHEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/data_book/cbhel_emu')),
            ],
        ),
        migrations.CreateModel(
            name='Medha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/data_book/medha')),
            ],
        ),
        migrations.CreateModel(
            name='MEMU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/data_book/memu')),
            ],
        ),
    ]
