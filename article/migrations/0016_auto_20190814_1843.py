# Generated by Django 2.2.4 on 2019-08-14 15:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20190814_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pro_content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]