# Generated by Django 5.0.1 on 2024-01-06 23:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_members_role'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('github_link', models.URLField()),
                ('image', models.ImageField(upload_to='images/')),
                ('project_description', models.CharField(max_length=1500)),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_name', to='teams.team')),
            ],
        ),
    ]
