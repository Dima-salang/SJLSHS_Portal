# Generated by Django 4.1.2 on 2022-11-23 01:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('std_portal', '0002_alter_post_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grades1stSem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr2', models.SmallIntegerField(default=0)),
                ('cpar', models.SmallIntegerField(default=0)),
                ('pe', models.SmallIntegerField(default=0)),
                ('spec', models.SmallIntegerField(default=0)),
                ('ucsp', models.SmallIntegerField(default=0)),
                ('philo', models.SmallIntegerField(default=0)),
                ('eapp', models.SmallIntegerField(default=0)),
                ('lrn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
