# Generated by Django 4.0.4 on 2022-05-26 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientside', '0004_alter_lavochki_date_added_alter_lavochki_descroption_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lavochki',
            old_name='descroption',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='lavochki',
            old_name='raiting',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='Lavochki_id',
            new_name='lavochka',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='raiting',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='user_id',
            new_name='user',
        ),
    ]