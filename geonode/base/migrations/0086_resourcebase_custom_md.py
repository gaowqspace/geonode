# Generated by Django 3.2.16 on 2023-05-27 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0085_alter_resourcebase_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcebase',
            name='custom_md',
            field=models.TextField(blank=True, help_text='a custom metadata field', null=True, verbose_name='Custom Md'),
        ),
    ]
