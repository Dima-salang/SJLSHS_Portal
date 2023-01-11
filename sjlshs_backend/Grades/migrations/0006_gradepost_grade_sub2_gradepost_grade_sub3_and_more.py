# Generated by Django 4.1.2 on 2022-12-25 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0005_delete_basesubjects'),
        ('Grades', '0005_remove_gradepost_sub1_remove_gradepost_sub2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gradepost',
            name='grade_sub2',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gradepost',
            name='grade_sub3',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gradepost',
            name='grade_sub4',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gradepost',
            name='grade_sub5',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gradepost',
            name='grade_sub6',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gradepost',
            name='grade_sub7',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gradepost',
            name='grade_sub8',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gradepost',
            name='sub1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub1', to='subjects.coresubjects'),
        ),
        migrations.AddField(
            model_name='gradepost',
            name='sub2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub2', to='subjects.coresubjects'),
        ),
        migrations.AddField(
            model_name='gradepost',
            name='sub3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub3', to='subjects.coresubjects'),
        ),
        migrations.AddField(
            model_name='gradepost',
            name='sub4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub4', to='subjects.coresubjects'),
        ),
        migrations.AddField(
            model_name='gradepost',
            name='sub5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub5', to='subjects.coresubjects'),
        ),
        migrations.AddField(
            model_name='gradepost',
            name='sub6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub6', to='subjects.coresubjects'),
        ),
        migrations.AddField(
            model_name='gradepost',
            name='sub7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub7', to='subjects.specializedsubjects'),
        ),
        migrations.AddField(
            model_name='gradepost',
            name='sub8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub8', to='subjects.specializedsubjects'),
        ),
        migrations.AlterField(
            model_name='gradepost',
            name='grade_sub1',
            field=models.SmallIntegerField(default=0, verbose_name='<django.db.models.fields.related.ForeignKey>'),
        ),
    ]
