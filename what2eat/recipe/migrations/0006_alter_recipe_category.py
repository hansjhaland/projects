# Generated by Django 4.0.2 on 2022-03-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_alter_recipe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('breakfast', 'Frokost'), ('lunch', 'lunch'), ('dinner', 'dinner')], max_length=10),
        ),
    ]
