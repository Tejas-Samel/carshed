# Generated by Django 4.0.1 on 2022-02-05 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_rename_railway_ememo_defects_reported_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ememo',
            name='IA',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ememo',
            name='IC',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ememo',
            name='M',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ememo',
            name='TI',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ememo',
            name='UST',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ememo',
            name='W',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ememo',
            name='poh',
            field=models.DateField(blank=True, null=True),
        ),
    ]