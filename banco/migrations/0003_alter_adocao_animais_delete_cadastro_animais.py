# Generated by Django 4.2.11 on 2024-03-28 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_animal', '0001_initial'),
        ('banco', '0002_alter_adotante_idade_alter_cadastro_animais_idade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adocao',
            name='animais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro_animal.animal'),
        ),
        migrations.DeleteModel(
            name='cadastro_animais',
        ),
    ]
