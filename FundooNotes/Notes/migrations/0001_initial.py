# Generated by Django 2.0 on 2019-10-30 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Labels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('color', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('reminder', models.DateTimeField(blank=True, null=True)),
                ('is_pinned', models.BooleanField(default=False)),
                ('is_trashed', models.BooleanField(default=False)),
                ('is_archived', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('collaborator', models.ManyToManyField(blank=True, related_name='notes', to=settings.AUTH_USER_MODEL)),
                ('labels', models.ManyToManyField(blank=True, related_name='notes', to='Labels.Label')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]