# Generated by Django 3.1 on 2020-08-09 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onCouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onCouse',
            options={'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterField(
            model_name='onCouse',
            name='activity_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
