# Generated by Django 5.0 on 2024-02-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platform_student', '0004_material_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='option1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='option2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='option3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]