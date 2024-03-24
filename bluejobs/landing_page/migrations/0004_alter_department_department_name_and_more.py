# Generated by Django 4.1.7 on 2024-03-24 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0003_remove_department_department_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_ID',
            field=models.IntegerField(default=200000, unique=True),
        ),
    ]
