# Generated by Django 5.0 on 2024-02-17 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platform_student', '0007_alter_material_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platform_student.section', verbose_name='Название секции'),
        ),
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.TextField(blank=True, max_length=110, null=True, verbose_name='Описание секции'),
        ),
    ]
