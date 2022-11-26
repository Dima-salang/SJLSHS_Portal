# Generated by Django 4.1.2 on 2022-11-26 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_teacheruser_contact_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='lrn',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='teacheruser',
            name='contact_num',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='teacheruser',
            name='teacher_id',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
