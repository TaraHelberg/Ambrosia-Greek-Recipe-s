# Generated by Django 3.2.16 on 2022-10-15 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_auto_20221011_1036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='create_on',
            new_name='created_on',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_posts', to=settings.AUTH_USER_MODEL),  # noqa
        ),
        migrations.AlterField(
            model_name='recipe',
            name='serves',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
