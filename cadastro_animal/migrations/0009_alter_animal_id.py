# Generated by Django 4.2.11 on 2024-04-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_animal', '0008_alter_animal_options_animal_adotado_animal_castrado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='id',
            field=models.CharField(editable=False, max_length=10, primary_key=True, serialize=False),
        ),
    ]
