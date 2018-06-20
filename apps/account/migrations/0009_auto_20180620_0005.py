# Generated by Django 2.0.4 on 2018-06-20 00:05

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'InActive'), ('archived', 'Archived')], default='active', max_length=10)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male')], default='male', max_length=20, verbose_name='Gender'),
        ),
    ]
