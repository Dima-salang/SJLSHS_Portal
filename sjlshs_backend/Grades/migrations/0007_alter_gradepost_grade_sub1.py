# Generated by Django 4.1.2 on 2022-12-25 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grades', '0006_gradepost_grade_sub2_gradepost_grade_sub3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradepost',
            name='grade_sub1',
            field=models.SmallIntegerField(default=0),
        ),
    ]
