# Generated by Django 2.0.4 on 2018-05-23 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auditentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='School',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Work',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='DOB'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='emergency_contact',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=20, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='guest_profiles',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='languages',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='native_location',
            field=models.TextField(default='Delhi'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='preferred_currency',
            field=models.CharField(default='Indian rupee', max_length=100, verbose_name='Currency'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='preferred_language',
            field=models.CharField(default='English', max_length=100, verbose_name='Language'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='shipping_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='time_zone',
            field=models.CharField(default='(UTC +5:30)', max_length=100, verbose_name='Time Zone'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='vat_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='work_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
