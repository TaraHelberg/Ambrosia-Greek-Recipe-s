# Generated by Django 3.2.16 on 2022-10-28 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-created_on']},
        ),
    ]
