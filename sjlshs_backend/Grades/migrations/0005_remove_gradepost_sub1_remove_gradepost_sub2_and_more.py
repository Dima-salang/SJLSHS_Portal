# Generated by Django 4.1.2 on 2022-12-24 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grades', '0004_gradepost_sub1_gradepost_sub2_gradepost_sub3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradepost',
            name='sub1',
        ),
        migrations.RemoveField(
            model_name='gradepost',
            name='sub2',
        ),
        migrations.RemoveField(
            model_name='gradepost',
            name='sub3',
        ),
        migrations.RemoveField(
            model_name='gradepost',
            name='sub4',
        ),
        migrations.RemoveField(
            model_name='gradepost',
            name='sub5',
        ),
        migrations.RemoveField(
            model_name='gradepost',
            name='sub6',
        ),
        migrations.RemoveField(
            model_name='gradepost',
            name='sub7',
        ),
        migrations.RemoveField(
            model_name='gradepost',
            name='sub8',
        ),
        migrations.AddField(
            model_name='gradepost',
            name='grade_sub1',
            field=models.SmallIntegerField(default=0, verbose_name='<django.db.models.fields.related_descriptors.ForwardManyToOneDescriptor object at 0x0000015B8B37BEE0>'),
        ),
    ]
