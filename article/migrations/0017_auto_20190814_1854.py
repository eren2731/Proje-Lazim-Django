# Generated by Django 2.2.4 on 2019-08-14 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20190814_1843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['pro_date']},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='article_image',
            new_name='pro_image',
        ),
    ]