# Generated by Django 4.0.1 on 2022-01-17 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_performance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/pt/assistance')),
            ],
        ),
        migrations.CreateModel(
            name='Cee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/pt/cee')),
            ],
        ),
        migrations.CreateModel(
            name='Good_works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/pt/gworks')),
            ],
        ),
        migrations.CreateModel(
            name='lpc_sheets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/pt/lpc')),
            ],
        ),
        migrations.CreateModel(
            name='Opr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/pt/opr')),
            ],
        ),
        migrations.CreateModel(
            name='Pcdo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/pt/pcdo')),
            ],
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/pt/ppt')),
            ],
        ),
    ]