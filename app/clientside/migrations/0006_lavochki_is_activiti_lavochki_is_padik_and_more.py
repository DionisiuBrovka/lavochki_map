# Generated by Django 4.0.4 on 2022-05-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientside', '0005_rename_descroption_lavochki_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lavochki',
            name='is_activiti',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='lavochki',
            name='is_padik',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='lavochki',
            name='is_ten',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
