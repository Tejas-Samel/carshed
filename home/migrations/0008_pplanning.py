# Generated by Django 4.0.1 on 2022-01-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_jointnotes21_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='pplanning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/pp_pdf/')),
            ],
        ),
    ]