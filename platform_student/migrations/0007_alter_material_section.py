# Generated by Django 5.0 on 2024-02-17 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platform_student', '0006_alter_test_correct_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='section',
            field=models.ForeignKey(max_length=110, on_delete=django.db.models.deletion.CASCADE, to='platform_student.section', verbose_name='Название секции'),
        ),
    ]
