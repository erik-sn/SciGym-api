# Generated by Django 2.1.3 on 2018-12-11 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('environments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='environment',
            name='api_url',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='fork',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='forks',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='git_url',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='github_id',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='homepage',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='html_url',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='license',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='private',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='public',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='pypi_name',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='raw_api_response',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='readme',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='size',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='ssh_url',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='stargazers_count',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='watchers',
        ),
    ]
