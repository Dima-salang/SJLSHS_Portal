# Generated by Django 4.1.2 on 2023-01-22 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_file', models.FileField(max_length=255, upload_to='media/schedules/')),
                ('section', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sched_section', to='accounts.studentsection')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=50, null=True)),
                ('Title', models.CharField(max_length=50)),
                ('Body', models.TextField(null=True)),
                ('Published', models.DateTimeField(auto_now_add=True)),
                ('Section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.studentsection')),
            ],
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='media/modules/module_thumbnails')),
                ('file', models.FileField(upload_to='media/modules/')),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grade', to='accounts.studentyear')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subject', to='accounts.subject')),
            ],
        ),
    ]
